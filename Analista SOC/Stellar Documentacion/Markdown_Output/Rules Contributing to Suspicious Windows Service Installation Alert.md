✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious Windows
Service Installation Alert
The following rules are used to identify suspicious activity with service installation activity. Any
one or more of these will trigger the Suspicious Windows Service Installation Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Windows Events Required: 4697
The Windows Detect Profile (Low Volume)  covers these required Windows events.
Title Description
Invoke-Obfuscation VAR++ Detects Obfuscated Powershell via VAR++ LAUNCHER
LAUNCHER OBFUSCATION -
More details
Security
Rule ID
windows_security_1
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['&&set', 'cmd', '/c', '-
f'], 'ServiceFileName|contains': ['{0}', '{1}', '{2}', '{
3}', '{4}', '{5}']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,4c54ba8f-73d2-4d40-8890-d9cf1dca3d30
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References

Title Description
| https://github.com/SigmaHQ/sigma/issues/1009 |     |     |    |     |
| -------------------------------------------- | --- | --- | --- | --- |
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |     |
| -------- | ------------- | ---------- | --------------- | --- |
| test     | 2020/10/13    | high       | Unknown         |     |
Malicious Service Installations Detects known malicious service installs that only appear in cases of lateral movement,
credential dumping, and other suspicious activities.
More details
Rule ID
windows_security_8
Query
{'selection': {'EventID': 4697}, 'malsvc_apt29': {'Servic
eName': 'javamtsup'}, 'condition': 'selection and 1 of ma
lsvc_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,cb062102-587e-4414-8efa-dbe3c7bf19c6
Author: Florian Roth (Nextron Systems), Daniil Yugoslavskiy, oscd.community (update)
Tactics, Techniques, and Procedures
| TA0002 , T1569.002 | , TA0003 | , T1543.003 , TA0006 | , T1003 |    |
| ------------------- | --------- | ---------------------- | -------- | --- |
References
| https://awakesecurity.com/blog/threat-hunting-for-paexec/ |     |     |    |     |
| --------------------------------------------------------- | --- | --- | --- | --- |
https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-
| profile.html                                                        |    |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- |
| https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf |     |     |     |    |
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |     |
| -------- | ------------- | ---------- | --------------- | --- |
| test     | 2017/03/27    | critical   |                 |     |
Unknown

Title Description
Invoke-Obfuscation Via Use Detects Obfuscated Powershell via use MSHTA in Scripts
MSHTA - Security
More details
Rule ID
windows_security_10
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['mshta', 'vbscript:createobject', '.run', 'window
.close']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,9b8d9203-4e0f-4cd9-bb06-4cc4ea6d0e9a
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high
Unknown
Service Installed By Unusual Detects a service installed by a client which has PID 0 or whose parent has PID 0
Client - Security
More details
Rule ID
windows_security_13
Query
{'selection': {'EventID': 4697}, 'selection_pid': [{'Clie
ntProcessId': 0}, {'ParentProcessId': 0}], 'condition': '
all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697

Title Description
Rule Source
SigmaHQ,c4e92a97-a9ff-4392-9d2d-7a4c642768ca
Author: Tim Rauch (Nextron Systems), Elastic (idea)
Tactics, Techniques, and Procedures
TA0003 , T1543 
References
https://www.elastic.co/guide/en/security/current/windows-service-installed-via-
an-unusual-client.html 
https://twitter.com/SBousseaden/status/1490608838701166596 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/15 high
Unknown
Meterpreter or Cobalt Strike Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting a specific
Getsystem Service Installation - service installation
Security
More details
Rule ID
windows_security_26
Query
{'selection_id': {'EventID': 4697}, 'selection': [{'Servi
ceFileName|contains|all': ['cmd', '/c', 'echo', '\\pipe\\
']}, {'ServiceFileName|contains|all': ['%COMSPEC%', '/c',
'echo', '\\pipe\\']}, {'ServiceFileName|contains|all': [
'cmd.exe', '/c', 'echo', '\\pipe\\']}, {'ServiceFileName|
contains|all': ['rundll32', '.dll,a', '/p:']}], 'conditio
n': 'selection_id and selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,ecbc5e16-58e0-4521-9c60-eb9a7ea4ad34
Author: Teymur Kheirkhabarov, Ecco, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1134 
References
https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-
windows-environment 

Title Description
https://blog.cobaltstrike.com/2014/04/02/what-happens-when-i-type-getsystem/

Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/26 critical
Highly unlikely
Invoke-Obfuscation RUNDLL Detects Obfuscated Powershell via RUNDLL LAUNCHER
LAUNCHER - Security
More details
Rule ID
windows_security_32
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['rundll32.exe', 'shell32.dll', 'shellexec_rundll'
, 'powershell']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,f241cf1b-3a6b-4e1a-b4f9-133c00dd95ca
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium
Unknown
Invoke-Obfuscation Via Use Detects Obfuscated Powershell via use Rundll32 in Scripts
Rundll32 - Security
More details
Rule ID

Title Description
windows_security_33
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['&&', 'rundll32', 'shell32.dll', 'shellexec_rundl
l'], 'ServiceFileName|contains': ['value', 'invoke', 'com
spec', 'iex']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,cd0f7229-d16f-42de-8fe3-fba365fbcb3a
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high
Unknown
Invoke-Obfuscation STDIN+ Detects Obfuscated use of stdin to execute PowerShell
Launcher - Security
More details
Rule ID
windows_security_50
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['cmd', 'powershell']}, 'selection2': {'ServiceFil
eName|contains': ['${input}', 'noexit']}, 'selection3': {
'ServiceFileName|contains': [' /c ', ' /r ']}, 'condition
': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,0c718a5e-4284-4fb9-b4d9-b9a50b3a1974

Title Description
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high
Unknown
Invoke-Obfuscation Via Stdin - Detects Obfuscated Powershell via Stdin in Scripts
Security
More details
Rule ID
windows_security_53
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['set', '&&'], 'ServiceFileName|contains': ['envir
onment', 'invoke', '${input)']}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,80b708f3-d034-40e4-a6c8-d23b7a7db3d1
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2020/10/12 high
Unknown
Invoke-Obfuscation CLIP+ Detects Obfuscated use of Clip.exe to execute PowerShell
Launcher - Security
More details
Rule ID
windows_security_55
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['cmd', '&&', 'clipboard]::']}, 'condition': 'sele
ction'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,4edf51e1-cb83-4e1a-bc39-800e396068e3
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/13 high
Unknown
Metasploit Or Impacket Service Detects usage of Metasploit SMB PsExec (exploit/windows/smb/psexec) and Impacket
Installation Via SMB PsExec psexec.py by triggering on specific service installation
More details
Rule ID
windows_security_61
Query
{'selection': {'EventID': 4697, 'ServiceFileName|re': '^%
systemroot%\\\\[a-zA-Z]
{8}\\.exe$', 'ServiceName|re': '(^[a-zA-Z]{4}$)|(^[a-zA-
Z]{8}$)|(^[a-zA-Z]
{16}$)', 'ServiceStartType': '3', 'ServiceType': '0x10'},

Title Description
'filter': {'ServiceName': 'PSEXESVC'}, 'condition': 'sel
ection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,6fb63b40-e02a-403e-9ffd-3bcc1d749442
Author: Bartlomiej Czyz, Relativity
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , TA0008 , T1021.002 , T1570 
References
https://bczyz1.github.io/2021/01/30/psexec.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturit Creatio Risk False Positives
y n Date Level
experim 2021/01/ high
Possible, different agents with a 8 character binary
ental 21 and a 4, 8 or 16 character service name
Invoke-Obfuscation Obfuscated Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-
IEX Invocation - Security Obfuscation framework from the code block linked in the references
More details
Rule ID
windows_security_71
Query
{'selection_eid': {'EventID': 4697}, 'selection_servicefi
lename': [{'ServiceFileName|re': '\\$PSHome\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$PSHome\\
['}, {'ServiceFileName|re': '\\$ShellId\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$ShellId\\
['}, {'ServiceFileName|re': '\\$env:Public\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$env:Public\\
['}, {'ServiceFileName|re': '\\$env:ComSpec\\
[(\\s*\\d{1,3}\\s*,)
{2}'}, {'ServiceFileName|re': '\\\\*mdr*\\W\\s*\\)\\.Name
'}, {'ServiceFileName|re': '\\$VerbosePreference\\.ToStri
ng\\
('}, {'ServiceFileName|re': '\\String\\]\\s*\\$VerbosePre
ference'}], 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,fd0f5778-d3cb-4c9a-9695-66759d04702a
Author: Daniel Bohannon (@Mandiant/@FireEye), oscd.community
Tactics, Techniques, and Procedures
TA0005 , T1027 
References
https://github.com/danielbohannon/Invoke-
Obfuscation/blob/f20e7f843edd0a3a7716736e9eddfa423395dd26/Out-
ObfuscatedStringCommand.ps1#L873-L888 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/11/08 high
Unknown
Invoke-Obfuscation Via Use Clip - Detects Obfuscated Powershell via use Clip.exe in Scripts
Security
More details
Rule ID
windows_security_76
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
': '(Clipboard|i'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,1a0a2ff1-611b-4dac-8216-8a7b47c618a6
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On

Title Description
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high
Unknown
Invoke-Obfuscation VAR+ Detects Obfuscated use of Environment Variables to execute PowerShell
Launcher - Security
More details
Rule ID
windows_security_90
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['cmd', '"set', '-
f'], 'ServiceFileName|contains': ['/c', '/r']}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,dcf2db1f-f091-425b-a821-c05875b8925a
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high
Unknown
Invoke-Obfuscation COMPRESS Detects Obfuscated Powershell via COMPRESS OBFUSCATION
OBFUSCATION - Security
More details
Rule ID
windows_security_102
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
|all': ['new-

Title Description
object', 'text.encoding]::ascii', 'readtoend'], 'ServiceF
ileName|contains': ['system.io.compression.deflatestream'
, 'system.io.streamreader']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,7a922f1b-2635-4d6c-91ef-af228b198ad3
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium
Unknown
PowerShell Scripts Installed as Detects powershell script installed as a Service
Services - Security
More details
Rule ID
windows_security_106
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
': ['powershell', 'pwsh']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,2a926e6a-4b81-4011-8a96-e36cc8c04302
Author: oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1569.002 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse 

Title Description
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/06 high
Unknown
HybridConnectionManager Rule to detect the Hybrid Connection Manager service installation.
Service Installation
More details
Rule ID
windows_security_110
Query
{'selection': {'EventID': 4697, 'ServiceName': 'HybridCon
nectionManager', 'ServiceFileName|contains': 'HybridConne
ctionManager'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,0ee4d8a5-4e67-4faf-acfa-62a78457d1f2
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0003 , T1554 
References
https://twitter.com/Cyb3rWard0g/status/1381642789369286662 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/04/1 high
Legitimate use of Hybrid Connection Manager via
2 Azure function apps.
Tap Driver Installation - Security Well-known TAP software installation. Possible preparation for data exfiltration using
tunnelling techniques
More details

Title Description
Rule ID
windows_security_114
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
': 'tap0901'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,9c8afa4d-0022-48f0-9456-3712466f9701
Author: Daniil Yugoslavskiy, Ian Davis, oscd.community
Tactics, Techniques, and Procedures
TA0010 , T1048 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 medium
Legitimate OpenVPN TAP insntallation
Credential Dumping Tools Service Detects well-known credential dumping tools execution via service execution events
Execution - Security
More details
Rule ID
windows_security_128
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains
': ['fgexec', 'dumpsvc', 'cachedump', 'mimidrv', 'gsecdum
p', 'servpw', 'pwdump']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log
the EID 4697
Rule Source
SigmaHQ,f0d1feba-4344-4ca9-8121-a6c97bd6df52
Author: Florian Roth (Nextron Systems), Teymur Kheirkhabarov, Daniil Yugoslavskiy,
oscd.community

Title Description
Tactics, Techniques, and Procedures
| TA0002 , T1569.002 | , TA0006 , T1003 |    |
| ------------------- | ------------------ | --- |
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-
| windows-environment |    |     |
| ------------------- | --- | --- |
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
| Matur Creation Risk | False Positives |     |
| ------------------- | --------------- | --- |
| ity Date Level      |                 |     |
| test 2017/03/0 high |                 |     |
Legitimate Administrator using credential dumping
5 tool for password recovery
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        