✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious Process
Creation Commandline Alert
The following rules are used to identify suspicious activity relating to command-line process
creation. Any one or more of these will trigger the Suspicious Process Creation Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Windows Events Required: 1
The Windows Detect Profile (Low Volume)  covers these required Windows events.
Title Description
SystemNightmare Exploitation Script Detects the exploitation of PrinterNightmare to get a shell as LOCAL_SYSTEM
Execution
More details
Rule ID
process_creation_commandline_1
Query
{'selection': {'CommandLine|contains': ['printnightmare.
gentilkiwi.com', ' /user:gentilguest ', 'Kiwi Legit Prin
ter']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c01f7bd6-0c1d-47aa-9c61-187b91273a16
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0004 , T1068 
References
https://github.com/GossiTheDog/SystemNightmare 
Severity

Title Description
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/11 critical
Unknown
Suspicious Reg Add Open Threat actors performed dumping of SAM, SECURITY and SYSTEM registry hives using
Command DelegateExecute key
More details
Rule ID
process_creation_commandline_2
Query
{'selection_1': {'CommandLine|contains|all': ['reg', 'ad
d', 'hkcu\\software\\classes\\ms-
settings\\shell\\open\\command', '/ve ', '/d']}, 'select
ion_2': {'CommandLine|contains|all': ['reg', 'add', 'hkc
u\\software\\classes\\ms-
settings\\shell\\open\\command', '/v', 'DelegateExecute'
]}, 'selection_3': {'CommandLine|contains|all': ['reg',
'delete', 'hkcu\\software\\classes\\ms-
settings']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,dd3ee8cc-f751-41c9-ba53-5a32ed47e563
Author: frack113, Swachchhanda Shrawan Poudel (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003 
References
https://thedfirreport.com/2021/12/13/diavol-ransomware/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/20 medium
Unknown
CL_LoadAssembly.ps1 Proxy Detects the use of a Microsoft signed script to execute commands and bypassing
Execution AppLocker.

Title Description
More details
Rule ID
process_creation_commandline_3
Query
{'selection': {'CommandLine|contains': ['\\CL_LoadAssemb
ly.ps1', 'LoadAssemblyFromPath ']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c57872c7-614f-4d7f-a40d-b78c8df2d30d
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://bohops.com/2018/01/07/executing-commands-and-bypassing-
applocker-with-powershell-diagnostic-scripts/ 
https://lolbas-project.github.io/lolbas/Scripts/CL_LoadAssembly/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/21 medium
Unknown
Suspicious Characters in Detects suspicious Unicode characters in the command line, which could be a sign of
CommandLine obfuscation or defense evasion
More details
Rule ID
process_creation_commandline_4
Query
{'selection_spacing_modifiers': {'CommandLine|contains':
['ˣ', '˪', 'ˢ']}, 'selection_unicode_slashes': {'Comman
dLine|contains': ['⁄', '⁄']}, 'selection_unicode_hyphens
': {'CommandLine|contains': ['―', '—']}, 'condition': '1
of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,2c0d2d7b-30d6-4d14-9751-7b9113042ab9
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/27 high
Unknown
Firewall Disabled via Netsh.EXE Detects netsh commands that turns off the Windows firewall
More details
Rule ID
process_creation_commandline_5
Query
{'selection_img': [{'Image|endswith': '\\netsh.exe'}, {'
OriginalFileName': 'netsh.exe'}], 'selection_cli_1': {'C
ommandLine|contains|all': ['firewall', 'set', 'opmode',
'disable']}, 'selection_cli_2': {'CommandLine|contains|a
ll': ['advfirewall', 'set', 'state', 'off']}, 'condition
': 'selection_img and 1 of selection_cli_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,57c4bf16-227f-4394-8ec7-1b745ee061c3
Author: Fatih Sirin
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.004 
References
https://www.winhelponline.com/blog/enable-and-disable-windows-firewall-
quickly-using-command-line/ 
https://app.any.run/tasks/210244b9-0b6b-4a2c-83a3-04bd3175d017/ 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/
T1562.004.md#atomic-test-1---disable-microsoft-defender-firewall 
Severity
49
Suppression Logic Based On

Title Description
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/11/01 medium
Legitimate administration activity
Ke3chang Registry Key Detects Registry modifications performed by Ke3chang malware in campaigns running
Modifications in 2019 and 2020
More details
Rule ID
process_creation_commandline_6
Query
{'selection1': {'CommandLine|contains': ['-
Property DWORD -name DisableFirstRunCustomize -value 2 -
Force', '-Property String -name Check_Associations -
value', '-Property DWORD -name IEHarden -value 0 -
Force']}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b544661-69fc-419f-9a59-82ccc328f205
Author: Markus Neis, Swisscom
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://www.verfassungsschutz.de/embed/broschuere-2020-06-bfv-cyber-
brief-2020-01.pdf 
https://unit42.paloaltonetworks.com/operation-ke3chang-resurfaces-with-
new-tidepool-malware/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2020/06/18 critical
Will need to be looked for combinations of
those processes
Potential PowerShell Obfuscation Detects suspicious encoded character syntax often used for defense evasion
Via WCHAR
More details
Rule ID
process_creation_commandline_7

Title Description
Query
{'selection': {'CommandLine|contains': '(WCHAR)0x'}, 'co
ndition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e312efd0-35a1-407f-8439-b8d434b438a6
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://twitter.com/0gtweet/status/1281103918693482496 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/09 high
Unknown
Conti Volume Shadow Listing Detects a command used by conti to find volume shadow backups
More details
Rule ID
process_creation_commandline_8
Query
{'selection': {'CommandLine|contains|all': ['vssadmin li
st shadows', 'log.txt']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b30e0a7-c675-4b24-8a46-82fa67e2433d
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0042 , T1587.001 , TA0002 , T1059.003 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369e
e2389b9daecaf06331a95410aa5f8/detection 

Title Description
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high
Unknown
InfDefaultInstall.exe .inf Execution Executes SCT script using scrobj.dll from a command in entered into a specially
prepared INF file.
More details
Rule ID
process_creation_commandline_9
Query
{'selection': {'CommandLine|contains|all': ['InfDefaultI
nstall.exe ', '.inf']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ce7cf472-6fcc-490a-9481-3786840b5d9b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T121
8.md#atomic-test-4---infdefaultinstallexe-inf-execution 
https://lolbas-project.github.io/lolbas/Binaries/Infdefaultinstall/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/13 medium
Unknown
Root Certificate Installed From Susp Adversaries may install a root certificate on a compromised system to avoid warnings
Locations when connecting to adversary controlled web servers.
More details
Rule ID

Title Description
process_creation_commandline_10
Query
{'selection': {'CommandLine|contains|all': ['Import-
Certificate', ' -
FilePath ', 'Cert:\\LocalMachine\\Root'], 'CommandLine|c
ontains': ['\\AppData\\Local\\Temp\\', ':\\Windows\\TEMP
\\', '\\Desktop\\', '\\Downloads\\', '\\Perflogs\\', ':\
\Users\\Public\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5f6a601c-2ecb-498b-9c33-660362323afa
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1553.004 
References
https://www.microsoft.com/security/blog/2022/09/07/profiling-dev-0270-
phosphorus-ransomware-operations/ 
https://docs.microsoft.com/en-us/powershell/module/pki/import-certificate?
view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/09 high
Unlikely
Suspicious PrinterPorts Creation Detects new commands that add new printer port which point to suspicious file
(CVE-2020-1048)
More details
Rule ID
process_creation_commandline_11
Query
{'selection1': {'CommandLine|contains': 'Add-
PrinterPort -
Name'}, 'selection2': {'CommandLine|contains': ['.exe',
'.dll', '.bat']}, 'selection3': {'CommandLine|contains':
'Generic / Text Only'}, 'condition': '(selection1 and s
election2) or selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,cc08d590-8b90-413a-aff6-31d1a99678d7
Author: EagleEye Team, Florian Roth
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://windows-internals.com/printdemon-cve-2020-1048/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/13 high
New printer port install on host
PowerShell Script Run in AppData Detects a suspicious command line execution that invokes PowerShell with reference to
an AppData folder
More details
Rule ID
process_creation_commandline_12
Query
{'selection1': {'CommandLine|contains': ['powershell.exe
', '\\powershell', '\\pwsh', 'pwsh.exe']}, 'selection2':
{'CommandLine|contains|all': ['/c ', '\\AppData\\'], 'C
ommandLine|contains': ['Local\\', 'Roaming\\']}, 'condit
ion': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ac175779-025a-4f12-98b0-acdaeb77ea85
Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://twitter.com/JohnLaTwC/status/1082851155481288706 
https://app.any.run/tasks/f87f1c4e-47e2-4c46-9cf4-31454c06ce03 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/01/09 medium
Administrative scripts
Potential Remote Desktop Tunneling Detects potential use of an SSH utility to establish RDP over a reverse SSH Tunnel. This
can be used by attackers to enable routing of network packets that would otherwise not
reach their intended destination.
More details
Rule ID
process_creation_commandline_13
Query
{'selection': {'CommandLine|contains': ':3389'}, 'select
ion_opt': {'CommandLine|contains': [' -L ', ' -P ', ' -
R ', ' -pw ', ' -
ssh ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8a3038e8-9c9d-46f8-b184-66234a160f6f
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1021 
References
https://www.elastic.co/guide/en/security/current/potential-remote-desktop-
tunneling-detected.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/27 medium
Unknown
MSTSC Shadowing Detects RDP session hijacking by using MSTSC shadowing
More details
Rule ID
process_creation_commandline_14
Query
{'selection': {'CommandLine|contains|all': ['noconsentpr
ompt', 'shadow:']}, 'condition': 'selection'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6ba5a05f-b095-4f0a-8654-b825f4f16334
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1563.002 
References
https://twitter.com/kmkz_security/status/1220694202301976576 
https://github.com/kmkz/Pentesting/blob/47592e5e160d3b86c2024f09ef04ce
b87d204995/Post-Exploitation-Cheat-Sheet 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/24 high
Unknown
Suspicious Scan Loop Network Adversaries may attempt to get a listing of other systems by IP address, hostname, or
other logical identifier on a network that may be used for Lateral Movement from the
current system
More details
Rule ID
process_creation_commandline_15
Query
{'selection_loop': {'CommandLine|contains': ['for ', 'fo
reach ']}, 'selection_tools': [{'CommandLine|re': '\\bns
lookup\\b'}, {'CommandLine|re': '\\bping\\b'}], 'conditi
on': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f8ad2e2c-40b6-4117-84d7-20b89896ab23
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1018 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T101
8.md 
https://ss64.com/nt/for.html 

Title Description
https://ss64.com/ps/foreach-object.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/12 medium
Legitimate script
Obfuscated IP Download Detects use of an encoded/obfuscated version of an IP address (hex, octal...) in an URL
combined with a download command
More details
Rule ID
process_creation_commandline_16
Query
{'selection_img': {'CommandLine|contains': ['Invoke-
WebRequest', 'iwr ', 'wget ', 'curl ', 'DownloadFile', '
DownloadString']}, 'selection_ip': [{'CommandLine|contai
ns': ['//0x', '.0x', '.00x']}, {'CommandLine|contains|al
l': ['http://%', '%2e']}], 'condition': 'all of selectio
n*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cb5a2333-56cf-4562-8fcb-22ba1bca728d
Author: Florian Roth (Nextron Systems), X__Junior (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://h.43z.one/ipconverter/ 
https://twitter.com/Yasser_Elsnbary/status/1553804135354564608 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/03 medium
Unknown
MSExchange Transport Agent Detects the Installation of a Exchange Transport Agent
Installation
More details

Title Description
Rule ID
process_creation_commandline_17
Query
{'selection': {'CommandLine|contains': 'Install-
TransportAgent'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,83809e84-4475-4b69-bc3e-4aad8568612f
Author: Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1505.002 
References
https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-
exchange-server-or-outlook?slide=7 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2021/06 mediu
Legitimate installations of exchange
/08 m TransportAgents. AssemblyPath is a good indicator
for this.
Pubprn.vbs Proxy Execution Detects the use of the 'Pubprn.vbs' Microsoft signed script to execute commands.
More details
Rule ID
process_creation_commandline_18
Query
{'selection': {'CommandLine|contains|all': ['\\pubprn.vb
s', 'script:']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1fb76ab8-fa60-4b01-bddd-71e89bf555da
Author: frack113
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1059.003 , TA0005 , T1216.001 
References
https://lolbas-project.github.io/lolbas/Scripts/Pubprn/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/28 medium
Unknown
Tamper Windows Defender Detects attempts to remove windows defender configuration using the 'MpPreference'
Remove-MpPreference cmdlet
More details
Rule ID
process_creation_commandline_19
Query
{'selection_remove': {'CommandLine|contains': 'Remove-
MpPreference'}, 'selection_tamper': {'CommandLine|contai
ns': ['-ControlledFolderAccessProtectedFolders ', '-
AttackSurfaceReductionRules_Ids ', '-
AttackSurfaceReductionRules_Actions ', '-
CheckForSignaturesBeforeRunningScan ']}, 'condition': 'a
ll of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,07e3cb2c-0608-410d-be4b-1511cb1a0448
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://techcommunity.microsoft.com/t5/core-infrastructure-and-
security/windows-10-controlled-folder-access-event-search/ba-p/2326088 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2022/08/05 high
Legitimate PowerShell scripts
AnyDesk Silent Installation Detects AnyDesk Remote Desktop silent installation. Which can be used by attackers to
gain remote access.
More details
Rule ID
process_creation_commandline_20
Query
{'selection': {'CommandLine|contains|all': ['--
install', '--start-with-win', '--
silent']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,114e7f1c-f137-48c8-8f54-3088c24ce4b9
Author: Ján Trenčanský
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1219 
References
https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/06 high
Legitimate deployment of AnyDesk
Execution via CL_Invocation.ps1 Detects Execution via SyncInvoke in CL_Invocation.ps1 module
More details
Rule ID
process_creation_commandline_21
Query
{'selection': {'CommandLine|contains|all': ['CL_Invocati
on.ps1', 'SyncInvoke']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,a0459f02-ac51-4c09-b511-b8c9203fc429
Author: Nasreddine Bencherchali (Nextron Systems), oscd.community, Natalia
Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/Cl_invocation/ 
https://twitter.com/bohops/status/948061991012327424 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/14 high
Unknown
Writing Of Malicious Files To The Monitors for the hiding possible malicious files in the C:\Windows\Fonts\ location. This
Fonts Folder folder doesn't require admin privillege to be written and executed from.
More details
Rule ID
process_creation_commandline_24
Query
{'selection_1': {'CommandLine|contains': ['echo', 'copy'
, 'type', 'file createnew', 'cacls']}, 'selection_2': {'
CommandLine|contains': 'C:\\Windows\\Fonts\\'}, 'selecti
on_3': {'CommandLine|contains': ['.sh', '.exe', '.dll',
'.bin', '.bat', '.cmd', '.js', '.msh', '.reg', '.scr', '
.ps', '.vb', '.jar', '.pl', '.inf', '.cpl', '.hta', '.ms
i', '.vbs']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ae9b0bd7-8888-4606-b444-0ed7410cb728
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1211 
References
https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/

Severity

Title Description
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/04/21 medium
Unknown
Suspicious FromBase64String Detects attempts of decoding a base64 Gzip archive via PowerShell. This technique is
Usage On Gzip Archive - Process often used as a method to load malicious content into memory afterward.
Creation
More details
Rule ID
process_creation_commandline_25
Query
{'selection': {'CommandLine|contains|all': ['FromBase64S
tring', 'MemoryStream', 'H4sI']}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d75d6b6b-adb9-48f7-824b-ac2e786efe1f
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=43 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium
Legitimate administrative script
Suspicious Usage Of Detects suspicious usage of the ShellExec_RunDLL function to launch other commands
ShellExec_RunDLL as seen in the the raspberry-robin attack
More details
Rule ID
process_creation_commandline_26
Query

Title Description
{'selection_openasrundll': {'CommandLine|contains': 'She
llExec_RunDLL'}, 'selection_suspcli': {'CommandLine|cont
ains': ['regsvr32', 'msiexec', '\\Users\\Public\\', 'odb
cconf', '\\Desktop\\', '\\Temp\\', 'Invoke-
', 'iex', 'comspec']}, 'condition': 'all of selection_*'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d87bd452-6da1-456e-8155-7dc988157b7d
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://redcanary.com/blog/raspberry-robin/ 
https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-
worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/ 
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/01 high
Unknown
Turla Group Lateral Movement Detects automated lateral movement by Turla group
More details
Rule ID
process_creation_commandline_27
Query
{'selection': {'CommandLine': ['net use \\\\%DomainContr
oller%\\C$ "P@ssw0rd" *', 'dir c:\\*.doc* /s', 'dir %TEM
P%\\*.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c601f20d-570a-4cde-a7d6-e17f99cb8e7f
Author: Markus Neis
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1059.003 , TA0007 , T1083 , T1135 , TA0008 ,
T1021.002 
References
https://securelist.com/the-epic-turla-operation/65545/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/11/07 critical
Unknown
Netsh RDP Port Opening Detects netsh commands that opens the port 3389 used for RDP, used in Sarwent
Malware
More details
Rule ID
process_creation_commandline_28
Query
{'selection1': {'CommandLine|contains|all': ['netsh', 'f
irewall add portopening', 'tcp 3389']}, 'selection2': {'
CommandLine|contains|all': ['netsh', 'advfirewall firewa
ll add rule', 'action=allow', 'protocol=TCP', 'localport
=3389']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,01aeb693-138d-49d2-9403-c4f52d7d3d62
Author: Sander Wiebing
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.004 
References
https://labs.sentinelone.com/sarwent-malware-updates-command-detonation/

Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/23 high
Legitimate administration

Title Description
PowerShell DownloadFile Detects the execution of powershell, a WebClient object creation and the invocation of
DownloadFile in a single command line
More details
Rule ID
process_creation_commandline_29
Query
{'selection': {'CommandLine|contains|all': ['powershell'
, '.DownloadFile', 'System.Net.WebClient']}, 'condition'
: 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8f70ac5f-1f6f-4f8e-b454-db19561216c5
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0011 , T1104 , T1105 
References
https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-
intrusion-campaign-using-multiple-exploits.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/08/28 high
Unknown
Powershell Defender Exclusion Detects requests to exclude files, folders or processes from Antivirus scanning using
PowerShell cmdlets
More details
Rule ID
process_creation_commandline_30
Query
{'selection1': {'CommandLine|contains': ['Add-
MpPreference ', 'Set-
MpPreference ']}, 'selection2': {'CommandLine|contains':
[' -ExclusionPath ', ' -ExclusionExtension ', ' -
ExclusionProcess ', ' -
ExclusionIpAddress ']}, 'condition': 'all of selection*'
}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,17769c90-230e-488b-a463-e05c08e9d48f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://docs.microsoft.com/en-us/microsoft-365/security/defender-
endpoint/configure-process-opened-file-exclusions-microsoft-defender-
antivirus 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/
T1562.001.md 
https://twitter.com/AdamTheAnalyst/status/1483497517119590403 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2021/04/29 medium
Possible Admin Activity
tal
Other Cmdlets that may use the same
parameters
Lazarus Loaders Detects different loaders as described in various threat reports on Lazarus group activity
More details
Rule ID
process_creation_commandline_31
Query
{'selection_cmd1': {'CommandLine|contains|all': ['cmd.ex
e /c ', ' -
p 0x']}, 'selection_cmd2': {'CommandLine|contains': ['C:
\\ProgramData\\', 'C:\\RECYCLER\\']}, 'selection_rundll1
': {'CommandLine|contains|all': ['rundll32.exe ', 'C:\\P
rogramData\\']}, 'selection_rundll2': {'CommandLine|cont
ains': ['.bin,', '.tmp,', '.dat,', '.io,', '.ini,', '.db
,']}, 'condition': '( selection_cmd1 and selection_cmd2
) or ( selection_rundll1 and selection_rundll2 )'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b49c990-4a9a-4e65-ba95-47c9cc448f6e
Author: Florian Roth (Nextron Systems), wagga

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.hvs-consulting.de/lazarus-report/ 
https://securelist.com/lazarus-covets-covid-19-related-intelligence/99906/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/12/23 critical
Unknown
Suspicious GrpConv Execution Detects the suspicious execution of a utility to convert Windows 3.x .grp files or for
persistence purposes by malicious software or actors
More details
Rule ID
process_creation_commandline_32
Query
{'selection': {'CommandLine|contains': ['grpconv.exe -
o', 'grpconv -o']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f14e169e-9978-4c69-acb3-1cff8200bc36
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547 
References
https://twitter.com/0gtweet/status/1526833181831200770 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/19 high
Unknown

Title Description
Disabled RestrictedAdminMode For Detect activation of DisableRestrictedAdmin to desable RestrictedAdmin mode.
RDS - ProcCreation RestrictedAdmin mode prevents the transmission of reusable credentials to the remote
system to which you connect using Remote Desktop. This prevents your credentials
from being harvested during the initial connection process if the remote server has been
compromise
More details
Rule ID
process_creation_commandline_33
Query
{'selection': {'CommandLine|contains|all': ['\\System\\C
urrentControlSet\\Control\\Lsa\\', 'DisableRestrictedAdm
in', ' 1']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,28ac00d6-22d9-4a3c-927f-bbd770104573
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1112 
References
https://github.com/redcanaryco/atomic-red-
team/blob/a8e3cf63e97b973a25903d3df9fd55da6252e564/atomics/T1112/T1
112.md 
https://social.technet.microsoft.com/wiki/contents/articles/32905.remote-
desktop-services-enable-restricted-admin-mode.aspx 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/13 high
Unknown
Malicious Base64 Encoded Detects base64 encoded powershell cmdlet invocation of known suspicious cmdlets
Powershell Invoke Cmdlets
More details
Rule ID
process_creation_commandline_34
Query
{'selection': {'CommandLine|contains': ['SQBuAHYAbwBrAGU
ALQBCAGwAbwBvAGQASABvAHUAbgBkA', 'kAbgB2AG8AawBlAC0AQgBs
AG8AbwBkAEgAbwB1AG4AZA', 'JAG4AdgBvAGsAZQAtAEIAbABvAG8AZ
ABIAG8AdQBuAGQA', 'SQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0A
HoA', 'kAbgB2AG8AawBlAC0ATQBpAG0AaQBrAGEAdAB6A', 'JAG4Ad

Title Description
gBvAGsAZQAtAE0AaQBtAGkAawBhAHQAeg', 'SQBuAHYAbwBrAGUALQB
XAE0ASQBFAHgAZQBjA', 'kAbgB2AG8AawBlAC0AVwBNAEkARQB4AGUA
Yw', 'JAG4AdgBvAGsAZQAtAFcATQBJAEUAeABlAGMA']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fd6e2919-3936-40c9-99db-0aa922c356f7
Author: pH-T (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/31 high
Unlikely
Uninstall Crowdstrike Falcon Adversaries may disable security tools to avoid possible detection of their tools and
activities by uninstalling Crowdstrike Falcon
More details
Rule ID
process_creation_commandline_35
Query
{'selection': {'CommandLine|contains|all': ['\\WindowsSe
nsor.exe', ' /uninstall', ' /quiet']}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f0f7be61-9cf5-43be-9836-99d6ef448a18
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/

Title Description
T1562.001.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/12 medium
Uninstall by admin
Suspicious Powershell No File or Detects suspicious powershell execution that ends with a common flag instead of a
Command command or a filename to execute (could be a sign of implicit execution that uses files in
WindowsApps directory)
More details
Rule ID
process_creation_commandline_36
Query
{'selection': {'CommandLine|endswith': [' -
windowstyle hidden"', ' -windowstyle hidden', " -
windowstyle hidden'", ' -w hidden"', ' -w hidden', " -
w hidden'", ' -ep bypass"', ' -ep bypass', " -
ep bypass'", ' -noni"', ' -noni', " -
noni'"]}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b66474aa-bd92-4333-a16c-298155b120df
Author: pH-T (Nextron Systems), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0003 , T1053.005 
References
https://blog.malwarebytes.com/threat-intelligence/2022/04/colibri-loader-
combines-task-scheduler-and-powershell-in-clever-persistence-technique/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/08 high
Unknown

Title Description
New Network Provider - Detects when an attacker tries to add a new network provider in order to dump clear text
CommandLine credentials, similar to how the NPPSpy tool does it
More details
Rule ID
process_creation_commandline_37
Query
{'selection': {'CommandLine|contains|all': ['\\System\\C
urrentControlSet\\Services\\', '\\NetworkProvider']}, 'f
ilter': {'CommandLine|contains': ['\\System\\CurrentCont
rolSet\\Services\\WebClient\\NetworkProvider', '\\System
\\CurrentControlSet\\Services\\LanmanWorkstation\\Networ
kProvider', '\\System\\CurrentControlSet\\Services\\RDPN
P\\NetworkProvider']}, 'condition': 'selection and not f
ilter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,baef1ec6-2ca9-47a3-97cc-4cf2bda10b77
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003 
References
https://docs.microsoft.com/en-us/troubleshoot/windows-
client/deployment/network-provider-settings-removed-in-place-upgrade 
https://github.com/gtworek/PSBits/tree/master/PasswordStealing/NPPSpy 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2022/08/2 high
Other legitimate network providers used and
ntal 3 not filtred in this rule
Turla Group Commands May 2020 Detects commands used by Turla group as reported by ESET in May 2020
More details
Rule ID
process_creation_commandline_38
Query
{'selection1': {'CommandLine|contains': ['tracert -
h 10 yahoo.com', '.WSqmCons))|iex;', 'Fr`omBa`se6`4Str`i

Title Description
ng']}, 'selection2': {'CommandLine|contains|all': ['net
use https://docs.live.net', '@aol.co.uk']}, 'condition':
'1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9e2e51c5-c699-4794-ba5a-29f5da40ac0c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0003 , T1053.005 , TA0005 , T1027 
References
https://www.welivesecurity.com/wp-
content/uploads/2020/05/ESET_Turla_ComRAT.pdf 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/26 critical
Unknown
Potential Data Stealing Via Detects chromium based browsers starting in headless and debugging mode and
Chromium Headless Debugging pointing to a user profile. This could be a sign of data stealing or remote control
More details
Rule ID
process_creation_commandline_39
Query
{'selection': {'CommandLine|contains|all': ['--remote-
debugging-', '--user-data-dir', '--
headless']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3e8207c5-fcd2-4ea6-9418-15d45b4890e4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1185 
References
https://github.com/defaultnamehere/cookie_crimes/ 
https://mango.pdf.zone/stealing-chrome-cookies-without-a-password 

p g p g p
Title Description
https://embracethered.com/blog/posts/2020/cookie-crimes-on-mirosoft-edge/

https://embracethered.com/blog/posts/2020/chrome-spy-remote-control/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 high
Unknown
Invoke-Obfuscation Via Use MSHTA Detects Obfuscated Powershell via use MSHTA in Scripts
More details
Rule ID
process_creation_commandline_40
Query
{'selection': {'CommandLine|contains|all': ['set', '&&',
'mshta', 'vbscript:createobject', '.run', '(window.clos
e)']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ac20ae82-8758-4f38-958e-b44a3140ca88
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/08 high
Unknown
Suspicious Rundll32 Script in Detects suspicious process related to rundll32 based on arguments
CommandLine
More details
Rule ID

Title Description
process_creation_commandline_41
Query
{'selection': {'CommandLine|contains|all': ['rundll32',
'mshtml,RunHTMLApplication'], 'CommandLine|contains': ['
javascript:', 'vbscript:']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,73fcad2e-ff14-4c38-b11d-4172c8ac86c7
Author: frack113, Zaw Min Htun (ZETA)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://gist.github.com/ryhanson/227229866af52e2d963cf941af135a52 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.011/
T1218.011.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creatio Risk False Positives
y n Date Level
experi 2021/12 mediu
False positives depend on scripts and
mental /04 m administrative tools used in the monitored
environment
Suspicious Base64 Encoded Detects base64 encoded powershell 'Invoke-' call
Powershell Invoke
More details
Rule ID
process_creation_commandline_42
Query
{'selection': {'CommandLine|contains': ['SQBuAHYAbwBrAGU
ALQ', 'kAbgB2AG8AawBlAC0A', 'JAG4AdgBvAGsAZQAtA']}, 'fil
ter_other_rule': {'CommandLine|contains': ['SQBuAHYAbwBr
AGUALQBCAGwAbwBvAGQASABvAHUAbgBkA', 'kAbgB2AG8AawBlAC0AQ
gBsAG8AbwBkAEgAbwB1AG4AZA', 'JAG4AdgBvAGsAZQAtAEIAbABvAG
8AZABIAG8AdQBuAGQA', 'SQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQ
B0AHoA', 'kAbgB2AG8AawBlAC0ATQBpAG0AaQBrAGEAdAB6A', 'JAG
4AdgBvAGsAZQAtAE0AaQBtAGkAawBhAHQAeg', 'SQBuAHYAbwBrAGUA
LQBXAE0ASQBFAHgAZQBjA', 'kAbgB2AG8AawBlAC0AVwBNAEkARQB4A
GUAYw', 'JAG4AdgBvAGsAZQAtAFcATQBJAEUAeABlAGMA']}, 'cond
ition': 'selection and not 1 of filter*'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6385697e-9f1b-40bd-8817-f4a91f40508e
Author: pH-T (Nextron Systems), Harjot Singh, @cyb3rjy0t
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/20 high
Unlikely
HackTool - Bloodhound/Sharphound Detects command line parameters used by Bloodhound and Sharphound hack tools
Execution
More details
Rule ID
process_creation_commandline_44
Query
{'selection_cli_1': {'CommandLine|contains': [' -
CollectionMethod All ', ' --
CollectionMethods Session ', ' --Loop --
Loopduration ', ' --PortScanTimeout ', '.exe -c All -
d ', 'Invoke-Bloodhound', 'Get-
BloodHoundData']}, 'selection_cli_2': {'CommandLine|cont
ains|all': [' -JsonFolder ', ' -
ZipFileName ']}, 'selection_cli_3': {'CommandLine|contai
ns|all': [' DCOnly ', ' --
NoSaveCache ']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f376c8a7-a2d0-4ddc-aa0c-16c17236d962
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1087 , T1482 , T1069 
References
https://github.com/BloodHoundAD/BloodHound 

Title Description
https://github.com/BloodHoundAD/SharpHound 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2019/12/ high
Other programs that use these command line
20 option and accepts an 'All' parameter
Explorer Process Tree Break Detects a command line process that uses explorer.exe to launch arbitrary commands
or binaries, which is similar to cmd.exe /c, only it breaks the process tree and makes its
parent a new instance of explorer spawning from "svchost"
More details
Rule ID
process_creation_commandline_45
Query
{'selection': [{'CommandLine|contains': '/factory,
{75dff2b7-6936-4c06-a8bb-
676a7b00b24b}'}, {'CommandLine|contains|all': ['explorer
.exe', ' /root,']}], 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,949f1ffb-6e85-4f00-ae1e-c3c5b190d605
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron
Systems), @gott_cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036 
References
https://twitter.com/CyberRaiju/status/1273597319322058752 
https://twitter.com/bohops/status/1276357235954909188?s=12 
https://twitter.com/nas_bench/status/1535322450858233858 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Maturi Creation Risk False Positives
ty Date Level
test 2019/06/2 medium
Unknown how many legitimate software
9 products use that method
Suspicious Del in CommandLine Detects suspicious command line to remove and 'exe' or 'dll'
More details
Rule ID
process_creation_commandline_46
Query
{'susp_del_exe': {'CommandLine|contains|all': ['del ', '
*.exe', '/f ', '/q ']}, 'susp_del_dll': {'CommandLine|co
ntains|all': ['del ', '*.dll', 'C:\\ProgramData\\']}, 'c
ondition': 'susp_del_exe or susp_del_dll'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,204b17ae-4007-471b-917b-b917b315c5db
Author: frack113 , X__Junior (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1070.004 
References
https://www.joesandbox.com/analysis/509330/0/html#1044F3BDBE3BB6F73
4E357235F4D5898582D 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/02 medium
Unknown
Invoke-Obfuscation COMPRESS Detects Obfuscated Powershell via COMPRESS OBFUSCATION
OBFUSCATION
More details
Rule ID
process_creation_commandline_47
Query
{'selection': {'CommandLine|contains|all': ['new-
object', 'text.encoding]::ascii'], 'CommandLine|contains
': ['system.io.compression.deflatestream', 'system.io.st
reamreader', 'readtoend(']}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7eedcc9d-9fdb-4d94-9c54-474e8affc0c7
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/18 medium
Unknown
Operation Wocao Activity Detects activity mentioned in Operation Wocao report
More details
Rule ID
process_creation_commandline_48
Query
{'selection': {'CommandLine|contains': ['checkadmin.exe
127.0.0.1 -
all', 'netsh advfirewall firewall add rule name=powershe
ll dir=in', 'cmd /c powershell.exe -ep bypass -
file c:\\s.ps1', '/tn win32times /f', 'create win32times
binPath=', '\\c$\\windows\\system32\\devmgr.dll', ' -
exec bypass -
enc JgAg', 'type *keepass\\KeePass.config.xml', 'iie.exe
iie.txt', 'reg query HKEY_CURRENT_USER\\Software\\*\\Pu
TTY\\Sessions\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,1cfac73c-be78-4f9a-9b08-5bde0c3953ab
Author: Florian Roth (Nextron Systems), frack113
Tactics, Techniques, and Procedures

Title Description
| TA0002 , T1059 | , TA0003 , T1053.005 | , TA0005 , T1036.004 | ,  |
| --------------- | ---------------------- | ---------------------- | --- |
| , TA0007       | , T1012              |                        |     |
T1027
References
| https://twitter.com/SBousseaden/status/1207671369963646976 |     |     |    |
| ---------------------------------------------------------- | --- | --- | --- |
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
| Matur Creation | Risk False Positives |     |     |
| -------------- | -------------------- | --- | --- |
| ity Date       | Level                |     |     |
| test 2019/12/  | high                 |     |     |
Administrators that use checkadmin.exe tool to
20 enumerate local administrators

Title Description
Fireball Archer Install Detects Archer malware invocation via rundll32
More details
Rule ID
process_creation_commandline_49
Query
{'selection': {'CommandLine|contains|all': ['rundll32.ex
e', 'InstallArcherSvc']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3d4aebe0-6d29-45b2-a8a4-3dfde586a26d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://www.virustotal.com/en/file/9b4971349ae85aa09c0a69852ed3e626c95
4954a3927b3d1b6646f139b930022/analysis/ 
https://www.hybrid-
analysis.com/sample/9b4971349ae85aa09c0a69852ed3e626c954954a3927
b3d1b6646f139b930022?environmentId=100 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/06/03 high
Unknown
Zip A Folder With PowerShell For Use living off the land tools to zip a file and stage it in the Windows temporary folder for
Staging In Temp later exfiltration
More details
Rule ID
process_creation_commandline_50
Query
{'selection': {'CommandLine|contains|all': ['Compress-
Archive ', ' -Path ', ' -
DestinationPath ', '$env:TEMP\\']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,85a8e5ba-bd03-4bfb-bbfa-a4409a8f8b98
Author: Nasreddine Bencherchali (Nextron Systems), frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1074.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1074.001/
T1074.001.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/20 medium
Unknown
Registry Dump of SAM Creds and Adversaries may attempt to extract credential material from the Security Account
Secrets Manager (SAM) database either through Windows Registry where the SAM database is
stored
More details
Rule ID
process_creation_commandline_51
Query
{'selection_reg': {'CommandLine|contains': ' save '}, 's
election_key': {'CommandLine|contains': ['HKLM\\sam', 'H
KLM\\system', 'HKLM\\security']}, 'condition': 'all of s
election_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,038cd51c-3ad8-41c5-ba8f-5d1c92f3cc1e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/
T1003.002.md#atomic-test-1---registry-dump-of-sam-creds-and-secrets 
Severity
74
Suppression Logic Based On

Title Description
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 high
Unknown
Procdump Evasion Detects uses of the SysInternals Procdump utility in which procdump or its output get
renamed or a dump file is moved ot copied to a different name
More details
Rule ID
process_creation_commandline_52
Query
{'selection1': {'CommandLine|contains': ['copy procdump'
, 'move procdump']}, 'selection2': {'CommandLine|contain
s|all': ['copy ', '.dmp '], 'CommandLine|contains': ['2.
dmp', 'lsass', 'out.dmp']}, 'selection3': {'CommandLine|
contains': ['copy lsass.exe_', 'move lsass.exe_']}, 'con
dition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,79b06761-465f-4f88-9ef2-150e24d3d737
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036 , TA0006 , T1003.001 
References
https://twitter.com/mrd0x/status/1480785527901204481 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2022/01/ high
Cases in which procdump just gets copied to a
11 different directory without any renaming
Powershell Token Obfuscation - Detects TOKEN OBFUSCATION technique from Invoke-Obfuscation
Process Creation
More details
Rule ID
process_creation_commandline_53

Title Description
Query
{'selection': [{'CommandLine|re': '\\w+`(\\w+|-
|.)`[\\w+|\\s]'}, {'CommandLine|re': '"(\\
{\\d\\})+"\\s*-f'}, {'CommandLine|re': '\\$\\
{((e|n|v)*`(e|n|v)*)+:path\\}|\\$\\
{((e|n|v)*`(e|n|v)*)+:((p|a|t|h)*`(p|a|t|h)*)+\\}|\\$\\
{env:
((p|a|t|h)*`(p|a|t|h)*)+\\}'}], 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,deb9b646-a508-44ee-b7c9-d8965921c6b6
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1027 
References
https://github.com/danielbohannon/Invoke-Obfuscation 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/27 high
Unknown
Suspicious Minimized MSEdge Start Detects the suspicious minimized start of MsEdge browser, which can be used to
download files from the Internet
More details
Rule ID
process_creation_commandline_54
Query
{'selection': {'CommandLine|contains': 'start /min msedg
e'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,94771a71-ba41-4b6e-a757-b531372eaab6
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron
Systems)

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://twitter.com/mrd0x/status/1478234484881436672?s=12 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Mat Creatio Risk False Positives
urity n Date Level
test 2022/0 high
Software that uses MsEdge to download components
1/11 in the background (see ParentImage,
ParentCommandLine)
Suspicious PowerShell Download Detects suspicious PowerShell download patterns that are often used in malicious
and Execute Pattern scripts, stagers or downloaders (make sure that your backend applies the strings case-
insensitive)
More details
Rule ID
process_creation_commandline_55
Query
{'selection': {'CommandLine|contains': ['IEX ((New-
Object Net.WebClient).DownloadString', 'IEX (New-
Object Net.WebClient).DownloadString', 'IEX((New-
Object Net.WebClient).DownloadString', 'IEX(New-
Object Net.WebClient).DownloadString', ' -command (New-
Object System.Net.WebClient).DownloadFile(', ' -c (New-
Object System.Net.WebClient).DownloadFile(']}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e6c54d94-498c-4562-a37c-b469d8e9a275
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://gist.github.com/jivoi/c354eaaf3019352ce32522f916c03d70 
https://www.trendmicro.com/en_us/research/22/j/lv-ransomware-exploits-
proxyshell-in-attack.html 
Severity
74

Title Description
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/02/ high
Software installers that pull packages from
ental 28 remote systems and execute them
Add User to Local Administrators Detects suspicious command line that adds an account to the local
administrators/administrateurs group
More details
Rule ID
process_creation_commandline_56
Query
{'selection_net': {'Image|endswith': ['\\net.exe', '\\ne
t1.exe'], 'CommandLine|contains|all': ['localgroup ', '
/add']}, 'selection_powershell': {'Image|endswith': ['\\
powershell.exe', '\\pwsh.exe'], 'CommandLine|contains|al
l': ['Add-LocalGroupMember ', ' -
Group ']}, 'selection_group': {'CommandLine|contains': [
' administrators ', ' administrateur']}, 'filter_domain_
admins_compliance': {'UserId': 'S-1-5-
18', 'CommandLine|contains': 'domain admin'}, 'condition
': '(selection_net or selection_powershell) and selectio
n_group and not filter_domain_admins_compliance'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1098 
References
https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/12 medium
Administrative activity
Taskkill Symantec Endpoint Detects one of the possible scenarios for disabling symantec endpoint protection.
Protection Symantec Endpoint Protection antivirus software services incorrectly implement the
protected service mechanism. As a result, the NT AUTHORITY/SYSTEM user can

Title Description
execute the taskkill /im command several times ccSvcHst.exe /f, thereby killing the
process belonging to the service, and thus shutting down the service.
More details
Rule ID
process_creation_commandline_57
Query
{'selection': {'CommandLine|contains|all': ['taskkill',
' /F ', ' /IM ', 'ccSvcHst.exe']}, 'condition': 'selecti
on'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,4a6713f6-3331-11ed-a261-0242ac120002
Author: Ilya Krestinichev, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://www.exploit-db.com/exploits/37525 
https://community.spiceworks.com/topic/2195015-batch-script-to-uninstall-
symantec-endpoint-protection 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/13 high
Unknown
MsiExec Web Install Detects suspicious msiexec process starts with web addresses as parameter
More details
Rule ID
process_creation_commandline_58
Query
{'selection': {'CommandLine|contains|all': [' msiexec',
'://']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f7b5f842-a6af-4da5-9e95-e32478f3cd2f

Title Description
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.007 , TA0011 , T1105 
References
https://blog.trendmicro.com/trendlabs-security-intelligence/attack-using-
windows-installer-msiexec-exe-leads-lokibot/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2018/02/ mediu
False positives depend on scripts and administrative
09 m tools used in the monitored environment
PsExec Service Start Detects a PsExec service start
More details
Rule ID
process_creation_commandline_59
Query
{'selection': {'CommandLine': 'C:\\Windows\\PSEXESVC.exe
'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3ede524d-21cc-472d-a3ce-d21b568d8db7
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 
References
N/A
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/13 low
Administrative activity

Title Description
Scheduled Task WScript VBScript Detects specific process parameters as used by ACTINIUM scheduled task persistence
creation.
More details
Rule ID
process_creation_commandline_60
Query
{'selection': {'CommandLine|contains|all': ['schtasks',
'create', 'wscript', 'e:vbscript']}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e1118a8f-82f5-44b3-bb6b-8a284e5df602
Author: Andreas Hunkeler (@Karneades)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1053.005 
References
https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-
ukrainian-organizations 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/07 high
Unlikely
Dropping Of Password Filter DLL Detects dropping of dll files in system32 that may be used to retrieve user credentials
from LSASS
More details
Rule ID
process_creation_commandline_61
Query
{'selection_cmdline': {'CommandLine|contains|all': ['HKL
M\\SYSTEM\\CurrentControlSet\\Control\\Lsa', 'scecli\\0*
', 'reg add']}, 'condition': 'selection_cmdline'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,b7966f4a-b333-455b-8370-8ca53c229762
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1556.002 
References
https://pentestlab.blog/2020/02/10/credential-access-password-filter-dll/ 
https://github.com/3gstudent/PasswordFilter/tree/master/PasswordFilter 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/29 medium
Unknown
Suspicious UltraVNC Execution Detects suspicious UltraVNC command line flag combination that indicate a auto
reconnect upon execution, e.g. startup (as seen being used by Gamaredon threat
group)
More details
Rule ID
process_creation_commandline_62
Query
{'selection': {'CommandLine|contains|all': ['-
autoreconnect ', '-connect ', '-
id:']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,871b9555-69ca-4993-99d3-35a59f9f3599
Author: Bhabesh Raj
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1021.005 
References
https://www.ria.ee/sites/default/files/content-
editors/kuberturve/tale_of_gamaredon_infection.pdf 
https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-
evolution 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine

Title Description
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/04 high
Unknown
Potential AMSI Bypass Using NULL Detects usage of special strings/null bits in order to potentially bypass AMSI
Bits - ProcessCreation functionalities
More details
Rule ID
process_creation_commandline_63
Query
{'selection': {'CommandLine|contains': ["if(0){{{0}}}' -
f $(0 -as [char]) +", '#
<NULL>']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,92a974db-ab84-457f-9ec0-55db83d7a825
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/r00t-3xp10it/hacking-material-
books/blob/43cb1e1932c16ff1f58b755bc9ab6b096046853f/obfuscation/simpl
e_obfuscation.md#amsi-bypass-using-null-bits-satoshi 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/04 medium
Unknown
Invoke-Obfuscation CLIP+ Launcher Detects Obfuscated use of Clip.exe to execute PowerShell
More details
Rule ID
process_creation_commandline_65
Query
{'selection': {'CommandLine|contains|all': ['cmd', '&&',
'clipboard]::', '-
f'], 'CommandLine|contains': ['/c', '/r']}, 'condition':
'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b222df08-0e07-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 high
Unknown
SyncAppvPublishingServer VBS Executes arbitrary PowerShell code using SyncAppvPublishingServer.vbs
Execute Arbitrary PowerShell Code
More details
Rule ID
process_creation_commandline_67
Query
{'selection': {'CommandLine|contains|all': ['\\SyncAppvP
ublishingServer.vbs', ';']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,36475a7d-0f6d-4dce-9b01-6aeb473bbaf1
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 , T1216 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1216/T121
6.md 
https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/ 
Severity
49

Title Description
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/16 medium
Unknown
Suspicious Add User to Remote Detects suspicious command line in which a user gets added to the local Remote
Desktop Users Group Desktop Users group
More details
Rule ID
process_creation_commandline_68
Query
{'selection_main': [{'CommandLine|contains|all': ['local
group ', ' /add']}, {'CommandLine|contains|all': ['Add-
LocalGroupMember ', ' -
Group ']}], 'selection_group': {'CommandLine|contains':
['Remote Desktop Users', 'Utilisateurs du Bureau à dista
nce', 'Usuarios de escritorio remoto']}, 'condition': 'a
ll of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ffa28e60-bdb1-46e0-9f82-05f7a61cc06e
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1133 , T1136.001 , TA0008 ,
T1021.001 
References
https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-
iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/06 high
Administrative activity
GatherNetworkInfo.vbs Script Usage Adversaries can abuse of C:\Windows\System32\gatherNetworkInfo.vbs script along
with cscript.exe to gather information about the target
More details
Rule ID

Title Description
process_creation_commandline_69
Query
{'selection': {'CommandLine|contains|all': ['cscript.exe
', 'gatherNetworkInfo.vbs']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,575dce0c-8139-4e30-9295-1ee75969f7fe
Author: blueteamer8699
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://posts.slayerlabs.com/living-off-the-land/#gathernetworkinfovbs 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/03 medium
Administrative activity
APT29 This method detects a suspicious PowerShell command line combination as used by
APT29 in a campaign against U.S. think tanks.
More details
Rule ID
process_creation_commandline_70
Query
{'selection': {'CommandLine|contains|all': ['-noni', '-
ep', 'bypass', '$']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,033fe7d6-66d1-4240-ac6b-28908009c71f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References

Title Description
https://www.microsoft.com/security/blog/2018/12/03/analysis-of-cyberattack-
on-u-s-think-tanks-non-profits-public-sector-by-unidentified-attackers/ 
https://www.fireeye.com/blog/threat-research/2018/11/not-so-cozy-an-
uncomfortable-examination-of-a-suspected-apt29-phishing-campaign.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/12/04 high
Unknown
Suspicious WMIC Detects WMIC executions in which a event consumer gets created in order to establish
ActiveScriptEventConsumer persistence
Creation
More details
Rule ID
process_creation_commandline_71
Query
{'selection': {'CommandLine|contains|all': ['ActiveScrip
tEventConsumer', ' CREATE ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ebef4391-1a81-4761-a40a-1db446c0e625
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.003 
References
https://twitter.com/johnlatwc/status/1408062131321270282?s=12 
https://www.fireeye.com/content/dam/fireeye-www/global/en/current-
threats/pdfs/wp-windows-management-instrumentation.pdf 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2021/06/25 high
Legitimate software creating script event
consumers

Title Description
TAIDOOR RAT DLL Load Detects specific process characteristics of Chinese TAIDOOR RAT malware load
More details
Rule ID
process_creation_commandline_72
Query
{'selection1': {'CommandLine|contains': ['dll,MyStart',
'dll MyStart']}, 'selection2a': {'CommandLine|endswith':
' MyStart'}, 'selection2b': {'CommandLine|contains': 'r
undll32.exe'}, 'condition': 'selection1 or ( selection2a
and selection2b )'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d1aa3382-abab-446f-96ea-4de52908210b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1055.001 
References
https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/30 high
Unknown
Empire PowerShell UAC Bypass Detects some Empire PowerShell UAC bypass methods
More details
Rule ID
process_creation_commandline_73
Query
{'selection': {'CommandLine|contains': [' -NoP -NonI -
w Hidden -
c $x=$((gp HKCU:Software\\Microsoft\\Windows Update).Upd
ate)', ' -NoP -NonI -
c $x=$((gp HKCU:Software\\Microsoft\\Windows Update).Upd
ate);']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

gp
Title Description
Rule Source
SigmaHQ,3268b746-88d8-4cd3-bffc-30077d02c787
Author: Ecco
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1548.002 
References
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f4
24906fe13055/data/module_source/privesc/Invoke-
EventVwrBypass.ps1#L64 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f4
24906fe13055/data/module_source/privesc/Invoke-
FodHelperBypass.ps1#L64 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/08/30 critical
Unknown
Emotet Process Creation Detects all Emotet like process executions that are not covered by the more generic
rules
More details
Rule ID
process_creation_commandline_74
Query
{'selection': {'CommandLine|contains': [' -
e* PAA', 'JABlAG4AdgA6AHUAcwBlAHIAcAByAG8AZgBpAGwAZQ', '
QAZQBuAHYAOgB1AHMAZQByAHAAcgBvAGYAaQBsAGUA', 'kAGUAbgB2A
DoAdQBzAGUAcgBwAHIAbwBmAGkAbABlA', 'IgAoACcAKgAnACkAOwAk
A', 'IAKAAnACoAJwApADsAJA', 'iACgAJwAqACcAKQA7ACQA', 'JA
BGAGwAeAByAGgAYwBmAGQ', 'PQAkAGUAbgB2ADoAdABlAG0AcAArACg
A', '0AJABlAG4AdgA6AHQAZQBtAHAAKwAoA', '9ACQAZQBuAHYAOgB
0AGUAbQBwACsAKA']}, 'filter': {'CommandLine|contains': [
'fAAgAEMAbwBuAHYAZQByAHQAVABvAC0ASgBzAG8AbgAgAC0ARQByAHI
AbwByAEEAYwB0AGkAbwBuACAAUwBpAGwAZQBuAHQAbAB5AEMAbwBuAHQ
AaQBuAHUAZQ', 'wAIABDAG8AbgB2AGUAcgB0AFQAbwAtAEoAcwBvAG4
AIAAtAEUAcgByAG8AcgBBAGMAdABpAG8AbgAgAFMAaQBsAGUAbgB0AGw
AeQBDAG8AbgB0AGkAbgB1AGUA', '8ACAAQwBvAG4AdgBlAHIAdABUAG
8ALQBKAHMAbwBuACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAG
kAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQBlA']}, 'condition':
'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,d02e8cf5-6099-48cf-9bfc-1eec2d0c7b18
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://app.any.run/tasks/e13ab713-64cf-4b23-ad93-6dceaa5429ac/ 
https://app.any.run/tasks/81f3c28c-c686-425d-8a2b-a98198d244e1/ 
https://app.any.run/tasks/97f875e8-0e08-4328-815f-055e971ba754/ 
https://app.any.run/tasks/84fc9b4a-ea2b-47b1-8aa6-9014402dfb56/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/09/30 high
Unlikely
Esentutl Gather Credentials Conti recommendation to its affiliates to use esentutl to access NTDS dumped file.
Trickbot also uses this utilities to get MSEdge info via its module pwgrab.
More details
Rule ID
process_creation_commandline_75
Query
{'selection': {'CommandLine|contains|all': ['esentutl',
' /p']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7df1713a-1a5b-4a4b-a071-dc83b144a101
Author: sam0x90
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003.003 
References
https://twitter.com/vxunderground/status/1423336151860002816 
https://attack.mitre.org/software/S0404/ 
https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-
trickbot-and-cobalt-strike/ 
Severity
49
Suppression Logic Based On
computer_name

Title Description
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/06 medium
To be determined
EvilNum Golden Chickens Detects Golden Chickens deployment method as used by Evilnum in report published in
Deployment via OCX Files July 2020
More details
Rule ID
process_creation_commandline_76
Query
{'selection': {'CommandLine|contains|all': ['regsvr32',
'/s', '/i', '\\AppData\\Roaming\\', '.ocx']}, 'condition
': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8acf3cfa-1e8c-4099-83de-a0c4038e18f0
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-
toolset/ 
https://app.any.run/tasks/33d37fdf-158d-4930-aa68-813e1d5eb8ba/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/10 critical
Unknown
Suspicious Dosfuscation Character Detects possible payload obfuscation via the commandline
in Commandline
More details
Rule ID
process_creation_commandline_77
Query
{'selection': {'CommandLine|contains': ['^^', ',;,', '%C
OMSPEC:~', ' s^et ', ' s^e^t ', ' se^t ']}, 'condition':
'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a77c1610-fc73-4019-8e29-0f51efc04a51
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/dosfuscation-
report.pdf 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/02/15 medium
Legitimate use
WhoAmI as Parameter Detects a suspicious process command line that uses whoami as first parameter (as
e.g. used by EfsPotato)
More details
Rule ID
process_creation_commandline_78
Query
{'selection': {'CommandLine|contains': '.exe whoami'}, '
condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e9142d84-fbe0-401d-ac50-3e519fb00c89
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1033 
References
https://twitter.com/blackarrowsec/status/1463805700602224645?s=12 
Severity
74
Suppression Logic Based On

Title Description
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/29 high
Unknown
Powershell Inline Execution From A Detects inline execution of PowerShell code from a file
File
More details
Rule ID
process_creation_commandline_79
Query
{'selection_exec': {'CommandLine|contains': ['iex ', 'In
voke-Expression ', 'Invoke-
Command ', 'icm ']}, 'selection_read': {'CommandLine|con
tains': ['cat ', 'get-
content ', 'type ']}, 'selection_raw': {'CommandLine|con
tains': ' -raw'}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ee218c12-627a-4d27-9e30-d6fb2fe22ed2
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=50 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/25 medium
Unknown
Base64 Encoded PowerShell Detects usage of the "FromBase64String" function in the commandline which is used to
Command Detected decode a base64 encoded string
More details
Rule ID
process_creation_commandline_80
Query

Title Description
{'selection': {'CommandLine|contains': '::FromBase64Stri
ng('}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e32d4572-9826-4738-b651-95fa63747e8a
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 , T1140 
References
https://gist.github.com/Neo23x0/6af876ee72b51676c82a2db8d2cd3639 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/29 high
Administrative script libraries
CL_Mutexverifiers.ps1 Proxy Detects the use of a Microsoft signed script to execute commands
Execution
More details
Rule ID
process_creation_commandline_81
Query
{'selection': {'CommandLine|contains|all': ['\\CL_Mutexv
erifiers.ps1', 'runAfterCancelProcess ']}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1e0e1a81-e79b-44bc-935b-ddb9c8006b3d
Author: Nasreddine Bencherchali (Nextron Systems), oscd.community, Natalia
Shornikova, frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/CL_mutexverifiers/ 
Severity

Title Description
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/21 medium
Unknown
Suspicious X509Enrollment - Detect use of X509Enrollment
Process Creation
More details
Rule ID
process_creation_commandline_82
Query
{'selection': {'CommandLine|contains': ['X509Enrollment.
CBinaryConverter', '884e2002-217d-11da-b2a4-
000e7bbb2b09']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,114de787-4eb2-48cc-abdb-c0b449f93ea4
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=42 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=41 
https://learn.microsoft.com/en-
us/dotnet/api/microsoft.hpc.scheduler.store.cx509enrollmentwebclassfactoryc
lass?view=hpc-sdk-5.1.6115 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium
Legitimate administrative script
Suspicious Regsvr32 HTTP IP Detects a certain command line flag combination used by regsvr32 when used to
Pattern download and register a DLL from a remote address which uses HTTP (not HTTPS) and
a IP address and not FQDN
More details

Title Description
Rule ID
process_creation_commandline_83
Query
{'selection_flags': {'CommandLine|contains|all': [' /s',
' /u']}, 'selection_ip': {'CommandLine|contains': [' /i
:http://1', ' /i:http://2', ' /i:http://3', ' /i:http://
4', ' /i:http://5', ' /i:http://6', ' /i:http://7', ' /i
:http://8', ' /i:http://9', ' /i:https://1', ' /i:https:
//2', ' /i:https://3', ' /i:https://4', ' /i:https://5',
' /i:https://6', ' /i:https://7', ' /i:https://8', ' /i
:https://9']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2dd2c217-bf68-437a-b57c-fe9fd01d5de8
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.010 
References
https://twitter.com/mrd0x/status/1461041276514623491c19-ps 
https://twitter.com/tccontre18/status/1480950986650832903 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/11 high
FQDNs that start with a number
Rundll32 Without Parameters Detects rundll32 execution without parameters as observed when running Metasploit
windows/smb/psexec exploit module
More details
Rule ID
process_creation_commandline_84
Query
{'selection': {'CommandLine': 'rundll32.exe'}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,5bb68627-3198-40ca-b458-49f973db8752
Author: Bartlomiej Czyz, Relativity
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 , TA0008 , T1021.002 , T1570 
References
https://bczyz1.github.io/2021/01/30/psexec.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/31 high
Unknown
Suspicious Ntdll Pipe Redirection Detects command that type the content of ntdll.dll to a different file or a pipe in order to
evade AV / EDR detection
More details
Rule ID
process_creation_commandline_85
Query
{'selection': {'CommandLine|contains': ['type %windir%\\
system32\\ntdll.dll', 'type %systemroot%\\system32\\ntdl
l.dll', 'type c:\\windows\\system32\\ntdll.dll', '\\ntdl
l.dll > \\\\.\\pipe\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bbc865e4-7fcd-45a6-8ff1-95ced28ec5b2
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2022/03/05 high
Unknown
Raccine Uninstall Detects commands that indicate a Raccine removal from an end system. Raccine is a
free ransomware protection tool.
More details
Rule ID
process_creation_commandline_86
Query
{'selection1': {'CommandLine|contains|all': ['taskkill '
, 'RaccineSettings.exe']}, 'selection2': {'CommandLine|c
ontains|all': ['reg.exe', 'delete', 'Raccine Tray']}, 's
election3': {'CommandLine|contains|all': ['schtasks', '/
DELETE', 'Raccine Rules Updater']}, 'condition': '1 of s
election*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a31eeaed-3fd5-478e-a8ba-e62c6b3f9ecc
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/Neo23x0/Raccine 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2021/01/21 high
Legitimate deinstallation by administrative
staff
REGISTER_APP.VBS Proxy Detects the use of a Microsoft signed script 'REGISTER_APP.VBS' to register a
Execution VSS/VDS Provider as a COM+ application.
More details
Rule ID
process_creation_commandline_88
Query
{'selection': {'CommandLine|contains|all': ['\\register_
app.vbs', '-register']}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1c8774a0-44d4-4db0-91f8-e792359c70bd
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://twitter.com/sblmsrsn/status/1456613494783160325?s=20 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creatio Risk False Positives
y n Date Level
experi 2022/08 mediu
Legitimate usage of the script. Always investigate
mental /19 m what's being registered to confirm if it's benign
PowerShell Get-Process LSASS Detects a "Get-Process" cmdlet and it's aliases on lsass process, which is in almost all
cases a sign of malicious activity
More details
Rule ID
process_creation_commandline_89
Query
{'selection': {'CommandLine|contains': ['Get-
Process lsas', 'ps lsas', 'gps lsas']}, 'condition': 'se
lection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b2815d0d-7481-4bf0-9b6c-a4c48a94b349
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1552.004 
References
https://twitter.com/PythonResponder/status/1385064506049630211 
Severity
74

Title Description
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/04/23 high
Unknown
Raspberry Robin Dot Ending File Detects commandline containing reference to files ending with a "." This scheme has
been seen used by raspberry-robin
More details
Rule ID
process_creation_commandline_90
Query
{'selection': {'CommandLine|re': '\\\\([a-zA-Z0-9]
{1,32})\\.([a-zA-Z0-9]{1,6})\\.(\\s*(["\'])|(\\s+[^a-zA-
Z0-9\\s.]))'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a35c97c8-d9c4-4c89-a3e7-533dc0bcb73a
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-
worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/28 high
Unknown
LockerGoga Ransomware Detects LockerGoga Ransomware command line.
More details
Rule ID
process_creation_commandline_91
Query
{'selection': {'CommandLine|contains': '-i SM-tgytutrc -
s'}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,74db3488-fd28-480a-95aa-b7af626de068
Author: Vasiliy Burov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1486 
References
https://medium.com/@malwaredancer/lockergoga-input-arguments-ipc-
communication-and-others-bd4e5a7ba80a 
https://blog.f-secure.com/analysis-of-lockergoga-ransomware/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2020/10/18 critical
Unlikely
Write Protect For Storage Disabled Looks for changes to registry to disable any write-protect property for storage devices.
This could be a precursor to a ransomware attack and has been an observed technique
used by cypherpunk group.
More details
Rule ID
process_creation_commandline_92
Query
{'selection': {'CommandLine|contains|all': ['reg add', '
\\system\\currentcontrolset\\control', 'write protection
', '0'], 'CommandLine|contains': ['storage', 'storagedev
icepolicies']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,75f7a0e2-7154-4c4d-9eae-5cdb4e0a5c13
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562 
References
N/A

Title Description
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/06/11 medium
Unknown
Audio Capture via PowerShell Detects audio capture via PowerShell Cmdlet.
More details
Rule ID
process_creation_commandline_93
Query
{'selection': {'CommandLine|contains': 'WindowsAudioDevi
ce-Powershell-Cmdlet'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,932fb0d8-692b-4b0f-a26e-5643a50fe7d6
Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame),
oscd.community, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1123 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1123/T112
3.md 
https://eqllib.readthedocs.io/en/latest/analytics/ab7a6ef4-0983-4275-a4f1-
5c6bd3c31c23.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2019/10/24 medium
Legitimate audio capture by legitimate
user.
Potential Suspicious Windows Detects usage of the built-in PowerShell cmdlet "Enable-WindowsOptionalFeature" used
Feature Enabled - ProcCreation as a Deployment Image Servicing and Management tool. Similar to DISM.exe, this
cmdlet is used to enumerate, install, uninstall, configure, and update features and
packages in Windows images

Title Description
More details
Rule ID
process_creation_commandline_94
Query
{'selection_cmd': {'CommandLine|contains|all': ['Enable-
WindowsOptionalFeature', '-Online', '-
FeatureName']}, 'selection_feature': {'CommandLine|conta
ins': ['TelnetServer', 'Internet-Explorer-Optional-
amd64', 'TFTP', 'SMB1Protocol', 'Client-
ProjFS', 'Microsoft-Windows-Subsystem-
Linux']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c740d4cf-a1e9-41de-bb16-8a46a4f57918
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://docs.microsoft.com/en-us/powershell/module/dism/enable-
windowsoptionalfeature?view=windowsserver2022-ps 
https://learn.microsoft.com/en-us/windows/win32/projfs/enabling-windows-
projected-file-system 
https://learn.microsoft.com/en-us/windows/wsl/install-on-server 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/29 medium
Unknown
Reg Disable Security Service Detects a suspicious reg.exe invocation that looks as if it would disable an important
security service
More details
Rule ID
process_creation_commandline_96
Query
{'selection_reg_add': {'CommandLine|contains|all': ['reg
', 'add']}, 'selection_cli_reg_start': {'CommandLine|con
tains|all': [' /d 4', ' /v Start'], 'CommandLine|contain
s': ['\\Sense', '\\WinDefend', '\\MsMpSvc', '\\NisSrv',
'\\WdBoot', '\\WdNisDrv', '\\WdNisSvc', '\\wscsvc', '\\S

Title Description
ecurityHealthService', '\\wuauserv', '\\UsoSvc', '\\WdFi
lter', '\\AppIDSvc']}, 'selection_cli_reg_disable_defend
er': {'CommandLine|contains|all': [' /d 1', 'Windows Def
ender'], 'CommandLine|contains': ['DisableIOAVProtection
', 'DisableOnAccessProtection', 'DisableRoutinelyTakingA
ction', 'DisableScanOnRealtimeEnable', 'DisableBlockAtFi
rstSeen', 'DisableBehaviorMonitoring', 'DisableEnhancedN
otifications', 'DisableAntiSpyware', 'DisableAntiSpyware
RealtimeProtection', 'DisableConfig', 'DisablePrivacyMod
e', 'SignatureDisableUpdateOnStartupWithoutEngine', 'Dis
ableArchiveScanning', 'DisableIntrusionPreventionSystem'
, 'DisableScriptScanning']}, 'condition': 'selection_reg
_add and 1 of selection_cli_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5e95028c-5229-4214-afae-d653d573d0ec
Author: Florian Roth (Nextron Systems), John Lambert (idea), elhoim
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://twitter.com/JohnLaTwC/status/1415295021041979392 
https://github.com/gordonbay/Windows-On-
Reins/blob/e587ac7a0407847865926d575e3c46f68cf7c68d/wor.ps1 
https://vms.drweb.fr/virus/?i=24144899 
https://bidouillesecurity.com/disable-windows-defender-in-powershell/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/14 high
Unknown
Other security solution installers
Serv-U Exploitation CVE-2021- Detects patterns as noticed in exploitation of Serv-U CVE-2021-35211 vulnerability by
35211 by DEV-0322 threat group DEV-0322
More details
Rule ID
process_creation_commandline_97
Query
{'selection_whoami': {'CommandLine|contains': 'whoami'},
'selection_cmd_1': {'CommandLine|contains': ['./Client/
Common/', '.\\Client\\Common\\']}, 'selection_cmd_2': {'
CommandLine|contains': 'C:\\Windows\\Temp\\Serv-

Title Description
U.bat'}, 'condition': 'selection_whoami and 1 of selecti
on_cmd*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,75578840-9526-4b2a-9462-af469a45e767
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1136.001 
References
https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-
threat-actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/14 critical
Unlikely
Suspicious Debugger Registration Detects the registration of a debugger for a program that is available in the logon screen
Cmdline (sticky key backdoor).
More details
Rule ID
process_creation_commandline_98
Query
{'selection1': {'CommandLine|contains': '\\CurrentVersio
n\\Image File Execution Options\\'}, 'selection2': {'Com
mandLine|contains': ['sethc.exe', 'utilman.exe', 'osk.ex
e', 'magnify.exe', 'narrator.exe', 'displayswitch.exe',
'atbroker.exe', 'HelpPane.exe']}, 'condition': 'all of s
election*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ae215552-081e-44c7-805f-be16f975c8a2
Author: Florian Roth (Nextron Systems), oscd.community, Jonhnathan Ribeiro
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.008 
References

Title Description
https://blogs.technet.microsoft.com/jonathantrull/2016/10/03/detecting-sticky-
key-backdoors/ 
https://bazaar.abuse.ch/sample/6f3aa9362d72e806490a8abce245331030d1
ab5ac77e400dd475748236a6cc81/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/09/06 high
Unknown
CrackMapExec Command Detect various execution methods of the CrackMapExec pentesting framework
Execution
More details
Rule ID
process_creation_commandline_99
Query
{'selection': {'CommandLine|endswith': ['cmd.exe /Q /c *
1> \\\\*\\*\\* 2>&1', 'cmd.exe /C * > \\\\*\\*\\* 2>&1'
, 'cmd.exe /C * > *\\Temp\\* 2>&1'], 'CommandLine|contai
ns': ['powershell.exe -exec bypass -noni -nop -w 1 -
C "', 'powershell.exe -noni -nop -w 1 -
enc ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,058f4380-962d-40a5-afce-50207d36d7e2
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0002 , T1047 , T1059 , TA0003 , T1053 
References
https://github.com/byt3bl33d3r/CrackMapExec 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2020/05/22 high
Unknown

Title Description
DevInit Lolbin Download Detects a certain command line flag combination used by devinit.exe lolbin to download
arbitrary MSI packages on a Windows system
More details
Rule ID
process_creation_commandline_100
Query
{'selection': {'CommandLine|contains|all': [' -t msi-
install ', ' -i http']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,90d50722-0483-4065-8e35-57efaadd354d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://twitter.com/mrd0x/status/1460815932402679809 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/11 high
Unknown
Sticky-Key Backdoor Copy Cmd.exe By replacing the sticky keys executable with the local admins CMD executable, an
attacker is able to access a privileged windows console session without authenticating
to the system. When the sticky keys are "activated" the privilleged shell is launched.
More details
Rule ID
process_creation_commandline_101
Query
{'selection': {'CommandLine': 'copy /y C:\\windows\\syst
em32\\cmd.exe C:\\windows\\system32\\sethc.exe'}, 'condi
tion': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,1070db9a-3e5d-412e-8e7b-7183b616e1b3
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.008 
References
https://www.fireeye.com/blog/threat-
research/2017/03/apt29_domain_frontin.html 
https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-
Kitten-Campaign-v1.pdf 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/02/18 medium
Unknown
Suspicious Use of Procdump on Detects suspicious uses of the SysInternals Procdump utility by using a special
LSASS command line parameter in combination with the lsass.exe process. This way we're also
able to catch cases in which the attacker has renamed the procdump executable.
More details
Rule ID
process_creation_commandline_102
Query
{'selection1': {'CommandLine|contains': [' -
ma ', ' /ma ']}, 'selection2': {'CommandLine|contains':
' ls'}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5afee48e-67dd-4e03-a783-f74259dcf998
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036 , TA0006 , T1003.001 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Title Description
Additional Information
Maturi Creation Risk False Positives
ty Date Level
stable 2018/10/3 high
Unlikely, because no one should dump an lsass
0 process memory
Another tool that uses the command line
switches of Procdump
Suspicious Rundll32 Activity Detects suspicious process related to rundll32 based on command line that includes a
Invoking Sys File *.sys file as seen being used by UNC2452
More details
Rule ID
process_creation_commandline_103
Query
{'selection1': {'CommandLine|contains': 'rundll32.exe'},
'selection2': {'CommandLine|contains': ['.sys,', '.sys
']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,731231b9-0b5d-4219-94dd-abb6959aa7ea
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-
sibot-analyzing-nobelium-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/03/05 high
Unknown
ETW Logging Tamper In .NET Detects changes to environment variables related to ETW logging. This could indicate
Processes potential adversaries stopping ETW providers recording loaded .NET assemblies.
More details
Rule ID
process_creation_commandline_104
Query

Title Description
{'selection': {'CommandLine|contains': ['COMPlus_ETWEnab
led', 'COMPlus_ETWFlags']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,41421f44-58f9-455d-838a-c398859841d4
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562 
References
https://twitter.com/_xpn_/status/1268712093928378368 
https://github.com/dotnet/runtime/blob/ee2355c801d892f2894b0f7b14a20e6c
c50e0e54/docs/design/coreclr/jit/viewing-jit-dumps.md#setting-configuration-
variables 
https://github.com/dotnet/runtime/blob/f62e93416a1799aecc6b0947adad55a
0d9870732/src/coreclr/src/inc/clrconfigvalues.h#L35-L38 
https://github.com/dotnet/runtime/blob/7abe42dc1123722ed385218268bb9fe
04556e3d3/src/coreclr/src/inc/clrconfig.h#L33-L39 
http://managed670.rssing.com/chan-5590147/all_p1.html 
https://github.com/dotnet/runtime/blob/4f9ae42d861fcb4be2fcd5d3d55d5f227
d30e723/docs/coding-guidelines/clr-jit-coding-conventions.md#1412-
disabling-code 
https://i.blackhat.com/EU-21/Wednesday/EU-21-Teodorescu-Veni-No-Vidi-
No-Vici-Attacks-On-ETW-Blind-EDRs.pdf 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/02 high
Unlikely
Suspicious WMIC Execution - Detects WMIC executing "process call create" with suspicious calls to processes such
ProcessCallCreate as "rundll32", "regsrv32"...etc
More details
Rule ID
process_creation_commandline_105
Query
{'selection': {'CommandLine|contains|all': ['process ',
'call ', 'create '], 'CommandLine|contains': ['rundll32'
, 'bitsadmin', 'regsvr32', 'cmd.exe /c ', 'cmd.exe /k ',
'cmd.exe /r ', 'cmd /c ', 'cmd /k ', 'cmd /r ', 'powers
hell', 'pwsh', 'certutil', 'cscript', 'wscript', 'mshta'
, '\\Users\\Public\\', '\\Windows\\Temp\\', '\\AppData\\
Local\\', '%temp%', '%tmp%', '%ProgramData%', '%appdata%

Title Description
', '%comspec%', '%localappdata%']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3c89a1e8-0fba-449e-8f1b-8409d6267ec8
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1047 , T1059.003 
References
https://thedfirreport.com/2020/10/08/ryuks-return/ 
https://symantec-enterprise-blogs.security.com/blogs/threat-
intelligence/ransomware-hive-conti-avoslocker 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/12 high
Unknown
Potential APT-C-12 BlueMushroom Detects potential BlueMushroom DLL loading activity via regsvr32 from AppData Local
DLL Load Activity Via Regsvr32
More details
Rule ID
process_creation_commandline_106
Query
{'selection': {'CommandLine|contains|all': ['regsvr32',
'\\AppData\\Local\\', '.dll', ',DllEntry']}, 'condition'
: 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bd70d3f8-e60e-4d25-89f0-0b5a9cff20e0
Author: Florian Roth (Nextron Systems), Tim Shelton, Nasreddine Bencherchali
(Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.010 
References
https://pbs.twimg.com/media/EF3yLGoWkAEGeLa?format=jpg 

p p g y jpg
Title Description
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/02 medium
Unknown
Mshtml DLL RunHTMLApplication Detects suspicious command line using the "mshtml.dll" RunHTMLApplication export to
Abuse run arbitrary code via different protocol handlers (vbscript, javascript, file, htpp...)
More details
Rule ID
process_creation_commandline_107
Query
{'selection': {'CommandLine|contains|all': ['\\..\\', 'm
shtml', 'RunHTMLApplication']}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,4782eb5a-a513-4523-a0ac-f3082b26ac5c
Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron
Systems), Josh Nickels, frack113, Zaw Min Htun (ZETA)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/n1nj4sec/status/1421190238081277959 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/14 high
Unlikely
Persistence Via TypedPaths - Detects modification addition to the 'TypedPaths' key in the user or admin registry via
CommandLine the commandline. Which might indicate persistence attempt
More details
Rule ID

Title Description
process_creation_commandline_109
Query
{'selection': {'CommandLine|contains': '\\Software\\Micr
osoft\\Windows\\CurrentVersion\\Explorer\\TypedPaths'},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ec88289a-7e1a-4cc3-8d18-bd1f60e4b9ba
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/dez_/status/1560101453150257154 
https://forensafe.com/blogs/typedpaths.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/22 medium
Unknown
UtilityFunctions.ps1 Proxy Dll Detects the use of a Microsoft signed script executing a managed DLL with PowerShell.
More details
Rule ID
process_creation_commandline_110
Query
{'selection': {'CommandLine|contains': ['UtilityFunction
s.ps1', 'RegSnapin ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0403d67d-6227-4ea8-8145-4e72db7da120
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References

Title Description
https://lolbas-project.github.io/lolbas/Scripts/UtilityFunctions/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/28 medium
Unknown
Unidentified Attacker November A sigma rule detecting an unidetefied attacker who used phishing emails to target high
2018 profile orgs on November 2018. The Actor shares some TTPs with YYTRIUM/APT29
campaign in 2016.
More details
Rule ID
process_creation_commandline_111
Query
{'selection': {'CommandLine|contains': 'cyzfc.dat,', 'Co
mmandLine|endswith': 'PointFunctionCall'}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7453575c-a747-40b9-839b-125a0aae324b
Author: Florian Roth (Nextron Systems), @41thexplorer
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://twitter.com/DrunkBinary/status/1063075530180886529 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/11/20 high N/A
Powershell AMSI Bypass via .NET Detects Request to "amsiInitFailed" that can be used to disable AMSI Scanning
Reflection
More details
Rule ID
process_creation_commandline_112

Title Description
Query
{'selection': {'CommandLine|contains': ['System.Manageme
nt.Automation.AmsiUtils', 'amsiInitFailed']}, 'condition
': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,30edb182-aa75-42c0-b0a9-e998bb29067c
Author: Markus Neis, @Kostastsale
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://s3cur3th1ssh1t.github.io/Bypass_AMSI_by_manual_modification/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/08/17 high
Unlikely
PowerShell SAM Copy Detects suspicious PowerShell scripts accessing SAM hives
More details
Rule ID
process_creation_commandline_113
Query
{'selection_1': {'CommandLine|contains|all': ['\\Harddis
kVolumeShadowCopy', 'System32\\config\\sam']}, 'selectio
n_2': {'CommandLine|contains': ['Copy-
Item', 'cp $_.', 'cpi $_.', 'copy $_.', '.File]::Copy(']
}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1af57a4b-460a-4738-9034-db68b880c665
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003.002 
References

Title Description
https://twitter.com/splinter_code/status/1420546784250769408 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2021/07/29 high
Some rare backup scenarios
PowerShell scripts fixing HiveNightmare /
SeriousSAM ACLs
UAC Bypass Using Event Viewer Detects the pattern of UAC Bypass using Event Viewer RecentViews
RecentViews
More details
Rule ID
process_creation_commandline_114
Query
{'selection_path': {'CommandLine|contains': ['\\Event Vi
ewer\\RecentViews', '\\EventV~1\\RecentViews']}, 'select
ion_redirect': {'CommandLine|contains': '>'}, 'condition
': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,30fc8de7-d833-40c4-96b6-28319fbc4f6c
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/orange_8361/status/1518970259868626944 
https://lolbas-project.github.io/lolbas/Binaries/Eventvwr/#execute 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/11/22 high
Unknown

Title Description
Suspicious Office Token Search Via Detects possible search for office tokens via CLI by looking for the string "eyJ0eX". This
CLI string is used as an anchor to look for the start of the JWT token used by office and
similar apps.
More details
Rule ID
process_creation_commandline_115
Query
{'selection': {'CommandLine|contains': ['eyJ0eXAiOi', '
eyJ0eX', ' "eyJ0eX"', " 'eyJ0eX'"]}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6d3a3952-6530-44a3-8554-cf17c116c615
Author: Nasreddine Bencherchali (Nextron Systems), kagebunsher
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1528 
References
https://mrd0x.com/stealing-tokens-from-office-applications/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/10/ mediu
Legitimate command-lines containing the string
ental 25 m mentioned in the command-line
Change Default File Association To Detects when a program changes the default file association of any extension to an
Executable executable
More details
Rule ID
process_creation_commandline_116
Query
{'selection': {'CommandLine|contains|all': ['cmd', 'asso
c ', 'exefile'], 'CommandLine|contains': [' /c ', ' /r '
, ' /k ']}, 'filter': {'CommandLine|contains': '.exe=exe
file'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring process creation
Rule Source
SigmaHQ,ae6f14e6-14de-45b0-9f44-c0986f50dc89
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.001 
References
https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/assoc 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 high
Unknown
Conti Backup Database Detects a command used by conti to dump database
More details
Rule ID
process_creation_commandline_118
Query
{'selection_tools': {'CommandLine|contains': ['sqlcmd ',
'sqlcmd.exe']}, 'selection_svr': {'CommandLine|contains
': ' -
S localhost '}, 'selection_query': {'CommandLine|contain
s': ['sys.sysprocesses', 'master.dbo.sysdatabases', 'BAC
KUP DATABASE']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2f47f1fd-0901-466e-a770-3b7092834a1b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1005 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369e
e2389b9daecaf06331a95410aa5f8/detection 
https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-
ver15 
Severity

Title Description
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/16 high
Unknown
Winnti Pipemon Characteristics Detects specific process characteristics of Winnti Pipemon malware reported by ESET
More details
Rule ID
process_creation_commandline_119
Query
{'selection1': {'CommandLine|contains': 'setup0.exe -
p'}, 'selection2a': {'CommandLine|contains': 'setup.exe'
}, 'selection2b': {'CommandLine|endswith': ['-x:0', '-
x:1', '-
x:2']}, 'condition': 'selection1 or all of selection2*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,73d70463-75c9-4258-92c6-17500fe972f2
Author: Florian Roth (Nextron Systems), oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1574.002 
References
https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2020/07/30 critical
Legitimate setups that use similar flags
Suspicious ZipExec Execution ZipExec is a Proof-of-Concept (POC) tool to wrap binary-based tools into a password-
protected zip file.
More details
Rule ID
process_creation_commandline_120

Title Description
Query
{'run': {'CommandLine|contains|all': ['/generic:Microsof
t_Windows_Shell_ZipFolder:filename=', '.zip', '/pass:',
'/user:']}, 'delete': {'CommandLine|contains|all': ['/de
lete', 'Microsoft_Windows_Shell_ZipFolder:filename=', '.
zip']}, 'condition': 'run or delete'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,90dcf730-1b71-4ae7-9ffc-6fcf62bd0132
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 , T1202 
References
https://twitter.com/SBousseaden/status/1451237393017839616 
https://github.com/Tylous/ZipExec 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/07 medium
Unknown
NirCmd Tool Execution As LOCAL Detects the use of NirCmd tool for command execution as SYSTEM user
SYSTEM
More details
Rule ID
process_creation_commandline_121
Query
{'selection': {'CommandLine|contains': ' runassystem '},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d9047477-0359-48c9-b8c7-792cedcdc9c4
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 

Title Description
References
https://www.nirsoft.net/utils/nircmd.html 
https://www.winhelponline.com/blog/run-program-as-system-localsystem-
account-windows/ 
https://www.nirsoft.net/utils/nircmd2.html#using 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/24 high
Legitimate use by administrators
Invoke-Obfuscation Via Use Clip Detects Obfuscated Powershell via use Clip.exe in Scripts
More details
Rule ID
process_creation_commandline_122
Query
{'selection': {'CommandLine|contains|all': ['echo', 'cli
p', '&&'], 'CommandLine|contains': ['clipboard', 'invoke
', 'i`', 'n`', 'v`', 'o`', 'k`', 'e`']}, 'condition': 's
election'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e1561947-b4e3-4a74-9bdd-83baed21bdb5
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/09 high
Unknown

Title Description
PowerShell Base64 Encoded Detects Base64 encoded Shellcode
Shellcode
More details
Rule ID
process_creation_commandline_123
Query
{'selection': {'CommandLine|contains': ['OiCAAAAYInlM',
'OiJAAAAYInlM']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2d117e49-e626-4c7c-bd1f-c3c0147774c8
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1027 
References
https://twitter.com/cyb3rops/status/1063072865992523776 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/11/17 critical
Unknown
Ryuk Ransomware Detects Ryuk ransomware activity
More details
Rule ID
process_creation_commandline_124
Query
{'selection': {'CommandLine|contains|all': ['Microsoft\\
Windows\\CurrentVersion\\Run', 'C:\\users\\Public\\']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c37510b8-2107-4b78-aa32-72f251e7a844
Author: Florian Roth (Nextron Systems), Vasiliy Burov, Nasreddine Bencherchali
(Nextron Systems)

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547.001 
References
https://app.any.run/tasks/d860402c-3ff4-4c1f-b367-0237da714ed1/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/12/16 high
Unlikely
Arbitrary Shell Command Execution The .SettingContent-ms file type was introduced in Windows 10 and allows a user to
Via Settingcontent-Ms create "shortcuts" to various Windows 10 setting pages. These files are simply XML and
contain paths to various Windows 10 settings binaries.
More details
Rule ID
process_creation_commandline_125
Query
{'selection': {'CommandLine|contains': '.SettingContent-
ms'}, 'filter': {'CommandLine|contains': 'immersivecontr
olpanel'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,24de4f3b-804c-4165-b442-5a06a2302c7e
Author: Sreeman
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , TA0002 , T1204 , T1059.003 
References
https://posts.specterops.io/the-tale-of-settingcontent-ms-files-
f1ea253e4d39 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/03/13 medium
Unknown

Title Description
Base64 Encoded Reflective Detects base64 encoded .NET reflective loading of Assembly
Assembly Load
More details
Rule ID
process_creation_commandline_127
Query
{'selection': {'CommandLine|contains': ['WwBSAGUAZgBsAGU
AYwB0AGkAbwBuAC4AQQBzAHMAZQBtAGIAbAB5AF0AOgA6AEwAbwBhAGQ
AKA', 'sAUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGw
AeQBdADoAOgBMAG8AYQBkACgA', 'bAFIAZQBmAGwAZQBjAHQAaQBvAG
4ALgBBAHMAcwBlAG0AYgBsAHkAXQA6ADoATABvAGEAZAAoA', 'AFsAc
gBlAGYAbABlAGMAdABpAG8AbgAuAGEAcwBzAGUAbQBiAGwAeQBdADoAO
gAoACIATABvAGEAZAAiAC', 'BbAHIAZQBmAGwAZQBjAHQAaQBvAG4AL
gBhAHMAcwBlAG0AYgBsAHkAXQA6ADoAKAAiAEwAbwBhAGQAIgAp', 'A
WwByAGUAZgBsAGUAYwB0AGkAbwBuAC4AYQBzAHMAZQBtAGIAbAB5AF0A
OgA6ACgAIgBMAG8AYQBkACIAK', 'WwBSAGUAZgBsAGUAYwB0AGkAbwB
uAC4AQQBzAHMAZQBtAGIAbAB5AF0AOgA6ACgAIgBMAG8AYQBkACIAKQ'
, 'sAUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGwAeQB
dADoAOgAoACIATABvAGEAZAAiACkA', 'bAFIAZQBmAGwAZQBjAHQAaQ
BvAG4ALgBBAHMAcwBlAG0AYgBsAHkAXQA6ADoAKAAiAEwAbwBhAGQAIg
ApA', 'WwByAGUAZgBsAGUAYwB0AGkAbwBuAC4AYQBzAHMAZQBtAGIAb
AB5AF0AOgA6AEwAbwBhAGQAKA', 'sAcgBlAGYAbABlAGMAdABpAG8Ab
gAuAGEAcwBzAGUAbQBiAGwAeQBdADoAOgBMAG8AYQBkACgA', 'bAHIA
ZQBmAGwAZQBjAHQAaQBvAG4ALgBhAHMAcwBlAG0AYgBsAHkAXQA6ADoA
TABvAGEAZAAoA']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,62b7ccc9-23b4-471e-aa15-6da3663c4d59
Author: Christian Burkard (Nextron Systems), pH-T (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb276
5d0ea08dcb6/yara/mal_revil.yar 
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/01 high
Unlikely
Suspicious NT Resource Kit Threat actors can use an older version of the auditpol binary available inside the NT
Auditpol Usage resource kit to change audit policy configuration to impair detection capability. This can

Title Description
be carried out by selectively disabling/removing certain audit policies as well as restoring
a custom policy owned by the threat actor.
More details
Rule ID
process_creation_commandline_128
Query
{'selection': {'CommandLine|contains': ['/logon:none', '
/system:none', '/sam:none', '/privilege:none', '/object:
none', '/process:none', '/policy:none']}, 'condition': '
selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c6c56ada-612b-42d1-9a29-adad3c5c2c1e
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.002 
References
https://github.com/3CORESec/MAL-
CL/tree/master/Descriptors/Windows%202000%20Resource%20Kit%20Tools
/AuditPol 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/18 high
Unknown
Weak or Abused Passwords In CLI Detects weak passwords or often abused passwords (seen used by threat actors) via
the CLI. An example would be a threat actor creating a new user via the net command
and providing the password inline
More details
Rule ID
process_creation_commandline_129
Query
{'selection': {'CommandLine|contains': ['Asd123.aaaa', '
password123', '123456789', 'P@ssw0rd!']}, 'condition': '
selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,91edcfb1-2529-4ac2-9ecc-7617f895c7e4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://symantec-enterprise-blogs.security.com/blogs/threat-
intelligence/espionage-asia-governments 
https://thedfirreport.com/2022/09/26/bumblebee-round-two/ 
https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-
society-opportunistic-ransomware-campaigns-impacting-us-education-sector/

Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creatio Risk False Positives
y n Date Level
experim 2022/09/ mediu
Legitimate usage of the passwords by users via
ental 14 m commandline (should be discouraged)
Other currently unknown false positives
Suspicious Encoded Obfuscated Detects suspicious base64 encoded and obbfuscated LOAD string often used for
LOAD String reflection.assembly load
More details
Rule ID
process_creation_commandline_130
Query
{'selection': {'CommandLine|contains': ['OgA6ACgAIgBMACI
AKwAiAG8AYQBkACIAKQ', 'oAOgAoACIATAAiACsAIgBvAGEAZAAiACk
A', '6ADoAKAAiAEwAIgArACIAbwBhAGQAIgApA', 'OgA6ACgAIgBMA
G8AIgArACIAYQBkACIAKQ', 'oAOgAoACIATABvACIAKwAiAGEAZAAiA
CkA', '6ADoAKAAiAEwAbwAiACsAIgBhAGQAIgApA', 'OgA6ACgAIgB
MAG8AYQAiACsAIgBkACIAKQ', 'oAOgAoACIATABvAGEAIgArACIAZAA
iACkA', '6ADoAKAAiAEwAbwBhACIAKwAiAGQAIgApA', 'OgA6ACgAJ
wBMACcAKwAnAG8AYQBkACcAKQ', 'oAOgAoACcATAAnACsAJwBvAGEAZ
AAnACkA', '6ADoAKAAnAEwAJwArACcAbwBhAGQAJwApA', 'OgA6ACg
AJwBMAG8AJwArACcAYQBkACcAKQ', 'oAOgAoACcATABvACcAKwAnAGE
AZAAnACkA', '6ADoAKAAnAEwAbwAnACsAJwBhAGQAJwApA', 'OgA6A
CgAJwBMAG8AYQAnACsAJwBkACcAKQ', 'oAOgAoACcATABvAGEAJwArA
CcAZAAnACkA', '6ADoAKAAnAEwAbwBhACcAKwAnAGQAJwApA']}, 'c
ondition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,9c0295ce-d60d-40bd-bd74-84673b7592b1
Author: pH-T (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb276
5d0ea08dcb6/yara/mal_revil.yar 
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/01 high
Unlikely
RunXCmd Tool Execution As Detects the use of RunXCmd tool for command execution
System
More details
Rule ID
process_creation_commandline_131
Query
{'selection': {'CommandLine|contains|all': [' /account=s
ystem ', '/exec=']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,93199800-b52a-4dec-b762-75212c196542
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 
References
https://www.d7xtech.com/free-software/runx/ 
https://www.winhelponline.com/blog/run-program-as-system-localsystem-
account-windows/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2022/01/24 high
Legitimate use by administrators
Base64 Encoded Listing of Detects base64 encoded listing Win32_Shadowcopy
Shadowcopy
More details
Rule ID
process_creation_commandline_132
Query
{'selection': {'CommandLine|contains': ['VwBpAG4AMwAyAF8
AUwBoAGEAZABvAHcAYwBvAHAAeQAgAHwAIABGAG8AcgBFAGEAYwBoAC0
ATwBiAGoAZQBjAHQA', 'cAaQBuADMAMgBfAFMAaABhAGQAbwB3AGMAb
wBwAHkAIAB8ACAARgBvAHIARQBhAGMAaAAtAE8AYgBqAGUAYwB0A', '
XAGkAbgAzADIAXwBTAGgAYQBkAG8AdwBjAG8AcAB5ACAAfAAgAEYAbwB
yAEUAYQBjAGgALQBPAGIAagBlAGMAdA']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,47688f1b-9f51-4656-b013-3cc49a166a36
Author: Christian Burkard (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb276
5d0ea08dcb6/yara/mal_revil.yar 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/01 high
Unlikely
MERCURY Command Line Patterns Detects suspicious command line patterns as seen being used by MERCURY threat
actor
More details
Rule ID
process_creation_commandline_133
Query
{'selection_base': {'CommandLine|contains|all': ['-
exec bypass -w 1 -

Title Description
enc', 'UwB0AGEAcgB0AC0ASgBvAGIAIAAtAFMAYwByAGkAcAB0AEIAb
ABvAGMAaw']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a62298a3-1fe0-422f-9a68-ffbcbc5a123d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://www.microsoft.com/security/blog/2022/08/25/mercury-leveraging-
log4j-2-vulnerabilities-in-unpatched-systems-to-target-israeli-organizations/

Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/26 high
Unknown
DTRACK Process Creation Detects specific process parameters as seen in DTRACK infections
More details
Rule ID
process_creation_commandline_134
Query
{'selection': {'CommandLine|contains': ' echo EEEE > '},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f1531fa4-5b84-4342-8f68-9cf3fdbd83d4
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References
https://securelist.com/my-name-is-dtrack/93338/ 
https://app.any.run/tasks/4bc9860d-ab51-4077-9e09-59ad346b92fd/ 
https://app.any.run/tasks/ce4deab5-3263-494f-93e3-afb2b9d79f14/ 

Title Description
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/10/30 critical
Unlikely
Suspicious Netsh Discovery Adversaries may look for details about the network configuration and settings of systems
Command they access or through information discovery of remote systems
More details
Rule ID
process_creation_commandline_135
Query
{'selection': {'CommandLine|contains|all': ['netsh ', 's
how ', 'firewall '], 'CommandLine|contains': ['config ',
'state ', 'rule ', 'name=all']}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0e4164da-94bc-450d-a7be-a4b176179f1f
Author: frack113, Christopher Peacock '@securepeacock', SCYTHE '@scythe_io'
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1016 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1016/T101
6.md#atomic-test-2---list-windows-firewall-rules 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/07 low
Administrative activity
F-Secure C3 Load by Rundll32 F-Secure C3 produces DLLs with a default exported StartNodeRelay function.
More details
Rule ID

Title Description
process_creation_commandline_136
Query
{'selection': {'CommandLine|contains|all': ['rundll32.ex
e', '.dll', 'StartNodeRelay']}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b18c9d4c-fac9-4708-bd06-dd5bfacf200f
Author: Alfie Champion (ajpc500)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://github.com/FSecureLABS/C3/blob/11a081fd3be2aaf2a879f6b6e9a96e
cdd24966ef/Src/NodeRelayDll/NodeRelayDll.cpp#L12 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/06/02 critical
Unknown
Suspicious RunAs-Like Flag Detects suspicious command line flags that let the user set a target user and command
Combination as e.g. seen in PsExec-like tools
More details
Rule ID
process_creation_commandline_137
Query
{'selection_user': {'CommandLine|contains': [' -
u system ', ' --user system ', ' -u NT', ' -u "NT', " -
u 'NT", ' --system ', ' -
u administrator ']}, 'selection_command': {'CommandLine|
contains': [' -c cmd', ' -c "cmd', ' -c powershell', ' -
c "powershell', ' --command cmd', ' --
command powershell', ' -c whoami', ' -c wscript', ' -
c cscript']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,50d66fb0-03f8-4da0-8add-84e77d12a020

Title Description
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.trendmicro.com/en_us/research/22/k/hack-the-real-box-apt41-
new-subgroup-earth-longzhi.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/11 medium
Unknown
Stop Or Remove Antivirus Service Detects usage of 'Stop-Service' or 'Remove-Service' powershell cmdlet to disable AV
services. Adversaries may disable security tools to avoid possible detection of their tools
and activities by stopping antivirus service
More details
Rule ID
process_creation_commandline_138
Query
{'selection_action': {'CommandLine|contains': ['Stop-
Service ', 'Remove-
Service ']}, 'selection_product': {'CommandLine|contains
': [' McAfeeDLPAgentService', ' Trend Micro Deep Securit
y Manager', ' TMBMServer', 'Sophos', 'Symantec']}, 'cond
ition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6783aa9e-0dc3-49d4-a94a-8b39c5fd700b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/
T1562.001.md 
https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-
3-0-ransomware-attack/ 
Severity
74
Suppression Logic Based On

Title Description
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/07 high
Unknown
Adwind RAT / JRAT Detects javaw.exe in AppData folder as used by Adwind / JRAT
More details
Rule ID
process_creation_commandline_139
Query
{'selection': [{'CommandLine|contains|all': ['\\AppData\
\Roaming\\Oracle', '\\java', '.exe ']}, {'CommandLine|co
ntains|all': ['cscript.exe', 'Retrive', '.vbs ']}], 'con
dition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1fac1481-2dbc-48b2-9096-753c49b4ec71
Author: Florian Roth (Nextron Systems), Tom Ueltschi, Jonhnathan Ribeiro,
oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://www.hybrid-
analysis.com/sample/ba86fa0d4b6af2db0656a88b1dd29f36fe362473ae8ad0
4255c4e52f214a541c?environmentId=100 
https://www.first.org/resources/papers/conf2017/Advanced-Incident-
Detection-and-Threat-Hunting-using-Sysmon-and-Splunk.pdf 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/11/10 high N/A
Suspicious AdvancedRun Runas Detects the execution of AdvancedRun utility in the context of the TrustedInstaller,
Priv User SYSTEM, Local Service or Network Service accounts
More details
Rule ID
process_creation_commandline_140
Query

Title Description
{'selection': {'CommandLine|contains': ['/EXEFilename',
'/CommandLine']}, 'selection_runas': [{'CommandLine|cont
ains': [' /RunAs 8 ', ' /RunAs 4 ', ' /RunAs 10 ', ' /Ru
nAs 11 ']}, {'CommandLine|endswith': ['/RunAs 8', '/RunA
s 4', '/RunAs 10', '/RunAs 11']}], 'condition': 'all of
selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fa00b701-44c6-4679-994d-5a18afa8a707
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/splinter_code/status/1483815103279603714 
https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-
targeting-ukraine-9d5d158f19f3 
https://www.winhelponline.com/blog/run-program-as-system-localsystem-
account-windows/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/20 high
Unknown
ShimCache Flush Detects actions that clear the local ShimCache and remove forensic evidence
More details
Rule ID
process_creation_commandline_141
Query
{'selection1a': {'CommandLine|contains|all': ['rundll32'
, 'apphelp.dll']}, 'selection1b': {'CommandLine|contains
': ['ShimFlushCache', '#250']}, 'selection2a': {'Command
Line|contains|all': ['rundll32', 'kernel32.dll']}, 'sele
ction2b': {'CommandLine|contains': ['BaseFlushAppcompatC
ache', '#46']}, 'condition': '( selection1a and selectio
n1b ) or ( selection2a and selection2b )'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,b0524451-19af-4efa-a46f-562a977f792e
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1112 
References
https://medium.com/@blueteamops/shimcache-flush-89daff28d15e 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2021/02/01 high
Unknown
Sliver C2 Implant Activity Pattern Detects process activity patterns as seen being used by Sliver C2 framework implants
More details
Rule ID
process_creation_commandline_142
Query
{'selection_cmdline': {'CommandLine|contains': '-
NoExit -Command [Console]::OutputEncoding=
[Text.UTF8Encoding]::UTF8'}, 'condition': '1 of selectio
n*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,42333b2c-b425-441c-b70e-99404a17170f
Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://github.com/BishopFox/sliver/blob/79f2d48fcdfc2bee4713b78d431ea4b
27f733f30/implant/sliver/shell/shell_windows.go#L36 
https://www.microsoft.com/security/blog/2022/08/24/looking-for-the-sliver-
lining-hunting-for-emerging-command-and-control-frameworks/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/25 critical
Unlikely
Disabled IE Security Features Detects command lines that indicate unwanted modifications to registry keys that
disable important Internet Explorer security features
More details
Rule ID
process_creation_commandline_143
Query
{'selection1': {'CommandLine|contains|all': [' -
name IEHarden ', ' -
value 0 ']}, 'selection2': {'CommandLine|contains|all':
[' -name DEPOff ', ' -
value 1 ']}, 'selection3': {'CommandLine|contains|all':
[' -name DisableFirstRunCustomize ', ' -
value 2 ']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fb50eb7a-5ab1-43ae-bcc9-091818cb8424
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://unit42.paloaltonetworks.com/operation-ke3chang-resurfaces-with-
new-tidepool-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2020/06/ high
Unknown, maybe some security software installer
19 disables these features temporarily
Invoke-Obfuscation RUNDLL Detects Obfuscated Powershell via RUNDLL LAUNCHER
LAUNCHER
More details
Rule ID
process_creation_commandline_144
Query

Title Description
{'selection': {'CommandLine|contains|all': ['rundll32.ex
e', 'shell32.dll', 'shellexec_rundll', 'powershell']}, '
condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,056a7ee1-4853-4e67-86a0-3fd9ceed7555
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/18 medium
Unknown
Tasks Folder Evasion The Tasks folder in system32 and syswow64 are globally writable paths. Adversaries
can take advantage of this and load or influence any script hosts or ANY .NET
Application in Tasks to load and execute a custom assembly into cscript, wscript,
regsvr32, mshta, eventvwr
More details
Rule ID
process_creation_commandline_145
Query
{'selection1': {'CommandLine|contains': ['echo ', 'copy
', 'type ', 'file createnew']}, 'selection2': {'CommandL
ine|contains': [' C:\\Windows\\System32\\Tasks\\', ' C:\
\Windows\\SysWow64\\Tasks\\']}, 'condition': 'all of sel
ection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cc4e02ba-9c06-48e2-b09e-2500cace9ae0
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1574.002 

Title Description
References
https://twitter.com/subTee/status/1216465628946563073 
https://gist.github.com/am0nsec/8378da08f848424e4ab0cc5b317fdd26 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/13 high
Unknown
Sofacy Trojan Loader Activity Detects Trojan loader activity as used by APT28
More details
Rule ID
process_creation_commandline_146
Query
{'selection1': {'CommandLine|contains|all': ['rundll32.e
xe', '%APPDATA%\\']}, 'selection2': [{'CommandLine|conta
ins': '.dat",'}, {'CommandLine|endswith': ['.dll",#1', '
.dll #1', '.dll" #1']}], 'condition': 'all of selection*
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ba778144-5e3d-40cf-8af9-e28fb1df1e20
Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-
multiple-government-entities/ 
https://twitter.com/ClearskySec/status/960924755355369472 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/01 high
Unknown

Title Description
Suspicious Commandline Escape Detects suspicious process that use escape characters
More details
Rule ID
process_creation_commandline_147
Query
{'selection': {'CommandLine|contains': ['h^t^t^p', 'h"t"
t"p']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f0cdd048-82dc-4f7a-8a7a-b87a52b6d0fd
Author: juju4
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1140 
References
https://twitter.com/vysecurity/status/885545634958385153 
https://twitter.com/Hexacorn/status/885553465417756673 
https://twitter.com/Hexacorn/status/885570278637678592 
https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-
wild.html 
http://www.windowsinspired.com/understanding-the-command-line-string-
and-arguments-received-by-a-windows-program/ 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2018/12/ low
False positives depend on scripts and administrative
11 tools used in the monitored environment
Suspicious Rundll32 Invoking Inline Detects suspicious process related to rundll32 based on command line that invokes
VBScript inline VBScript as seen being used by UNC2452
More details
Rule ID
process_creation_commandline_148
Query
{'selection': {'CommandLine|contains|all': ['rundll32.ex
e', 'Execute', 'RegRead', 'window.close']}, 'condition':
'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1cc50f3f-1fc8-4acf-b2e9-6f172e1fdebd
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1055 
References
https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-
sibot-analyzing-nobelium-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/03/05 high
Unknown
Disabled Volume Snapshots Detects commands that temporarily turn off Volume Snapshots
More details
Rule ID
process_creation_commandline_149
Query
{'selection': {'CommandLine|contains|all': ['reg', ' add
', '\\Services\\VSS\\Diag', '/d Disabled']}, 'condition
': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,dee4af55-1f22-4e1d-a9d2-4bdc7ecb472a
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://twitter.com/0gtweet/status/1354766164166115331 
Severity
74
Suppression Logic Based On
computer_name

Title Description
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/28 high
Legitimate administration
PowerShell Get-Clipboard Cmdlet Detects usage of the 'Get-Clipboard' cmdlet via CLI
Via CLI
More details
Rule ID
process_creation_commandline_150
Query
{'selection': {'CommandLine|contains': 'Get-
Clipboard'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b9aeac14-2ffd-4ad3-b967-1354a4e628c3
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1115 
References
https://github.com/OTRF/detection-hackathon-apt29/issues/16 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/02 medium
Unknown
Suspicious Reg Add BitLocker Detects suspicious addition to BitLocker related registry keys via the reg.exe utility
More details
Rule ID
process_creation_commandline_151
Query
{'selection': {'CommandLine|contains|all': ['REG', 'ADD'
, '\\SOFTWARE\\Policies\\Microsoft\\FVE', '/v', '/f'], '
CommandLine|contains': ['EnableBDEWithNoTPM', 'UseAdvanc
edStartup', 'UseTPM', 'UseTPMKey', 'UseTPMKeyPIN', 'Reco
veryKeyMessageSource', 'UseTPMPIN', 'RecoveryKeyMessage'
]}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0e0255bf-2548-47b8-9582-c0955c9283f5
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1486 
References
https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-
ransomware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/15 high
Unlikely
Suspicious Reconnaissance Activity Detects suspicious reconnaissance command line activity on Windows systems using
Using Get-LocalGroupMember the PowerShell Get-LocalGroupMember Cmdlet
Cmdlet
More details
Rule ID
process_creation_commandline_152
Query
{'selection_cmdlet': {'CommandLine|contains': 'Get-
LocalGroupMember '}, 'selection_group': {'CommandLine|co
ntains': ['domain admins', ' administrator', ' administr
ateur', 'enterprise admins', 'Exchange Trusted Subsystem
', 'Remote Desktop Users', 'Utilisateurs du Bureau à dis
tance', 'Usuarios de escritorio remoto']}, 'condition':
'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c8a180d6-47a3-4345-a609-53f9c3d834fc
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1087.001 
References
https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/


Title Description
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/10 medium
Administrative activity
Conti Ransomware Execution Conti ransomware command line ioc
More details
Rule ID
process_creation_commandline_153
Query
{'selection': {'CommandLine|contains|all': ['-m ', '-
net ', '-size ', '-nomutex ', '-
p \\\\', '$']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,689308fc-cfba-4f72-9897-796c1dc61487
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1486 
References
https://news.sophos.com/en-us/2021/09/03/conti-affiliates-use-proxyshell-
exchange-exploit-in-ransomware-attacks/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/10/12 critical
Unlikely
Snatch Ransomware Detects specific process characteristics of Snatch ransomware word document droppers
More details
Rule ID
process_creation_commandline_154
Query

Title Description
{'selection': {'CommandLine|contains': ['shutdown /r /f
/t 00', 'net stop SuperBackupMan']}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5325945e-f1f0-406e-97b8-65104d393fff
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1204 , T1059.003 
References
https://news.sophos.com/en-us/2019/12/09/snatch-ransomware-reboots-pcs-
into-safe-mode-to-bypass-protection/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
stabl 2020/08/ high
Scripts that shutdown the system immediately and
e 26 reboot them in safe mode are unlikely
Copy from Volume Shadow Copy Detects a copy execution that targets a shadow copy (sometimes used to copy registry
hives that are in use)
More details
Rule ID
process_creation_commandline_155
Query
{'selection': {'CommandLine|contains': 'copy \\\\?
\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy'}, 'condi
tion': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c73124a7-3e89-44a3-bdc1-25fe4df754b1
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References

Title Description
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369e
e2389b9daecaf06331a95410aa5f8/detection 
https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/09 medium
Some rare backup scenarios
Suspicious VBScript UN2452 Detects suspicious inline VBScript keywords as used by UNC2452
Pattern
More details
Rule ID
process_creation_commandline_156
Query
{'selection': {'CommandLine|contains|all': ['Execute', '
CreateObject', 'RegRead', 'window.close', '\\Microsoft\\
Windows\\CurrentVersion']}, 'filter': {'CommandLine|cont
ains': '\\Software\\Microsoft\\Windows\\CurrentVersion\\
Run'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,20c3f09d-c53d-4e85-8b74-6aa50e2f1b61
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547.001 
References
https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-
sibot-analyzing-nobelium-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/03/05 high
Unknown

Title Description
Sensitive Registry Access via Detects a command that accesses password storing registry hives via volume shadow
Volume Shadow Copy backups
More details
Rule ID
process_creation_commandline_157
Query
{'selection_1': {'CommandLine|contains': '\\\\?
\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy'}, 'selec
tion_2': {'CommandLine|contains': ['\\NTDS.dit', '\\SYST
EM', '\\SECURITY', 'C:\\tmp\\log']}, 'condition': 'all o
f selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f57f8d16-1f39-4dcb-a604-6c73d9b54b3d
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369e
e2389b9daecaf06331a95410aa5f8/detection 
https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/09 high
Some rare backup scenarios
Abusable Invoke- RemoteFXvGPUDisablement.exe is an abusable, signed PowerShell host executable
ATHRemoteFXvGPUDisablementCo that was introduced in Windows 10 and Server 2019 (OS Build 17763.1339).
mmand
More details
Rule ID
process_creation_commandline_158
Query
{'selection_cmd': {'CommandLine|contains': 'Invoke-
ATHRemoteFXvGPUDisablementCommand '}, 'selection_opt': {
'CommandLine|contains': ['-ModuleName ', '-
ModulePath ', '-ScriptBlock ', '-

Title Description
RemoteFXvGPUDisablementFilePath']}, 'condition': 'all of
selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a6fc3c46-23b8-4996-9ea2-573f4c4d88c5
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T121
8.md 
https://github.com/redcanaryco/AtomicTestHarnesses/blob/7e1e4da116801e
3d6fcc6bedb207064577e40572/TestHarnesses/T1218_SignedBinaryProxyEx
ecution/InvokeRemoteFXvGPUDisablementCommand.ps1 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/13 medium
Unknown
Execute From Alternate Data Detects execution from an Alternate Data Stream (ADS). Adversaries may use NTFS file
Streams attributes to hide their malicious data in order to evade detection
More details
Rule ID
process_creation_commandline_159
Query
{'selection_stream': {'CommandLine|contains': 'txt:'}, '
selection_tools_type': {'CommandLine|contains|all': ['ty
pe ', ' > ']}, 'selection_tools_makecab': {'CommandLine|
contains|all': ['makecab ', '.cab']}, 'selection_tools_r
eg': {'CommandLine|contains|all': ['reg ', ' export ']},
'selection_tools_regedit': {'CommandLine|contains|all':
['regedit ', ' /E ']}, 'selection_tools_esentutl': {'Co
mmandLine|contains|all': ['esentutl ', ' /y ', ' /d ', '
/o ']}, 'condition': 'selection_stream and (1 of select
ion_tools_*)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,7f43c430-5001-4f8b-aaa9-c3b88f18fa5c
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1564.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/
T1564.004.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/01 medium
Unknown
Potential Tampering With Security Detects uninstallation or termination of security products using the WMIC utility
Products Via WMIC
More details
Rule ID
process_creation_commandline_160
Query
{'selection_cli_1': {'CommandLine|contains|all': ['wmic'
, 'product where ', 'call uninstall', '/nointeractive']}
, 'selection_cli_2': {'CommandLine|contains|all': ['wmic
', 'caption like '], 'CommandLine|contains': ['call dele
te', 'call terminate']}, 'selection_cli_3': {'CommandLin
e|contains|all': ['process ', 'where ', 'delete']}, 'sel
ection_product': {'CommandLine|contains': ['%carbon%', '
%cylance%', '%endpoint%', '%eset%', '%malware%', '%Sopho
s%', '%symantec%', 'Antivirus', 'AVG ', 'Carbon Black',
'CarbonBlack', 'Cb Defense Sensor 64-
bit', 'Crowdstrike Sensor', 'Cylance ', 'Dell Threat Def
ense', 'DLP Endpoint', 'Endpoint Detection', 'Endpoint P
rotection', 'Endpoint Security', 'Endpoint Sensor', 'ESE
T File Security', 'LogRhythm System Monitor Service', 'M
alwarebytes', 'McAfee Agent', 'Microsoft Security Client
', 'Sophos Anti-
Virus', 'Sophos AutoUpdate', 'Sophos Credential Store',
'Sophos Management Console', 'Sophos Management Database
', 'Sophos Management Server', 'Sophos Remote Management
System', 'Sophos Update Manager', 'Threat Protection',
'VirusScan', 'Webroot SecureAnywhere', 'Windows Defender
']}, 'condition': '1 of selection_cli_* and selection_pr
oduct'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,847d5ff3-8a31-4737-a970-aeae8fe21765
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://twitter.com/cglyer/status/1355171195654709249 
https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-
hours/ 
https://www.mandiant.com/resources/unc2165-shifts-to-evade-sanctions 
https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-
3-0-ransomware-attack/ 
https://www.trendmicro.com/en_us/research/23/a/vice-society-ransomware-
group-targets-manufacturing-companies.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/30 high
Legitimate administration
Potential Download/Upload Activity Detects usage of the "type" command to download/upload data from WebDAV server
Using Type Command
More details
Rule ID
process_creation_commandline_161
Query
{'selection_upload': {'CommandLine|contains|all': ['type
', ' > \\\\']}, 'selection_download': {'CommandLine|con
tains|all': ['type \\\\', ' > ']}, 'condition': '1 of se
lection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,aa0b3a82-eacc-4ec3-9150-b5a9a3e3f82f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://mr0range.com/a-new-lolbin-using-the-windows-type-command-to-
upload-download-files-81d7b6179e22 
Severity

Title Description
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/14 medium
Unknown
Invoke-Obfuscation Via Stdin Detects Obfuscated Powershell via Stdin in Scripts
More details
Rule ID
process_creation_commandline_162
Query
{'selection': {'CommandLine|contains|all': ['set', '&&']
, 'CommandLine|contains': ['environment', 'invoke', 'inp
ut']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9c14c9fa-1a63-4a64-8e57-d19280559490
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/12 high
Unknown
Wscript Shell Run In CommandLine Detects the presence of the keywords "Wscript", "Shell" and "Run" in the command,
which could indicate a suspicious activity
More details
Rule ID
process_creation_commandline_163
Query

Title Description
{'selection': {'CommandLine|contains|all': ['Wscript.',
'.Shell', '.Run']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2c28c248-7f50-417a-9186-a85b223010ee
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
http://blog.talosintelligence.com/2022/08/modernloader-delivers-multiple-
stealers.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2022/08/31 high
Rare legitimate inline scripting by some
ntal administrators
Reg Add RUN Key Detects suspicious command line reg.exe tool adding key to RUN key in Registry
More details
Rule ID
process_creation_commandline_164
Query
{'selection': {'CommandLine|contains|all': ['reg', ' ADD
', 'Software\\Microsoft\\Windows\\CurrentVersion\\Run']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,de587dce-915e-4218-aac4-835ca6af6f70
Author: Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547.001 
References
https://app.any.run/tasks/9c0f37bc-867a-4314-b685-e101566766d7/ 

Title Description
https://docs.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-
registry-keys 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2021/06 mediu
Legitimate software automatically (mostly, during
/28 m installation) sets up autorun keys for legitimate
reasons.
Legitimate administrator sets up autorun keys for
legitimate reasons.
Discord
Disable or Delete Windows Eventlog Detects command that is used to disable or delete Windows eventlog via logman
Windows utility
More details
Rule ID
process_creation_commandline_165
Query
{'selection_tools': {'CommandLine|contains': 'logman '},
'selection_action': {'CommandLine|contains': ['stop ',
'delete ']}, 'selection_service': {'CommandLine|contains
': 'EventLog-System'}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cd1f961e-0b96-436b-b7c6-38da4583ec00
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 , T1070.001 
References
https://twitter.com/0gtweet/status/1359039665232306183?s=21 
https://ss64.com/nt/logman.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Matur Creation Risk False Positives
ity Date Level
test 2021/02/ high
Legitimate deactivation by administrative staff
11
Installer tools that disable services, e.g. before log
collection agent installation
Java Running with Remote Detects a JAVA process running with remote debugging allowing more than just
Debugging localhost to connect
More details
Rule ID
process_creation_commandline_166
Query
{'selection_jdwp_transport': {'CommandLine|contains': 't
ransport=dt_socket,address='}, 'selection_old_jvm_versio
n': {'CommandLine|contains': ['jre1.', 'jdk1.']}, 'exclu
sion': [{'CommandLine|contains': 'address=127.0.0.1'}, {
'CommandLine|contains': 'address=localhost'}], 'conditio
n': 'all of selection* and not exclusion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8f88e3f6-2a49-48f5-a5c4-2f7eedf78710
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1203 , T1059.003 
References
https://dzone.com/articles/remote-debugging-java-applications-with-jdwp 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/01/16 medium
Unknown
Monitoring For Persistence Via BITS BITS will allow you to schedule a command to execute after a successful download to
notify you that the job is finished. When the job runs on the system the command
specified in the BITS job will be executed. This can be abused by actors to create a
backdoor within the system and for persistence. It will be chained in a BITS job to
schedule the download of malware/additional binaries and execute the program after
being downloaded
More details
Rule ID

Title Description
process_creation_commandline_167
Query
{'selection_1': {'CommandLine|contains|all': ['bitsadmin
', '/SetNotifyCmdLine'], 'CommandLine|contains': ['%COMS
PEC%', 'cmd.exe', 'regsvr32.exe']}, 'selection_2': {'Com
mandLine|contains|all': ['bitsadmin', '/Addfile'], 'Comm
andLine|contains': ['http:', 'https:', 'ftp:', 'ftps:']}
, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b9cbbc17-d00d-4e3d-a827-b06d03d2380d
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1197 
References
https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-
with-a-ransomware-chaser.html 
http://0xthem.blogspot.com/2014/03/t-emporal-persistence-with-and-
schtasks.html 
https://isc.sans.edu/diary/Wipe+the+drive+Stealthy+Malware+Persistence+M
echanism+-+Part+1/15394 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/29 medium
Unknown
Obfuscated Command Line Using Adversaries may attempt to make an executable or file difficult to discover or analyze by
Special Unicode Characters encrypting, encoding, or otherwise obfuscating its contents on the system or in transit.
More details
Rule ID
process_creation_commandline_168
Query
{'selection': {'CommandLine|contains': ['â', '€', '£', '
¯', '®', 'µ', '¶']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,e0552b19-5a83-4222-b141-b36184bb8d79
Author: frack113, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1027 
References
https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027/T102
7.md#atomic-test-6---dlp-evasion-via-sensitive-data-in-vba-macro-over-
http 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/15 high
Unknown
Compress Data and Lock With An adversary may compress or encrypt data that is collected prior to exfiltration using
Password for Exfiltration With 7-ZIP 3rd party utilities
More details
Rule ID
process_creation_commandline_169
Query
{'selection_7z': {'CommandLine|contains': ['7z.exe', '7z
a.exe']}, 'selection_password': {'CommandLine|contains':
' -
p'}, 'selection_action': {'CommandLine|contains': [' a '
, ' u ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9fbf5927-5261-4284-a71d-f681029ea574
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/
T1560.001.md 
Severity
49

Title Description
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/07/2 medium
Command line parameter combinations that
7 contain all included strings
Suspicious DIR Execution Detects usage of the "dir" command that's part of windows batch/cmd to collect
information about directories
More details
Rule ID
process_creation_commandline_170
Query
{'selection': {'CommandLine|contains|all': ['dir ', ' /s
', ' /b']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7c9340a9-e2ee-4e43-94c5-c54ebbea1006
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1217 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T121
7.md 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/13 low
Unknown
Suspicious Diantz Download and Download and compress a remote file and store it in a cab file on local machine.
Compress Into a CAB File
More details
Rule ID
process_creation_commandline_172
Query

Title Description
{'selection': {'CommandLine|contains|all': ['diantz.exe'
, ' \\\\', '.cab']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,185d7418-f250-42d0-b72e-0c8b70661e93
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://lolbas-project.github.io/lolbas/Binaries/Diantz/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/26 medium
Unknown
Invoke-Obfuscation VAR++ Detects Obfuscated Powershell via VAR++ LAUNCHER
LAUNCHER OBFUSCATION
More details
Rule ID
process_creation_commandline_173
Query
{'selection': {'CommandLine|contains|all': ['&&set', 'cm
d', '/c', '-
f'], 'CommandLine|contains': ['{0}', '{1}', '{2}', '{3}'
, '{4}', '{5}']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e9f55347-2928-4c06-88e5-1a7f8169942e
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity

Title Description
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 high
Unknown
Ps.exe Renamed SysInternals Tool Detects renamed SysInternals tool execution with a binary named ps.exe as used by
Dragonfly APT group and documented in TA17-293A report
More details
Rule ID
process_creation_commandline_174
Query
{'selection': {'CommandLine': 'ps.exe -
accepteula'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,18da1007-3f26-470f-875d-f77faf1cab31
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036.003 
References
https://www.us-cert.gov/ncas/alerts/TA17-293A 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/10/22 high
Renamed SysInternals tool
TropicTrooper Campaign November Detects TropicTrooper activity, an actor who targeted high-profile organizations in the
2018 energy and food and beverage sectors in Asia
More details
Rule ID
process_creation_commandline_175
Query

Title Description
{'selection': {'CommandLine|contains': 'abCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCc'}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8c7090c3-e0a0-4944-bd08-08c3a0cecf79
Author: @41thexplorer, Microsoft Defender ATP
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://cloudblogs.microsoft.com/microsoftsecure/2018/11/28/windows-
defender-atp-device-risk-score-exposes-new-cyberattack-drives-conditional-
access-to-protect-networks/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/11/12 high N/A
Shadow Copies Access via Symlink Shadow Copies storage symbolic link creation using operating systems utilities
More details
Rule ID
process_creation_commandline_176
Query
{'selection': {'CommandLine|contains|all': ['mklink', 'H
arddiskVolumeShadowCopy']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,40b19fa6-d835-400c-b301-41f3a2baacaf
Author: Teymur Kheirkhabarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003 
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-
windows-environment 
Severity

Title Description
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
| Matu Creation Risk  | False Positives |     |
| ------------------- | --------------- | --- |
| rity Date Level     |                 |     |
| test 2019/10/ mediu |                 |     |
Legitimate administrator working with shadow
| 22 m | copies, access for backup purposes |     |
| ---- | ---------------------------------- | --- |
Suspicious Desktopimgdownldr Detects a suspicious Microsoft desktopimgdownldr execution with parameters used to
Command download files from the Internet
More details
Rule ID
process_creation_commandline_177
Query
{'selection1': {'CommandLine|contains': ' /lockscreenurl
:'}, 'selection1_filter': {'CommandLine|contains': ['.jp
g', '.jpeg', '.png']}, 'selection_reg': {'CommandLine|co
ntains|all': ['reg delete', '\\PersonalizationCSP']}, 'c
ondition': '( selection1 and not selection1_filter ) or
selection_reg'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bb58aa4a-b80b-415a-a2c0-2f65a4c81009
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
| TA0002 , T1059.003 | , TA0011 , T1105 |    |
| ------------------- | ------------------ | --- |
References
https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-
| downldr/  |     |     |
| ---------- | --- | --- |
https://twitter.com/SBousseaden/status/1278977301745741825 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
| Matu Creatio Risk  | False Positives |     |
| ------------------ | --------------- | --- |
| rity n Date Level  |                 |     |
| test 2020/07/ high |                 |     |
False positives depend on scripts and administrative
| 03  | tools used in the monitored environment |     |
| --- | --------------------------------------- | --- |

Title Description
Rundll32 JS RunHTMLApplication Detects suspicious command line patterns used when rundll32 is used to run JavaScript
Pattern code
More details
Rule ID
process_creation_commandline_178
Query
{'selection1': {'CommandLine|contains|all': ['rundll32',
'javascript', '..\\..\\mshtml,RunHTMLApplication']}, 's
election2': {'CommandLine|contains': ';document.write();
GetObject("script'}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9f06447a-a33a-4cbe-a94f-a3f43184a7a3
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
http://hyp3rlinx.altervista.org/advisories/MICROSOFT_WINDOWS_DEFEND
ER_DETECTION_BYPASS.txt 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/14 high
Unlikely
ADCSPwn Hack Tool Detects command line parameters used by ADCSPwn, a tool to escalate privileges in an
active directory network by coercing authenticate from machine accounts and relaying to
the certificate service
More details
Rule ID
process_creation_commandline_179
Query
{'selection': {'CommandLine|contains|all': [' --
adcs ', ' --port ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,cd8c163e-a19b-402e-bdd5-419ff5859f12
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1557.001 
References
https://github.com/bats3c/ADCSPwn 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/31 high
Unlikely
Potential PowerShell Execution Detects changes to the PowerShell execution policy registry key in order to bypass
Policy Tampering - ProcCreation signing requirements for script execution from the CommandLine
More details
Rule ID
process_creation_commandline_180
Query
{'selection_path': {'CommandLine|contains': ['\\ShellIds
\\Microsoft.PowerShell\\ExecutionPolicy', '\\Policies\\M
icrosoft\\Windows\\PowerShell\\ExecutionPolicy']}, 'sele
ction_values': {'CommandLine|contains': ['Bypass', 'Remo
teSigned', 'Unrestricted']}, 'condition': 'all of select
ion_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cf2e938e-9a3e-4fe8-a347-411642b28a9f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://learn.microsoft.com/de-
de/powershell/module/microsoft.powershell.security/set-executionpolicy?
view=powershell-7.3 
Severity
74
Suppression Logic Based On

Title Description
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/11 high
Unknown
CrackMapExec PowerShell The CrachMapExec pentesting framework implements a PowerShell obfuscation with
Obfuscation some static strings detected by this rule.
More details
Rule ID
process_creation_commandline_181
Query
{'powershell_execution': {'CommandLine|contains': ['powe
rshell.exe', 'pwsh.exe']}, 'snippets': {'CommandLine|con
tains': ['join*split', "
( $ShellId[1]+$ShellId[13]+'x')", '( $PSHome[*]+$PSHOME[
*]+', "( $env:Public[13]+$env:Public[5]+'x')", "
( $env:ComSpec[4,*,25]-Join'')", "[1,3]+'x'-
Join'')"]}, 'condition': 'powershell_execution and snipp
ets'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6f8b3439-a203-45dc-a88b-abf57ea15ccf
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027.005 
References
https://github.com/byt3bl33d3r/CrackMapExec 
https://github.com/byt3bl33d3r/CrackMapExec/blob/0a49f75347b625e81ee6a
a8c33d3970b5515ea9e/cme/helpers/powershell.py#L242 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/22 high
Unknown
Copy DMP Files From Share Detects usage of the copy command to copy files with the .dmp extensions from a
remote share
More details

Title Description
Rule ID
process_creation_commandline_182
Query
{'selection': {'CommandLine|contains|all': ['.dmp', 'cop
y ', ' \\\\'], 'CommandLine|contains': [' /c ', ' /r ',
' /k ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,044ba588-dff4-4918-9808-3f95e8160606
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://thedfirreport.com/2022/09/26/bumblebee-round-two/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/27 high
Unknown
Deletion of Volume Shadow Copies Detects deletion of Windows Volume Shadow Copies with PowerShell code and Get-
via WMI with PowerShell WMIObject. This technique is used by numerous ransomware families such as
Sodinokibi/REvil
More details
Rule ID
process_creation_commandline_183
Query
{'selection_get': {'CommandLine|contains': ['Get-
WmiObject', 'gwmi', 'Get-
CimInstance', 'gcim']}, 'selection_shadowcopy': {'Comman
dLine|contains': 'Win32_Shadowcopy'}, 'selection_delete'
: {'CommandLine|contains': ['.Delete()', 'Remove-
WmiObject', 'rwmi', 'Remove-
CimInstance', 'rcim']}, 'condition': 'all of selection*'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,21ff4ca9-f13a-41ad-b828-0077b2af2e40
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T149
0.md#atomic-test-5---windows---delete-volume-shadow-copies-via-wmi-with-
powershell 
https://www.elastic.co/guide/en/security/current/volume-shadow-copy-
deletion-via-powershell.html 
Severity
80
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/20 high
Unknown
ScreenConnect Remote Access Detects ScreenConnect program starts that establish a remote access to that system
(not meeting, not remote support)
More details
Rule ID
process_creation_commandline_184
Query
{'selection': {'CommandLine|contains|all': ['e=Access&',
'y=Guest&', '&p=', '&c=', '&k=']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,75bfe6e6-cd8e-429e-91d3-03921e1d7962
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1133 
References
https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-
conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-
agencies 
Severity
74
Suppression Logic Based On
computer_name

Title Description
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/02/11 high
Legitimate use by administrative staff
Curl Start Combination Adversaries can use curl to download payloads remotely and execute them. Curl is
included by default in Windows 10 build 17063 and later.
More details
Rule ID
process_creation_commandline_185
Query
{'selection': {'CommandLine|contains|all': [' /c ', 'cur
l ', 'http', '-o', '&']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,21dd6d38-2b18-4453-9404-a0fe4a0cc288
Author: Sreeman, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 , TA0011 , T1105 
References
https://medium.com/@reegun/curl-exe-is-the-new-rundll32-exe-lolbin-
3f79c5f35983 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/13 high
Administrative scripts (installers)
Suspicious Usage of the Manage- Detects usage of the manage-bde.wsf script that may indicate an attempt of proxy
bde.wsf Script execution from script
More details
Rule ID
process_creation_commandline_186
Query
{'selection': {'CommandLine|contains|all': ['cscript', '
manage-bde.wsf']}, 'condition': 'selection'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c363385c-f75d-4753-a108-c1a8e28bdbda
Author: oscd.community, Natalia Shornikova, Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/Manage-bde/ 
https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712 
https://twitter.com/bohops/status/980659399495741441 
https://twitter.com/JohnLaTwC/status/1223292479270600706 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1216/T121
6.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 medium
Unknown
Potential COM Objects Download Detects usage of COM objects that can be abused to download files in PowerShell by
Cradles Usage - Process Creation CLSID
More details
Rule ID
process_creation_commandline_187
Query
{'selection_1': {'CommandLine|contains': '[Type]::GetTyp
eFromCLSID('}, 'selection_2': {'CommandLine|contains': [
'0002DF01-0000-0000-C000-000000000046', 'F6D90F16-9C73-
11D3-B32E-00C04F990BB4', 'F5078F35-C551-11D3-89B9-
0000F81FE221', '88d96a0a-f192-11d4-a65f-
0040963251e5', 'AFBA6B42-5692-48EA-8141-
DC517DCF0EF1', 'AFB40FFD-B609-40A3-9828-
F88BBE11E4E3', '88d96a0b-f192-11d4-a65f-
0040963251e5', '2087c2f4-2cef-4953-a8ab-
66779b670495', '000209FF-0000-0000-C000-
000000000046', '00024500-0000-0000-C000-
000000000046']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,02b64f1b-3f33-4e67-aede-ef3b0a5a8fcf
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://learn.microsoft.com/en-us/dotnet/api/system.type.gettypefromclsid?
view=net-7.0 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=57 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/25 medium
Legitimate use of the library
Base64 MZ Header In Detects encoded base64 MZ header in the commandline
CommandLine
More details
Rule ID
process_creation_commandline_188
Query
{'selection': {'CommandLine|contains': ['TVqQAAMAAAAEAAA
A', 'TVpQAAIAAAAEAA8A', 'TVqAAAEAAAAEABAA', 'TVoAAAAAAAA
AAAAA', 'TVpTAQEAAAAEAAAA']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,22e58743-4ac8-4a9f-bf19-00a0428d8c5f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/07/12 high
Unlikely
Capture a Network Trace with Detects capture a network trace via netsh.exe trace functionality
netsh.exe
More details
Rule ID
process_creation_commandline_189
Query
{'selection': {'CommandLine|contains|all': ['netsh', 'tr
ace', 'start']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d3c3861d-c504-4c77-ba55-224ba82d0118
Author: Kutepov Anton, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1040 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2019/10/ mediu
Legitimate administrator or user uses netsh.exe
24 m trace functionality for legitimate reason
Baby Shark Activity Detects activity that could be related to Baby Shark malware
More details
Rule ID
process_creation_commandline_190
Query
{'selection': {'CommandLine|contains': ['reg query "HKEY
_CURRENT_USER\\Software\\Microsoft\\Terminal Server Clie
nt\\Default"', 'powershell.exe mshta.exe http', 'cmd.exe
/c taskkill /im cmd.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring process creation
Rule Source
SigmaHQ,2b30fa36-3a18-402f-a22d-bf4ce2189f35
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1218.005 , TA0007 , T1012 
References
https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-
national-security-think-tanks/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/02/24 high
Unknown
Suspicious Ping/Del Command Detects a method often used by ransomware. Which combines the "ping" to wait a
Combination couple of seconds and then "del" to delete the file in question. Its used to hide the file
responsible for the initial infection for example
More details
Rule ID
process_creation_commandline_191
Query
{'selection_count': {'CommandLine|contains': [' -
n ', ' /n ']}, 'selection_nul': {'CommandLine|contains':
'Nul'}, 'selection_del_param': {'CommandLine|contains':
[' /f ', ' -f ', ' /q ', ' -
q ']}, 'selection_all': {'CommandLine|contains|all': ['p
ing', 'del ']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,54786ddc-5b8a-11ed-9b6a-0242ac120002
Author: Ilya Krestinichev
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1070.004 
References
https://blog.sygnia.co/kaseya-ransomware-supply-chain-attack 
https://media.kasperskycontenthub.com/wp-
content/uploads/sites/43/2022/06/23093553/Common-TTPs-of-the-modern-
ransomware_low-res.pdf 

Title Description
https://www.acronis.com/en-us/blog/posts/lockbit-ransomware/ 
https://symantec-enterprise-blogs.security.com/blogs/threat-
intelligence/blackbyte-exbyte-ransomware 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2022/11/0 high
False positive could occur in admin scripts
ntal 3 that execute inline
Change Default File Association When a file is opened, the default program used to open the file (also called the file
association or handler) is checked. File association selections are stored in the Windows
Registry and can be edited by users, administrators, or programs that have Registry
access or by administrators using the built-in assoc utility. Applications can modify the
file association for a given file extension to call an arbitrary program when a file with the
given extension is opened.
More details
Rule ID
process_creation_commandline_192
Query
{'selection': {'CommandLine|contains|all': ['cmd', 'asso
c'], 'CommandLine|contains': [' /c ', ' /k ', ' /r ']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3d3aa6cd-6272-44d6-8afc-7e88dfef7061
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.001/
T1546.001.md 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2019/10/21 low
Admin activity
PowerShell Web Download and Detects suspicious ways to download files or content and execute them using
Execution PowerShell Invoke-Expression
More details
Rule ID
process_creation_commandline_193
Query
{'selection_download': {'CommandLine|contains': ['.Downl
oadString(', '.DownloadFile(', 'Invoke-
WebRequest ', 'iwr ']}, 'selection_iex': {'CommandLine|c
ontains': ['IEX(', 'IEX (', 'I`EX', 'IE`X', 'I`E`X', '|
IEX', '|IEX ', 'Invoke-
Expression', ';iex $']}, 'condition': 'all of selection_
*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,85b0b087-eddf-4a2b-b033-d771fa2b9775
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://github.com/VirtualAlllocEx/Payload-Download-
Cradles/blob/88e8eca34464a547c90d9140d70e9866dcbc6a12/Download-
Cradles.cmd 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2022/03/24 high
Scripts or tools that download files and
tal execute them
Empire PowerShell Launch Detects suspicious powershell command line parameters used in Empire
Parameters
More details
Rule ID
process_creation_commandline_194
Query

Title Description
{'selection': {'CommandLine|contains': [' -NoP -sta -
NonI -W Hidden -Enc ', ' -noP -sta -w 1 -enc ', ' -NoP -
NonI -W Hidden -enc ', ' -noP -sta -w 1 -enc', ' -
enc SQB', ' -nop -exec bypass -
EncodedCommand ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,79f4ede3-402e-41c8-bc3e-ebbf5f162581
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://github.com/EmpireProject/Empire/blob/c2ba61ca8d2031dad0cfc1d577
0ba723e8b710db/lib/common/helpers.py#L165 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f4
24906fe13055/lib/modules/powershell/persistence/powerbreach/deaduser.py
#L191 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f4
24906fe13055/lib/modules/powershell/persistence/powerbreach/resolver.py#
L178 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f4
24906fe13055/data/module_source/privesc/Invoke-
EventVwrBypass.ps1#L64 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2019/04/2 high
Other tools that incidentally use the same
0 command line parameters
Invoke-Obfuscation STDIN+ Detects Obfuscated use of stdin to execute PowerShell
Launcher
More details
Rule ID
process_creation_commandline_195
Query
{'selection_main': {'CommandLine|contains|all': ['cmd',
'powershell'], 'CommandLine|contains': ['/c', '/r']}, 's
election_other': [{'CommandLine|contains': 'noexit'}, {'
CommandLine|contains|all': ['input', '$']}], 'condition'
: 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring process creation
Rule Source
SigmaHQ,6c96fc76-0eb1-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/15 high
Unknown
Conti NTDS Exfiltration Command Detects a command used by conti to exfiltrate NTDS
More details
Rule ID
process_creation_commandline_196
Query
{'selection': {'CommandLine|contains|all': ['7za.exe', '
\\C$\\temp\\log.zip']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,aa92fd02-09f2-48b0-8a93-864813fb8f41
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369e
e2389b9daecaf06331a95410aa5f8/detection 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high
Unknown
Covenant Launcher Indicators Detects suspicious command lines used in Covenant luanchers
More details
Rule ID
process_creation_commandline_198
Query
{'selection': {'CommandLine|contains|all': ['-Sta', '-
Nop', '-Window', 'Hidden'], 'CommandLine|contains': ['-
Command', '-
EncodedCommand']}, 'selection2': {'CommandLine|contains'
: ['sv o (New-
Object IO.MemorySteam);sv d ', 'mshta file.hta', 'GruntH
TTP', '-
EncodedCommand cwB2ACAAbwAgA']}, 'condition': 'selection
or selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c260b6db-48ba-4b4a-a76f-2f67644e99d2
Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1564.003 
References
https://posts.specterops.io/covenant-v0-5-eee0507b85ba 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/06/04 high N/A
UNC2452 PowerShell Pattern Detects a specific PowerShell command line pattern used by the UNC2452 actors as
mentioned in Microsoft and Symantec reports
More details
Rule ID
process_creation_commandline_199
Query

Title Description
{'selection1': {'CommandLine|contains|all': ['Invoke-
WMIMethod win32_process -name create -
argumentlist', 'rundll32 c:\\windows']}, 'selection2': {
'CommandLine|contains|all': ['wmic /node:', 'process cal
l create "rundll32 c:\\windows']}, 'condition': '1 of se
lection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b7155193-8a81-4d8f-805d-88de864ca50c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , T1047 
References
https://symantec-enterprise-blogs.security.com/blogs/threat-
intelligence/solarwinds-raindrop-malware 
https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-
compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-
microsoft-defender-helps-protect/ 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1047/T104
7.md#atomic-test-7---create-a-process-using-wmi-query-and-an-encoded-
command 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/20 critical
Unlikely
Launch-VsDevShell.PS1 Proxy Detects the use of the 'Launch-VsDevShell.ps1' Microsoft signed script to execute
Execution commands.
More details
Rule ID
process_creation_commandline_200
Query
{'selection_script': {'CommandLine|contains': 'Launch-
VsDevShell.ps1'}, 'selection_flags': {'CommandLine|conta
ins': ['VsWherePath ', 'VsInstallationPath ']}, 'conditi
on': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Title Description
SigmaHQ,45d3a03d-f441-458c-8883-df101a3bb146
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216.001 
References
https://twitter.com/nas_bench/status/1535981653239255040 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experiment 2022/08/19 medium
Legitimate usage of the script by a
al developer
Detect Virtualbox Driver Installation Adversaries can carry out malicious operations using a virtual instance to avoid
OR Starting Of VMs detection. This rule is built to detect the registration of the Virtualbox driver or start of a
Virtualbox VM.
More details
Rule ID
process_creation_commandline_201
Query
{'selection_1': {'CommandLine|contains': ['VBoxRT.dll,RT
R3Init', 'VBoxC.dll', 'VBoxDrv.sys']}, 'selection_2': {'
CommandLine|contains': ['startvm', 'controlvm']}, 'condi
tion': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bab049ca-7471-4828-9024-38279a4c04da
Author: Janantha Marasinghe
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1564.006 
References
https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-
deploys-virtual-machine-to-dodge-security/ 
https://threatpost.com/maze-ransomware-ragnar-locker-virtual-
machine/159350/ 
Severity
24
Suppression Logic Based On

Title Description
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creatio Risk False Positives
y n Date Level
experi 2020/09 low
This may have false positives on hosts where
mental /26 Virtualbox is legitimately being used for operations
Suspicious RDP Redirect Using Detects a suspicious RDP session redirect using tscon.exe
TSCON
More details
Rule ID
process_creation_commandline_202
Query
{'selection': {'CommandLine|contains': ' /dest:rdp-
tcp:'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f72aa3e8-49f9-4c7d-bd74-f8ab84ff9bbb
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1563.002 , T1021.001 
References
http://www.korznikov.com/2017/03/0-day-or-feature-privilege-
escalation.html 
https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-
remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/17 high
Unknown
Rar Usage with Password and Detects the use of rar.exe, on the command line, to create an archive with password
Compression Level protection or with a specific compression level. This is pretty indicative of malicious
actions.
More details
Rule ID
process_creation_commandline_203
Query

Title Description
{'selection_password': {'CommandLine|contains': ' -
hp'}, 'selection_other': {'CommandLine|contains': [' -
m', ' a ']}, 'condition': 'selection_password and select
ion_other'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,faa48cae-6b25-4f00-a094-08947fef582f
Author: @ROxPinTeddy
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560.001 
References
https://labs.sentinelone.com/the-anatomy-of-an-apt-attack-and-cobaltstrike-
beacons-encoded-configuration/ 
https://ss64.com/bash/rar.html 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/
T1560.001.md 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2020/05/12 high
Legitimate use of Winrar command line
version
Other command line tools, that use these
flags
Invoke-Obfuscation VAR+ Launcher Detects Obfuscated use of Environment Variables to execute PowerShell
More details
Rule ID
process_creation_commandline_204
Query
{'selection': {'CommandLine|contains|all': ['cmd', '"set
', '-
f'], 'CommandLine|contains': ['/c', '/r']}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,27aec9c9-dbb0-4939-8422-1742242471d0

Title Description
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
| TA0002 , T1059 | , TA0005 , T1027 |    |     |
| --------------- | ------------------ | --- | --- |
References
| https://github.com/SigmaHQ/sigma/issues/1009 |     |     |    |
| -------------------------------------------- | --- | --- | --- |
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |
| -------- | ------------- | ---------- | --------------- |
| test     | 2020/10/15    | high       |                 |
Unknown

Title Description
Suspicious SYSVOL Domain Group Detects Access to Domain Group Policies stored in SYSVOL
Policy Access
More details
Rule ID
process_creation_commandline_205
Query
{'selection': {'CommandLine|contains|all': ['\\SYSVOL\\'
, '\\policies\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,05f3c945-dcc8-4393-9f3d-af65077a8f86
Author: Markus Neis, Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1552.006 
References
https://adsecurity.org/?p=2288 
https://www.hybrid-
analysis.com/sample/f2943f5e45befa52fb12748ca7171d30096e1d4fc3c3655
61497c618341299d5?environmentId=100 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/04/09 medium
Administrative activity
AnyDesk Piped Password Via CLI Detects piping the password to an anydesk instance via CMD and the '--set-password'
flag.
More details
Rule ID
process_creation_commandline_206
Query
{'selection': {'CommandLine|contains|all': ['/c ', 'echo
', '.exe --set-password']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b1377339-fda6-477a-b455-ac0923f9ec2c

Title Description
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
| TA0002 , T1059.003 | , TA0011 , T1219 |    |
| ------------------- | ------------------ | --- |
References
| https://redcanary.com/blog/misbehaving-rats/ |     |    |
| -------------------------------------------- | --- | --- |
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
| Maturit Creatio Risk | False Positives |     |
| -------------------- | --------------- | --- |
| y n Date Level       |                 |     |
| experi 2022/09 mediu |                 |     |
Legitimate piping of the password to anydesk
| mental /28 m |     |     |
| ------------ | --- | --- |
Some FP could occure with similar tools that uses
the same command line '--set-password'
Suspicious PowerShell Mailbox Detects usage of the powerShell New-MailboxExportRequest Cmdlet to exports a
Export to Share mailbox to a remote or local share, as used in ProxyShell exploitations
More details
Rule ID
process_creation_commandline_207
Query
{'selection': {'CommandLine|contains|all': ['New-
MailboxExportRequest', ' -Mailbox ', ' -
FilePath \\\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,889719ef-dd62-43df-86c3-768fb08dc7c0
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
| TA0002 , T1059.003 |    |     |
| ------------------- | --- | --- |
References
| https://youtu.be/5mqid-7zp8k?t=2481 |     |    |
| ----------------------------------- | --- | --- |
https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-
| exchange-part-1.html |    |     |
| -------------------- | --- | --- |
https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-
| 49743a4ea9a1 |    |     |
| ------------ | --- | --- |
https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-
| server-logs/ |    |     |
| ------------ | --- | --- |
Severity
95

Title Description
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/07 critical
Unknown
Compress Data and Lock With An adversary may compress or encrypt data that is collected prior to exfiltration using
Password for Exfiltration With 3rd party utilities
WINZIP
More details
Rule ID
process_creation_commandline_208
Query
{'selection_winzip': {'CommandLine|contains': ['winzip.e
xe', 'winzip64.exe']}, 'selection_password': {'CommandLi
ne|contains': '-
s"'}, 'selection_other': {'CommandLine|contains': [' -
min ', ' -a ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e2e80da2-8c66-4e00-ae3c-2eebd29f6b6d
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/
T1560.001.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/27 medium
Unknown
Network Reconnaissance Activity Detects a set of suspicious network related commands often used in recon stages
More details
Rule ID
process_creation_commandline_209
Query

Title Description
{'selection_nslookup': {'CommandLine|contains|all': ['ns
lookup', '_ldap._tcp.dc._msdcs.']}, 'condition': '1 of s
election*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e6313acd-208c-44fc-a0ff-db85d572e90e
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1087 , T1082 
References
https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2022/02/ high
False positives depend on scripts and administrative
07 tools used in the monitored environment
File overwritten by cipher tool The Windows tool cipher can be used to remove data from available unused disk space
on the entire volume. Ransomware could use this technique to prevent the victim from
using file recovery tools to recover their files.
More details
Rule ID
process_creation_commandline_301
Query
{'selection3': {'Image|contains': '\\cipher.exe'}, 'sele
ction5': {'CommandLine|re': '\\/w\\:[A-Z]
{1}'}, 'condition': 'selection3 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A

Title Description
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
PowerShell reverse shell one-liner A PowerShell process with arguments that may indicate a reverse shell execution has
been detected.
More details
Rule ID
process_creation_commandline_302
Query
{'selection3': {'Image|contains': 'powershell.exe'}, 'se
lection5': {'CommandLine|contains': 'Sockets.TCPClient'}
, 'selection6': {'CommandLine|contains': 'GetStream()'},
'selection7': {'CommandLine|contains': 'IEX'}, 'selecti
on8': {'CommandLine|contains': 'DownloadString'}, 'selec
tion9': {'CommandLine|contains': 'mini-
reverse.ps1'}, 'condition': 'selection3 and ((selection5
and selection6) or (selection7 and selection8 and selec
tion9))'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Shellcode execution via Suspicious file/code has been executed via InstallUtil.exe. This is a common technique
InstallUtil.exe used by malware to install additional malicious components and/or execute Shellcode.
More details

Title Description
Rule ID
process_creation_commandline_303
Query
{'selection3': {'Image|contains': 'InstallUtil.exe'}, 's
election4': {'CommandLine|contains': '/LogToConsole=fals
e'}, 'selection5': {'CommandLine|contains': '/logfile= '
}, 'condition': 'selection3 and selection4 and selection
5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
ALPC Task Scheduler Exploit LPE Microsoft Windows task scheduler contains a local privilege escalation vulnerability in
the Advanced Local Procedure Call (ALPC) interface, which can allow an attacker to
perform a local privilege escalation.
More details
Rule ID
process_creation_commandline_304
Query
{'selection3': {'Image|contains': '\\schtasks.exe'}, 'se
lection5': {'CommandLine|contains': '/change /TN'}, 'sel
ection6': {'CommandLine|contains': '/RU'}, 'selection7':
{'CommandLine|contains': '/RP'}, 'condition': 'selectio
n3 and selection5 and selection6 and selection7'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
TA0003 , T1053.005 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Behavior DNS cache cleared The DNS cache has been cleared in the system.
More details
Rule ID
process_creation_commandline_305
Query
{'selection': {'Image|endswith': '\\ipconfig.exe', 'Comm
andLine|contains': '/flushdns', 'ParentImage|endswith':
['\\cmd.exe', '\\powershell.exe', '\\pwsh.exe', '\\wscri
pt.exe', '\\cscript.exe', '\\mshta.exe']}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
WMIC sending output to clipboard WMIC command is using /output:clipboard as a way to hide the normal output of
process creation that is printed when creating a process with WMIC.
More details
Rule ID

Title Description
process_creation_commandline_307
Query
{'selection3': {'Image|contains': '\\wmic.exe'}, 'select
ion5': {'CommandLine|contains': '/output:clipboard'}, 's
election6': {'CommandLine|contains': 'process call creat
e'}, 'condition': 'selection3 and selection5 and selecti
on6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1036 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
CnC Channel through Nslookup A Windows process was detected using Nslookup with abnormal flag(s) usually used by
malware to communicate with the Command and Control.
More details
Rule ID
process_creation_commandline_308
Query
{'selection3': {'Image|contains': '\\slookup.exe'}, 'sel
ection4': {'CommandLine|contains': ' aaaa'}, 'selection5
': {'CommandLine|contains': '=aaaa'}, 'selection6': {'Co
mmandLine|re': '[a-z0-9]{15,45}\\. [a-z0-9]{1,15}\\.[a-
z0-9]
{1,4}'}, 'condition': 'selection3 and (selection4 or sel
ection5) and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
WMIC Retrieving Security The wmic.exe command was executed to get information from the security
Configuration configurations. This could be an indication of malicious activity.
More details
Rule ID
process_creation_commandline_309
Query
{'selection3': {'Image|contains': '\\wmic.exe'}, 'select
ion4': {'CommandLine|contains': 'SecurityCenter2'}, 'sel
ection5': {'CommandLine|contains': ['AntiVirusProduct',
'FirewallProduct']}, 'condition': 'selection3 and select
ion4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1005 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Taskkill killing Antivirus process An attempt to kill an Antivirus process has been detected. This can be the result of a
manual command used by an attacker or an automated process as part of malware
being deployed in the system.

Title Description
More details
Rule ID
process_creation_commandline_310
Query
{'selection3': {'Image|contains': 'Taskkill'}, 'selectio
n4': {'CommandLine|re': '(?:fsav32|MsMpEng|FPAVServer|TM
BMSRV|Mcshield|avgnsx|AvastSvc|dwengine|secenter|avguard
|ccSvcHst|avp|360sd|360tray|AvastUi)\\.exe'}, 'condition
': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
WSH Injection via PubPrn An attempt to inject malicious code into a Microsoft signed WSH script has been
detected. This can be an attempt to bypass whitelisting restrictions.
More details
Rule ID
process_creation_commandline_312
Query
{'selection3': {'Image|contains': 'wscript.exe'}, 'selec
tion4': {'CommandLine|contains': 'pubprn.vbs'}, 'selecti
on5': {'CommandLine|contains': 'script:'}, 'condition':
'selection3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
TA0005 , T1055 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
AppLocker Bypass A successful attempt to bypass AppLocker has been detected. This can indicate an
attacker is trying to bypass whitelisting technologhies and escalate privileges or/and
move laterally in your network.
More details
Rule ID
process_creation_commandline_314
Query
{'selection3': {'Image|contains': '\\regsvr32.exe'}, 'se
lection4': {'CommandLine|contains': '/s'}, 'selection5':
{'CommandLine|contains': '/i:http'}, 'selection6': {'Co
mmandLine|contains': 'scrobj.dll'}, 'condition': 'select
ion3 and selection4 and selection5 and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.010 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
File Deletion Backup files deleted An attempt to delete files and folders that migth contain backup data has been detected.
recursively This could be an indication of a ransomware infection or an attacker trying to cause
damage.

Title Description
More details
Rule ID
process_creation_commandline_315
Query
{'selection3': {'Image|contains': '\\cmd.exe'}, 'selecti
on4': {'CommandLine|contains': ' del '}, 'selection5': {
'CommandLine|re': '(?:backup|bkup|\\.bak|\\.bac|\\.dsk|\
\.win|\\.bkf|\\.wbcat)'}, 'condition': 'selection3 and s
election4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Attempt to stop or delete Windows Windows Defender Real-time Protection scanning for malware and other potentially
Defender service unwanted software has been stopped.
More details
Rule ID
process_creation_commandline_316
Query
{'selection3': {'Image|contains': '\\et.exe'}, 'selectio
n5': {'Image|contains': '\\sc.exe'}, 'selection7': {'Com
mandLine|contains': 'stop'}, 'selection8': {'CommandLine
|contains': 'delete'}, 'selection9': {'CommandLine|conta
ins': 'WinDefend'}, 'condition': '(selection3 or selecti
on5) and (selection7 or selection8) and selection9'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber

Title Description
Tactics, Techniques, and Procedures
TA0005 , T1562.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows Process Argument A process has been launched with a Base64 encoded argument. Once decoded, the
contains Base64 Encoded PE argument corresponds to the PE Header. This can indicate an attacker is trying to
Header bypass any present execution policy.
More details
Rule ID
process_creation_commandline_317
Query
{'selection3': {'CommandLine|contains': 'TVqQAAMAAAAEAAA
'}, 'condition': 'selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1140 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Cobalt Gang Windows script A known Cobalt Gang script has been executed in the system. This could mean that
execution your computer has been compromised and malicious code is running in your endpoint.
More details

Title Description
Rule ID
process_creation_commandline_319
Query
{'selection3': {'Image|contains': '\\wscript.exe'}, 'sel
ection5': {'CommandLine|contains': 'error_log.vbe'}, 'co
ndition': '(selection3) and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows execution using odbcconf The odbcconf tool allows users to configure Open Database Connectivity (ODBC)
tool drivers. The utility can be misused to execute malicious code and evade detection
techniques.
More details
Rule ID
process_creation_commandline_320
Query
{'selection3': {'Image|contains': '\\odbcconf.exe'}, 'se
lection5': {'CommandLine|contains': 'REGSVR'}, 'conditio
n': 'selection3 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A

Title Description
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows INF file launch The Advanced INF Package Installer (advpack.dll) can use the LaunchINFSection
function to invoke a section from .inf files. This could be used by attackers to remotely
launch staged SCT files with malicious code.
More details
Rule ID
process_creation_commandline_321
Query
{'selection3': {'Image|contains': '\\rundll32.exe'}, 'se
lection5': {'CommandLine|re': 'advpack\\.dll, (?:LaunchI
NFSection|#46)\\s+'}, 'condition': 'selection3 and selec
tion5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows MavInject DLL Injection MavInject is a Windows utility that can be used to execute code. Mavinject can be used
to inject a DLL into a running process.
More details
Rule ID
process_creation_commandline_322
Query

Title Description
{'selection3': {'Image|re': '\\\\Mavinject(?:32|64)?.exe
'}, 'selection5': {'CommandLine|contains': '/INJECTRUNNI
NG'}, 'condition': 'selection3 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Suspicious ACL Change A suspicious change was detected to an access control list (ACL). In this case, 'Full
Access' was granted to 'Everyone' on a file or folder.
More details
Rule ID
process_creation_commandline_324
Query
{'selection3': {'Image|contains': '\\icacls.exe'}, 'sele
ction4': {'CommandLine|re': '\\/grant(?::r)?
\\s+Everyone:F'}, 'condition': 'selection3 and selection
4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50

Title Description
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Credential Access Tool Detected - LaZagne is a multiplatform tool capable to retrieve user credentials from several system
LaZagne services and applications, such as web browsers.
More details
Rule ID
process_creation_commandline_325
Query
{'selection3': {'Image|contains': '\\lazagne'}, 'selecti
on4': {'CommandLine|contains': '-
quiet'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Indirect command execution using An user tried to use a Windows pcalua.exe utility to execute commands in an alternative
pcalua.exe way (without using cmd.exe or powershell.exe). Attackers may use this technique to
avoid invoking the cmd but still execute commands.
More details
Rule ID
process_creation_commandline_327
Query
{'selection3': {'Image|contains': '\\pcalua.exe'}, 'sele
ction5': {'CommandLine|contains': ' -
a '}, 'selection6': {'CommandLine|re': '\\.

Title Description
(?:hta|vbs|vbe|js|jse|wsf|wsh)'}, 'condition': 'selectio
n3 and selection5 and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1202 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows UAC Bypass A User Account Control Bypass activity was detected. This can be due to either regular
operation or because an attacker is trying to escalate privileges.
More details
Rule ID
process_creation_commandline_328
Query
{'selection3': {'CommandLine|contains': 'TpmInitUACBypas
s.exe'}, 'condition': 'selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1548.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
SAM, SECURITY or SYSTEM These hives can be used with a password cracker or creddump to dump the
Registry Hive Export LANMAN/NTLM hashes, view cached credentials, and decrypt LSA secrets. This could
be an indication of a ransomware infection or an attacker trying to cause damage.
More details
Rule ID
process_creation_commandline_329
Query
{'selection3': {'Image|contains': '\\reg.exe'}, 'selecti
on4': {'CommandLine|re': 'save.+ (?:hklm|hkey_local_mach
ine)\\\\
(?:system|security|sam)'}, 'condition': 'selection3 and
selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Suspicious PowerShell Argument PowerShell was executed with suspicious command line argument. The script is likely
attempting to download files from a remote server. This could be an indication of
malicious activity.
More details
Rule ID
process_creation_commandline_330
Query
{'selection3': {'Image|contains': '\\powershell.exe'}, '
selection4': {'CommandLine|contains': 'Net.WebClient'},
'selection5': {'CommandLine|contains': 'Download'}, 'con
dition': 'selection3 and selection4 and selection5'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows UAC bypass - UACME User Account Control Bypass activity was detected. This can be due to either a regular
tool operation or because an attacker is trying to escalate privileges.
More details
Rule ID
process_creation_commandline_331
Query
{'selection9': {'CommandLine|re': '\\.exe\\".*cleanmgr\\
.exe \\/autoclean'}, 'condition': 'selection9'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1548.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Ransomware Decryption After a ransomware malware infects a host machine, a file with instructions to recover
Instructions File Detected the encrypted files is created. A file with these characteristics was opened in the system,
what is an indicator of ransomware infection.
More details
Rule ID
process_creation_commandline_332
Query
{'selection3': {'CommandLine|re': '_Locky_recover_instru
ctions.txt|Coin.Locker.txt DECRYPT_ReadMe.TXT|Contact_He
re_To_Recover_Your_Files.txt|DECRYPT_INSTRUCTION.TXT|DEC
RYPT_INSTRUCTIONS.TXT|DecryptAllFiles.txt|encryptor_raas
_readme_liesmich.txt|FILESAREGONE.TXT|help_decrypt_your_
files.html|HELP_RECOVER_FILES.txt|HELP_TO_DECRYPT_YOUR_F
ILES.txt|HELPDECRYPT.TXT|HELPDECYPRT_YOUR_FILES.HTML|How
_To_Recover_Files.txt|Howto_Restore_FILES.TXT|HOW TO DEC
RYPT YOUR DATA.txt|IHAVEYOURSECRET.KEY|INSTRUCCIONES_DES
CIFRADO.TXT|ReadDecryptFilesHere.txt|Readme to restore y
our files.txt|!SBLOCK_INFO!.rtf|
КАК ВОССТАНОВИТЬ ЗАШИФРОВАННЫЕ ФАЙЛЫ.TXT|README_LOCKED.t
xt'}, 'condition': 'selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1486 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows Autorun Registry Entry An executable was added to the Windows Autorun registry. While this may have
Added via reg.exe occurred due to normal software installation, this is a common technique used by
malware to ensure it is started after reboots.
More details
Rule ID
process_creation_commandline_333

Title Description
Query
{'selection3': {'Image|contains': 'reg.exe'}, 'selection
4': {'CommandLine|contains': 'SOFTWARE\\Microsoft\\Windo
ws\\CurrentVersion\\Run'}, 'selection5': {'CommandLine|c
ontains': ' add '}, 'condition': 'selection3 and selecti
on4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1547.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
File Deletion Backup Catalog If the backup catalog is deleted for a computer, you will not be able to access the
Deletion backups created of that computer using the Windows Server Backup snap-in. This could
be an indication of a ransomware infection or an attacker trying to cause damage.
More details
Rule ID
process_creation_commandline_334
Query
{'selection3': {'Image|contains': '\\wbadmin.exe'}, 'sel
ection4': {'CommandLine|contains': 'delete catalog'}, 'c
ondition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A

Title Description
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Wireless Network Password The password of a wireless network was accessed. This could be an indication of
Retrieval malicious activity.
More details
Rule ID
process_creation_commandline_335
Query
{'selection3': {'ParentImage|contains': '\\etsh.exe'}, '
selection5': {'CommandLine|contains': 'wlan'}, 'selectio
n6': {'CommandLine|contains': 'key=clear'}, 'condition':
'selection3 and selection5 and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1555 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Metasploit MSSQL Command An attacked gained access to the MSSQL Server database and is executing the
Execution Metasploit module mssql_exec.
More details
Rule ID
process_creation_commandline_337
Query

Title Description
{'selection3': {'ParentImage|contains': 'sqlservr.exe'},
'selection4': {'CommandLine|contains': 'echo OWNED'}, '
condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Internet Explorer executing An attacker can execute code after a successful exploit attack. Internet Explorer is a
suspicious wmic command commonly targeted software in Exploit Kit campaigns.
More details
Rule ID
process_creation_commandline_338
Query
{'selection3': {'ParentImage|contains': '\\iexplore.exe'
}, 'selection4': {'Image|contains': '\\WMIC.exe'}, 'sele
ction6': {'CommandLine|contains': 'process call create'}
, 'selection7': {'CommandLine|contains': '\\Temp\\'}, 'c
ondition': 'selection3 and (selection4 and selection6 an
d selection7)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1203 
References
N/A
Severity

Title Description
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
File Deletion Windows Shadow An attempt to delete all shadow copies using the Windows Volume Shadow Copy
Copies Deletion via Powershell Service (VSS) via Powershell has been detected. This could be an indication of a
ransomware infection or an attacker trying to cause damage.
More details
Rule ID
process_creation_commandline_339
Query
{'selection7': {'Image|contains': '\\powershell.exe'}, '
selection8': {'CommandLine|contains': 'RwBlAHQALQBXAG0Aa
QBPAGIAagBlAGMAdAAgAFcAaQBuADMAMgBfAFMAaABhAGQAbwB3AGMAb
wBwAHkAIAB8ACAARgBvAHIARQBhAGMAaAAtAE8AYgBqAGUAYwB0ACAAe
wAkAF8ALgBEAGUAbABlAHQAZQAoACkAOwB9AA=='}, 'condition':
'(selection7 and selection8)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
HackTool - Certipy Execution Detects Certipy execution, a tool for Active Directory Certificate Services enumeration
and abuse based on PE metadata characteristics and common command line
arguments.
More details
Rule ID
process_creation_commandline_340

Title Description
Query
{'selection_img': [{'Image|endswith': '\\Certipy.exe'}],
'selection_cli_commands': {'CommandLine|contains': [' a
ccount ', ' auth ', ' cert ', ' find ', ' forge ', ' ptt
', ' relay ', ' req ', ' shadow ', ' template ']}, 'sel
ection_cli_flags': {'CommandLine|contains': [' -
bloodhound', ' -ca-pfx ', ' -dc-ip ', ' -kirbi', ' -old-
bloodhound', ' -pfx ', ' -target', ' -template', ' -
username ', ' -vulnerable', 'auth -
pfx', 'shadow auto', 'shadow list']}, 'condition': 'sele
ction_img or all of selection_cli_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6938366d-8954-4ddc-baff-c830b3ba8fcd
Author: pH-T (Nextron Systems), Sittikorn Sangrattanapitak
Tactics, Techniques, and Procedures
TA0006 , T1649 
References
https://github.com/ly4k/Certipy 
https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-
authentication-and-request-methods-and-more-7237d88061f7 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2023-04-17 high
Unlikely
Findstr GPP Passwords Look for the encrypted cpassword value within Group Policy Preference files on the
Domain Controller. This value can be decrypted with gpp-decrypt.
More details
Rule ID
process_creation_commandline_341
Query
{'selection_img': [{'Image|endswith': ['\\find.exe', '\\
findstr.exe']}], 'selection_cli': {'CommandLine|contains
|all': ['cpassword', '\\sysvol\\', '.xml']}, 'condition'
: 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,91a2c315-9ee6-4052-a853-6f6a8238f90d
Author: frack113
Tactics, Techniques, and Procedures
TA0006 , T1552.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.006/
T1552.006.md#atomic-test-1---gpp-passwords-findstr 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021-12-27 high
Unknown
Domain Trust Discovery Via Detects execution of "dsquery.exe" for domain trust discovery
Dsquery
More details
Rule ID
process_creation_commandline_342
Query
{'selection_img': [{'Image|endswith': '\\dsquery.exe'}],
'selection_cli': {'CommandLine|contains': 'trustedDomai
n'}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3bad990e-4848-4a78-9530-b427d854aac0
Author: E.M. Anhaus, Tony Lambert, oscd.community, omkar72
Tactics, Techniques, and Procedures
TA0007 , T1482 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1482/T148
2.md 
https://posts.specterops.io/an-introduction-to-manual-active-directory-
querying-with-dsquery-and-ldapsearch-84943c13d7eb?gi=41b97a644843 
Severity
50
Suppression Logic Based On
computer_name

Title Description
event_data.CommandLine
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2019-10- medium
Legitimate use of the utilities by legitimate user
24 for legitimate reason
PUA - DIT Snapshot Viewer Detects the use of Ditsnap tool, an inspection tool for Active Directory database, ntds.dit.
More details
Rule ID
process_creation_commandline_343
Query
{'selection': [{'Image|endswith': '\\ditsnap.exe'}, {'Co
mmandLine|contains': 'ditsnap.exe'}], 'condition': 'sele
ction'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d3b70aad-097e-409c-9df2-450f80dc476b
Author: Furkan Caliskan (@caliskanfurkan_)
Tactics, Techniques, and Procedures
TA0006 , T1003.003 
References
https://thedfirreport.com/2020/06/21/snatch-ransomware/ 
https://web.archive.org/web/20201124182207/https://github.com/yosqueoy/dit
snap 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020-07-04 high
Legitimate admin usage
Suspicious Process Patterns Detects suspicious process patterns used in NTDS.DIT exfiltration
NTDS.DIT Exfil
More details
Rule ID
process_creation_commandline_344
Query
{'selection_tool': [{'Image|endswith': ['\\NTDSDump.exe'
, '\\NTDSDumpEx.exe']}, {'CommandLine|contains|all': ['n

Title Description
tds.dit', 'system.hiv']}, {'CommandLine|contains': 'NTDS
grab.ps1'}], 'selection_oneliner_1': {'CommandLine|conta
ins|all': ['ac i ntds', 'create full']}, 'selection_onli
ner_2': {'CommandLine|contains|all': ['/c copy ', '\\win
dows\\ntds\\ntds.dit']}, 'selection_onliner_3': {'Comman
dLine|contains|all': ['activate instance ntds', 'create
full']}, 'selection_powershell': {'CommandLine|contains|
all': ['powershell', 'ntds.dit']}, 'set1_selection_ntds_
dit': {'CommandLine|contains': 'ntds.dit'}, 'set1_select
ion_image_folder': [{'ParentImage|contains': ['\\apache'
, '\\tomcat', '\\AppData\\', '\\Temp\\', '\\Public\\', '
\\PerfLogs\\']}, {'Image|contains': ['\\apache', '\\tomc
at', '\\AppData\\', '\\Temp\\', '\\Public\\', '\\PerfLog
s\\']}], 'condition': '1 of selection* or all of set1*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8bc64091-6875-4881-aaf9-7bd25b5dda08
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1003.003 
References
https://www.ired.team/offensive-security/credential-access-and-credential-
dumping/ntds.dit-enumeration 
https://www.n00py.io/2022/03/manipulating-user-passwords-without-
mimikatz/ 
https://pentestlab.blog/tag/ntds-dit/ 
https://github.com/samratashok/nishang/blob/414ee1104526d7057f9adaeee1
96d91ae447283e/Gather/Copy-VSS.ps1 
https://github.com/zcgonvh/NTDSDumpEx 
https://github.com/rapid7/metasploit-
framework/blob/d297adcebb5c1df6fe30b12ca79b161deb71571c/data/post/p
owershell/NTDSgrab.ps1 
https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022-03-11 high
Unknown
Get-ForestTrust with PowerShell The following analytic detects the execution of the Get-ForestTrust command via
PowerShell, commonly used by adversaries to gather domain trust information. This
detection leverages data from Endpoint Detection and Response (EDR) agents,
focusing on process names and command-line executions. Identifying this activity is
crucial as it indicates potential reconnaissance efforts to map out domain trusts, which
can inform further attacks. If confirmed malicious, this activity could allow attackers to

Title Description
understand domain relationships, aiding in lateral movement and privilege escalation
within the network.
More details
Rule ID
process_creation_commandline_345
Query
{'selection1': {'Image|endswith': ['powershell.exe', 'cm
d.exe']}, 'selection2': {'CommandLine|contains': 'get-
foresttrust'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1482 
References
https://powersploit.readthedocs.io/en/latest/Recon/Get-ForestTrust/ 
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
produ 2024- mediu
Limited false positives as this requires an active
ction 11-13 m Administrator or adversary to bring in, import, and
execute.
Renamed AdFind Execution Detects the use of a renamed Adfind.exe. AdFind continues to be seen across majority
of breaches. It is used to domain trust discovery to plan out subsequent steps in the
attack chain.
More details
Rule ID
process_creation_commandline_346
Query
{'selection_1': {'CommandLine|contains': ['domainlist',
'trustdmp', 'dcmodes', 'adinfo', ' dclist ', 'computer_p
wdnotreqd', 'objectcategory=', '-subnets -
f', 'name="Domain Admins"', '-
sc u:', 'domainncs', 'dompol', ' oudmp ', 'subnetdmp', '
gpodmp', 'fspdmp', 'users_noexpire', 'computers_active',
'computers_pwdnotreqd']}, 'selection_2': {'Hashes|conta
ins': ['IMPHASH=BCA5675746D13A1F246E2DA3C2217492', 'IMPH
ASH=53E117A96057EAF19C41380D0E87F1C2']}, 'selection_3':

Title Description
{'OriginalFileName': 'AdFind.exe'}, 'filter': {'Image|en
dswith': '\\AdFind.exe'}, 'condition': '1 of selection*
and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,df55196f-f105-44d3-a675-e9dfb6cc2f2b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0007 , T1018 , T1087.002 , T1482 , T1069.002 
References
https://www.joeware.net/freetools/tools/adfind/ 
https://thedfirreport.com/2020/05/08/adfind-recon/ 
https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/ 
https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-
solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/

https://social.technet.microsoft.com/wiki/contents/articles/7535.adfind-
command-examples.aspx 
https://github.com/center-for-threat-informed-
defense/adversary_emulation_library/blob/bf62ece1c679b07b5fb49c4bae947
fe24c81811f/fin6/Emulation_Plan/Phase1.md 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022-08-21 high
Unknown
Enumerating Domain Trusts via Identifies the use of nltest.exe for domain trust discovery purposes. Adversaries may
NLTEST.EXE use this command-line utility to enumerate domain trusts and gain insight into trust
relationships, as well as the state of Domain Controller (DC) replication in a Microsoft
Windows NT Domain.
More details
Rule ID
process_creation_commandline_347
Query
{'selection1': {'Image|endswith': '\\nltest.exe'}, 'sele
ction2': {'CommandLine|contains': ['/dclist:', '/dcname:
', '/parentdomain', '/domain_trusts', '/bdc_query:']}, '
filter_parent': {'ParentImage|endswith': 'PDQInventorySc
anner.exe'}, 'filter_system_users': {'UserId': ['S-1-5-
18', 'S-1-5-19', 'S-1-5-
20']}, 'condition': 'selection1 and selection2 and (not
filter_parent) and (not filter_system_users)'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1018 , T1482 
References
N/A
Severity
25
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urit ion Lev
y Date el
test 2022/ low
Domain administrators may use this command-line utility
05/31 for legitimate information gathering purposes, but it is not
common for environments with Windows Server 2012 and
newer.
Potential SPN Enumeration Via Detects service principal name (SPN) enumeration used for Kerberoasting
Setspn.EXE
More details
Rule ID
process_creation_commandline_348
Query
{'selection_pe': [{'Image|endswith': '\\setspn.exe'}], '
selection_cli': {'CommandLine|contains': [' -
q ', ' /q ']}, 'selection_cli2': {'CommandLine|contains|
all': [' -t ', ' -
f ']}, 'condition': 'selection_pe and (selection_cli or
selection_cli2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1558.003 
References
https://web.archive.org/web/20200329173843/https://p16.praetorian.com/blog
/how-to-use-kerberoasting-t1208-for-privilege-escalation 
https://www.praetorian.com/blog/how-to-use-kerberoasting-t1208-for-
privilege-escalation/?edition=2019 

Title Description
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018-11-14 medium
Administration activity
HackTool - Mimikatz Execution Detects well-known mimikatz command line arguments
More details
Rule ID
process_creation_commandline_349
Query
{'selection_tools_name': {'CommandLine|contains': ['Dump
Creds', 'mimikatz']}, 'selection_function_names': {'Comm
andLine|contains': ['::aadcookie', '::detours', '::memss
p', '::mflt', '::ncroutemon', '::ngcsign', '::printnight
mare', '::skeleton', '::preshutdown', '::mstsc', '::mult
irdp']}, 'selection_module_names': {'CommandLine|contain
s': ['rpc::', 'token::', 'crypto::', 'dpapi::', 'sekurls
a::', 'kerberos::', 'lsadump::', 'privilege::', 'process
::', 'vault::']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a642964e-bead-4bed-8910-1bb4d63e3b4d
Author: Teymur Kheirkhabarov, oscd.community, David ANDRE (additional
keywords), Tim Shelton
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-
windows-environment 
https://tools.thehacker.recipes/mimikatz/modules 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/08/13 high
Unlikely

Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  