✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Potentially Malicious
Windows Event Alerts
The following rules are used to identify suspicious activity with Windows events. This is a generic
rule name. Any one or more of these will trigger Potentially Malicious Windows Event Alert.
Details for each rule can be viewed by clicking the More Details link in the description.
Windows Events Required: 3, 10, 517, 675, 1102, 1116, 2013, 4611, 4624, 4625, 4648, 4649,
4656, 4657, 4658, 4660, 4661, 4663, 4673, 4674, 4688, 4692, 4698, 4699, 4701, 4702, 4704,
4706, 4713, 4714, 4726, 4732, 4738, 4768, 4769, 4771, 4776, 4781, 4782, 4794, 4799, 4898,
4899, 5001, 5379, 6423
The Windows Detect Profile (Low Volume)  covers these required Windows events.
Title Description
ETW Logging Disabled In .NET Potential adversaries stopping ETW providers recording loaded .NET assemblies.
Processes - Registry
More details
Rule ID
windows_security_3
Query
{'selection_etw_enabled': {'EventID': 4657, 'ObjectName|e
ndswith': '\\SOFTWARE\\Microsoft\\.NETFramework', 'Object
ValueName': 'ETWEnabled', 'NewValue': '0'}, 'selection_co
mplus': {'EventID': 4657, 'ObjectName|contains': '\\Envir
onment', 'ObjectValueName': ['COMPlus_ETWEnabled', 'COMPl
us_ETWFlags'], 'NewValue': '0'}, 'condition': '1 of selec
tion_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,a4c90ea1-2634-4ca0-adbb-35eae169b6fc
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)

Title Description
Tactics, Techniques, and Procedures
| TA0005 , T1112 | , T1562  |     |     |
| --------------- | ---------- | --- | --- |
References

https://twitter.com/_xpn_/status/1268712093928378368
https://github.com/dotnet/runtime/blob/ee2355c801d892f2894b0f7b14a20e6cc
50e0e54/docs/design/coreclr/jit/viewing-jit-dumps.md#setting-configuration-
| variables |    |     |     |
| --------- | --- | --- | --- |
https://github.com/dotnet/runtime/blob/f62e93416a1799aecc6b0947adad55a0
| d9870732/src/coreclr/src/inc/clrconfigvalues.h#L35-L38 |     |     |    |
| ------------------------------------------------------ | --- | --- | --- |
https://github.com/dotnet/runtime/blob/7abe42dc1123722ed385218268bb9fe0
| 4556e3d3/src/coreclr/src/inc/clrconfig.h#L33-L39      |     |     |    |
| ----------------------------------------------------- | --- | --- | --- |
| http://managed670.rssing.com/chan-5590147/all_p1.html |     |     |    |
https://github.com/dotnet/runtime/blob/4f9ae42d861fcb4be2fcd5d3d55d5f227d
30e723/docs/coding-guidelines/clr-jit-coding-conventions.md#1412-disabling-
| code |    |     |     |
| ---- | --- | --- | --- |
https://i.blackhat.com/EU-21/Wednesday/EU-21-Teodorescu-Veni-No-Vidi-No-
| Vici-Attacks-On-ETW-Blind-EDRs.pdf |     |    |     |
| ---------------------------------- | --- | --- | --- |
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |
| -------- | ------------- | ---------- | --------------- |
| test     | 2020/06/05    | high       |                 |
Unknown
NetNTLM Downgrade Attack Detects NetNTLM downgrade attack
More details
Rule ID
windows_security_4
Query
{'selection': {'EventID': 4657, 'ObjectName|contains|all'
: ['\\REGISTRY\\MACHINE\\SYSTEM', 'ControlSet', '\\Contro
l\\Lsa'], 'ObjectValueName': ['LmCompatibilityLevel', 'Nt
lmMinClientSec', 'RestrictSendingNTLMTraffic']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: Audit Policy : Object Access > Audit Registry (Success)
Rule Source
SigmaHQ,d3abac66-f11c-4ed0-8acb-50cc29c97eed
Author: Florian Roth (Nextron Systems), wagga
Tactics, Techniques, and Procedures
| , T1562.001 | , T1112  |     |     |
| ------------ | ---------- | --- | --- |
TA0005
References

Title Description
https://www.optiv.com/blog/post-exploitation-using-netntlm-downgrade-
attacks 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/20 high
Unknown
Windows Defender Discarded Dynamic Signature Service signature of Windows Defender has been discarded. This
Signature may be due to an attacker or a user disabling a security feature that can led the computer
exposed to malware and other threats.
More details
Rule ID
windows_security_5
Query
{'selection2': {'EventID': 2013}, 'condition': 'selection
2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.006 
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
test 2022/05/01 medium N/A
PetitPotam Suspicious Kerberos Detect suspicious Kerberos TGT requests. Once an attacer obtains a computer certificate
TGT Request by abusing Active Directory Certificate Services in combination with PetitPotam, the next
step would be to leverage the certificate for malicious purposes. One way of doing this is
to request a Kerberos Ticket Granting Ticket using a tool like Rubeus. This request will
generate a 4768 event with some unusual fields depending on the environment. This
analytic will require tuning, we recommend filtering Account_Name to the Domain
Controller computer accounts.
More details

Title Description
Rule ID
windows_security_7
Query
{'selection': {'EventID': 4768, 'TargetUserName|endswith'
: '$', 'CertThumbprint|contains': '*'}, 'filter_local': {
'IpAddress': '::1'}, 'filter_thumbprint': {'CertThumbprin
t': ''}, 'condition': 'selection and not 1 of filter_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Account Logon > Kerberos Authentication
Service" must be configured for Success/Failure
Rule Source
SigmaHQ,6a53d871-682d-40b6-83e0-b7c1a6c4e3a5
Author: Mauricio Velazco, Michael Haag
Tactics, Techniques, and Procedures
TA0006 , T1187 
References
https://github.com/topotam/PetitPotam 
https://isc.sans.edu/forums/diary/Active+Directory+Certificate+Services+ADCS
+PKI+domain+admin+vulnerability/27668/ 
https://github.com/splunk/security_content/blob/develop/detections/endpoint/p
etitpotam_suspicious_kerberos_tgt_request.yml 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Matu Creat Risk False Positives
rity ion Lev
Date el
exper 2021/ high
False positives are possible if the environment is using
iment 09/02 certificates for authentication. We recommend filtering
al Account_Name to the Domain Controller computer
accounts.
DPAPI Domain Master Key Backup Detects anyone attempting a backup for the DPAPI Master Key. This events gets
Attempt generated at the source and not the Domain Controller.
More details
Rule ID
windows_security_18
Query
{'selection': {'EventID': 4692}, 'condition': 'selection'
}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,39a94fd1-8c9a-4ff6-bf22-c058762f8014
Author: Roberto Rodriguez @Cyb3rWard0g
Tactics, Techniques, and Procedures
TA0006 , T1003.004 
References
https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urit on Level
y Date
test 2019/0 medi
If a computer is a member of a domain, DPAPI has a
8/10 um backup mechanism to allow unprotection of the data.
Which will trigger this event.
Scanner PoC for CVE-2019-0708 Detects the use of a scanner by zerosum0x0 that discovers targets vulnerable to CVE-
RDP RCE Vuln 2019-0708 RDP RCE aka BlueKeep
More details
Rule ID
windows_security_21
Query
{'selection': {'EventID': 4625, 'TargetUserName': 'AAAAAA
A'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,8400629e-79a9-4737-b387-5db940ab2367
Author: Florian Roth (Nextron Systems), Adam Bradbury (idea)
Tactics, Techniques, and Procedures
TA0008 , T1210 
References
https://twitter.com/AdamTheAnalyst/status/1134394070045003776 
https://github.com/zerosum0x0/CVE-2019-0708 
Severity

Title Description
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/06/02 high
Unlikely
Suspicious Scheduled Task Update Detects update to a scheduled task event that contain suspicious keywords.
More details
Rule ID
windows_security_23
Query
{'selection_eid': {'EventID': 4702}, 'selection_paths': {
'TaskContentNew|contains': ['\\AppData\\Local\\Temp\\', '
\\AppData\\Roaming\\', '\\Users\\Public\\', '\\WINDOWS\\T
emp\\', 'C:\\Temp\\', '\\Desktop\\', '\\Downloads\\', '\\
Temporary Internet', 'C:\\ProgramData\\', 'C:\\Perflogs\\
']}, 'selection_commands': {'TaskContentNew|contains': ['
regsvr32', 'rundll32', 'cmd.exe</Command>', 'cmd</Command
>', '<Arguments>/c ', '<Arguments>/k ', '<Arguments>/r ',
'powershell', 'pwsh', 'mshta', 'wscript', 'cscript', 'ce
rtutil', 'bitsadmin', 'bash.exe', 'bash ', 'scrcons', 'wm
ic ', 'wmic.exe', 'forfiles', 'scriptrunner', 'hh.exe']},
'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The Advanced Audit Policy setting Object Access > Audit Other Object Access
Events has to be configured to allow this detection. We also recommend
extracting the Command field from the embedded XML in the event data.
Rule Source
SigmaHQ,614cf376-6651-47c4-9dcc-6b9527f749f4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://learn.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-4698 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2022/12/05 high
Unknown
Windows Defender Disabled Windows Defender Real-time Protection scanning for malware and other potentially
unwanted software was disabled.
More details
Rule ID
windows_security_28
Query
{'selection2': {'EventID': 5001}, 'condition': 'selection
2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
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
test 2022/05/01 medium N/A
ADCS Certificate Template Detects certificate creation with template allowing risk permission subject
Configuration Vulnerability
More details
Rule ID
windows_security_29
Query
{'selection1': {'EventID': 4898, 'TemplateContent|contain
s': 'CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT'}, 'selection2': {
'EventID': 4899, 'NewTemplateContent|contains': 'CT_FLAG_
ENROLLEE_SUPPLIES_SUBJECT'}, 'condition': 'selection1 or
selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Certificate services loaded a template would trigger event ID 4898 and
certificate Services template was updated would trigger event ID 4899. A risk
permission seems to be coming if template contain specific flag.

Title Description
Rule Source
SigmaHQ,5ee3a654-372f-11ec-8d3d-0242ac130003
Author: Orlinum , BlueDefenZer
Tactics, Techniques, and Procedures
TA0004 , T1068 
References
https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf 
Severity
25
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2021/11/17 low
Administrator activity
Proxy SSL certificate with subject
modification
Smart card enrollement
Addition of Domain Trusts Addition of domains is seldom and should be verified for legitimacy.
More details
Rule ID
windows_security_38
Query
{'selection': {'EventID': 4706}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,0255a820-e564-4e40-af2b-6ac61160335c
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id

Title Description
Additional Information
Maturit Creation Risk False Positives
y Date Level
stable 2019/12/03 medium
Legitimate extension of domain
structure
User Added to Local Administrators This rule triggers on user accounts that are added to the local Administrators group,
which could be legitimate activity or a sign of privilege escalation activity
More details
Rule ID
windows_security_40
Query
{'selection': {'EventID': 4732}, 'selection_group1': {'Ta
rgetUserName|startswith': 'Administr'}, 'selection_group2
': {'TargetSid': 'S-1-5-32-
544'}, 'filter': {'SubjectUserName|endswith': '$'}, 'cond
ition': 'selection and (1 of selection_group*) and not fi
lter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,c265cf08-3f99-46c1-8d59-328247057d57
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1078 , T1098 
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
stable 2017/03/14 medium
Legitimate administrative activity
Sensitive Privilege Identifies the assignment of the SeEnableDelegationPrivilege sensitive "user right" to a
SeEnableDelegationPrivilege user. The SeEnableDelegationPrivilege "user right" enables computer and user accounts
assigned to a User to be trusted for delegation. Attackers can abuse this right to compromise Active Directory
accounts and elevate their privileges.
More details
Rule ID
windows_security_41
Query

Title Description
{'selection1': {'EventID': 4704}, 'selection2': {'Privile
geList': 'SeEnableDelegationPrivilege'}, 'condition': 'se
lection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/01/27 high N/A
Suspicious Computer Account Detects the renaming of an existing computer account to a account name that doesn't
Name Change CVE-2021-42287 contain a $ symbol as seen in attacks against CVE-2021-42287
More details
Rule ID
windows_security_44
Query
{'selection': {'EventID': 4781, 'OldTargetUserName|contai
ns': '$'}, 'filter': {'NewTargetUserName|contains': '$'},
'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,45eb2ae2-9aa2-4c3a-99a5-6e5077655466
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1078 
References
https://medium.com/@mvelazco/hunting-for-samaccountname-spoofing-cve-
2021-42287-and-domain-controller-impersonation-f704513c8a45 
Severity
75

Title Description
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/22 high
Unknown
Suspicious Remote Logon with Detects suspicious processes logging on with explicit credentials
Explicit Credentials
More details
Rule ID
windows_security_45
Query
{'selection': {'EventID': 4648, 'ProcessName|endswith': [
'\\cmd.exe', '\\powershell.exe', '\\pwsh.exe', '\\winrs.e
xe', '\\wmic.exe', '\\net.exe', '\\net1.exe', '\\reg.exe'
]}, 'filter1': {'TargetServerName': 'localhost'}, 'filter
2': {'SubjectUserName|endswith': '$', 'TargetUserName|end
swith': '$'}, 'condition': 'selection and not 1 of filter
*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,941e5c45-cda7-4864-8cea-bbb7458d194a
Author: oscd.community, Teymur Kheirkhabarov @HeirhabarovT, Zach Stanford
@svch0st, Tim Shelton
Tactics, Techniques, and Procedures
TA0003 , T1078 
References
https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view

Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2020/10/0 medium
Administrators that use the RunAS command
ntal 5 or scheduled tasks
The Password Hash of an Account The Password Hash of an Account was Accessed. This could be an indication of
was Accessed malicious activity.
More details

Title Description
Rule ID
windows_security_46
Query
{'selection1': {'EventID': 4782}, 'condition': 'selection
1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
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
test 2022/05/01 medium N/A
Defrag Deactivation - Security Detects the deactivation and disabling of the Scheduled defragmentation task as seen by
Slingshot APT group
More details
Rule ID
windows_security_49
Query
{'selection': {'EventID': 4701, 'TaskName': '\\Microsoft\
\Windows\\Defrag\\ScheduledDefrag'}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: Audit Policy : Audit Other Object Access Events > Success
Rule Source
SigmaHQ,c5a178bf-9cfb-4340-b584-e4df39b6a3e7
Author: Florian Roth (Nextron Systems), Bartlomiej Czyz (@bczyz1)
Tactics, Techniques, and Procedures
TA0003 , T1053 
References
https://securelist.com/apt-slingshot/84312/ 

Title Description
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/03/04 medium
Unknown
Password Protected ZIP File Detects the extraction of password protected ZIP archives. See the filename variable for
Opened (Email Attachment) more details on which file has been opened.
More details
Rule ID
windows_security_59
Query
{'selection': {'EventID': 5379, 'TargetName|contains|all'
: ['Microsoft_Windows_Shell_ZipFolder:filename', '\\Tempo
rary Internet Files\\Content.Outlook']}, 'condition': 'se
lection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,571498c8-908e-40b4-910b-d2369159a3da
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
https://twitter.com/sbousseaden/status/1523383197513379841 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimenta 2022/05/09 high
Legitimate used of encrypted ZIP
l files
AD Privileged Users or Groups Detect priv users or groups recon based on 4661 eventid and known privileged users or
Reconnaissance groups SIDs
More details

Title Description
Rule ID
windows_security_62
Query
{'selection': {'EventID': 4661, 'ObjectType': ['SAM_USER'
, 'SAM_GROUP']}, 'selection_object': [{'ObjectName|endswi
th': ['-512', '-502', '-500', '-505', '-519', '-520', '-5
44', '-551', '-555']}, {'ObjectName|contains': 'admin'}],
'filter': {'SubjectUserName|endswith': '$'}, 'condition'
: 'selection and selection_object and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: enable Object Access SAM on your Domain Controllers
Rule Source
SigmaHQ,35ba1d85-724d-42a3-889f-2e2362bcaf23
Author: Samir Bousseaden
Tactics, Techniques, and Procedures
TA0007 , T1087.002 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2019/04/0 high
If source account name is not an admin then
ntal 3 its super suspicious
Password Protected ZIP File Detects the extraction of password protected ZIP archives with suspicious file names.
Opened (Suspicious Filenames) See the filename variable for more details on which file has been opened.
More details
Rule ID
windows_security_63
Query
{'selection': {'EventID': 5379, 'TargetName|contains': 'M
icrosoft_Windows_Shell_ZipFolder:filename'}, 'selection_f
ilename': {'TargetName|contains': ['invoice', 'new order'
, 'rechnung', 'factura', 'delivery', 'purchase', 'order',
'payment']}, 'condition': 'selection and selection_filen
ame'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Collecting Windows security events
Rule Source
SigmaHQ,54f0434b-726f-48a1-b2aa-067df14516e4
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
https://twitter.com/sbousseaden/status/1523383197513379841 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimenta 2022/05/09 high
Legitimate used of encrypted ZIP
l files
Security Eventlog Cleared One of the Windows Eventlogs has been cleared. e.g. caused by "wevtutil cl" command
execution
More details
Rule ID
windows_security_82
Query
{'selection_517': {'EventID': 517, 'ProviderName': 'Secur
ity'}, 'selection_1102': {'EventID': 1102, 'ProviderName'
: 'Microsoft-Windows-
Eventlog'}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,d99b79d2-0a6f-4f46-ad8b-260b6e17f982
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1070.001 
References
https://twitter.com/deviouspolack/status/832535435960209408 
https://www.hybrid-
analysis.com/sample/027cc450ef5f8c5f653329641ec1fed91f694e0d22992896
3b30f6b0d7d3a745?environmentId=100 
Severity
75

Title Description
Suppression Logic Based On
computer_name
event_id
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2017/01/ high
Rollout of log collection agents (the setup routine
10 often includes a reset of the local Eventlog)
System provisioning (system reset before the golden
image creation)
Operation Wocao Activity - Security Detects activity mentioned in Operation Wocao report
More details
Rule ID
windows_security_83
Query
{'selection': {'EventID': 4799, 'TargetUserName|startswit
h': 'Administr', 'CallerProcessName|endswith': '\\checkad
min.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,74ad4314-482e-4c3e-b237-3f7ed3b9ca8d
Author: Florian Roth (Nextron Systems), frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1053.005 , TA0005 , T1036.004 ,
T1027 , TA0007 , T1012 
References
https://twitter.com/SBousseaden/status/1207671369963646976 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2019/12/ high
Administrators that use checkadmin.exe tool to
20 enumerate local administrators
Kerberos Manipulation This method triggers on rare Kerberos Failure Codes caused by manipulations of
Kerberos messages
More details

Title Description
Rule ID
windows_security_84
Query
{'selection': {'EventID': [675, 4768, 4769, 4771], 'Failu
reCode': ['0x9', '0xA', '0xB', '0xF', '0x10', '0x11', '0x
13', '0x14', '0x1A', '0x1F', '0x21', '0x22', '0x23', '0x2
4', '0x26', '0x27', '0x28', '0x29', '0x2C', '0x2D', '0x2E
', '0x2F', '0x31', '0x32', '0x3E', '0x3F', '0x40', '0x41'
, '0x43', '0x44']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,f7644214-0eb0-4ace-9455-331ec4c09253
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/02/10 high
Faulty legacy applications
Windows Login Default Point Of Windows has reported a login from a user with the default username used by a Point of
Sale Credentials Sale system. These are well known and are often used as the targets of brute force
attacks leading to unauthorized access of the payment infrastructure.
More details
Rule ID
windows_security_85
Query
{'selection2': {'EventID': 4625}, 'selection3': {'TargetU
serName': 'aloha'}, 'selection4': {'TargetUserName': 'mic
ros'}, 'selection5': {'TargetUserName': 'posi'}, 'selecti
on7': {'TargetUserName': 'ddpos'}, 'selection8': {'Target
UserName': 'term1'}, 'selection9': {'TargetUserName': 'po
s'}, 'selection10': {'TargetUserName': 'pos2'}, 'conditio
n': 'selection2 and (selection3 or selection4 or selectio
n5 or selection7 or selection8 or selection9 or selection
10)'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1110 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.TargetUserName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
SCM Database Privileged Detects non-system users performing privileged operation os the SCM database
Operation
More details
Rule ID
windows_security_86
Query
{'selection': {'EventID': 4674, 'ObjectType': 'SC_MANAGER
OBJECT', 'ObjectName': 'servicesactive', 'PrivilegeList'
: 'SeTakeOwnershipPrivilege'}, 'filter': {'SubjectLogonId
': '0x3e4', 'ProcessName|endswith': ':\\Windows\\System32
\\services.exe'}, 'condition': 'selection and not filter'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,dae8171c-5ec6-4396-b210-8466585b53e9
Author: Roberto Rodriguez @Cyb3rWard0g, Tim Shelton
Tactics, Techniques, and Procedures
TA0005 , T1548 
References
https://threathunterplaybook.com/hunts/windows/190826-
RemoteSCMHandle/notebook.html 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/15 medium
Unknown
Reconnaissance Activity Detects activity as "net user administrator /domain" and "net group domain admins
/domain"
More details
Rule ID
windows_security_88
Query
{'selection': {'EventID': 4661, 'AccessMask': '0x2d', 'Ob
jectType': ['SAM_USER', 'SAM_GROUP'], 'ObjectName|startsw
ith': 'S-1-5-21-
', 'ObjectName|endswith': ['-500', '-512']}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The volume of Event ID 4661 is high on Domain Controllers and therefore
"Audit SAM" and "Audit Kernel Object" advanced audit policy settings are not
configured in the recommendations for server systems
Rule Source
SigmaHQ,968eef52-9cff-4454-8992-1e74b9cbad6c
Author: Florian Roth (Nextron Systems), Jack Croock (method), Jonhnathan Ribeiro
(improvements), oscd.community
Tactics, Techniques, and Procedures
TA0007 , T1087.002 , T1069.002 
References
https://findingbad.blogspot.de/2017/01/hunting-what-does-it-look-like.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/07 high
Administrator activity
Kerberos Policy was Changed The Kerberos policy was changed. This could be an indication of malicious activity.
More details
Rule ID
windows_security_89
Query

Title Description
{'selection1': {'EventID': 4713}, 'condition': 'selection
1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
test 2022/05/01 medium N/A
Hacking Tool detected by Antivirus The Windows Defender AntiVirus has detected a hacking tool in the system. This is an
indication that an attacker has access to your system and is trying to install tools to gain
persistence, compromise other systems, etc.
More details
Rule ID
windows_security_92
Query
{'selection2': {'EventID': 1116}, 'selection3': {'Malware
Family|re': '(?:hacktool|meterpreter|metasploit|powersplo
it|cobalt|mimikatz|wpdump|htool|wce)'}, 'selection4': {'F
ileName': ''}, 'selection5': {'MalwareFamily': ''}, 'cond
ition': 'selection2 and selection3 and not selection4 and
not selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1518 
References
N/A
Severity
50
Suppression Logic Based On

Title Description
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Important Scheduled Task Detects when adversaries stop services or processes by deleting or disabling their
Deleted/Disabled respective scheduled tasks in order to conduct data destructive activities
More details
Rule ID
windows_security_95
Query
{'selection': {'EventID': [4699, 4701], 'TaskName|contain
s': ['\\Windows\\SystemRestore\\SR', '\\Windows\\Windows
Defender\\', '\\Windows\\BitLocker', '\\Windows\\WindowsB
ackup\\', '\\Windows\\WindowsUpdate\\', '\\Windows\\Updat
eOrchestrator\\Schedule', '\\Windows\\ExploitGuard']}, 'f
ilter_sys_username': {'EventID': 4699, 'SubjectUserName|e
ndswith': '$', 'TaskName|contains': '\\Windows\\Windows D
efender\\'}, 'condition': 'selection and not 1 of filter_
*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The Advanced Audit Policy setting Object Access > Audit Other Object Access
Events has to be configured to allow this detection. We also recommend
extracting the Command field from the embedded XML in the event data.
Rule Source
SigmaHQ,7595ba94-cf3b-4471-aa03-4f6baa9e5fad
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://learn.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-4699 
https://learn.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-4701 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/05 high
Unknown

Title Description
Account Tampering - Suspicious This method uses uncommon error codes on failed logons to determine suspicious
Failed Logon Reasons activity and tampering with accounts that have been disabled or somehow restricted.
More details
Rule ID
windows_security_97
Query
{'selection': {'EventID': [4625, 4776], 'Status': ['0xC00
00072', '0xC000006F', '0xC0000070', '0xC0000413', '0xC000
018C', '0xC000015B']}, 'filter': {'SubjectUserSid': 'S-1-
0-0'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,9eb99343-d336-4020-a3cd-67f3819e68ee
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1078 
References
https://docs.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-4625 
https://twitter.com/SBousseaden/status/1101431884540710913 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2017/02/19 medium
User using a disabled account
Encrypted Data Recovery Policy The Encrypted Data policy was changed. This could be an indication of malicious activity.
was Changed
More details
Rule ID
windows_security_99
Query
{'selection1': {'EventID': 4714}, 'condition': 'selection
1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber

Title Description
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
test 2022/05/01 medium N/A
ADCS Certificate Template Detects certificate creation with template allowing risk permission subject and risky EKU
Configuration Vulnerability with
More details
Risky EKU
Rule ID
windows_security_104
Query
{'selection10': {'EventID': 4898, 'TemplateContent|contai
ns': ['1.3.6.1.5.5.7.3.2', '1.3.6.1.5.2.3.4', '1.3.6.1.4.
1.311.20.2.2', '2.5.29.37.0']}, 'selection11': {'Template
Content|contains': 'CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT'},
'selection20': {'EventID': 4899, 'NewTemplateContent|cont
ains': ['1.3.6.1.5.5.7.3.2', '1.3.6.1.5.2.3.4', '1.3.6.1.
4.1.311.20.2.2', '2.5.29.37.0']}, 'selection21': {'NewTem
plateContent|contains': 'CT_FLAG_ENROLLEE_SUPPLIES_SUBJEC
T'}, 'condition': '(selection10 and selection11) or (sele
ction20 and selection21)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Certificate services loaded a template would trigger event ID 4898 and
certificate Services template was updated would trigger event ID 4899. A risk
permission seems to be coming if template contain specific flag with risky
EKU.
Rule Source
SigmaHQ,bfbd3291-de87-4b7c-88a2-d6a5deb28668
Author: Orlinum , BlueDefenZer
Tactics, Techniques, and Procedures
TA0004 , T1068 
References
https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf 
Severity
75
Suppression Logic Based On

Title Description
event_id
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2021/11/17 high
Administrator activity
Proxy SSL certificate with subject
modification
Smart card enrollement
KRBTGT Delegation Backdoor Identifies the modification of the msDS-AllowedToDelegateTo attribute to KRBTGT.
Attackers can use this technique to maintain persistence to the domain by having the
ability to request tickets for the KRBTGT service.
More details
Rule ID
windows_security_109
Query
{'selection1': {'EventID': 4738}, 'selection2': {'Allowed
ToDelegateTo': '*krbtgt*'}, 'condition': 'selection1 and
selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 , TA0006 , T1558 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/01/27 high N/A
Password Change on Directory The Directory Service Restore Mode (DSRM) account is a local administrator account on
Service Restore Mode (DSRM) Domain Controllers. Attackers may change the password to gain persistence.
Account
More details
Rule ID
windows_security_112
Query

Title Description
{'selection': {'EventID': 4794}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,53ad8e36-f573-46bf-97e4-15ba5bf4bb51
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://adsecurity.org/?p=1714 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2017/02/19 high
Initial installation of a domain controller
Suspicious Scheduled Task Detects suspicious scheduled task creation events. Based on attributes such as paths,
Creation commands line flags, etc.
More details
Rule ID
windows_security_115
Query
{'selection_eid': {'EventID': 4698}, 'selection_paths': {
'TaskContent|contains': ['\\AppData\\Local\\Temp\\', '\\A
ppData\\Roaming\\', '\\Users\\Public\\', '\\WINDOWS\\Temp
\\', 'C:\\Temp\\', '\\Desktop\\', '\\Downloads\\', '\\Tem
porary Internet', 'C:\\ProgramData\\', 'C:\\Perflogs\\']}
, 'selection_commands': {'TaskContent|contains': ['regsvr
32', 'rundll32', 'cmd.exe</Command>', 'cmd</Command>', '<
Arguments>/c ', '<Arguments>/k ', '<Arguments>/r ', 'powe
rshell', 'pwsh', 'mshta', 'wscript', 'cscript', 'certutil
', 'bitsadmin', 'bash.exe', 'bash ', 'scrcons', 'wmic ',
'wmic.exe', 'forfiles', 'scriptrunner', 'hh.exe']}, 'cond
ition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The Advanced Audit Policy setting Object Access > Audit Other Object Access
Events has to be configured to allow this detection. We also recommend
extracting the Command field from the embedded XML in the event data.
Rule Source

Title Description
SigmaHQ,3a734d25-df5c-4b99-8034-af1ddb5883a4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://learn.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-4698 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/05 high
Unknown
User Account Deleted A user account has been deleted. This could be an indication of malicious activity.
More details
Rule ID
windows_security_118
Query
{'selection1': {'EventID': 4726}, 'condition': 'selection
1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
test 2022/05/01 medium N/A
Replay Attack Detected Detects possible Kerberos Replay Attack on the domain controllers when
"KRB_AP_ERR_REPEAT" Kerberos response is sent to the client

Title Description
More details
Rule ID
windows_security_124
Query
{'selection': {'EventID': 4649}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,5a44727c-3b85-4713-8c44-4401d5499629
Author: frack113
Tactics, Techniques, and Procedures
TA0008 , T1550 
References
https://github.com/Yamato-
Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6
aa4ef19def/ConfiguringSecurityLogAuditPolicies.md 
https://learn.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-4649 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/14 high
Unknown
Device Installation Blocked Detects an installation of a device that is forbidden by the system policy
More details
Rule ID
windows_security_130
Query
{'selection': {'EventID': 6423}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,c9eb55c3-b468-40ab-9089-db2862e42137
Author: frack113

Title Description
Tactics, Techniques, and Procedures
TA0001 , T1200 
References
https://github.com/Yamato-
Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6
aa4ef19def/ConfiguringSecurityLogAuditPolicies.md 
https://learn.microsoft.com/en-us/windows/security/threat-
protection/auditing/event-6423 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/14 medium
Unknown
Webshell detected by Antivirus The Windows Defender AntiVirus has detected a webshell in the system. This is an
indication that an attacker gained access to your server and he is trying to deploy a
webshell in the webserver.
More details
Rule ID
windows_security_131
Query
{'selection1': {'EventID': 1116}, 'selection2': {'Malware
Family|contains': 'webshell'}, 'selection3': {'MalwareFam
ily|contains': 'chopper'}, 'selection4': {'MalwareFamily|
re': '(?:PHP|JSP|ASP) [\\/]Backdoor'}, 'selection5': {'Ma
lwareFamily|re': 'Backdoor[.:]
(?:PHP|JSP|ASP)'}, 'condition': 'selection1 and (selectio
n2 or selection3 or selection4 or selection5)'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1505.003 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
OilRig APT Schedule Task Detects OilRig schedule task persistence as reported by Nyotron in their March 2018
Persistence - Security report
More details
Rule ID
windows_security_132
Query
{'selection_service': {'EventID': 4698, 'TaskName': ['SC
Scheduled Scan', 'UpdatMachine']}, 'condition': 'selectio
n_service'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,c0580559-a6bd-4ef6-b9b7-83703d98b561
Author: Florian Roth (Nextron Systems), Markus Neis, Jonhnathan Ribeiro, Daniil
Yugoslavskiy, oscd.community
Tactics, Techniques, and Procedures
TA0003 , T1053.005 , T1543.003 , TA0005 , T1112 , TA0011 ,
T1071.004 
References
https://web.archive.org/web/20180402134442/https://nyotron.com/wp-
content/uploads/2018/03/Nyotron-OilRig-Malware-Report-March-2018C.pdf 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/23 critical
Unlikely
Startup/Logon Script added to Detects the modification of Group Policy Objects (GPO) to add a startup/logon script to
Group Policy Object users or computer objects.
More details
Rule ID
windows_security_171
Query
{'selection1': {'EventID': 5136}, 'selection2': {'Attribu
teLDAPDisplayName': ['gPCMachineExtensionNames', 'gPCUser
ExtensionNames']}, 'selection3': {'AttributeValue|contain
s': '42B5FAAE-6536-11D2-AE5A-
0000F87571E3'}, 'selection4': {'AttributeValue|contains':

Title Description
['40B66650-4972-11D1-A7CA-0000F87571E3', '40B6664F-4972-
11D1-A7CA-
0000F87571E3']}, 'condition': 'selection1 and selection2
and selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1484.001 , T1547 
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
production 2021/11/08 medium
Legitimate Administrative Activity
Windows Privilege Escalation This rule detects request for privilege escalation by modifying windows security group
through Security Group
More details
Modification
Rule ID
windows_security_201
Query
{'selection1': {'EventID': [632, 4728, 636, 4732, 660, 47
56]}, 'selection2': {'TargetUserName': ['Group Policy Cre
ator Owners', 'Administrators', 'DHCP Administrators', 'D
NS Admins', 'Domain Admins', 'Enterprise Admins', 'Enterp
rise Key Admins', 'Hyper-
V Administrators', 'Key Admins', 'Schema Admins', 'Storag
e Replica Administrators']}, 'condition': 'selection1 and
selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1078 , T1098 
References
N/A

Title Description
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2023/06/22 high
Legitimate administrative activity
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  