✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious PowerShell
Script Alert Type
The following rules are used to identify suspicious activity relating to PowerShell scripts. Any one
or more of these will trigger the PowerShell Script Alert. Details for each rule can be viewed by
clicking the More Details link in the description.
Windows Events Required: 4104
The Windows Detect Profile (Low Volume)  covers these required Windows events.
Title Description
PowerShell Mailbox Collection Script Detects PowerShell scripts that can be used to collect data from mailboxes.
Adversaries may target user email to collect sensitive information.
More details
Rule ID
powershell_scriptblock_1
Query
{'selection1': {'ScriptBlockText|contains': ['Microsoft
.Office.Interop.Outlook', 'Interop.Outlook.olDefaultFol
ders', '::olFolderInBox', 'Microsoft.Exchange.WebServic
es.Data.Folder', 'Microsoft.Exchange.WebServices.Data.F
ileAttachment']}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1114 
References
N/A

Title Description
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/11 medium N/A
Live Memory Dump Using Powershell Detects usage of a PowerShell command to dump the live memory of a Windows
machine
More details
Rule ID
powershell_scriptblock_3
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
StorageDiagnosticInfo', '-
IncludeLiveDump']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,cd185561-4760-45d6-a63e-a51325112cae
Author: Max Altgelt (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 
References
https://docs.microsoft.com/en-us/powershell/module/storage/get-
storagediagnosticinfo 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/21 high
Diagnostics
Invoke-Obfuscation CLIP+ Launcher - Detects Obfuscated use of Clip.exe to execute PowerShell
PowerShell
More details
Rule ID
powershell_scriptblock_4
Query

Title Description
{'selection_4104': {'ScriptBlockText|re': '.*cmd.{0,5}
(?:/c|/r).+clip(?:\\.exe)?.{0,4}&&.+clipboard]::\\
(\\s\\\\"\\{\\d\\}.+-
f.+"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,73e67340-0d25-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/13 high
Unknown
Suspicious Service DACL Modification Detects usage of the "Set-Service" powershell cmdlet to configure a new
Via Set-Service Cmdlet - PS SecurityDescriptor that allows a service to be hidden from other utilities such as
"sc.exe", "Get-Service"...etc. (Works only in powershell 7)
More details
Rule ID
powershell_scriptblock_5
Query
{'selection_sddl_flag': {'ScriptBlockText|contains': ['
-SecurityDescriptorSddl ', '-
sd ']}, 'selection_set_service': {'ScriptBlockText|cont
ains|all': ['Set-
Service ', 'D;;'], 'ScriptBlockText|contains': [';;;IU'
, ';;;SU', ';;;BA', ';;;SY', ';;;WD']}, 'condition': 'a
ll of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,22d80745-6f2c-46da-826b-77adaededd74
Author: Nasreddine Bencherchali (Nextron Systems)

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.011 
References
https://twitter.com/Alh4zr3d/status/1580925761996828672 
https://learn.microsoft.com/en-
us/powershell/module/microsoft.powershell.management/set-service?
view=powershell-7.2 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experim 2022/10/ high
Rare intended use of hidden services
ental 24
Rare FP could occure due to the non linearity
of the ScriptBlockText log
Potential Invoke-Mimikatz PowerShell Detects Invoke-Mimikatz PowerShell script and alike. Mimikatz is a credential dumper
Script capable of obtaining plaintext Windows account logins and passwords.
More details
Rule ID
powershell_scriptblock_6
Query
{'selection_1': {'ScriptBlockText|contains|all': ['Dump
Creds', 'DumpCerts']}, 'selection_2': {'ScriptBlockText
|contains': 'sekurlsa::logonpasswords'}, 'selection_3':
{'ScriptBlockText|contains|all': ['crypto::certificate
s', 'CERT_SYSTEM_STORE_LOCAL_MACHINE']}, 'condition': '
1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
SigmaHQ,189e3b02-82b2-4b90-9662-411eb64486d4
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 
References
https://www.elastic.co/guide/en/security/current/potential-invoke-mimikatz-
powershell-script.html#potential-invoke-mimikatz-powershell-script 
Severity
74
Suppression Logic Based On
computer_name

Title Description
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2022/09/2 high
Mimikatz can be useful for testing the
ntal 8 security of networks
Disable-WindowsOptionalFeature Detect built in PowerShell cmdlet Disable-WindowsOptionalFeature, Deployment
Command PowerShell Image Servicing and Management tool. Similar to DISM.exe, this cmdlet is used to
enumerate, install, uninstall, configure, and update features and packages in Windows
images
More details
Rule ID
powershell_scriptblock_7
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['Di
sable-WindowsOptionalFeature', '-Online', '-
FeatureName']}, 'selection_feature': {'ScriptBlockText|
contains': ['Windows-Defender-Gui', 'Windows-Defender-
Features', 'Windows-Defender', 'Windows-Defender-
ApplicationGuard']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,99c4658d-2c5e-4d87-828d-7c066ca537c3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/5b67c9b141fa3918017f8fa44f2f88f0b1ecb9e1/atomics/T1562.00
1/T1562.001.md 
https://docs.microsoft.com/en-us/powershell/module/dism/disable-
windowsoptionalfeature?view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/10 high
Unknown
Powershell DNSExfiltration DNSExfiltrator allows for transferring (exfiltrate) a file over a DNS request covert
channel

Title Description
More details
Rule ID
powershell_scriptblock_8
Query
{'selection_cmdlet': [{'ScriptBlockText|contains': 'Inv
oke-
DNSExfiltrator'}, {'ScriptBlockText|contains|all': [' -
i ', ' -d ', ' -p ', ' -doh ', ' -
t ']}], 'condition': 'selection_cmdlet'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,d59d7842-9a21-4bc6-ba98-64bfe0091355
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0010 , T1048 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048/T1
048.md#atomic-test-3---dnsexfiltration-doh 
https://github.com/Arno0x/DNSExfiltrator 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/07 high
Legitimate script
Powershell Empire agent CnC activity A Powershell Empire framework agent is running on the machine, and it's trying to
access the CnC server.
More details
Rule ID
powershell_scriptblock_9
Query
{'selection1': {'ScriptBlockText|contains': 'IF($PSVERS
IonTAblE.PSVERsIOn.MajOr -ge 3)
{'}, 'selection2': {'ScriptBlockText|contains': '[Ref].
ASsEmbLY.GeTTYpe('}, 'selection3': {'ScriptBlockText|co
ntains': 'System.Management.Automation.AmsiUtils'}, 'co
ndition': 'selection1 and selection2 and selection3'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Powershell Directory Enumeration Detects technique used by MAZE ransomware to enumerate directories using
Powershell
More details
Rule ID
powershell_scriptblock_10
Query
{'selection': {'ScriptBlockText|contains|all': ['foreac
h', 'Get-ChildItem', '-Path ', '-
ErrorAction ', 'SilentlyContinue', 'Out-File ', '-
append']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,162e69a7-7981-4344-84a9-0f1c9a217a52
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1083 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1083/T1
083.md 
https://www.mandiant.com/resources/tactics-techniques-procedures-
associated-with-maze-ransomware-incidents 
Severity
49

Title Description
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/17 medium
Legitimate PowerShell scripts
Invoke-Obfuscation Via Use MSHTA - Detects Obfuscated Powershell via use MSHTA in Scripts
PowerShell
More details
Rule ID
powershell_scriptblock_11
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['s
et', '&&', 'mshta', 'vbscript:createobject', '.run', '(
window.close)']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e55a5195-4724-480e-a77e-3ebe64bd3759
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/08 high
Unknown
Root Certificate Installed - PowerShell Adversaries may install a root certificate on a compromised system to avoid warnings
when connecting to adversary controlled web servers.
More details
Rule ID
powershell_scriptblock_12
Query
{'selection1': {'ScriptBlockText|contains|all': ['Move-
Item', 'Cert:\\LocalMachine\\Root']}, 'selection2': {'S
criptBlockText|contains|all': ['Import-

Title Description
Certificate', 'Cert:\\LocalMachine\\Root']}, 'condition
': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,42821614-9264-4761-acfc-5772c3286f76
Author: oscd.community, @redcanary, Zach Stanford @svch0st
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.00
4/T1553.004.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Matur Creati Risk False Positives
ity on Level
Date
experi 2020/1 medi
Help Desk or IT may need to manually add a
menta 0/10 um corporate Root CA on occasion. Need to test if GPO
l push doesn't trigger FP
Clearing Windows Console History Identifies when a user attempts to clear console history. An adversary may clear the
command history of a compromised account to conceal the actions undertaken during
an intrusion.
More details
Rule ID
powershell_scriptblock_15
Query
{'selection1': {'ScriptBlockText|contains': 'Clear-
History'}, 'selection2a': {'ScriptBlockText|contains':
['Remove-
Item', 'rm']}, 'selection2b': {'ScriptBlockText|contain
s': ['ConsoleHost_history.txt', '(Get-
PSReadlineOption).HistorySavePath']}, 'condition': 'sel
ection1 or selection2a and selection2b'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source

Title Description
SigmaHQ,bde47d4b-9987-405c-94c7-b080410e8ea7
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://stefanos.cloud/blog/kb/how-to-clear-the-powershell-command-
history/ 
https://www.shellhacks.com/clear-history-powershell/ 
https://community.sophos.com/sophos-labs/b/blog/posts/powershell-
command-history-forensics 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/25 high
Unknown
Windows Firewall Profile Disabled Detects when a user disables the Windows Firewall via a Profile to help evade
defense.
More details
Rule ID
powershell_scriptblock_16
Query
{'selection_args': {'ScriptBlockText|contains|all': ['S
et-NetFirewallProfile ', ' -
Enabled ', ' False']}, 'selection_opt': {'ScriptBlockTe
xt|contains': [' -
All ', 'Public', 'Domain', 'Private']}, 'condition': 'a
ll of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,488b44e7-3781-4a71-888d-c95abfacf44d
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.004 
References
https://docs.microsoft.com/en-us/powershell/module/netsecurity/set-
netfirewallprofile?view=windowsserver2019-ps 
https://www.tutorialspoint.com/how-to-get-windows-firewall-profile-settings-
using-powershell 
http://powershellhelp.space/commands/set-netfirewallrule-psv5.php 

Title Description
http://woshub.com/manage-windows-firewall-powershell/ 
https://www.elastic.co/guide/en/security/current/windows-firewall-disabled-
via-powershell.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/12 medium
Unknown
Suspicious Portable Executable Detects the presence of a portable executable (PE) in a PowerShell script by looking
Encoded in Powershell Script for its encoded header. Attackers embed PEs into PowerShell scripts to inject them
into memory, avoiding defences by not writing to disk.
More details
Rule ID
powershell_scriptblock_17
Query
{'selection1': {'ScriptBlockText|contains': 'TVqQAAMAAA
AEAAAA'}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/15 medium N/A
PowerShell Suspicious Script with Detects PowerShell scripts that can take screenshots, which is a common feature in
Screenshot Capabilities post-exploitation kits and remote access tools (RATs).
More details
Rule ID
powershell_scriptblock_19

Title Description
Query
{'selection1': {'ScriptBlockText|contains': 'CopyFromSc
reen'}, 'selection2': {'ScriptBlockText|contains': 'Sys
tem.Drawing.Bitmap'}, 'selection3': {'ScriptBlockText|c
ontains': 'Drawing.Bitmap'}, 'selection4': {'UserId': '
S-1-5-
18'}, 'condition': 'selection1 and (selection2 or selec
tion3) and (not selection4)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1113 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/19 medium N/A
Registry-Free Process Scope Adversaries may leverage the COR_PROFILER environment variable to hijack the
COR_PROFILER execution flow of programs that load the .NET CLR. The COR_PROFILER is a .NET
Framework feature which allows developers to specify an unmanaged (or external of
.NET) profiling DLL to be loaded into each .NET process that loads the Common
Language Runtime (CLR). These profiliers are designed to monitor, troubleshoot, and
debug managed code executed by the .NET CLR. (Citation: Microsoft Profiling Mar
2017) (Citation: Microsoft COR_PROFILER Feb 2013)
More details
Rule ID
powershell_scriptblock_20
Query
{'selection': {'ScriptBlockText|contains|all': ['$env:C
OR_ENABLE_PROFILING', '$env:COR_PROFILER', '$env:COR_PR
OFILER_PATH']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,23590215-4702-4a70-8805-8dc9e58314a2

Title Description
Author: frack113
Tactics, Techniques, and Procedures
| TA0002 , T1059.001 | , TA0003 | , T1574.012  |
| ------------------- | --------- | -------------- |
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.01
2/T1574.012.md#atomic-test-3---registry-free-process-scope-
| cor_profiler |    |     |
| ------------ | --- | --- |
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
| Maturity Creation Date | Risk Level | False Positives |
| ---------------------- | ---------- | --------------- |
| test 2021/12/30        | medium     |                 |
Legitimate administrative script

Title Description
Invoke-Obfuscation RUNDLL Detects Obfuscated Powershell via RUNDLL LAUNCHER
LAUNCHER - PowerShell
More details
Rule ID
powershell_scriptblock_21
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['r
undll32.exe', 'shell32.dll', 'shellexec_rundll', 'power
shell']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e6cb92b4-b470-4eb8-8a9d-d63e8583aae0
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium
Unknown
Execution via CL_Invocation.ps1 - Detects Execution via SyncInvoke in CL_Invocation.ps1 module
Powershell
More details
Rule ID
powershell_scriptblock_23
Query
{'selection': {'ScriptBlockText|contains|all': ['CL_Inv
ocation.ps1', 'SyncInvoke']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4cd29327-685a-460e-9dac-c3ab96e549dc

Title Description
Author: oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/Cl_invocation/ 
https://twitter.com/bohops/status/948061991012327424 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/14 high
Unknown
Suspicious TCP Tunnel Via Detects powershell scripts that creates sockets/listeners which could be indicative of
PowerShell Script tunneling activity
More details
Rule ID
powershell_scriptblock_24
Query
{'selection': {'ScriptBlockText|contains|all': ['[Syste
m.Net.HttpWebRequest]', 'System.Net.Sockets.TcpListener
', 'AcceptTcpClient']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,bd33d2aa-497e-4651-9893-5c5364646595
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1090 
References
https://github.com/Arno0x/PowerShellScripts/blob/a6b7d5490fbf0b20f91195
838f3a11156724b4f7/proxyTunnel.ps1 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2022/07/08 medium
Unknown
Powershell Store File In Alternate Storing files in Alternate Data Stream (ADS) similar to Astaroth malware.
Data Stream
More details
Rule ID
powershell_scriptblock_25
Query
{'selection_compspec': {'ScriptBlockText|contains|all':
['Start-Process', '-FilePath "$env:comspec" ', '-
ArgumentList ', '>']}, 'condition': 'selection_compspec
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a699b30e-d010-46c8-bbd1-ee2e26765fe9
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1564.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.00
4/T1564.004.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/02 medium
Unknown
Potential PowerShell Obfuscation Detects specific techniques often seen used inside of PowerShell scripts to obfscuate
Using Character Join Alias creation
More details
Rule ID
powershell_scriptblock_26
Query
{'selection': {'ScriptBlockText|contains|all': ['-
Alias', ' -Value (-join(']}, 'condition': 'selection'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e8314f79-564d-4f79-bc13-fbc0bf2660d8
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
N/A
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/09 low
Unknown
Windows UAC Bypass A User Account Control Bypass activity was detected. This can be due to either regular
operation or because an attacker is trying to escalate privileges.
More details
Rule ID
powershell_scriptblock_27
Query
{'selection1': {'ScriptBlockText|contains': 'Invoke-
UACBypass'}, 'selection2': {'ScriptBlockText|contains':
'Invoke-
EventVwrBypass'}, 'selection3': {'ScriptBlockText|conta
ins': 'Invoke-
SDCLTBypass'}, 'condition': 'selection1 or selection2 o
r selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49

Title Description
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Suspicious IO.FileStream Open a handle on the drive volume via the \\.\ DOS device path specifier and perform
direct access read of the first few bytes of the volume.
More details
Rule ID
powershell_scriptblock_28
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
Object', 'IO.FileStream', '\\\\.\\']}, 'condition': 'se
lection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,70ad982f-67c8-40e0-a955-b920c2fa05cb
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1006/T1
006.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/09 medium
Legitimate PowerShell scripts
Invoke-Obfuscation VAR+ Launcher - Detects Obfuscated use of Environment Variables to execute PowerShell
PowerShell
More details
Rule ID
powershell_scriptblock_29
Query
{'selection_4104': {'ScriptBlockText|re': '.*cmd.{0,5}
(?:/c|/r)(?:\\s|)"set\\s[a-zA-Z]{3,6}.*(?:\\{\\d\\})

Title Description
{1,}\\\\"\\s+?-f(?:.*\\))
{1,}.*"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,0adfbc14-0ed1-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high
Unknown
Powershell XML Execute Command Adversaries may abuse PowerShell commands and scripts for execution. PowerShell
is a powerful interactive command-line interface and scripting environment included in
the Windows operating system. (Citation: TechNet PowerShell) Adversaries can use
PowerShell to perform a number of actions, including discovery of information and
execution of code
More details
Rule ID
powershell_scriptblock_30
Query
{'selection_xml': {'ScriptBlockText|contains|all': ['Ne
w-
Object', 'System.Xml.XmlDocument', '.Load']}, 'selectio
n_exec': {'ScriptBlockText|contains': ['IEX ', 'Invoke-
Expression ', 'Invoke-Command ', 'ICM -
']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,6c6c6282-7671-4fe9-a0ce-a2dcebdc342b
Author: frack113

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.00
1/T1059.001.md#atomic-test-8---powershell-xml-requests 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/19 medium
Legitimate administrative script
Dump Credentials from Windows Adversaries may search for common password storage locations to obtain user
Credential Manager With PowerShell credentials. Passwords are stored in several places on a system, depending on the
operating system or application holding the credentials.
More details
Rule ID
powershell_scriptblock_33
Query
{'selection_kiddie': {'ScriptBlockText|contains': ['Get
-PasswordVaultCredentials', 'Get-
CredManCreds']}, 'selection_rename_Password': {'ScriptB
lockText|contains|all': ['New-
Object', 'Windows.Security.Credentials.PasswordVault']}
, 'selection_rename_credman': {'ScriptBlockText|contain
s|all': ['New-
Object', 'Microsoft.CSharp.CSharpCodeProvider', '[Syste
m.Runtime.InteropServices.RuntimeEnvironment]::GetRunti
meDirectory())', 'Collections.ArrayList', 'System.CodeD
om.Compiler.CompilerParameters']}, 'condition': '1 of s
election_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,99c49d9c-34ea-45f7-84a7-4751ae6b2cbc
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1555 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555/T1
555.md 

Title Description
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/20 medium
Unknown
Potential Suspicious Windows Feature Detects usage of the built-in PowerShell cmdlet "Enable-WindowsOptionalFeature"
Enabled used as a Deployment Image Servicing and Management tool. Similar to DISM.exe,
this cmdlet is used to enumerate, install, uninstall, configure, and update features and
packages in Windows images
More details
Rule ID
powershell_scriptblock_35
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['En
able-WindowsOptionalFeature', '-Online', '-
FeatureName']}, 'selection_feature': {'ScriptBlockText|
contains': ['TelnetServer', 'Internet-Explorer-
Optional-amd64', 'TFTP', 'SMB1Protocol', 'Client-
ProjFS', 'Microsoft-Windows-Subsystem-
Linux']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,55c925c1-7195-426b-a136-a9396800e29b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
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
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2022/09/10 medium
Unknown
Suspicious PowerShell Mailbox SMTP Detects usage of the powerShell Set-Mailbox Cmdlet to set-up an SMTP forwarding
Forward Rule rule.
More details
Rule ID
powershell_scriptblock_36
Query
{'selection': {'ScriptBlockText|contains|all': ['Set-
Mailbox ', ' -DeliverToMailboxAndForward ', ' -
ForwardingSmtpAddress ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,15b7abbb-8b40-4d01-9ee2-b51994b1d474
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-
server-logs/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2022/10/26 medium
Legitimate usage of the cmdlet to
tal forward emails
Powershell Add Name Resolution Detects powershell scripts that adds a Name Resolution Policy Table (NRPT) rule for
Policy Table Rule the specified namespace. This will bypass the default DNS server and uses a
specified server for answering the query.
More details
Rule ID
powershell_scriptblock_37
Query
{'selection': {'ScriptBlockText|contains|all': ['Add-
DnsClientNrptRule', '-Namesp', '-
NameSe']}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4368354e-1797-463c-bc39-a309effbe8d7
Author: Borna Talebi
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1565 
References
https://twitter.com/NathanMcNulty/status/1569497348841287681 
https://docs.microsoft.com/en-us/powershell/module/dnsclient/add-
dnsclientnrptrule?view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/14 high
Unknown
Security Software Discovery by Adversaries may attempt to get a listing of security software, configurations, defensive
Powershell tools, and sensors that are installed on a system or in a cloud environment. This may
include things such as firewall rules and anti-viru
More details
Rule ID
powershell_scriptblock_38
Query
{'selection_1': {'ScriptBlockText|contains|all': ['get-
process', '.Description', '-
like']}, 'selection_2': {'ScriptBlockText|contains': ['
"*virus*"', '"*carbonblack*"', '"*defender*"', '"*cylan
ce*"']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,904e8e61-8edf-4350-b59c-b905fc8e810c
Author: frack113, Anish Bogati, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1518.001 

Title Description
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518.00
1/T1518.001.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/16 low
Unknown
Suspicious New-PSDrive to Admin Adversaries may use to interact with a remote network share using Server Message
Share Block (SMB). The adversary may then perform actions as the logged-on user.
More details
Rule ID
powershell_scriptblock_39
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
PSDrive', '-psprovider ', 'filesystem', '-
root ', '\\\\', '$']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1c563233-030e-4a07-af8c-ee0490a66d3a
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0008 , T1021.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.00
2/T1021.002.md#atomic-test-2---map-admin-share-powershell 
https://docs.microsoft.com/en-
us/powershell/module/microsoft.powershell.management/new-psdrive?
view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/13 medium
Unknown

Title Description
PowerShell Script with Token Detects scripts that contain PowerShell functions, structures, or Windows API
Impersonation Capabilities functions related to token impersonation/theft. Attackers may duplicate then
impersonate another user's token to escalate privileges and bypass access controls.
More details
Rule ID
powershell_scriptblock_40
Query
{'selection1': {'ScriptBlockText|contains': ['Invoke-
TokenManipulation', 'ImpersonateNamedPipeClient', 'NtIm
personateThread']}, 'selection2': {'ScriptBlockText|con
tains': 'STARTUPINFOEX'}, 'selection3': {'ScriptBlockTe
xt|contains': 'UpdateProcThreadAttribute'}, 'selection4
': {'ScriptBlockText|contains': 'AdjustTokenPrivileges'
}, 'selection5': {'ScriptBlockText|contains': 'SeDebugP
rivilege'}, 'selection6': {'UserId': 'S-1-5-
18'}, 'condition': '(selection1 or (selection2 and sele
ction3) or (selection4 and selection5)) and (not select
ion6)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , T1106 , TA0005 , T1134 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/08/17 medium N/A
Disable of ETW Trace - Powershell Detects usage of powershell cmdlets to disable or remove ETW trace sessions
More details
Rule ID
powershell_scriptblock_41
Query
{'selection_pwsh_remove': {'ScriptBlockText|contains':
'Remove-
EtwTraceProvider '}, 'selection_pwsh_set': {'ScriptBloc
kText|contains|all': ['Set-

Title Description
EtwTraceProvider ', '0x11']}, 'condition': '1 of select
ion*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,115fdba9-f017-42e6-84cf-d5573bf2ddf8
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070 , T1562.006 
References
https://medium.com/palantir/tampering-with-windows-event-tracing-
background-offense-and-defense-4be7ac62ac63 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 high
Unknown
Service Registry Permissions Adversaries may execute their own malicious payloads by hijacking the Registry
Weakness Check entries used by services. Adversaries may use flaws in the permissions for registry to
redirect from the originally specified executable to one that they control, in order to
launch their own code at Service start. Windows stores local service configuration
information in the Registry under HKLM\SYSTEM\CurrentControlSet\Services
More details
Rule ID
powershell_scriptblock_42
Query
{'selection': {'ScriptBlockText|contains|all': ['get-
acl', 'REGISTRY::HKLM\\SYSTEM\\CurrentControlSet\\Servi
ces\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,95afc12e-3cbb-40c3-9340-84a032e596a3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.011 

Title Description
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.01
1/T1574.011.md#atomic-test-1---service-registry-permissions-weakness 
https://docs.microsoft.com/en-
us/powershell/module/microsoft.powershell.security/get-acl?
view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/30 medium
Legitimate administrative script
Potential COM Objects Download Detects usage of COM objects that can be abused to download files in PowerShell by
Cradles Usage - PS Script CLSID
More details
Rule ID
powershell_scriptblock_43
Query
{'selection_1': {'ScriptBlockText|contains': '[Type]::G
etTypeFromCLSID('}, 'selection_2': {'ScriptBlockText|co
ntains': ['0002DF01-0000-0000-C000-
000000000046', 'F6D90F16-9C73-11D3-B32E-
00C04F990BB4', 'F5078F35-C551-11D3-89B9-
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
Monitoring PowerShell scripts
Script Block Logging must be enable
Rule Source
SigmaHQ,3c7d1587-3b13-439f-9941-7d14313dbdfe
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://learn.microsoft.com/en-us/dotnet/api/system.type.gettypefromclsid?
view=net-7.0 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=57 

Title Description
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/25 medium
Legitimate use of the library
Dnscat Execution Dnscat exfiltration tool execution
More details
Rule ID
powershell_scriptblock_44
Query
{'selection': {'ScriptBlockText|contains': 'Start-
Dnscat2'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a6d67db4-6220-436d-8afc-f3842fe05d43
Author: Daniil Yugoslavskiy, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0010 , T1048 
References
N/A
Severity
95
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2019/10/ critical
Legitimate usage of PowerShell Dnscat2 —
24 DNS Exfiltration tool (unlikely)
Suspicious Unblock-File Remove the Zone.Identifier alternate data stream which identifies the file as
downloaded from the internet.
More details
Rule ID
powershell_scriptblock_45

Title Description
Query
{'selection': {'ScriptBlockText|contains|all': ['Unbloc
k-File ', '-Path ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,5947497f-1aa4-41dd-9693-c9848d58727d
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.00
5/T1553.005.md#atomic-test-3---remove-the-zoneidentifier-alternate-data-
stream 
https://docs.microsoft.com/en-
us/powershell/module/microsoft.powershell.utility/unblock-file?
view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/01 medium
Legitimate PowerShell scripts
AMSI Bypass Pattern Assembly Detects code fragments found in small and obfuscated AMSI bypass PowerShell
GetType scripts
More details
Rule ID
powershell_scriptblock_47
Query
{'selection': {'ScriptBlockText|contains|all': ['[Ref].
Assembly.GetType', 'SetValue($null,$true)', 'NonPublic,
Static']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e0d6c087-2d1c-47fd-8799-3904103c5a98
Author: Florian Roth (Nextron Systems)

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.001 
References
https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-
evasion/ 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/09 high
Unknown
Remove Account From Domain Admin Adversaries may interrupt availability of system and network resources by inhibiting
Group access to accounts utilized by legitimate users. Accounts may be deleted, locked, or
manipulated (ex: changed credentials) to remove access to accounts.
More details
Rule ID
powershell_scriptblock_48
Query
{'selection': {'ScriptBlockText|contains|all': ['Remove
-ADGroupMember', '-Identity ', '-
Members ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,48a45d45-8112-416b-8a67-46e03a4b2107
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1531 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1531/T1
531.md#atomic-test-3---remove-account-from-domain-admin-group 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2021/12/26 medium
Unknown
Suspicious Hyper-V Cmdlets Adversaries may carry out malicious operations using a virtual instance to avoid
detection
More details
Rule ID
powershell_scriptblock_49
Query
{'selection': {'ScriptBlockText|contains': ['New-
VM', 'Set-VMFirmware', 'Start-
VM']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,42d36aa1-3240-4db0-8257-e0118dcdd9cd
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1564.006 
References
https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-
start/enable-hyper-v 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.00
6/T1564.006.md#atomic-test-3---create-and-start-hyper-v-virtual-
machine 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/09 medium
Legitimate PowerShell scripts
Zip A Folder With PowerShell For Use living off the land tools to zip a file and stage it in the Windows temporary folder
Staging In Temp - PowerShell Script for later exfiltration
More details
Rule ID
powershell_scriptblock_50
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['C
ompress-Archive ', ' -Path ', ' -

Title Description
DestinationPath ', '$env:TEMP\\']}, 'condition': 'selec
tion_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,b7a3c9a3-09ea-4934-8864-6a32cacd98d9
Author: Nasreddine Bencherchali (Nextron Systems), frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1074.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1074.00
1/T1074.001.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/20 medium
Unknown
PowerShell ShellCode Detects Base64 encoded Shellcode
More details
Rule ID
powershell_scriptblock_52
Query
{'selection': {'ScriptBlockText|contains': 'AAAAYInlM'}
, 'selection2': {'ScriptBlockText|contains': ['OiCAAAAY
InlM', 'OiJAAAAYInlM']}, 'condition': 'selection and se
lection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,16b37b70-6fcf-4814-a092-c36bd3aafcbd
Author: David Ledbetter (shellcode), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1055 
References

Title Description
https://twitter.com/cyb3rops/status/1063072865992523776 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/11/17 high
Unknown
Suspicious Eventlog Clear Detects usage of known powershell cmdlets such as "Clear-EventLog" to clear the
windows event logs
More details
Rule ID
powershell_scriptblock_53
Query
{'selection': {'ScriptBlockText|contains': ['Clear-
EventLog ', 'Remove-EventLog ', 'Limit-
EventLog ', 'Clear-
WinEvent ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,0f017df3-8f5a-414f-ad6b-24aff1128278
Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan
Poudel (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.001 
References
https://twitter.com/oroneequalsone/status/1568432028361830402 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.00
1/T1070.001.md 
https://eqllib.readthedocs.io/en/latest/analytics/5b223758-07d6-4100-9e11-
238cfdd0fe97.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Title Description
Matu Creat Risk False Positives
rity ion Lev
Date el
exper 2022/ medi
Rare need to clear logs before doing something.
iment 09/12 um Sometimes used by installers or cleaner scripts. The
al script should be investigated to determine if it's
legitimate
Powershell Local Email Collection Adversaries may target user email on local systems to collect sensitive information.
Files containing email data can be acquired from a users local system, such as
Outlook storage or cache files.
More details
Rule ID
powershell_scriptblock_54
Query
{'selection': {'ScriptBlockText|contains': ['Get-
Inbox.ps1', 'Microsoft.Office.Interop.Outlook', 'Micros
oft.Office.Interop.Outlook.olDefaultFolders', '-
comobject outlook.application']}, 'condition': 'selecti
on'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,2837e152-93c8-43d2-85ba-c3cd3c2ae614
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1114.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1114.001
/T1114.001.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/21 medium
Unknown
Suspicious FromBase64String Usage Detects attempts of decoding a base64 Gzip archive in a PowerShell script. This
On Gzip Archive - Ps Script technique is often used as a method to load malicious content into memory afterward.
More details
Rule ID
powershell_scriptblock_55

Title Description
Query
{'selection': {'ScriptBlockText|contains|all': ['FromBa
se64String', 'MemoryStream', 'H4sI']}, 'condition': 'se
lection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,df69cb1d-b891-4cd9-90c7-d617d90100ce
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=43 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium
Legitimate administrative script
PowerShell ADRecon Execution Detects execution of ADRecon.ps1 for AD reconnaissance which has been reported to
be actively used by FIN7
More details
Rule ID
powershell_scriptblock_56
Query
{'selection': {'ScriptBlockText|contains': ['Function G
et-ADRExcelComOb', 'Get-ADRGPO', 'Get-
ADRDomainController', 'ADRecon-
Report.xlsx']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,bf72941a-cba0-41ea-b18c-9aca3925690d
Author: Bhabesh Raj
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1059.001 
References
https://github.com/sense-of-
security/ADRecon/blob/11881a24e9c8b207f31b56846809ce1fb189bcc9/AD
Recon.ps1 
https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-
fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/16 high
Unknown
Access to Browser Login Data Adversaries may acquire credentials from web browsers by reading files specific to the
target browser. Web browsers commonly save credentials such as website usernames
and passwords so that they do not need to be entered manually in the future. Web
browsers typically store the credentials in an encrypted format within a credential
store.
More details
Rule ID
powershell_scriptblock_57
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['Co
py-Item', '-
Destination']}, 'selection_path': {'ScriptBlockText|con
tains': ['\\Opera Software\\Opera Stable\\Login Data',
'\\Mozilla\\Firefox\\Profiles', '\\Microsoft\\Edge\\Use
r Data\\Default', '\\Google\\Chrome\\User Data\\Default
\\Login Data', '\\Google\\Chrome\\User Data\\Default\\L
ogin Data For Account']}, 'condition': 'all of selectio
n_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,fc028194-969d-4122-8abe-0470d5b8f12f
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1555.003 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555.00
3/T1555.003.md 
Severity

Title Description
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/30 medium
Unknown
Abuse of Service Permissions to Hide Detects usage of the "Set-Service" powershell cmdlet to configure a new
Services Via Set-Service - PS SecurityDescriptor that allows a service to be hidden from other utilities such as
"sc.exe", "Get-Service"...etc. (Works only in powershell 7)
More details
Rule ID
powershell_scriptblock_58
Query
{'selection': {'ScriptBlockText|contains|all': ['Set-
Service ', 'DCLCWPDTSD'], 'ScriptBlockText|contains': [
'-SecurityDescriptorSddl ', '-
sd ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,953945c5-22fe-4a92-9f8a-a9edc1e522da
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.011 
References
https://twitter.com/Alh4zr3d/status/1580925761996828672 
https://learn.microsoft.com/en-
us/powershell/module/microsoft.powershell.management/set-service?
view=powershell-7.2 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experim 2022/10/ high
Rare intended use of hidden services
ental 17
Rare FP could occure due to the non linearity
of the ScriptBlockText log
Computer Discovery And Export Via Detects usage of the Get-ADComputer cmdlet to collect computer information and
Get-ADComputer Cmdlet - output it to a file

Title Description
PowerShell More details
Rule ID
powershell_scriptblock_59
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
ADComputer ', ' -
Filter *'], 'ScriptBlockText|contains': [' |
Select ', 'Out-File', 'Set-Content', 'Add-
Content']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,db885529-903f-4c5d-9864-28fe199e6370
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1033 
References
http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html 
https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-
beware-a-case-for-post-ransomware-investigations/ 
https://www.cisa.gov/uscert/sites/default/files/publications/aa22-
320a_joint_csa_iranian_government-
sponsored_apt_actors_compromise_federal%20network_deploy_crypto%2
0miner_credential_harvester.pdf 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Matu Creat Risk False Positives
rity ion Leve
Date l
exper 2022/ medi
Legitimate admin scripts may use the same technique,
iment 11/17 um it's better to exclude specific computers or users who
al execute these commands or scripts often
PowerShell PSAttack Detects the use of PSAttack PowerShell hack tool
More details
Rule ID
powershell_scriptblock_60
Query
{'selection': {'ScriptBlockText|contains': 'PS ATTACK!!
!'}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,b7ec41a4-042c-4f31-a5db-d0fcde9fa5c5
Author: Sean Metcalf (source), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://adsecurity.org/?p=2921 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/05 high
Unknown
PowerShell Invoke-NinjaCopy script Detects PowerShell scripts that contain the default exported functions used on Invoke-
NinjaCopy. Attackers can use Invoke-NinjaCopy to read SYSTEM files that are
normally locked, such as the NTDS.dit file or registry hives.
More details
Rule ID
powershell_scriptblock_61
Query
{'selection1': {'ScriptBlockText|contains': ['StealthRe
adFile', 'StealthReadFileAddr', 'StealthCloseFileDelega
te', 'StealthOpenFile', 'StealthCloseFile', 'Invoke-
NinjaCopy']}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 
References
N/A
Severity
49

Title Description
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/23 medium N/A
Delete Volume Shadow Copies via Deletes Windows Volume Shadow Copies with PowerShell code and Get-WMIObject.
WMI with PowerShell - PS Script This technique is used by numerous ransomware families such as Sodinokibi/REvil
More details
Rule ID
powershell_scriptblock_62
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
WmiObject', 'Win32_Shadowcopy', '.Delete()']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e17121b4-ef2a-4418-8a59-12fb1631fa9e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1490 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1
490.md#atomic-test-5---windows---delete-volume-shadow-copies-via-wmi-
with-powershell 
Severity
80
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/26 high
Unknown
PowerShell ICMP Exfiltration Detects Exfiltration Over Alternative Protocol - ICMP. Adversaries may steal data by
exfiltrating it over an un-encrypted network protocol other than that of the existing
command and control channel.
More details
Rule ID
powershell_scriptblock_63
Query

Title Description
{'selection': {'ScriptBlockText|contains|all': ['New-
Object', 'System.Net.NetworkInformation.Ping', '.Send('
]}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4c4af3cd-2115-479c-8193-6b8bfce9001c
Author: Bartlomiej Czyz @bczyz1, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0010 , T1048.003 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048.00
3/T1048.003.md#atomic-test-2---exfiltration-over-alternative-protocol---
icmp 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2020/10/1 medium
Legitimate usage of
0 System.Net.NetworkInformation.Ping class
AD Groups Or Users Enumeration Adversaries may attempt to find domain-level groups and permission settings. The
Using PowerShell - ScriptBlock knowledge of domain-level permission groups can help adversaries determine which
groups exist and which users belong to a particular group. Adversaries may use this
information to determine which users have elevated permissions, such as domain
administrators.
More details
Rule ID
powershell_scriptblock_64
Query
{'test_2': {'ScriptBlockText|contains': 'get-
ADPrincipalGroupMembership'}, 'test_7': {'ScriptBlockTe
xt|contains|all': ['get-aduser', '-f ', '-
pr ', 'DoesNotRequirePreAuth']}, 'condition': '1 of tes
t_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source

Title Description
SigmaHQ,88f0884b-331d-403d-a3a1-b668cf035603
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1069.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.00
2/T1069.002.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/15 low
Unknown
Tamper Windows Defender Remove- Detects attempts to remove windows defender configuration using the 'MpPreference'
MpPreference - ScriptBlockLogging cmdlet
More details
Rule ID
powershell_scriptblock_65
Query
{'selection_remove': {'ScriptBlockText|contains': 'Remo
ve-
MpPreference'}, 'selection_tamper': {'ScriptBlockText|c
ontains': ['-
ControlledFolderAccessProtectedFolders ', '-
AttackSurfaceReductionRules_Ids ', '-
AttackSurfaceReductionRules_Actions ', '-
CheckForSignaturesBeforeRunningScan ']}, 'condition': '
all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,ae2bdd58-0681-48ac-be7f-58ab4e593458
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.001 
References
https://techcommunity.microsoft.com/t5/core-infrastructure-and-
security/windows-10-controlled-folder-access-event-search/ba-
p/2326088 
Severity

Title Description
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/05 high
Legitimate PowerShell scripts
Invoke-Obfuscation COMPRESS Detects Obfuscated Powershell via COMPRESS OBFUSCATION
OBFUSCATION - PowerShell
More details
Rule ID
powershell_scriptblock_66
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['n
ew-
object', 'text.encoding]::ascii'], 'ScriptBlockText|con
tains': ['system.io.compression.deflatestream', 'system
.io.streamreader'], 'ScriptBlockText|endswith': 'readto
end'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,20e5497e-331c-4cd5-8d36-935f6e2a9a07
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium
Unknown
Potential Data Exfiltration Via Audio Detects potential exfiltration attempt via audio file using PowerShell
File
More details
Rule ID
powershell_scriptblock_67
Query

Title Description
{'selection_main': {'ScriptBlockText|contains|all': ['[
System.Math]::', '[IO.FileMode]::', 'BinaryWriter']}, '
selection_header_wav': {'ScriptBlockText|contains|all':
['0x52', '0x49', '0x46', '0x57', '0x41', '0x56', '0x45
', '0xAC']}, 'condition': 'selection_main and 1 of sele
ction_header_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e4f93c99-396f-47c8-bb0f-201b1fa69034
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/gtworek/PSBits/blob/e97cbbb173b31cbc4d37244d3412d
e0a114dacfb/NoDLP/bin2wav.ps1 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/16 medium
Unknown
Create Volume Shadow Copy with Adversaries may attempt to access or create a copy of the Active Directory domain
Powershell database in order to steal credential information
More details
Rule ID
powershell_scriptblock_68
Query
{'selection': {'ScriptBlockText|contains|all': ['win32_
shadowcopy', ').Create(', 'ClientAccessible']}, 'condit
ion': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,afd12fed-b0ec-45c9-a13d-aa86625dac81
Author: frack113
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1059.001 , TA0006 , T1003.003 
References
https://attack.mitre.org/datasources/DS0005/ 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/12 high
Legitimate PowerShell scripts
Invoke-Obfuscation Obfuscated IEX Detects all variations of obfuscated powershell IEX invocation code generated by
Invocation - PowerShell Invoke-Obfuscation framework from the following code block \u2014
More details
Rule ID
powershell_scriptblock_69
Query
{'selection_iex': [{'ScriptBlockText|re': '\\$PSHome\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$PSHome\\
['}, {'ScriptBlockText|re': '\\$ShellId\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$ShellId\\
['}, {'ScriptBlockText|re': '\\$env:Public\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$env:Public\\
['}, {'ScriptBlockText|re': '\\$env:ComSpec\\
[(\\s*\\d{1,3}\\s*,)
{2}'}, {'ScriptBlockText|re': '\\*mdr\\*\\W\\s*\\)\\.Na
me'}, {'ScriptBlockText|re': '\\$VerbosePreference\\.To
String\\('}], 'condition': 'selection_iex'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1b9dc62e-6e9e-42a3-8990-94d7a10007f7
Author: Daniel Bohannon (@Mandiant/@FireEye), oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/danielbohannon/Invoke-
Obfuscation/blob/f20e7f843edd0a3a7716736e9eddfa423395dd26/Out-
ObfuscatedStringCommand.ps1#L873-L888 
Severity
74
Suppression Logic Based On
computer_name

Title Description
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/11/08 high
Unknown
Malicious ShellIntel PowerShell Detects Commandlet names from ShellIntel exploitation scripts.
Commandlets
More details
Rule ID
powershell_scriptblock_70
Query
{'selection': {'ScriptBlockText|contains': ['Invoke-
SMBAutoBrute', 'Invoke-GPOLinks', 'Invoke-
Potato']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,402e1e1d-ad59-47b6-bf80-1ee44985b3a7
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/Shellntel/scripts/ 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high
Unknown
Change User Agents with Adversaries may communicate using application layer protocols associated with web
WebRequest traffic to avoid detection/network filtering by blending in with existing traffic.
Commands to the remote system, and often the results of those commands, will be
embedded within the protocol traffic between the client and server.
More details
Rule ID
powershell_scriptblock_71
Query
{'selection': {'ScriptBlockText|contains|all': ['Invoke
-WebRequest', '-
UserAgent ']}, 'condition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,d4488827-73af-4f8d-9244-7b7662ef046e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1071.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1071.00
1/T1071.001.md#t1071001---web-protocols 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/23 medium
Unknown
Powershell Timestomp Adversaries may modify file time attributes to hide new or changes to existing files.
Timestomping is a technique that modifies the timestamps of a file (the modify, access,
create, and change times), often to mimic files that are in the same folder.
More details
Rule ID
powershell_scriptblock_72
Query
{'selection_ioc': {'ScriptBlockText|contains': ['.Creat
ionTime =', '.LastWriteTime =', '.LastAccessTime =', '[
IO.File]::SetCreationTime', '[IO.File]::SetLastAccessTi
me', '[IO.File]::SetLastWriteTime']}, 'condition': 'sel
ection_ioc'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c6438007-e081-42ce-9483-b067fbef33c3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.006 
References

Title Description
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.00
6/T1070.006.md 
https://www.offensive-security.com/metasploit-unleashed/timestomp/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/03 medium
Legitimate admin script
Powershell MsXml COM Object Adversaries may abuse PowerShell commands and scripts for execution. PowerShell
is a powerful interactive command-line interface and scripting environment included in
the Windows operating system. (Citation: TechNet PowerShell) Adversaries can use
PowerShell to perform a number of actions, including discovery of information and
execution of code
More details
Rule ID
powershell_scriptblock_73
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
Object', '-
ComObject', 'MsXml2.', 'XmlHttp']}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,78aa1347-1517-4454-9982-b338d6df8343
Author: frack113, MatilJ
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.00
1/T1059.001.md#atomic-test-7---powershell-msxml-com-object---with-
prompt 
https://docs.microsoft.com/en-us/previous-
versions/windows/desktop/ms766431(v=vs.85) 
https://www.trendmicro.com/en_id/research/22/e/uncovering-a-kingminer-
botnet-attack-using-trend-micro-managed-x.html 
Severity
49
Suppression Logic Based On
computer_name

Title Description
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/19 medium
Legitimate administrative script
User Discovery And Export Via Get- Detects usage of the Get-ADUser cmdlet to collect user information and output it to a
ADUser Cmdlet - PowerShell file
More details
Rule ID
powershell_scriptblock_74
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
ADUser ', ' -
Filter *'], 'ScriptBlockText|contains': [' > ', ' |
Select ', 'Out-File', 'Set-Content', 'Add-
Content']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c2993223-6da8-4b1a-88ee-668b8bf315e9
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1033 
References
http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html 
https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-
beware-a-case-for-post-ransomware-investigations/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Matu Creat Risk False Positives
rity ion Leve
Date l
exper 2022/ medi
Legitimate admin scripts may use the same technique,
iment 11/17 um it's better to exclude specific computers or users who
al execute these commands or scripts often
Active Directory Group Enumeration Detects usage of the "Get-AdGroup" cmdlet to enumerate Groups within Active
With Get-AdGroup Directory
More details
Rule ID

Title Description
powershell_scriptblock_75
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
AdGroup ', '-Filter']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,8c3a6607-b7dc-4f0d-a646-ef38c00b76ee
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1069.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1
018.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/03/17 low
Unknown
WMIC Unquoted Services Path Detects known WMI recon method to look for unquoted service paths, often used by
Lookup - PowerShell pentest inside of powershell scripts attackers enum scripts
More details
Rule ID
powershell_scriptblock_76
Query
{'selection': {'ScriptBlockText|contains': ['Get-
WmiObject ', 'gwmi '], 'ScriptBlockText|contains|all':
[' Win32_Service ', 'Name', 'DisplayName', 'PathName',
'StartMode']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,09658312-bc27-4a3b-91c5-e49ab9046d1b
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1047 , T1059.001 
References
https://github.com/nccgroup/redsnarf/blob/35949b30106ae543dc6f2bc3f1b
e10c6d9a8d40e/redsnarf.py 
https://github.com/S3cur3Th1sSh1t/Creds/blob/eac23d67f7f90c7fc8e31305
87d86158c22aa398/PowershellScripts/jaws-enum.ps1 
https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-
Guide/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/20 medium
Unknown
Get-ADUser Enumeration Using Detects AS-REP roasting is an attack that is often-overlooked. It is not very common
UserAccountControl Flags as you have to explicitly set accounts that do not require pre-authentication.
More details
Rule ID
powershell_scriptblock_77
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
ADUser', '-Filter', 'useraccountcontrol', '-
band', '4194304']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,96c982fe-3d08-4df4-bed2-eb14e02f21c8
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1033 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.00
2/T1069.002.md#atomic-test-11---get-aduser-enumeration-using-
useraccountcontrol-flags-as-rep-roasting 
https://shellgeek.com/useraccountcontrol-flags-to-manipulate-properties/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/17 medium
Legitimate PowerShell scripts
Windows Defender Exclusions Added Detects modifications to the Windows Defender configuration settings using
- PowerShell PowerShell to add exclusions
More details
Rule ID
powershell_scriptblock_79
Query
{'selection_args_exc': {'ScriptBlockText|contains': ['
-ExclusionPath ', ' -ExclusionExtension ', ' -
ExclusionProcess ', ' -
ExclusionIpAddress ']}, 'selection_args_pref': {'Script
BlockText|contains': ['Add-MpPreference ', 'Set-
MpPreference ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c1344fa2-323b-4d2e-9176-84b4d4821c88
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562 
References
https://www.elastic.co/guide/en/security/current/windows-defender-
exclusions-added-via-powershell.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/16 medium
Unknown
Suspicious Get-ADReplAccount The DSInternals PowerShell Module exposes several internal features of Active
Directory and Microsoft Entra ID. These include FIDO2 and NGC key auditing, offline
ntds.dit file manipulation, password auditing, DC recovery from IFM backups and
password hash calculation.
More details
Rule ID
powershell_scriptblock_80
Query

Title Description
{'selection': {'ScriptBlockText|contains|all': ['Get-
ADReplAccount', '-All ', '-
Server ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,060c3ef1-fd0a-4091-bf46-e7d625f60b73
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003.006 
References
https://www.powershellgallery.com/packages/DSInternals 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.00
6/T1003.006.md#atomic-test-2---run-dsinternals-get-adreplaccount 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/06 medium
Legitimate PowerShell scripts
PowerShell Suspicious Script with Detects PowerShell scripts that can record audio, a common feature in popular post-
Audio Capture Capabilities exploitation tooling.
More details
Rule ID
powershell_scriptblock_81
Query
{'selection1': {'ScriptBlockText|contains': 'Get-
MicrophoneAudio'}, 'selection2': {'ScriptBlockText|cont
ains': 'waveInGetNumDevs'}, 'selection3': {'ScriptBlock
Text|contains': 'mciSendStringA'}, 'selection4': {'User
Id': 'S-1-5-
18'}, 'condition': '(selection1 or (selection2 and sele
ction3)) and (not selection4)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1059.001 , TA0009 , T1123 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/19 medium N/A
PowerShell Suspicious Script with Detects PowerShell scripts that can get the contents of the clipboard, which attackers
Clipboard Retrieval Capabilities can abuse to retrieve sensitive information like credentials, messages, etc.
More details
Rule ID
powershell_scriptblock_82
Query
{'selection1': {'ScriptBlockText|contains': 'Get-
Clipboard'}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1115 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/12 medium N/A
PowerShell Get-Process LSASS in Detects a Get-Process command on lsass process, which is in almost all cases a sign
ScriptBlock of malicious activity
More details
Rule ID
powershell_scriptblock_83

Title Description
Query
{'selection': {'ScriptBlockText|contains': 'Get-
Process lsass'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,84c174ab-d3ef-481f-9c86-a50d0b8e3edb
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003.001 
References
https://twitter.com/PythonResponder/status/1385064506049630211 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urit on Leve
y Date l
test 2021/0 high
Legitimate certificate exports invoked by
4/23 administrators or users (depends on processes in the
environment - filter if unusable)
Password Policy Discovery With Get- Detetcts PowerShell activity in which Get-Addefaultdomainpasswordpolicy is used to
AdDefaultDomainPasswordPolicy get the default password policy for an Active Directory domain.
More details
Rule ID
powershell_scriptblock_84
Query
{'selection': {'ScriptBlockText|contains': 'Get-
AdDefaultDomainPasswordPolicy'}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,bbb9495b-58fc-4016-b9df-9a3a1b67ca82
Author: frack113
Tactics, Techniques, and Procedures

Title Description
TA0002 , T1059.001 , TA0007 , T1201 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1201/T1
201.md#atomic-test-9---enumerate-active-directory-password-policy-with-
get-addefaultdomainpasswordpolicy 
https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-
addefaultdomainpasswordpolicy 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/17 low
Legitimate PowerShell scripts
Suspicious PowerShell Invocations - Detects suspicious PowerShell invocation command parameters
Generic
More details
Rule ID
powershell_scriptblock_85
Query
{'selection_encoded': {'ScriptBlockText|contains': [' -
enc ', ' -EncodedCommand ', ' -
ec ']}, 'selection_hidden': {'ScriptBlockText|contains'
: [' -w hidden ', ' -window hidden ', ' -
windowstyle hidden ', ' -
w 1 ']}, 'selection_noninteractive': {'ScriptBlockText|
contains': [' -noni ', ' -
noninteractive ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,ed965133-513f-41d9-a441-e38076a0798f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2017/03/12 high
Very special / sneaky PowerShell
scripts
NTFS Alternate Data Stream Detects writing data into NTFS alternate data streams from powershell. Needs Script
Block Logging.
More details
Rule ID
powershell_scriptblock_88
Query
{'selection_content': {'ScriptBlockText|contains': ['se
t-content', 'add-
content']}, 'selection_stream': {'ScriptBlockText|conta
ins': '-stream'}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,8c521530-5169-495d-a199-0a3a881ad24e
Author: Sami Ruohonen
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1564.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.00
4/T1564.004.md 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/07/24 high
Unknown
Suspicious Invoke-Item From Mount- Adversaries may abuse container files such as disk image (.iso, .vhd) file formats to
DiskImage deliver malicious payloads that may not be tagged with MOTW.
More details
Rule ID
powershell_scriptblock_89
Query

Title Description
{'selection': {'ScriptBlockText|contains|all': ['Mount-
DiskImage ', '-ImagePath ', 'Get-
Volume', '.DriveLetter', 'invoke-
item ', '):\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,902cedee-0398-4e3a-8183-6f3a89773a96
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.00
5/T1553.005.md#atomic-test-2---mount-an-iso-image-and-run-executable-
from-the-iso 
https://docs.microsoft.com/en-us/powershell/module/storage/mount-
diskimage?view=windowsserver2022-ps 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/01 medium
Legitimate PowerShell scripts
PowerShell WMI Win32_Product Detects the execution of an MSI file using PowerShell and the WMI Win32_Product
Install MSI class
More details
Rule ID
powershell_scriptblock_90
Query
{'selection': {'ScriptBlockText|contains|all': ['Invoke
-CimMethod ', '-ClassName ', 'Win32_Product ', '-
MethodName ', '.msi']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,91109523-17f0-4248-a800-f81d9e7c081d
Author: frack113

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1218.007 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.00
7/T1218.007.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/24 medium
Unknown
Suspicious GetTypeFromCLSID Detects suspicious Powershell code that execute COM Objects
ShellExecute
More details
Rule ID
powershell_scriptblock_92
Query
{'selection': {'ScriptBlockText|contains|all': ['::GetT
ypeFromCLSID(', '.ShellExecute(']}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,8bc063d5-3a3a-4f01-a140-bc15e55e8437
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1546.015 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.01
5/T1546.015.md#atomic-test-2---powershell-execute-com-object 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/02 medium
Legitimate PowerShell scripts

Title Description
Silence.EDA Detection Detects Silence EmpireDNSAgent as described in the Group-IP report
More details
Rule ID
powershell_scriptblock_93
Query
{'empire': {'ScriptBlockText|contains|all': ['System.Di
agnostics.Process', 'Stop-Computer', 'Restart-
Computer', 'Exception in execution', '$cmdargs', 'Close
-
Dnscat2Tunnel']}, 'dnscat': {'ScriptBlockText|contains|
all': ['set type=$LookupType`nserver', '$Command |
nslookup 2>&1 | Out-String', 'New-
RandomDNSField', '[Convert]::ToString($SYNOptions, 16)'
, '$Session.Dead = $True', '$Session["Driver"] -
eq']}, 'condition': 'empire and dnscat'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,3ceb2083-a27f-449a-be33-14ec1b7cc973
Author: Alina Stepchenkova, Group-IB, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1071.004 , T1572 , TA0040 ,
T1529 
References
https://www.group-ib.com/resources/threat-
research/silence_2.0.going_global.pdf 
Severity
95
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/11/01 critical
Unknown
Potential Active Directory Enumeration Detects usage of the "Import-Module" cmdlet to load the
Using AD Module - PsScript "Microsoft.ActiveDirectory.Management.dl" DLL. Which is often used by attackers to
perform AD enumeration.
More details
Rule ID
powershell_scriptblock_94
Query

Title Description
{'selection_generic': {'ScriptBlockText|contains|all':
['Import-
Module ', 'Microsoft.ActiveDirectory.Management.dll']},
'selection_specific': {'ScriptBlockText|contains': 'ip
mo Microsoft.ActiveDirectory.Management.dll'}, 'conditi
on': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enable
Rule Source
SigmaHQ,9e620995-f2d8-4630-8430-4afd89f77604
Author: frack113, Nasreddine Bencherchali
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/samratashok/ADModule 
https://twitter.com/cyb3rops/status/1617108657166061568?s=20 
https://www.ired.team/offensive-security-experiments/active-directory-
kerberos-abuse/active-directory-enumeration-with-ad-module-without-rsat-
or-admin-privileges 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2023/01/22 medium
Legitimate use of the library for
ntal administrative activity
Automated Collection Bookmarks Adversaries may enumerate browser bookmarks to learn more about compromised
Using Get-ChildItem PowerShell hosts. Browser bookmarks may reveal personal information about users (ex: banking
sites, interests, social media, etc.) as well as details about internal network resources
such as servers, tools/dashboards, or other related infrastructure.
More details
Rule ID
powershell_scriptblock_95
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
ChildItem', ' -Recurse ', ' -Path ', ' -
Filter Bookmarks', ' -
ErrorAction SilentlyContinue', ' -
Force']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e0565f5d-d420-4e02-8a68-ac00d864f9cf
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1217 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T1
217.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/13 low
Unknown
SyncAppvPublishingServer Execution Detects SyncAppvPublishingServer process execution which usually utilized by
to Bypass Powershell Restriction adversaries to bypass PowerShell execution restrictions.
More details
Rule ID
powershell_scriptblock_96
Query
{'selection': {'ScriptBlockText|contains': 'SyncAppvPub
lishingServer.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,dddfebae-c46f-439c-af7a-fdb6bde90218
Author: Ensar Şamil, @sblmsrsn, OSCD Community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1218 
References
https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/05 medium
App-V clients
Disable Powershell Command History Detects scripts or commands that disabled the Powershell command history by
removing psreadline module
More details
Rule ID
powershell_scriptblock_97
Query
{'selection': {'ScriptBlockText|contains|all': ['Remove
-Module', 'psreadline']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,602f5669-6927-4688-84db-0d4b7afb2150
Author: Ali Alwashali
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://twitter.com/DissectMalware/status/1062879286749773824 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2022/08/21 high
Legitimate script that disables the
tal command history
Manipulation of User Computer or Adversaries may create a domain account to maintain access to victim systems.
Group Security Principals Across AD Domain accounts are those managed by Active Directory Domain Services where
access and permissions are configured across systems and services that are part of
that domain..
More details
Rule ID
powershell_scriptblock_98
Query
{'selection': {'ScriptBlockText|contains': 'System.Dire
ctoryServices.AccountManagement'}, 'condition': 'select

Title Description
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,b29a93fb-087c-4b5b-a84d-ee3309e69d08
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1136.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.00
2/T1136.002.md#atomic-test-3---create-a-new-domain-account-using-
powershell 
https://docs.microsoft.com/en-
us/dotnet/api/system.directoryservices.accountmanagement?view=dotnet-
plat-ext-6.0 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/28 medium
Legitimate administrative script
PowerShell Suspicious Payload Identifies the use of .NET functionality for decompression and base64 decoding
Encoded and Compressed combined in PowerShell scripts, which malware and security tools heavily use to
deobfuscate payloads and load them directly in memory to bypass defenses.
More details
Rule ID
powershell_scriptblock_99
Query
{'selection1': {'ScriptBlockText|contains': 'System.IO.
Compression.DeflateStream'}, 'selection2': {'ScriptBloc
kText|contains': 'System.IO.Compression.GzipStream'}, '
selection3': {'ScriptBlockText|contains': 'IO.Compressi
on.DeflateStream'}, 'selection4': {'ScriptBlockText|con
tains': 'IO.Compression.GzipStream'}, 'selection5': {'S
criptBlockText|contains': 'FromBase64String'}, 'selecti
on6': {'UserId': 'S-1-5-
18'}, 'condition': '(selection1 or selection2 or select
ion3 or selection4) and selection5 and (not selection6)
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Title Description
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 , T1140 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2021/10/ mediu
Legitimate PowerShell Scripts which makes use
tion 19 m of compression and encoding.
Powershell Trigger Profiles by Adversaries may gain persistence and elevate privileges by executing malicious
Add_Content content triggered by PowerShell profiles.
More details
Rule ID
powershell_scriptblock_100
Query
{'selection': {'ScriptBlockText|contains|all': ['Add-
Content', '$profile', '-
Value'], 'ScriptBlockText|contains': ['Start-
Process', '""']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,05b3e303-faf0-4f4a-9b30-46cc13e69152
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1546.013 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.01
3/T1546.013.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/18 medium
Unknown
Windows Screen Capture with Adversaries may attempt to take screen captures of the desktop to gather information
CopyFromScreen over the course of an operation. Screen capturing functionality may be included as a
feature of a remote access tool used in post-compromise operations
More details
Rule ID
powershell_scriptblock_101
Query
{'selection': {'ScriptBlockText|contains': '.CopyFromSc
reen'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,d4a11f63-2390-411c-9adf-d791fd152830
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1113 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1113/T11
13.md#atomic-test-6---windows-screen-capture-copyfromscreen 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/28 medium
Unknown
Clear PowerShell History - PowerShell Detects keywords that could indicate clearing PowerShell history
More details
Rule ID
powershell_scriptblock_102
Query
{'selection1a': {'ScriptBlockText|contains': ['del', 'R
emove-
Item', 'rm']}, 'selection1b': {'ScriptBlockText|contain
s': '(Get-

Title Description
PSReadlineOption).HistorySavePath'}, 'selection_2': {'S
criptBlockText|contains|all': ['Set-
PSReadlineOption', '–
HistorySaveStyle', 'SaveNothing']}, 'selection_3': {'Sc
riptBlockText|contains|all': ['Set-
PSReadlineOption', '-
HistorySaveStyle', 'SaveNothing']}, 'condition': '1 of
selection_* or all of selection1*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,26b692dc-1722-49b2-b496-a8258aa6371d
Author: Ilyas Ochkov, Jonhnathan Ribeiro, Daniil Yugoslavskiy, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://gist.github.com/hook-s3c/7363a856c3cdbadeb71085147f042c1a 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/25 medium
Legitimate PowerShell scripts
PowerShell Share Enumeration Script Detects scripts that contain PowerShell functions, structures, or Windows API
functions related to windows share enumeration activities. Attackers, mainly
ransomware groups, commonly identify and inspect network shares, looking for critical
information for encryption and/or exfiltration.
More details
Rule ID
powershell_scriptblock_103
Query
{'selection1': {'ScriptBlockText|contains': ['Invoke-
ShareFinder', 'Invoke-
ShareFinderThreaded']}, 'selection2': {'ScriptBlockText
|contains': 'shi1_netname'}, 'selection3': {'ScriptBloc
kText|contains': 'shi1_remark'}, 'selection4': {'Script
BlockText|contains': 'NetShareEnum'}, 'selection5': {'S
criptBlockText|contains': 'NetApiBufferFree'}, 'selecti
on6': {'UserId': 'S-1-5-
18'}, 'condition': '(selection1 or (selection2 and sele
ction3) or (selection4 and selection5)) and (not select
ion6)'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , T1106 , TA0007 , T1135 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/08/17 medium N/A
DirectorySearcher Powershell Enumerates Active Directory to determine computers that are joined to the domain
Exploitation
More details
Rule ID
powershell_scriptblock_104
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
Object ', 'System.DirectoryServices.DirectorySearcher',
'.PropertiesToLoad.Add', '.findall()', 'Properties.nam
e']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1f6399cf-2c80-4924-ace1-6fcff3393480
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1018 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1
018.md#atomic-test-15---enumerate-domain-computers-within-active-
directory-using-directorysearcher 
Severity
49
Suppression Logic Based On

Title Description
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/12 medium
Unknown
Invoke-Obfuscation STDIN+ Launcher Detects Obfuscated use of stdin to execute PowerShell
- Powershell
More details
Rule ID
powershell_scriptblock_105
Query
{'selection_4104': {'ScriptBlockText|re': '.*cmd.{0,5}
(?:/c|/r).+powershell.+(?:\\$?\\{?input\\}?
|noexit).+"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,779c8c12-0eb1-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high
Unknown
Powershell Install a DLL in System Uses PowerShell to install/copy a a file into a system directory such as "System32" or
Directory "SysWOW64"
More details
Rule ID
powershell_scriptblock_106
Query
{'selection_copy': {'ScriptBlockText|contains|all': ['C
opy-Item ', '-
Destination ']}, 'selection_paths': {'ScriptBlockText|c

Title Description
ontains': ['\\Windows\\System32', '\\Windows\\SysWOW64'
]}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,63bf8794-9917-45bc-88dd-e1b5abc0ecfd
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1556.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1556.00
2/T1556.002.md#atomic-test-1---install-and-register-password-filter-dll 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/27 high
Unknown
Deletion of Volume Shadow Copies Detects deletion of Windows Volume Shadow Copies with PowerShell code and Get-
via WMI with PowerShell - PS Script WMIObject. This technique is used by numerous ransomware families such as
Sodinokibi/REvil
More details
Rule ID
powershell_scriptblock_107
Query
{'selection_get': {'ScriptBlockText|contains': ['Get-
WmiObject', 'gwmi', 'Get-
CimInstance', 'gcim']}, 'selection_shadowcopy': {'Scrip
tBlockText|contains': 'Win32_Shadowcopy'}, 'selection_d
elete': {'ScriptBlockText|contains': ['.Delete()', 'Rem
ove-WmiObject', 'rwmi', 'Remove-
CimInstance', 'rcim']}, 'condition': 'all of selection*
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
SigmaHQ,c1337eb8-921a-4b59-855b-4ba188ddcc42
Author: Tim Rauch, frack113

Title Description
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1490 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1
490.md#atomic-test-5---windows---delete-volume-shadow-copies-via-wmi-
with-powershell 
https://www.elastic.co/guide/en/security/current/volume-shadow-copy-
deletion-via-powershell.html 
Severity
80
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/20 high
Unknown
Code Executed Via Office Add-in XLL Adversaries may abuse Microsoft Office add-ins to obtain persistence on a
File compromised system. Office add-ins can be used to add functionality to Office
programs
More details
Rule ID
powershell_scriptblock_108
Query
{'selection': {'ScriptBlockText|contains|all': ['new-
object ', '-
ComObject ', '.application', '.RegisterXLL']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,36fbec91-fa1b-4d5d-8df1-8d8edcb632ad
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1137.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1137.00
6/T1137.006.md 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/28 high
Unknown
PSAsyncShell - Asynchronous TCP Detects the use of PSAsyncShell an Asynchronous TCP Reverse Shell written in
Reverse Shell powershell
More details
Rule ID
powershell_scriptblock_109
Query
{'selection': {'ScriptBlockText|contains': 'PSAsyncShel
l'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,afd3df04-948d-46f6-ae44-25966c44b97f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/JoelGMSec/PSAsyncShell 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/04 high
Unlikely
Recon Information for Export with Once established within a system or network, an adversary may use automated
PowerShell techniques for collecting internal data
More details
Rule ID
powershell_scriptblock_110
Query
{'selection_action': {'ScriptBlockText|contains': ['Get
-Service ', 'Get-ChildItem ', 'Get-
Process ']}, 'selection_redirect': {'ScriptBlockText|co
ntains': '> $env:TEMP\\'}, 'condition': 'all of selecti
on*'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a9723fcc-881c-424c-8709-fd61442ab3c3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1119 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1119/T11
19.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/30 medium
Unknown
Enable Windows Remote Adversaries may use Valid Accounts to interact with remote systems using Windows
Management Remote Management (WinRM). The adversary may then perform actions as the
logged-on user.
More details
Rule ID
powershell_scriptblock_111
Query
{'selection_cmdlet': {'ScriptBlockText|contains': 'Enab
le-PSRemoting '}, 'condition': 'selection_cmdlet'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,991a9744-f2f0-44f2-bd33-9092eba17dc3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0008 , T1021.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.00
6/T1021.006.md#atomic-test-1---enable-windows-remote-management 

Title Description
https://docs.microsoft.com/en-
us/powershell/module/microsoft.powershell.core/enable-psremoting?
view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/07 medium
Legitimate script
Enumerate Credentials from Windows Adversaries may search for common password storage locations to obtain user
Credential Manager With PowerShell credentials. Passwords are stored in several places on a system, depending on the
operating system or application holding the credentials.
More details
Rule ID
powershell_scriptblock_112
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['va
ultcmd', '/listcreds:']}, 'selection_option': {'ScriptB
lockText|contains': ['Windows Credentials', 'Web Creden
tials']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,603c6630-5225-49c1-8047-26c964553e0e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1555 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555/T1
555.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/20 medium
Unknown

Title Description
Potential Persistence Via Security Detects usage of certain functions and keywords that are used to manipulate security
Descriptors - ScriptBlock descriptors in order to potentially set a backdoor. As seen used in the DAMP project.
More details
Rule ID
powershell_scriptblock_114
Query
{'selection': {'ScriptBlockText|contains|all': ['win32_
Trustee', 'win32_Ace', '.AccessMask', '.AceType', '.Set
SecurityDescriptor'], 'ScriptBlockText|contains': ['\\L
sa\\JD', '\\Lsa\\Skew1', '\\Lsa\\Data', '\\Lsa\\GBG']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,2f77047c-e6e9-4c11-b088-a3de399524cd
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/HarmJ0y/DAMP 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/05 high
Unknown
PowerShell Script with Identifies the use of Cmdlets and methods related to encryption/decryption of files in
Encryption/Decryption Capabilities PowerShell scripts, which malware and offensive security tools can abuse to encrypt
data or decrypt payloads to bypass security solutions.
More details
Rule ID
powershell_scriptblock_115
Query
{'selection1': {'ScriptBlockText|contains': 'Cryptograp
hy.AESManaged'}, 'selection2': {'ScriptBlockText|contai
ns': 'Cryptography.RijndaelManaged'}, 'selection3': {'S
criptBlockText|contains': 'Cryptography.SHA1Managed'},
'selection4': {'ScriptBlockText|contains': 'Cryptograph
y.SHA256Managed'}, 'selection5': {'ScriptBlockText|cont

Title Description
ains': 'Cryptography.SHA384Managed'}, 'selection6': {'S
criptBlockText|contains': 'Cryptography.SHA512Managed'}
, 'selection7': {'ScriptBlockText|contains': 'Cryptogra
phy.SymmetricAlgorithm'}, 'selection8': {'ScriptBlockTe
xt|contains': 'PasswordDeriveBytes'}, 'selection9': {'S
criptBlockText|contains': 'Rfc2898DeriveBytes'}, 'selec
tion10': {'ScriptBlockText|contains': 'CipherMode'}, 's
election11': {'ScriptBlockText|contains': 'PaddingMode'
}, 'selection12': {'ScriptBlockText|contains': '.Create
Encryptor'}, 'selection13': {'ScriptBlockText|contains'
: '.CreateDecryptor'}, 'selection14': {'UserId': 'S-1-
5-
18'}, 'condition': '(selection1 or selection2 or select
ion3 or selection4 or selection5 or selection6 or selec
tion7 or selection8 or selection9) and selection10 and
selection11 and (selection12 or selection13) and (not s
election14)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1140 , T1027 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
producti 2023/01/2 medium
Legitimate PowerShell Scripts which makes
on 3 use of encryption.
Suspicious SSL Connection Adversaries may employ a known encryption algorithm to conceal command and
control traffic rather than relying on any inherent protections provided by a
communication protocol.
More details
Rule ID
powershell_scriptblock_116
Query
{'selection': {'ScriptBlockText|contains|all': ['System
.Net.Security.SslStream', 'Net.Security.RemoteCertifica
teValidationCallback', '.AuthenticateAsClient']}, 'cond
ition': 'selection'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,195626f3-5f1b-4403-93b7-e6cfd4d6a078
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1573 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1573/T1
573.md#atomic-test-1---openssl-c2 
https://medium.com/walmartglobaltech/openssl-server-reverse-shell-from-
windows-client-aee2dbfa0926 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/23 low
Legitimate administrative script
Potential Keylogger Activity Detects PowerShell scripts that contains reference to keystroke capturing functions
More details
Rule ID
powershell_scriptblock_117
Query
{'selection': {'ScriptBlockText|contains': '[Windows.In
put.Keyboard]::IsKeyDown([System.Windows.Input.Key]::'}
, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,965e2db9-eddb-4cf6-a986-7a967df651e4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1056.001 
References
https://twitter.com/ScumBots/status/1610626724257046529 
https://www.virustotal.com/gui/file/d4486b63512755316625230e0c9c81655
093be93876e0d80732e7eeaf7d83476/content 

Title Description
https://www.virustotal.com/gui/file/720a7ee9f2178c70501d7e3f4bcc28a4f45
6e200486dbd401b25af6da3b4da62/content 
https://learn.microsoft.com/en-
us/dotnet/api/system.windows.input.keyboard.iskeydown?
view=windowsdesktop-7.0 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/04 medium
Unknown
Invoke-Obfuscation Via Use Clip - Detects Obfuscated Powershell via use Clip.exe in Scripts
Powershell
More details
Rule ID
powershell_scriptblock_118
Query
{'selection_4104': {'ScriptBlockText|re': '(?i).*?
echo.*clip.*&&.*(Clipboard|i`?n`?v`?o`?k`?
e`?).*'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,db92dd33-a3ad-49cf-8c2c-608c3e30ace0
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high
Unknown
Execution via CL_Mutexverifiers.ps1 Detects Execution via runAfterCancelProcess in CL_Mutexverifiers.ps1 module
More details
Rule ID

Title Description
powershell_scriptblock_119
Query
{'selection': {'ScriptBlockText|contains|all': ['CL_Mut
exverifiers.ps1', 'runAfterCancelProcess']}, 'condition
': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,39776c99-1c7b-4ba0-b5aa-641525eee1a4
Author: oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/CL_mutexverifiers/ 
https://twitter.com/pabraeken/status/995111125447577600 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/14 high
Unknown
Bloodhound Hack Tool Usage via Detects the usage of PowerShell to execute Bloodhound hacktool on endpoint
PowerShell
More details
Rule ID
powershell_scriptblock_120
Query
{'selection': {'ScriptBlockText|contains': ['Invoke-
BloodHound', 'Invoke-AzureHound', 'Get-
BloodHoundData']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1482 
References

Title Description
https://github.com/BloodHoundAD/BloodHound 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2023/03/30 high
Unknown
Suspicious X509Enrollment - Ps Detect use of X509Enrollment
Script
More details
Rule ID
powershell_scriptblock_121
Query
{'selection': {'ScriptBlockText|contains': ['X509Enroll
ment.CBinaryConverter', '884e2002-217d-11da-b2a4-
000e7bbb2b09']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,504d63cb-0dba-4d02-8531-e72981aace2c
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=42 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?
slide=41 
https://learn.microsoft.com/en-
us/dotnet/api/microsoft.hpc.scheduler.store.cx509enrollmentwebclassfactor
yclass?view=hpc-sdk-5.1.6115 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium
Legitimate administrative script
Add New Windows Capability - Detects usage of the "Add-WindowsCapability" cmdlet to add new windows
ScriptBlock capabilities. Notable capabilities could be "OpenSSH" and others.

Title Description
More details
Rule ID
powershell_scriptblock_122
Query
{'selection_cmdlet': {'ScriptBlockText|contains': 'Add-
WindowsCapability '}, 'selection_capa': {'ScriptBlockTe
xt|contains': 'OpenSSH.'}, 'condition': 'all of selecti
on_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,155c7fd5-47b4-49b2-bbeb-eb4fab335429
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://learn.microsoft.com/en-us/windows-
server/administration/openssh/openssh_install_firstuse?tabs=powershell 
https://www.virustotal.com/gui/file/af1c82237b6e5a3a7cdbad82cc498d298c
67845d92971bada450023d1335e267/content 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2023/01/ mediu
Legitimate usage of the capabilities by
ental 22 m administartors or users. Filter accordingly
Invoke-Obfuscation Via Use Rundll32 Detects Obfuscated Powershell via use Rundll32 in Scripts
- PowerShell
More details
Rule ID
powershell_scriptblock_123
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['&
&', 'rundll32', 'shell32.dll', 'shellexec_rundll'], 'Sc
riptBlockText|contains': ['value', 'invoke', 'comspec',
'iex']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Title Description
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a5a30a6e-75ca-4233-8b8c-42e0f2037d3b
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/10/08 high
Unknown
Anti-VM check with WMI Query WMI Queries allow to inspect Windows properties like the BIOS features. This
technique is used by malware to identify virtual and sandboxed host machines, in
order to evade security analysis.
More details
Rule ID
powershell_scriptblock_124
Query
{'selection1': {'ScriptBlockText|contains': '-
query'}, 'selection2': {'ScriptBlockText|re': '.*(Get-
WMIObject|gwmi) .*?-
query .*? win32_(BIOS|SystemBIOS).*?
(bochs|qemu|VBOX|VirtualBox|VM).*'}, 'condition': 'sele
ction1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Suspicious Connection to Remote Adversaries with no prior knowledge of legitimate credentials within the system or
Account environment may guess passwords to attempt access to accounts. Without knowledge
of the password for an account, an adversary may opt to systematically guess the
password using a repetitive or iterative mechanism
More details
Rule ID
powershell_scriptblock_125
Query
{'selection': {'ScriptBlockText|contains': ['System.Dir
ectoryServices.Protocols.LdapDirectoryIdentifier', 'Sys
tem.Net.NetworkCredential', 'System.DirectoryServices.P
rotocols.LdapConnection']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1883444f-084b-419b-ac62-e0d0c5b3693f
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1110.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1110.001
/T1110.001.md#atomic-test-2---brute-force-credentials-of-single-active-
directory-domain-user-via-ldap-against-domain-controller-ntlm-or-
kerberos 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/27 low
Unknown
Suspicious Export-PfxCertificate Detects Commandlet that is used to export certificates from the local certificate store
and sometimes used by threat actors to steal private keys from compromised
machines
More details
Rule ID
powershell_scriptblock_126

Title Description
Query
{'selection': {'ScriptBlockText|contains': ['Export-
PfxCertificate', 'export-
certificate']}, 'filter_moduleexport': {'ScriptBlockTex
t|contains': 'CmdletsToExport = @('}, 'condition': 'sel
ection and not 1 of filter*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,aa7a3fce-bef5-4311-9cc1-5f04bb8c308c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1552.004 
References
https://us-cert.cisa.gov/ncas/analysis-reports/ar21-112a 
https://docs.microsoft.com/en-us/powershell/module/pki/export-
pfxcertificate 
https://dev.to/iamthecarisma/managing-windows-pfx-certificates-through-
powershell-3pj 
https://learn.microsoft.com/en-us/powershell/module/pki/export-certificate?
view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Matur Creati Risk False Positives
ity on Leve
Date l
experi 2021/0 high
Legitimate certificate exports invoked by
menta 4/23 administrators or users (depends on processes in
l the environment - filter if unusable)
Powershell Sensitive File Discovery Detect adversaries enumerate sensitive files
More details
Rule ID
powershell_scriptblock_127
Query
{'selection_action': {'ScriptBlockText|contains': ['ls'
, 'get-
childitem', 'gci']}, 'selection_recurse': {'ScriptBlock
Text|contains': '-
recurse'}, 'selection_file': {'ScriptBlockText|contains
': ['.pass', '.kdbx', '.kdb']}, 'condition': 'all of se
lection_*'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,7d416556-6502-45b2-9bad-9d2f05f38997
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1083 
References
https://twitter.com/malmoeb/status/1570814999370801158 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/16 medium
Unknown
Invoke-Obfuscation VAR++ Detects Obfuscated Powershell via VAR++ LAUNCHER
LAUNCHER OBFUSCATION -
PowerShell More details
Rule ID
powershell_scriptblock_128
Query
{'selection_4104': {'ScriptBlockText|re': '(?
i).*&&set.*(\\{\\d\\}){2,}\\\\"\\s+?-
f.*&&.*cmd.*/c'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e54f5149-6ba3-49cf-b153-070d24679126
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On

Title Description
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/13 high
Unknown
Testing Usage of Uncommonly Used Adversaries may communicate using a protocol and port paring that are typically not
Port associated. For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019)
or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port
443.
More details
Rule ID
powershell_scriptblock_129
Query
{'selection': {'ScriptBlockText|contains|all': ['Test-
NetConnection', '-ComputerName ', '-
port ']}, 'filter': {'ScriptBlockText|contains': [' 443
', ' 80 ']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,adf876b3-f1f8-4aa9-a4e4-a64106feec06
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1571 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1571/T1
571.md#atomic-test-1---testing-usage-of-uncommonly-used-port-with-
powershell 
https://docs.microsoft.com/en-us/powershell/module/nettcpip/test-
netconnection?view=windowsserver2022-ps 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/23 medium
Legitimate administrative script
Troubleshooting Pack Cmdlet Detects execution of "TroubleshootingPack" cmdlets to leverage CVE-2022-30190 or
Execution action similar to "msdt" lolbin (as described in LOLBAS)
More details
Rule ID

Title Description
powershell_scriptblock_130
Query
{'selection': {'ScriptBlockText|contains|all': ['Invoke
-
TroubleshootingPack', 'C:\\Windows\\Diagnostics\\System
\\PCW', '-AnswerFile', '-
Unattended']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,03409c93-a7c7-49ba-9a4c-a00badf2a153
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1202 
References
https://twitter.com/nas_bench/status/1537919885031772161 
https://lolbas-project.github.io/lolbas/Binaries/Msdt/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/06/ mediu
Legitimate usage of "TroubleshootingPack"
ental 21 m cmdlet for troubleshooting purposes
Invoke-Obfuscation Via Stdin - Detects Obfuscated Powershell via Stdin in Scripts
Powershell
More details
Rule ID
powershell_scriptblock_131
Query
{'selection_4104': {'ScriptBlockText|re': '(?i).*
(set).*&&\\s?set.*(environment|invoke|\\$\\{?
input).*&&.*"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,86b896ba-ffa1-4fea-83e3-ee28a4c915c7

Title Description
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/12 high
Unknown
Suspicious Mount-DiskImage Adversaries may abuse container files such as disk image (.iso, .vhd) file formats to
deliver malicious payloads that may not be tagged with MOTW.
More details
Rule ID
powershell_scriptblock_132
Query
{'selection': {'ScriptBlockText|contains|all': ['Mount-
DiskImage ', '-ImagePath ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,29e1c216-6408-489d-8a06-ee9d151ef819
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.00
5/T1553.005.md#atomic-test-1---mount-iso-image 
https://docs.microsoft.com/en-us/powershell/module/storage/mount-
diskimage?view=windowsserver2022-ps 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2022/02/01 low
Legitimate PowerShell scripts
Suspicious PowerShell Mailbox Export Detects usage of the powerShell New-MailboxExportRequest Cmdlet to exports a
to Share - PS mailbox to a remote or local share, as used in ProxyShell exploitations
More details
Rule ID
powershell_scriptblock_133
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
MailboxExportRequest', ' -Mailbox ', ' -
FilePath \\\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4a241dea-235b-4a7e-8d76-50d817b146c4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://youtu.be/5mqid-7zp8k?t=2481 
https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-
exchange-part-1.html 
https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-
49743a4ea9a1 
https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-
server-logs/ 
Severity
95
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/26 critical
Unknown
Data Compressed - PowerShell An adversary may compress data (e.g., sensitive documents) that is collected prior to
exfiltration in order to make it portable and minimize the amount of data sent over the
network.
More details
Rule ID
powershell_scriptblock_134
Query

Title Description
{'selection': {'ScriptBlockText|contains|all': ['-
Recurse', '|', 'Compress-
Archive']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,6dc5d284-69ea-42cf-9311-fb1c3932a69a
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1560 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560/T1
560.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2019/10/21 low
Highly likely if archive operations are done
via PowerShell.
PowerShell Create Local User Detects creation of a local user via PowerShell
More details
Rule ID
powershell_scriptblock_135
Query
{'selection': {'ScriptBlockText|contains': 'New-
LocalUser'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,243de76f-4725-4f2e-8225-a8a69b15ad61
Author: @ROxPinTeddy
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1136.001 
References

Title Description
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.00
1/T1136.001.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/04/11 medium
Legitimate user creation
WMI lateral movement using MSI Windows Management Instrumentation (WMI) is able to install MSI packages in
package remote computers. An attacker can use it to performa lateral movement and execute
malicious code.
More details
Rule ID
powershell_scriptblock_136
Query
{'selection1': {'ScriptBlockText|contains': 'win32_prod
uct'}, 'selection2': {'ScriptBlockText|contains': 'inst
all'}, 'selection3': {'ScriptBlockText|contains': '-
ComputerName'}, 'selection4': {'ScriptBlockText|contain
s': '-
Credential'}, 'condition': 'selection1 and selection2 a
nd selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Replace Desktop Wallpaper by An adversary may deface systems internal to an organization in an attempt to
Powershell intimidate or mislead users. This may take the form of modifications to internal
websites, or directly to user systems with the replacement of the desktop wallpaper

Title Description
More details
Rule ID
powershell_scriptblock_137
Query
{'selection_1': {'ScriptBlockText|contains|all': ['Get-
ItemProperty', 'Registry::', 'HKEY_CURRENT_USER\\Contro
l Panel\\Desktop\\', 'WallPaper']}, 'selection_2': {'Sc
riptBlockText|contains': 'SystemParametersInfo(20,0,*,3
)'}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c5ac6a1e-9407-45f5-a0ce-ca9a0806a287
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1491.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1491.00
1/T1491.001.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/26 low
Unknown
PowerShell MiniDump Script This rule detects PowerShell scripts capable of dumping process memory using
WindowsErrorReporting or Dbghelp.dll MiniDumpWriteDump. Attackers can use this
tooling to dump LSASS and get access to credentials.
More details
Rule ID
powershell_scriptblock_138
Query
{'selection1': {'ScriptBlockText|contains': ['MiniDumpW
riteDump', 'MiniDumpWithFullMemory', 'pmuDetirWpmuDiniM
']}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Title Description
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
producti 2021/10/0 high
PowerShell scripts that use this capability
on 5 for troubleshooting.
PowerShell PSReflect Script Detects the use of PSReflect in PowerShell scripts. Attackers leverage PSReflect as a
library that enables PowerShell to access win32 API functions.
More details
Rule ID
powershell_scriptblock_139
Query
{'selection1': {'ScriptBlockText|contains': ['New-
InMemoryModule', 'Add-
Win32Type', 'psenum', 'DefineDynamicAssembly', 'DefineD
ynamicModule', 'Reflection.TypeAttributes', 'Reflection
.Emit.OpCodes', 'Reflection.Emit.CustomAttributeBuilder
', 'Runtime.InteropServices.DllImportAttribute']}, 'sel
ection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , T1106 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id

Title Description
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2021/10/ mediu
Legitimate PowerShell scripts that make use of
tion 15 m PSReflect to access the win32 API
Winlogon Helper DLL Winlogon.exe is a Windows component responsible for actions at logon/logoff as well
as the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete. Registry entries in
HKLM\Software[Wow6432Node]Microsoft\Windows NT\CurrentVersion\Winlogon\ and
HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ are used to manage
additional helper programs and functionalities that support Winlogon. Malicious
modifications to these Registry keys may cause Winlogon to load and execute
malicious DLLs and/or executables.
More details
Rule ID
powershell_scriptblock_140
Query
{'selection': {'ScriptBlockText|contains': 'CurrentVers
ion\\Winlogon'}, 'selection2': {'ScriptBlockText|contai
ns': ['Set-ItemProperty', 'New-
Item']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,851c506b-6b7c-4ce2-8802-c703009d03c0
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1547.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.00
4/T1547.004.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/10/21 medium
Unknown
Code Executed Via Office Add-in Adversaries may abuse Microsoft Office add-ins to obtain persistence on a
compromised system. Office add-ins can be used to add functionality to Office
programs.
More details

Title Description
Rule ID
powershell_scriptblock_147
Query
{'selection_xll': {'ScriptBlockText|contains|all': ['Co
py', '\\Microsoft\\AddIns\\', '.xll']}, 'selection_wll'
: {'ScriptBlockText|contains|all': ['Copy', '\\Microsof
t\\Word\\Startup\\', '.wll']}, 'selection_xlam': {'Scri
ptBlockText|contains|all': ['Copy', '\\Microsoft\\Excel
\\XLSTART\\', '.xlam']}, 'selection_ppam': {'ScriptBloc
kText|contains|all': ['Copy', '\\Microsoft\\Addins\\',
'.ppam']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1137.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1137.00
6/T1137.006.md 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2024/01/26 high
Unknown
Potential Unconstrained Delegation Detects the use of the "Get-ADComputer" cmdlet in order to identify systems which
Discovery Via Get-ADComputer - are configured for unconstrained delegation.
ScriptBlock
More details
Rule ID
powershell_scriptblock_148
Query
{'selection1': {'ScriptBlockText|contains': 'Get-
ADComputer'}, 'selection2': {'ScriptBlockText|contains'
: ['-Properties*TrustedForDelegation', '-
Properties*TrustedToAuthForDelegation', '-
Properties*msDS-AllowedToDelegateTo', '-
Properties*PrincipalsAllowedToDelegateToAccount', '-
LDAPFilter*
(userAccountControl:1.2.840.113556.1.4.803:=524288)']},
'condition': 'selection1 and selection2'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enable
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0043 , T1589.002 , TA0007 , T1018 , TA0006 , T1558 
References
https://pentestlab.blog/2022/03/21/unconstrained-delegation/ 
https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-
adcomputer?view=windowsserver2022-ps 
Severity
50
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2025-03-05 medium
Legitimate use of the library for
ntal administrative activity
PowerShell Kerberos Ticket Dump Detects PowerShell scripts that have the capability of dumping Kerberos tickets from
LSA, which potentially indicates an attacker's attempt to acquire credentials for lateral
movement.
More details
Rule ID
powershell_scriptblock_149
Query
{'selection1': {'ScriptBlockText|contains': 'LsaCallAut
henticationPackage'}, 'selection2': {'ScriptBlockText|c
ontains': ['KerbRetrieveEncodedTicketMessage', 'KerbQue
ryTicketCacheMessage', 'KerbQueryTicketCacheExMessage',
'KerbQueryTicketCacheEx2Message', 'KerbRetrieveTicketM
essage', 'KerbDecryptDataMessage']}, 'condition': 'sele
ction1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 , T1558 
References

Title Description
N/A
Severity
75
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/07/26 high N/A
DSInternals Suspicious PowerShell Detects execution and usage of the DSInternals PowerShell module. Which can be
Cmdlets - ScriptBlock used to perform what might be considered as suspicious activity such as dumping
DPAPI backup keys or manipulating NTDS.DIT files. The DSInternals PowerShell
Module exposes several internal features of Active Directory and Azure Active
Directory. These include FIDO2 and NGC key auditing, offline ntds.dit file
manipulation, password auditing, DC recovery from IFM backups and password hash
calculation.
More details
Rule ID
powershell_scriptblock_150
Query
{'selection': {'ScriptBlockText|contains': ['Add-
ADDBSidHistory', 'Add-ADNgcKey', 'Add-
ADReplNgcKey', 'ConvertFrom-
ADManagedPasswordBlob', 'ConvertFrom-
GPPrefPassword', 'ConvertFrom-
ManagedPasswordBlob', 'ConvertFrom-
UnattendXmlPassword', 'ConvertFrom-
UnicodePassword', 'ConvertTo-AADHash', 'ConvertTo-
GPPrefPassword', 'ConvertTo-KerberosKey', 'ConvertTo-
LMHash', 'ConvertTo-MsoPasswordHash', 'ConvertTo-
NTHash', 'ConvertTo-OrgIdHash', 'ConvertTo-
UnicodePassword', 'Disable-ADDBAccount', 'Enable-
ADDBAccount', 'Get-ADDBAccount', 'Get-
ADDBBackupKey', 'Get-ADDBDomainController', 'Get-
ADDBGroupManagedServiceAccount', 'Get-
ADDBKdsRootKey', 'Get-ADDBSchemaAttribute', 'Get-
ADDBServiceAccount', 'Get-
ADDefaultPasswordPolicy', 'Get-ADKeyCredential', 'Get-
ADPasswordPolicy', 'Get-ADReplAccount', 'Get-
ADReplBackupKey', 'Get-ADReplicationAccount', 'Get-
ADSIAccount', 'Get-AzureADUserEx', 'Get-BootKey', 'Get-
KeyCredential', 'Get-LsaBackupKey', 'Get-
LsaPolicy', 'Get-SamPasswordPolicy', 'Get-
SysKey', 'Get-SystemKey', 'New-
ADDBRestoreFromMediaScript', 'New-
ADKeyCredential', 'New-ADNgcKey', 'New-
NTHashSet', 'Remove-ADDBObject', 'Save-
DPAPIBlob', 'Set-ADAccountPasswordHash', 'Set-
ADDBAccountPassword', 'Set-ADDBBootKey', 'Set-
ADDBDomainController', 'Set-ADDBPrimaryGroup', 'Set-
ADDBSysKey', 'Set-AzureADUserEx', 'Set-
LsaPolicy', 'Set-SamAccountPasswordHash', 'Set-
WinUserPasswordHash', 'Test-

Title Description
ADDBPasswordQuality', 'Test-ADPasswordQuality', 'Test-
ADReplPasswordQuality', 'Test-
PasswordQuality', 'Unlock-ADDBAccount', 'Write-
ADNgcKey', 'Write-
ADReplNgcKey']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,846c7a87-8e14-4569-9d49-ecfd4276a01c
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/MichaelGrafnetter/DSInternals/blob/39ee8a69bbdc1cfd1
2c9afdd7513b4788c4895d4/Src/DSInternals.PowerShell/DSInternals.psd1

Severity
75
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experim 2024-06- high
Legitimate usage of DSInternals for
ental 26 administration or audit purpose.
Windows PowerSploit GPP Discovery The following analytic detects the execution of the Get-GPPPassword PowerShell
cmdlet, which is used to search for unsecured credentials in Group Policy Preferences
(GPP). This detection leverages PowerShell Script Block Logging to identify specific
script block text associated with this cmdlet. Monitoring this activity is crucial as it can
indicate an attempt to retrieve and decrypt stored credentials from SYSVOL,
potentially leading to unauthorized access. If confirmed malicious, this activity could
allow an attacker to escalate privileges or move laterally within the network by
exploiting exposed credentials.
More details
Rule ID
powershell_scriptblock_151
Query
{'selection': {'ScriptBlockText|contains': ['Get-
GPPPassword', 'Get-
CachedGPPPassword']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Title Description
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1552.006 
References
https://pentestlab.blog/2017/03/20/group-policy-preferences/ 
https://adsecurity.org/?p=2288 
https://www.hackingarticles.in/credential-dumping-group-policy-
preferences-gpp/ 
https://adsecurity.org/?p=2288 
https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-
policy-preferences-could-allow-elevation-of-privilege-may-13-2014-
60734e15-af79-26ca-ea53-8cd617073c30 
Severity
50
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2025-02-10 medium
Unknown
Windows PowerView Unconstrained The following analytic detects the use of PowerView commandlets to discover
Delegation Discovery Windows endpoints with Kerberos Unconstrained Delegation. It leverages PowerShell
Script Block Logging (EventCode=4104) to identify specific commands like `Get-
DomainComputer` or `Get-NetComputer` with the `-Unconstrained` parameter. This
activity is significant as it indicates potential reconnaissance efforts by adversaries or
Red Teams to map out privileged delegation settings in Active Directory. If confirmed
malicious, this could allow attackers to identify high-value targets for further
exploitation, potentially leading to privilege escalation or lateral movement within the
network.
More details
Rule ID
powershell_scriptblock_152
Query
{'selection1': {'ScriptBlockText|contains': ['Get-
DomainComputer', 'Get-
NetComputer']}, 'selection2': {'ScriptBlockText|contain
s': '-
Unconstrained'}, 'condition': 'selection1 and selection
2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
| TA0007 , T1018 |    |     |     |
| --------------- | --- | --- | --- |
References
| https://adsecurity.org/?p=1667 |     |    |     |
| ------------------------------ | --- | --- | --- |
https://docs.microsoft.com/en-us/defender-for-identity/cas-isp-
| unconstrained-kerberos |     |    |     |
| ---------------------- | --- | --- | --- |
https://www.ired.team/offensive-security-experiments/active-directory-
kerberos-abuse/domain-compromise-via-unrestricted-kerberos-
| delegation |    |     |     |
| ---------- | --- | --- | --- |
https://www.cyberark.com/resources/threat-research-blog/weakness-within-
| kerberos-delegation |     |    |     |
| ------------------- | --- | --- | --- |
Severity
50
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
| Matur Creatio | Risk False Positives |                                            |     |
| ------------- | -------------------- | ------------------------------------------ | --- |
| ity n Date    | Level                |                                            |     |
| produ 2024-   | mediu                | Administrators or power users may leverage |     |
| ction 11-13   | m                    | PowerView for system management or         |     |
troubleshooting.
Get-ForestTrust with PowerShell The following analytic detects the execution of the Get-ForestTrust command from
Script Block PowerSploit using PowerShell Script Block Logging (EventCode=4104). This method
captures the full command sent to PowerShell, providing detailed visibility into
potentially suspicious activities. Monitoring this behavior is crucial as it can indicate an
attempt to gather domain trust information, which is often a precursor to lateral
movement or privilege escalation. If confirmed malicious, this activity could allow an
attacker to map trust relationships within the domain, facilitating further exploitation
and access to sensitive resources.
More details
Rule ID
powershell_scriptblock_153
Query
{'selection': {'ScriptBlockText|contains': ['get-
foresttrust']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
| TA0002 , T1059.001 | , TA0007 | , T1482 |    |
| ------------------- | --------- | -------- | --- |
References
https://powersploit.readthedocs.io/en/latest/Recon/Get-ForestTrust/ 
https://www.splunk.com/en_us/blog/security/hunting-for-malicious-
| powershell-using-script-block-logging.html |     |     |    |
| ------------------------------------------ | --- | --- | --- |
Severity

Title Description
50
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
producti 2024-11-13 medium
False positives may be present. Tune as
on needed.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  