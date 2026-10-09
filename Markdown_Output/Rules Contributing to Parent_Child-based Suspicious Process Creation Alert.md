✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Parent/Child-based
Suspicious Process Creation Alert
The following rules are used to identify suspicious activity with parent/child relationships
associated with process creation. Any one or more of these will trigger the Parent-Child
Suspicious Process Creation Alert. Details for each rule can be viewed by clicking the More
Details link in the description.
Windows Events Required: 1, 4688
The Windows Detect Profile (Low Volume)  covers these required Windows events.
Title Description
MSHTA Spawning Windows It is suspicious for the mshta process to launch a Windows command line executable.
Shell
More details
Rule ID
parent_child_1
Query
{'selection': {'ParentImage|endswith': '\\mshta.exe'}, 'se
lection2': [{'Image|endswith': ['\\cmd.exe', '\\powershell
.exe', '\\wscript.exe', '\\cscript.exe', '\\sh.exe', '\\ba
sh.exe', '\\reg.exe', '\\regsvr32.exe']}, {'Image|contains
': ['\\BITSADMIN']}], 'condition': 'selection and selectio
n2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,03cc0c25-389f-4bf8-b48d-11878079f1ca
Author: Michael Haag
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218.005 

Title Description
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/01/16 high
Printer software / driver installations
HP software
New Lolbin Process by Office A Microsoft Office application that launches a new LOLBin process is very suspicious.
Applications
More details
Rule ID
parent_child_2
Query
{'selection1': {'Image|endswith': ['\\regsvr32.exe', '\\ru
ndll32.exe', '\\msiexec.exe', '\\mshta.exe', '\\verclsid.e
xe']}, 'selection2': {'ParentImage|endswith': ['\\winword.
exe', '\\excel.exe', '\\powerpnt.exe']}, 'condition': 'sel
ection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,23daeb52-e6eb-493c-8607-c4f0246cb7d8
Author: Vadim Khrykov (ThreatIntel), Cyb3rEng (Rule), Michael Haag, Christopher
Peacock @securepeacock (Update), SCYTHE @scythe_io (Update)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 , T1047 , TA0005 ,
T1218.010 
References
https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/ 
https://github.com/vadim-hunter/Detection-Ideas-
Rules/blob/main/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sod
inokibi_(aka_REvil)_Ransomware.yaml 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2021/08/23 high
Unknown
Droppers Exploiting CVE-2017- This is indicative an attempt to exploit vulnerabilities described in CVE-2017-11882, in
11882 which exploits often start EQNEDT32.EXE and other sub-processes such as mshta.exe.
More details
Rule ID
parent_child_3
Query
{'selection': {'ParentImage|endswith': '\\EQNEDT32.EXE'},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,678eb5f4-8597-4be6-8be7-905e4234b53a
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 ,
T1204.002 
References
https://www.hybrid-
analysis.com/sample/2a4ae284c76f868fc51d3bb65da8caa6efacb707f265b25c3
0f34250b76b7507?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/11/23 critical
unknown
Exploit for CVE-2017-8759 As described in CVE-2017-8759, launch of csc.exe from Winword may be an exploit
attempt.
More details
Rule ID
parent_child_4
Query
{'selection': {'ParentImage|endswith': '\\WINWORD.EXE', 'I
mage|endswith': '\\csc.exe'}, 'condition': 'selection'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fdd84c68-a1f6-47c9-9477-920584f94905
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 ,
T1204.002 
References
https://www.hybrid-
analysis.com/sample/0b4ef455e385b750d9f90749f1467eaf00e46e8d6c2885c26
0e1b78211a51684?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/09/15 critical
Unknown
Suspicious Shells Spawn by A WinRM host process that launches a shell is suspicious.
WinRM
More details
Rule ID
parent_child_5
Query
{'selection': {'ParentImage': '*\\wsmprovhost.exe', 'Image
': ['*\\cmd.exe', '*\\sh.exe', '*\\bash.exe', '*\\powershe
ll.exe', '*\\schtasks.exe', '*\\certutil.exe', '*\\whoami.
exe', '*\\bitsadmin.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5cc2cda8-f261-4d88-a2de-e9e193c86716
Author: Andreas Hunkeler (@Karneades), Markus Neis
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 
References
N/A
Severity
74

Title Description
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/05/20 high
Legitimate WinRM usage
Suspicious Shells Spawned by A Java host process that launches certain child processes, particularly a shell process, is
Java suspicious and may indicate exploitation such as log4j.
More details
Rule ID
parent_child_6
Query
{'selection': {'ParentImage|endswith': '\\java.exe', 'Imag
e|endswith': ['\\sh.exe', '\\bash.exe', '\\powershell.exe'
, '\\schtasks.exe', '\\certutil.exe', '\\whoami.exe', '\\b
itsadmin.exe', '\\wscript.exe', '\\cscript.exe', '\\scrcon
s.exe', '\\regsvr32.exe', '\\hh.exe', '\\wmic.exe', '\\msh
ta.exe', '\\rundll32.exe', '\\forfiles.exe', '\\scriptrunn
er.exe', '\\mftrace.exe', '\\AppVLP.exe', '\\curl.exe']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0d34ed8b-1c12-4ff2-828c-16fc860b766d
Author: Andreas Hunkeler (@Karneades), Florian Roth
Tactics, Techniques, and Procedures
XTA0001 , XT1002 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/17 high
Legitimate calls to system binaries
Company specific internal usage
WMI Backdoor Exchange This indicates that a WMI event filter has been used to create a backdoor in an Exchange
Transport Agent Transport Agent.
More details

Title Description
Rule ID
parent_child_7
Query
{'selection': {'ParentImage|endswith': '\\EdgeTransport.ex
e'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,797011dc-44f4-4e6f-9f10-a8ceefbe566b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1546.003 
References
https://twitter.com/cglyer/status/1182389676876980224 
https://twitter.com/cglyer/status/1182391019633029120 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/11 critical
Unknown
Exploit for CVE-2017-0261 Launch of FLTLDR.exe from Winword is uncommon and indicative of exploits described in
CVE-2017-0261 and CVE-2017-0262.
More details
Rule ID
parent_child_8
Query
{'selection': {'ParentImage|endswith': '\\WINWORD.EXE', 'I
mage|contains': '\\FLTLDR.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,864403a1-36c9-40a2-a982-4c9a45f7d833
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures

Title Description
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 ,
T1204.002 
References
https://www.fireeye.com/blog/threat-research/2017/05/eps-processing-zero-
days.html 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
test 2018/02/ mediu
Several false positives identified, check for suspicious
22 m file names or locations (e.g. Temp folders)
Exploited CVE-2020-10189 Zoho This is indicative of CVE-2020-10189 which describes exploitation of Zoho ManageEngine
ManageEngine Desktop Central - Java Deserialization.
More details
Rule ID
parent_child_9
Query
{'selection': {'ParentImage|endswith': 'DesktopCentral_Ser
ver\\jre\\bin\\java.exe', 'Image|endswith': ['\\cmd.exe',
'\\powershell.exe', '\\bitsadmin.exe']}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,846b866e-2a57-46ee-8e16-85fa92759be7
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0002 , T1059 
References
https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-
intrusion-campaign-using-multiple-exploits.html 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2020/03/25 critical
Unknown
Microsoft Office Product It is suspicious for a Microsoft Office application to launch a Windows command and
Spawning Windows Shell scripting interpreter executable.
More details
Rule ID
parent_child_10
Query
{'selection': {'ParentImage|endswith': ['\\WINWORD.EXE', '
\\EXCEL.EXE', '\\POWERPNT.exe', '\\MSPUB.exe', '\\VISIO.ex
e', '\\MSACCESS.EXE', '\\EQNEDT32.EXE'], 'Image|endswith':
['\\cmd.exe', '\\powershell.exe', '\\wscript.exe', '\\csc
ript.exe', '\\sh.exe', '\\bash.exe', '\\scrcons.exe', '\\s
chtasks.exe', '\\regsvr32.exe', '\\hh.exe', '\\wmic.exe',
'\\mshta.exe', '\\rundll32.exe', '\\msiexec.exe', '\\forfi
les.exe', '\\scriptrunner.exe', '\\mftrace.exe', '\\AppVLP
.exe', '\\svchost.exe', '\\msbuild.exe']}, 'condition': 's
election'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,438025f9-5856-4663-83f7-52f878a70a50
Author: Florian Roth (Nextron Systems), Markus Neis, FPT.EagleEye Team, Vadim
Khrykov, Cyb3rEng, Michael Haag, Christopher Peacock @securepeacock, @scythe_io
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 
References
https://www.hybrid-
analysis.com/sample/465aabe132ccb949e75b8ab9c5bda36d80cf2fd503d52b8b
ad54e295f28bbc21?environmentId=100 
https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/04/06 high
unknown
Suspicious Parent of Csc.exe It is considered suspicious when certain parent processes (such as wscript or mshta) have
launched cwc.exe.
More details

Title Description
Rule ID
parent_child_11
Query
{'selection': {'Image|endswith': '\\csc.exe', 'ParentImage
|endswith': ['\\wscript.exe', '\\cscript.exe', '\\mshta.ex
e']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b730a276-6b63-41b8-bcf8-55930c8fc6ee
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems),
X__Junior (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 , TA0005 , T1218.005 ,
T1027.004 
References
https://twitter.com/SBousseaden/status/1094924091256176641 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/02/11 high
Unknown
MSHTA Spawned by SVCHOST This is indicative of LethalHTA (a lateral movement technique).
More details
Rule ID
parent_child_12
Query
{'selection': {'ParentImage|endswith': '\\svchost.exe', 'I
mage|endswith': '\\mshta.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ed5d72a6-f8f4-479d-ba79-02f6a80d7471
Author: Markus Neis
Tactics, Techniques, and Procedures

Title Description
XTA0001 , XT1002 , TA0005 , T1218.005 
References
https://codewhitesec.blogspot.com/2018/07/lethalhta.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/06/07 high
Unknown
Suspicious HWP Sub Processes Certain sub-processes of the Hangul Word Processor (Hanword) application may indicate
an exploitation attempt.
More details
Rule ID
parent_child_13
Query
{'selection': {'ParentImage|endswith': '\\Hwp.exe', 'Image
|endswith': '\\gbb.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,023394c4-29d5-46ab-92b8-6a534c6f447b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 ,
T1059.003 
References
https://www.securitynewspaper.com/2016/11/23/technical-teardown-exploit-
malware-hwp-files/ 
https://twitter.com/cyberwar_15/status/1187287262054076416 
https://blog.alyac.co.kr/1901 
https://en.wikipedia.org/wiki/Hangul_(word_processor) 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Title Description
| Maturity | Creation Date | Risk Level | False Positives |     |
| -------- | ------------- | ---------- | --------------- | --- |
| test     | 2019/10/24    | high       |                 |     |
Unknown
Time Travel Debugging Utility Use of the Time Travel Debugging Utility (tttracer.exe) is suspicious since adversaries can
Usage use it to run malicious processes and dump processes, such as lsass.exe.
More details
Rule ID
parent_child_14
Query
{'selection': {'ParentImage|endswith': '\\tttracer.exe'},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0b4ae027-2a2d-4b93-8c7e-962caaba5b2a
Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
Tactics, Techniques, and Procedures
| XTA0001 , XT1002 | , TA0005 , T1218 | , TA0006 | , T1003.001 |    |
| ----------------- | ------------------ | --------- | ------------ | --- |
References
| https://lolbas-project.github.io/lolbas/Binaries/Tttracer/    |     |     |    |     |
| ------------------------------------------------------------- | --- | --- | --- | --- |
| https://twitter.com/mattifestation/status/1196390321783025666 |     |     |     |    |
| https://twitter.com/oulusoyum/status/1191329746069655553      |     |     |     |    |
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
| Maturity | Creation Risk | False Positives |     |     |
| -------- | ------------- | --------------- | --- | --- |
Date Level
| experiment | 2020/10/06 high |     |     |     |
| ---------- | --------------- | --- | --- | --- |
Legitimate usage by software
| al  |     | developers/testers |     |     |
| --- | --- | ------------------ | --- | --- |
CMSTP Execution Process This is an indicator of an attempt to use Microsoft Connection Manager Profile to bypass
Creation UAC.
More details
Rule ID
parent_child_15
Query
{'selection': {'ParentImage|endswith': '\\cmstp.exe'}, 'co
ndition': 'selection'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7d4cdc5a-0076-40ca-aac8-f7e714570e47
Author: Nik Seetharaman
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218.003 
References
https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/dete
cting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
stable 2018/07/1 high
Legitimate CMSTP use (unlikely in modern
6 enterprise environments)
Winnti Malware HK University This is a characteristic of Winnti malware as reported in a Dec/Jan 2020 campaign against
Campaign Hong Kong universities.
More details
Rule ID
parent_child_16
Query
{'selection2': {'ParentImage|startswith': 'C:\\ProgramData
\\DRM', 'Image|endswith': '\\wmplayer.exe'}, 'selection3':
{'ParentImage|endswith': '\\Test.exe', 'Image|endswith':
'\\wmplayer.exe'}, 'selection4': {'Image': 'C:\\ProgramDat
a\\DRM\\CLR\\CLR.exe'}, 'selection5': {'ParentImage|starts
with': 'C:\\ProgramData\\DRM\\Windows', 'Image|endswith':
'\\SearchFilterHost.exe'}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3121461b-5aa0-4a41-b910-66d25524edbb
Author: Florian Roth (Nextron Systems), Markus Neis
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1574.002 

Title Description
References
https://www.welivesecurity.com/2020/01/31/winnti-group-targeting-universities-
hong-kong/ 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/02/01 critical
Unlikely
Shells Spawned by Web Servers A web server process that runs a shell process indicates a possible placement of a web
shell for malicious use.
More details
Rule ID
parent_child_17
Query
{'selection': {'ParentImage|endswith': ['\\w3wp.exe', '\\h
ttpd.exe', '\\nginx.exe', '\\php-
cgi.exe', '\\tomcat.exe', '\\UMWorkerProcess.exe', '\\ws_T
omcatService.exe'], 'Image|endswith': ['\\cmd.exe', '\\sh.
exe', '\\bash.exe', '\\powershell.exe', '\\bitsadmin.exe']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8202070f-edeb-4d31-a010-a26c72ac5600
Author: Thomas Patzke, Florian Roth (Nextron Systems), Zach Stanford @svch0st, Tim
Shelton, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0003 , T1505.003 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Title Description
Maturi Creation Risk False Positives
ty Date Level
test 2019/01/16 high
Particular web applications may spawn a shell
process legitimately
Sdclt Child Processes The sdclt process creating a child process indicates a possible attempt to bypass UAC.
More details
Rule ID
parent_child_18
Query
{'selection': {'ParentImage|endswith': '\\sdclt.exe'}, 'co
ndition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,da2738f2-fadb-4394-afa7-0a0674885afa
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://github.com/OTRF/detection-hackathon-apt29/issues/6 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/02 medium
unknown
LOLBins Process Creation with A LOLBin process created by wmiprvse is suspicious.
WmiPrvse
More details
Rule ID
parent_child_19
Query
{'selection1': {'Image|endswith': ['\\regsvr32.exe', '\\ru
ndll32.exe', '\\msiexec.exe', '\\mshta.exe', '\\verclsid.e
xe']}, 'selection2': {'ParentImage|endswith': '\\wbem\\Wmi
PrvSE.exe'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring process creation
Rule Source
SigmaHQ,8a582fe2-0882-4b89-a82a-da6b2dc32937
Author: Vadim Khrykov (ThreatIntel), Cyb3rEng, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 , T1047 , TA0005 ,
T1218.010 
References
https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/ 
https://github.com/vadim-hunter/Detection-Ideas-
Rules/blob/main/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sod
inokibi_(aka_REvil)_Ransomware.yaml 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/23 high
Unknown
MMC Spawning Windows Shell It is suspicious for MMC to launch a Windows command-line executable.
More details
Rule ID
parent_child_20
Query
{'selection': {'ParentImage|endswith': '\\mmc.exe'}, 'sele
ction2': [{'Image|endswith': ['\\cmd.exe', '\\powershell.e
xe', '\\wscript.exe', '\\cscript.exe', '\\sh.exe', '\\bash
.exe', '\\reg.exe', '\\regsvr32.exe']}, {'Image|contains':
['\\BITSADMIN']}], 'condition': 'selection and selection2
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,05a2ab7e-ce11-4b63-86db-ab32e763e11d
Author: Karneades, Swisscom CSIRT
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0008 , T1021.003 
References
https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-
application-com-object/ 

Title Description
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/05 high N/A
Suspicious Shells Spawn by It is suspicious for the Java utility keytool process to launch a shell and indicates potential
Java Utility Keytool exploitations, such as adselfservice.
More details
Rule ID
parent_child_21
Query
{'selection': {'ParentImage|endswith': '\\keytool.exe', 'I
mage|endswith': ['\\cmd.exe', '\\sh.exe', '\\bash.exe', '\
\powershell.exe', '\\schtasks.exe', '\\certutil.exe', '\\w
hoami.exe', '\\bitsadmin.exe', '\\wscript.exe', '\\cscript
.exe', '\\scrcons.exe', '\\regsvr32.exe', '\\hh.exe', '\\w
mic.exe', '\\mshta.exe', '\\rundll32.exe', '\\forfiles.exe
', '\\scriptrunner.exe', '\\mftrace.exe', '\\AppVLP.exe']}
, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,90fb5e62-ca1f-4e22-b42e-cc521874c938
Author: Andreas Hunkeler (@Karneades)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 
References
https://redcanary.com/blog/intelligence-insights-december-2021 
https://www.synacktiv.com/en/publications/how-to-exploit-cve-2021-40539-on-
manageengine-adselfservice-plus.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/22 high
unknown

Title Description
UAC Bypass via Windows Event A UAC bypass attempt to run code with elevated permissions may be indicated when
Viewer eventvwr.exe launches mmc.exe or WerFault.exe.
More details
Rule ID
parent_child_22
Query
{'methprocess': {'ParentImage|endswith': '\\eventvwr.exe'}
, 'filterprocess': {'Image': ['?:\\Windows\\SysWOW64\\mmc.
exe', '?:\\Windows\\System32\\mmc.exe', '?:\\Windows\\SysW
OW64\\WerFault.exe', '?:\\Windows\\System32\\WerFault.exe'
]}, 'condition': 'methprocess and not filterprocess'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,be344333-921d-4c4d-8bb8-e584cf584780
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-
registry-hijacking/ 
https://www.hybrid-
analysis.com/sample/e122bc8bf291f15cab182a5d2d27b8db1e7019e4e96bb5cd
bd1dfe7446f3f51f?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2017/03/19 critical
unknown
Malicious PE Execution by The MS VS Just-In-Time Debugger (vsjitdebugger.exe), which is a signed/verified binary,
Microsoft Visual Studio can be exploited to launch malicious code.
Debugger
More details
Rule ID
parent_child_23
Query
{'selection': {'ParentImage|endswith': '\\vsjitdebugger.ex
e'}, 'reduction1': {'Image|endswith': '\\vsimmersiveactiva
tehelper*.exe'}, 'reduction2': {'Image|endswith': '\\deven

Title Description
v.exe'}, 'condition': 'selection and not (reduction1 or re
duction2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,15c7904e-6ad1-4a45-9b46-5fb25df37fd2
Author: Agro (@agro_sev), Ensar Şamil (@sblmsrsn), oscd.community
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
https://twitter.com/pabraeken/status/990758590020452353 
https://github.com/LOLBAS-
Project/LOLBAS/blob/master/yml/OtherMSBinaries/Vsjitdebugger.yml 
https://docs.microsoft.com/en-us/visualstudio/debugger/debug-using-the-just-in-
time-debugger?view=vs-2019 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2020/10/14 medium
the process spawned by vsjitdebugger.exe is
tal uncommon.
CVE-2021-26857 Exchange The CVE-2021-26857 vulnerability is indicated when abnormal subprocesses are launched
Exploitation from Microsoft Exchange Server’s Unified Messaging service.
More details
Rule ID
parent_child_24
Query
{'selection': {'ParentImage|endswith': '\\UMWorkerProcess.
exe'}, 'filter': {'Image|endswith': ['\\wermgr.exe', '\\We
rFault.exe']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cd479ccc-d8f0-4c66-ba7d-e06286f3f887
Author: Bhabesh Raj
Tactics, Techniques, and Procedures

Title Description
| XTA0001 , XT1002 | , TA0002 , T1203 |    |     |
| ----------------- | ------------------ | --- | --- |
References
https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-
| servers/ |    |     |     |
| -------- | --- | --- | --- |
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |
| -------- | ------------- | ---------- | --------------- |
| stable   | 2021/03/03    | critical   |                 |
Unknown

Title Description
MS Office Product Spawning It is suspicious for a Microsoft Office application to launch an executable in the Users
Exe in User Dir directory.
More details
Rule ID
parent_child_25
Query
{'selection': {'ParentImage|endswith': ['\\WINWORD.EXE', '
\\EXCEL.EXE', '\\POWERPNT.exe', '\\MSPUB.exe', '\\VISIO.ex
e'], 'Image|startswith': 'C:\\users\\', 'Image|endswith':
'.exe'}, 'filter': {'Image|endswith': '\\Teams.exe'}, 'con
dition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,aa3a6f94-890e-4e22-b634-ffdfd54792cc
Author: Jason Lynch
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 
References
https://blog.morphisec.com/fin7-not-finished-morphisec-spots-new-campaign 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/04/02 high
unknown
Execution via stordiag.exe The stordiag.exe process launch processes such as systeminfo.exe from a non-standard
path is suspicious.
More details
Rule ID
parent_child_26
Query
{'selection': {'ParentImage|endswith': '\\stordiag.exe', '
Image|endswith': ['\\schtasks.exe', '\\systeminfo.exe', '\
\fltmc.exe']}, 'filter': {'ParentImage|startswith': ['c:\\
windows\\system32\\', 'c:\\windows\\syswow64\\']}, 'condit
ion': 'selection and not filter'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,961e0abb-1b1e-4c84-a453-aafe56ad0d34
Author: Austin Songer (@austinsonger)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
https://strontic.github.io/xcyclopedia/library/stordiag.exe-
1F08FC87C373673944F6A7E8B18CD845.html 
https://twitter.com/eral4m/status/1451112385041911809 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/21 high
Legitimate usage of stordiag.exe.
Always Install Elevated MSI Detects Windows Installer service (msiexec.exe) spawning "cmd" or "powershell".
Spawned Cmd And Powershell
More details
Rule ID
parent_child_27
Query
{'selection_img': {'Image|endswith': ['\\cmd.exe', '\\powe
rshell.exe', '\\pwsh.exe']}, 'selection_parent': {'ParentI
mage|contains|all': ['\\Windows\\Installer\\', 'msi'], 'Pa
rentImage|endswith': ['tmp']}, 'filter': {'CommandLine|con
tains': '\\program files\\aella\\bins'}, 'condition': 'all
of selection_* and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1e53dd56-8d83-4eb4-a43e-b790a05510aa
Author: Teymur Kheirkhabarov (idea), Mangatas Tondang (rule), oscd.community
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://image.slidesharecdn.com/kheirkhabarovoffzonefinal-
181117201458/95/hunting-for-privilege-escalation-in-windows-environment-50-
638.jpg 

Title Description
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 medium
Penetration test
Wsreset UAC Bypass The Wsreset.exe tool can be used to reset the Windows Store to bypass UAC.
More details
Rule ID
parent_child_28
Query
{'selection': {'ParentImage|endswith': ['\\WSreset.exe']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bdc8918e-a1d5-49d1-9db7-ea0fd91aa2ae
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://lolbas-project.github.io/lolbas/Binaries/Wsreset/ 
https://www.activecyber.us/activelabs/windows-uac-bypass 
https://twitter.com/ReaQta/status/1222548288731217921 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/30 high
Unknown sub processes of Wsreset.exe
DNS RCE CVE-2020-1350 This indicates possible exploitation of a DNS RCE bug, as described in CVE-2020-1350.
More details
Rule ID
parent_child_29
Query

Title Description
{'selection': {'ParentImage|endswith': '\\System32\\dns.ex
e'}, 'filter': {'Image|endswith': ['\\System32\\werfault.e
xe', '\\System32\\conhost.exe', '\\System32\\dnscmd.exe',
'\\System32\\dns.exe']}, 'condition': 'selection and not f
ilter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b5281f31-f9cc-4d0d-95d0-45b91c45b487
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0002 , T1569.002 
References
https://research.checkpoint.com/2020/resolving-your-way-into-domain-admin-
exploiting-a-17-year-old-bug-in-windows-dns-servers/ 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2020/07/1 critical
Unknown but benign sub processes of the Windows
5 DNS service dns.exe
ScreenConnect Backstage Mode This indicates the use of Backstage mode of the ScreenConnect client, which is suspicious.
Anomaly
More details
Rule ID
parent_child_30
Query
{'selection': {'ParentImage|endswith': '\\ScreenConnect.Cl
ientService.exe', 'Image|endswith': ['\\cmd.exe', '\\power
shell.exe', '\\pwsh.exe']}, 'selection_cli': {'CommandLine
|contains': '\\TEMP\\ScreenConnect\\'}, 'condition': 'sele
ction and selection_cli'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
XTA0001 , XT1002 , TA0011 , T1219 
References
https://www.mandiant.com/resources/telegram-malware-iranian-espionage 
https://docs.connectwise.com/ConnectWise_Control_Documentation/Get_started
/Host_client/View_menu/Backstage_mode 
Severity
50
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/02/ mediu
Case in which administrators are allowed to use
ental 25 m ScreenConnect's Backstage mode
Suspicious LSASS Process This is a suspicious LSASS process clone, which could be a sign of process dumping
Clone activity.
More details
Rule ID
parent_child_31
Query
{'selection': {'Image|endswith': '\\Windows\\System32\\lsa
ss.exe', 'ParentImage|endswith': '\\Windows\\System32\\lsa
ss.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c8da0dfd-4ed0-4b68-962d-13c9c884384e
Author: Florian Roth (Nextron Systems), Samir Bousseaden
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0006 , T1003.001 
References
https://www.matteomalvica.com/blog/2019/12/02/win-defender-atp-cred-bypass/

https://twitter.com/Hexacorn/status/1420053502554951689 
https://twitter.com/SBousseaden/status/1464566846594691073?s=20 
Severity
80
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/27 critical
Unknown
Visual Basic Command Line Use of vbc.exe with child process cvtres.exe (Windows Resource to Object Converter)
Compiler Usage should not be seen in an enterprise environment.
More details
Rule ID
parent_child_32
Query
{'selection': {'ParentImage|endswith': '\\vbc.exe', 'Image
|endswith': '\\cvtres.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b10f171-7f04-47c7-9fa2-5be43c76e535
Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1027.004 
References
https://lolbas-project.github.io/lolbas/Binaries/Vbc/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2020/10/07 high
Utilization of this tool should not be seen in
enterprise environment
Suspicious Service Run-time The services or svchost process running in a non-standard directory is suspicious.
Directory
More details
Rule ID
parent_child_33
Query
{'selection': {'Image|contains': ['\\Users\\Public\\', '\\
$Recycle.bin', '\\Users\\All Users\\', '\\Users\\Default\\
', '\\Users\\Contacts\\', '\\Users\\Searches\\', 'C:\\Perf
logs\\', '\\config\\systemprofile\\', '\\Windows\\Fonts\\'
, '\\Windows\\IME\\', '\\Windows\\addins\\'], 'ParentImage

Title Description
|endswith': ['\\services.exe', '\\svchost.exe']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,883faa95-175a-4e22-8181-e5761aeb373c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1202 
References
https://blog.truesec.com/2021/03/07/exchange-zero-day-proxylogon-and-
hafnium/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/03/09 high
Unknown
Mshta Spawning Windows Shell The mshta.exe process launching a command shell process is suspicious.
More details
Rule ID
parent_child_34
Query
{'selection': {'ParentImage|endswith': '\\mshta.exe', 'Ima
ge|endswith': ['\\powershell.exe', '\\cmd.exe', '\\WScript
.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,772bb24c-8df2-4be0-9157-ae4dfa794037
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 , TA0005 , T1218 
References
https://app.any.run/tasks/f0fac90f-84ac-4faa-b5b2-f4353c388969/# 
https://app.any.run/tasks/9c0f37bc-867a-4314-b685-e101566766d7/ 
Severity

Title Description
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/06/28 high
Unknown
Bypass UAC via Fodhelper.exe This could indicate the use of Fodhelper.exe to bypass User Account Control. Adversaries
may use this technique to run privileged processes.
More details
Rule ID
parent_child_35
Query
{'selection': {'ParentImage|endswith': '\\fodhelper.exe'},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7f741dcf-fc22-4759-87b4-9ae8376676a2
Author: E.M. Anhaus (originally from Atomic Blue Detections, Tony Lambert),
oscd.community
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://eqllib.readthedocs.io/en/latest/analytics/e491ce22-792f-11e9-8f5c-
d46d6d62a49e.html 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.002/T15
48.002.md 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2019/10/24 high
Legitimate use of fodhelper.exe utility by
legitimate user
Suspicious Serv-U Process Certain child processes launched by Serve-U.exe indicate possible exploitation.
Pattern
More details

Title Description
Rule ID
parent_child_36
Query
{'selection': {'ParentImage|endswith': '\\Serv-
U.exe', 'Image|endswith': ['\\cmd.exe', '\\powershell.exe'
, '\\wscript.exe', '\\cscript.exe', '\\sh.exe', '\\bash.ex
e', '\\schtasks.exe', '\\regsvr32.exe', '\\wmic.exe', '\\m
shta.exe', '\\rundll32.exe', '\\msiexec.exe', '\\forfiles.
exe', '\\scriptrunner.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,58f4ea09-0fc2-4520-ba18-b85c540b0eaf
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0006 , T1555 
References
https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-
actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/ 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creatio Risk False Positives
ty n Date Level
experi 2021/07 critical
Legitimate uses in which users or programs use the
mental /14 SSH service of Serv-U for remote command execution
HTML Help Shell Spawn It is a suspicious a child process of the Microsoft HTML Help system.
More details
Rule ID
parent_child_37
Query
{'selection': {'ParentImage': 'C:\\Windows\\hh.exe', 'Imag
e|endswith': ['\\cmd.exe', '\\powershell.exe', '\\wscript.
exe', '\\cscript.exe', '\\regsvr32.exe', '\\wmic.exe', '\\
rundll32.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,52cad028-0ff0-4854-8f67-d25dfcbc78b4
Author: Maxim Pavlunin, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 , T1047 , TA0005 , T1218 
References
https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/chm-badness-
delivers-a-banking-trojan/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/04/01 high
unknown
Regedit as Trusted Installer Running the regedit process as a TrustedInstaller is suspicious.
More details
Rule ID
parent_child_38
Query
{'selection': {'Image|endswith': '\\regedit.exe', 'ParentI
mage|endswith': ['\\TrustedInstaller.exe', '\\ProcessHacke
r.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,883835a7-df45-43e4-bf1d-4268768afda4
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548 
References
https://twitter.com/1kwpeter/status/1397816101455765504 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
experimental 2021/05/27 high
Unlikely
Script Event Consumer The scrcons.exe process launching PowerShell or other uncommon processes is
Spawning Process suspicious.
More details
Rule ID
parent_child_39
Query
{'selection': {'ParentImage|endswith': ['\\scrcons.exe'],
'Image|endswith': ['\\svchost.exe', '\\dllhost.exe', '\\po
wershell.exe', '\\pwsh.exe', '\\wscript.exe', '\\cscript.e
xe', '\\schtasks.exe', '\\regsvr32.exe', '\\mshta.exe', '\
\rundll32.exe', '\\msiexec.exe', '\\msbuild.exe']}, 'condi
tion': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f6d1dd2f-b8ce-40ca-bc23-062efb686b34
Author: Sittikorn S
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1047 
References
https://redcanary.com/blog/child-processes/ 
https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-
reference/cortex-xdr-analytics-alert-reference/scrcons-exe-rare-child-
process.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/06/21 high
Unknown
WMI Persistence - Script Event A persistent scrcons.exe child process indicates a WMI backdoor may have been created.
Consumer
More details
Rule ID
parent_child_40
Query

Title Description
{'selection': {'Image': 'C:\\WINDOWS\\system32\\wbem\\scrc
ons.exe', 'ParentImage': 'C:\\Windows\\System32\\svchost.e
xe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ec1d5e28-8f3b-4188-a6f8-6e8df81dc28e
Author: Thomas Patzke
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1546.003 
References
https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/ 
Severity
50
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urit on Leve
y Date l
test 2018/ medi
Legitimate event consumers
03/07 um
Dell computers on some versions register an event
consumer that is known to cause false positives when
brightness is changed by the corresponding keyboard button
Suspicious Svchost Process Launch of svchost.exe from certain parent processes is suspicious.
More details
Rule ID
parent_child_41
Query
{'selection': {'Image|endswith': '\\svchost.exe'}, 'filter
': {'ParentImage|endswith': ['\\services.exe', '\\MsMpEng.
exe', '\\Mrt.exe', '\\rpcnet.exe', '\\svchost.exe', '\\nge
n.exe', '\\TiWorker.exe']}, 'filter_null1': {'ParentImage'
: None}, 'filter_null2': {'ParentImage': ''}, 'filter_empt
ysysmon': {'ParentImage': '-
'}, 'condition': 'selection and not 1 of filter*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,01d2e2a1-5f09-44f7-9fc1-24faa7479b6d

Title Description
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036.005 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2017/08/15 high
Unknown
Exploit for CVE-2015-1641 Launch of MicroScMgmt.exe from Winword is uncommon and indicative of exploits
described in CVE-2015-1641.
More details
Rule ID
parent_child_42
Query
{'selection': {'ParentImage|endswith': '\\WINWORD.EXE', 'I
mage|endswith': '\\MicroScMgmt.exe'}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7993792c-5ce2-4475-a3db-a3a5539827ef
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036.005 
References
https://www.virustotal.com/en/file/5567408950b744c4e846ba8ae726883cb15268
a539f3bb21758a466e47021ae8/analysis/ 
https://www.hybrid-
analysis.com/sample/5567408950b744c4e846ba8ae726883cb15268a539f3bb21
758a466e47021ae8?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/02/22 critical
Unknown
TA505 Dropper Load Pattern Loading of the mshta process by the wmiprvse process is indicative of TA505 malicious
documents.
More details
Rule ID
parent_child_43
Query
{'selection': {'Image|endswith': '\\mshta.exe', 'ParentIma
ge|endswith': '\\wmiprvse.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,18cf6cf0-39b0-4c22-9593-e244bdc9a2d4
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1106 
References
https://twitter.com/ForensicITGuy/status/1334734244120309760 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/12/08 critical
unknown
Execution via WorkFolders.exe It is suspicious for WorkFolders.exe to run an arbitrary control.exe.
More details
Rule ID
parent_child_44
Query
{'selection': {'Image|endswith': '\\control.exe', 'ParentI
mage|endswith': '\\WorkFolders.exe'}, 'filter': {'Image':
'C:\\Windows\\System32\\control.exe'}, 'condition': 'selec
tion and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring process creation
Requirements: Sysmon ProcessCreation logging must be activated
Rule Source
SigmaHQ,0bbc6369-43e3-453d-9944-cae58821c173
Author: Maxime Thiebaut (@0xThiebaut)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
https://twitter.com/elliotkillick/status/1449812843772227588 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2021/10/2 high
Legitimate usage of the uncommon Windows
ntal 1 Work Folders feature.
Microsoft Outlook Product It is suspicious for Microsoft Outlook to start a Windows command and scripting interpreter
Spawning Windows Shell executable.
More details
Rule ID
parent_child_45
Query
{'selection': {'ParentImage|endswith': '\\OUTLOOK.EXE', 'I
mage|endswith': ['\\cmd.exe', '\\powershell.exe', '\\wscri
pt.exe', '\\cscript.exe', '\\sh.exe', '\\bash.exe', '\\scr
cons.exe', '\\schtasks.exe', '\\regsvr32.exe', '\\hh.exe',
'\\wmic.exe', '\\mshta.exe', '\\msiexec.exe', '\\forfiles
.exe', '\\scriptrunner.exe', '\\mftrace.exe', '\\AppVLP.ex
e', '\\svchost.exe', '\\msbuild.exe']}, 'condition': 'sele
ction'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,208748f7-881d-47ac-a29c-07ea84bf691d
Author: Michael Haag, Florian Roth (Nextron Systems), Markus Neis, Elastic,
FPT.EagleEye Team
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 

Title Description
References
https://www.hybrid-
analysis.com/sample/465aabe132ccb949e75b8ab9c5bda36d80cf2fd503d52b8b
ad54e295f28bbc21?environmentId=100 
https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/28 high
unknown

Title Description
Bypass UAC via WSReset.exe This could indicate the use of WSReset.exe to bypass User Account Control. Adversaries
may use this technique to run privileged processes.
More details
Rule ID
parent_child_46
Query
{'selection': {'ParentImage|endswith': '\\wsreset.exe'}, '
filter': {'Image|endswith': '\\conhost.exe'}, 'condition':
'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d797268e-28a9-49a7-b9a8-2f5039011c5c
Author: E.M. Anhaus (originally from Atomic Blue Detections, Tony Lambert),
oscd.community, Florian Roth
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://eqllib.readthedocs.io/en/latest/analytics/532b5ed4-7930-11e9-8f5c-
d46d6d62a49e.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high
Unknown
Emissary Panda Malware This indicates running of DLL side-loading malware which is used by the threat group
SLLauncher Emissary Panda, also known as APT27.
More details
Rule ID
parent_child_48
Query
{'selection': {'ParentImage|endswith': '\\sllauncher.exe',
'Image|endswith': '\\svchost.exe'}, 'condition': 'selecti
on'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Title Description
Rule Source
SigmaHQ,9aa01d62-7667-4d3b-acb8-8cb5103e2014
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1574.002 
References
https://app.any.run/tasks/579e7587-f09d-4aae-8b07-472833262965 
https://twitter.com/cyb3rops/status/1168863899531132929 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/09/03 critical
Unknown
Suspicious JAVA Child Process This may indicate an attempt to run a malicious JAR file or an attempt to exploit a JAVA-
specific vulnerability.
More details
Rule ID
parent_child_49
Query
{'selection1': {'ParentImage|endswith': '/java'}, 'selecti
on2': {'Image|endswith': ['/sh', '/bash', '/dash', '/ksh',
'/tcsh', '/zsh', '/curl', '/wget']}, 'condition': 'select
ion1 and selection2'}
Log Source
Stellar Cyber linux configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
49
Suppression Logic Based On
hostip
parent_proc_name
process_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/01/19 medium N/A
Suspicious SolarWinds Child A SolarWinds process that launches a child process may indicate an attempt to run
Process malicious programs.
More details
Rule ID
parent_child_50
Query
{'selection1': {'ParentImage|endswith': ['\\SolarWinds.Bus
inessLayerHost.exe', '\\SolarWinds.BusinessLayerHostx64.ex
e']}, 'selection2': {'Image|endswith': ['\\APMServiceContr
ol.exe', '\\ExportToPDFCmd.Exe', '\\SolarWinds.Credentials
.Orion.WebApi.exe', '\\SolarWinds.Orion.Topology.Calculato
r.exe', '\\Database-
Maint.exe', '\\SolarWinds.Orion.ApiPoller.Service.exe', '\
\WerFault.exe', '\\WerMgr.exe']}, 'condition': 'selection1
and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1195 , XTA0001 , XT1002 , TA0002 , T1106 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Matur Creatio Risk False Positives
ity n Date Level
produ 2020/12 mediu
Trusted SolarWinds child processes, verify process
ction /14 m details such as network connections and file writes.
Execution via MSSQL Use of MSSQL to run a stored procedure with xp_cmdshell, disabled by default, indicates a
xp_cmdshell Stored Procedure user may be attempting to elevate their privileges.
More details
Rule ID
parent_child_51
Query

Title Description
{'selection1': {'Image|endswith': '\\cmd.exe'}, 'selection
2': {'ParentImage|endswith': '\\sqlservr.exe'}, 'condition
': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/14 high N/A
Process Activity via Compiled Compiled HTML files (.chm), commonly distributed as help systems, have the capability of
HTML File concealing malicious code and delivering to a victim system. It is suspicious when the
runtime program for .chm files (hh.exe) launches other certain processes (such as a
command shell).
More details
Rule ID
parent_child_52
Query
{'selection1': {'ParentImage|endswith': '\\hh.exe'}, 'sele
ction2': {'Image|endswith': ['\\mshta.exe', '\\cmd.exe', '
\\powershell.exe', '\\pwsh.exe', '\\powershell_ise.exe', '
\\cscript.exe', '\\wscript.exe']}, 'condition': 'selection
1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204 , TA0005 , T1218 
References
N/A

Title Description
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urity on Leve
Date l
prod 2020/ medi
The HTML Help executable program (hh.exe) runs
uctio 02/18 um whenever a user clicks a compiled help (.chm) file or menu
n item that opens the help file inside the Help Viewer. This is
not always malicious, but adversaries may abuse this
technology to conceal malicious code.
Signed Proxy Execution via MS Use of Windows Work Folders to run a control.exe file in the current working directory is
WorkFolders indicative of potential malicious activity.
More details
Rule ID
parent_child_53
Query
{'selection1': {'Image|endswith': '\\control.exe'}, 'selec
tion2': {'ParentImage|endswith': '\\WorkFolders.exe'}, 'se
lection3': {'Image': ['?:\\Windows\\System32\\control.exe'
, '?:\\Windows\\SysWOW64\\control.exe']}, 'condition': 'se
lection1 and selection2 and (not selection3)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/03/02 medium N/A

Title Description
Microsoft Exchange Server UM The CVE-2021-26857 vulnerability may be indicated when Exchange Server UM processes
Spawning Suspicious Processes launch unexpected child processes.
More details
Rule ID
parent_child_54
Query
{'selection1': {'ParentImage|endswith': ['\\UMService.exe'
, '\\UMWorkerProcess.exe']}, 'selection2': {'Image|endswit
h': ['\\werfault.exe', '\\wermgr.exe']}, 'condition': 'sel
ection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urity on Leve
Date l
prod 2021/ medi
Legitimate processes may be spawned from the Microsoft
uctio 03/04 um Exchange Server Unified Messaging (UM) service. If known
n processes are causing false positives, they can be
exempted from the rule.
Unusual Parent-Child A Windows program run from an unexpected parent process could indicate masquerading
Relationship or other strange activity on a system.
More details
Rule ID
parent_child_55
Query
{'selection1': {'Image|endswith': '\\autochk.exe'}, 'selec
tion2': {'ParentImage|endswith': '\\smss.exe'}, 'selection
3': {'Image|endswith': ['\\fontdrvhost.exe', '\\dwm.exe']}
, 'selection4': {'ParentImage|endswith': ['\\wininit.exe',
'\\winlogon.exe']}, 'selection5': {'Image|endswith': ['\\
consent.exe', '\\RuntimeBroker.exe', '\\TiWorker.exe']}, '

Title Description
selection6': {'ParentImage|endswith': '\\svchost.exe'}, 's
election7': {'Image|endswith': '\\SearchIndexer.exe'}, 'se
lection8': {'ParentImage|endswith': '\\services.exe'}, 'se
lection9': {'Image|endswith': '\\SearchProtocolHost.exe'},
'selection10': {'ParentImage|endswith': ['\\SearchIndexer
.exe', '\\dllhost.exe']}, 'selection11': {'Image|endswith'
: '\\dllhost.exe'}, 'selection12': {'ParentImage|endswith'
: ['\\services.exe', '\\svchost.exe']}, 'selection13': {'I
mage|endswith': '\\smss.exe'}, 'selection14': {'ParentImag
e|endswith': ['System', '\\smss.exe']}, 'selection15': {'I
mage|endswith': '\\csrss.exe'}, 'selection16': {'ParentIma
ge|endswith': ['\\smss.exe', '\\svchost.exe']}, 'selection
17': {'Image|endswith': '\\wininit.exe'}, 'selection18': {
'Image|endswith': '\\winlogon.exe'}, 'selection19': {'Imag
e|endswith': ['\\lsass.exe', '\\LsaIso.exe']}, 'selection2
0': {'ParentImage|endswith': '\\wininit.exe'}, 'selection2
1': {'Image|endswith': '\\LogonUI.exe'}, 'selection22': {'
Image|endswith': '\\services.exe'}, 'selection23': {'Image
|endswith': '\\svchost.exe'}, 'selection24': {'ParentImage
|endswith': ['\\MsMpEng.exe', '\\services.exe']}, 'selecti
on25': {'Image|endswith': '\\spoolsv.exe'}, 'selection26':
{'Image|endswith': '\\taskhost.exe'}, 'selection27': {'Im
age|endswith': '\\taskhostw.exe'}, 'selection28': {'Image|
endswith': '\\userinit.exe'}, 'selection29': {'ParentImage
|endswith': ['\\dwm.exe', '\\winlogon.exe']}, 'selection30
': {'Image|endswith': ['\\wmiprvse.exe', '\\wsmprovhost.ex
e', '\\winrshost.exe']}, 'selection31': {'ParentImage|ends
with': ['\\SearchProtocolHost.exe', '\\csrss.exe']}, 'sele
ction32': {'Image|endswith': ['\\werfault.exe', '\\wermgr.
exe', '\\WerFaultSecure.exe']}, 'selection33': {'ParentIma
ge|endswith': '\\autochk.exe'}, 'selection34': {'Image|end
swith': ['\\chkdsk.exe', '\\doskey.exe', '\\WerFault.exe']
}, 'selection35': {'Image|endswith': ['\\autochk.exe', '\\
smss.exe', '\\csrss.exe', '\\wininit.exe', '\\winlogon.exe
', '\\setupcl.exe', '\\WerFault.exe']}, 'selection36': {'P
arentImage|endswith': '\\wermgr.exe'}, 'selection37': {'Im
age|endswith': ['\\WerFaultSecure.exe', '\\wermgr.exe', '\
\WerFault.exe']}, 'selection38': {'ParentImage|endswith':
'\\conhost.exe'}, 'selection39': {'Image|endswith': ['\\ms
corsvw.exe', '\\wermgr.exe', '\\WerFault.exe', '\\WerFault
Secure.exe']}, 'condition': '((selection1 and (not selecti
on2)) or (selection3 and (not selection4)) or (selection5
and (not selection6)) or (selection7 and (not selection8))
or (selection9 and (not selection10)) or (selection11 and
(not selection12)) or (selection13 and (not selection14))
or (selection15 and (not selection16)) or (selection17 an
d (not selection2)) or (selection18 and (not selection2))
or (selection19 and (not selection20)) or (selection21 and
(not selection4)) or (selection22 and (not selection20))
or (selection23 and (not selection24)) or (selection25 and
(not selection8)) or (selection26 and (not selection12))
or (selection27 and (not selection12)) or (selection28 and
(not selection29)) or (selection30 and (not selection6))
or (selection31 and (not selection32)) or (selection33 and
(not selection34)) or (selection2 and (not selection35))
or (selection36 and (not selection37)) or (selection38 and
(not selection39)))'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1055 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/02/18 medium N/A
Suspicious Process from A suspicious Conhost child process may indicate code injection activity.
Conhost
More details
Rule ID
parent_child_56
Query
{'selection1': {'ParentImage|endswith': '\\conhost.exe'},
'selection2': {'Image': ['?:\\Windows\\splwow64.exe', '?:\
\Windows\\System32\\WerFault.exe', '?:\\Windows\\System32\
\conhost.exe']}, 'condition': 'selection1 and (not selecti
on2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1055 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/31 high N/A
Suspicious Zoom Child Process Launch of Zoom from a command shell may indicate an attempt to run Zoom undetected.
More details
Rule ID
parent_child_57
Query
{'selection1': {'ParentImage|endswith': '\\Zoom.exe'}, 'se
lection2': {'Image|endswith': ['\\cmd.exe', '\\powershell.
exe', '\\pwsh.exe', '\\powershell_ise.exe']}, 'condition':
'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036 , T1055 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/09/03 medium N/A
Unusual Parent Process for Launching of cmd.exe from an unusual parent process is suspicious.
cmd.exe
More details
Rule ID
parent_child_58
Query
{'selection1': {'Image|endswith': '\\cmd.exe'}, 'selection
2': {'ParentImage|endswith': ['\\lsass.exe', '\\csrss.exe'
, '\\epad.exe', '\\regsvr32.exe', '\\dllhost.exe', '\\Logo
nUI.exe', '\\wermgr.exe', '\\spoolsv.exe', '\\jucheck.exe'
, '\\jusched.exe', '\\ctfmon.exe', '\\taskhostw.exe', '\\G
oogleUpdate.exe', '\\sppsvc.exe', '\\sihost.exe', '\\slui.
exe', '\\SIHClient.exe', '\\SearchIndexer.exe', '\\SearchP
rotocolHost.exe', '\\FlashPlayerUpdateService.exe', '\\Wer

Title Description
Fault.exe', '\\WUDFHost.exe', '\\unsecapp.exe', '\\wlanext
.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/21 medium N/A
Suspicious MS Office Child Certain child processes being launched from MS Office applications or documents with
Process macros are indicative of malicious activity.
More details
Rule ID
parent_child_59
Query
{'selection1': {'ParentImage|endswith': ['\\eqnedt32.exe',
'\\excel.exe', '\\fltldr.exe', '\\msaccess.exe', '\\mspub
.exe', '\\powerpnt.exe', '\\winword.exe']}, 'selection2':
{'Image|endswith': ['\\Microsoft.Workflow.Compiler.exe', '
\\arp.exe', '\\atbroker.exe', '\\bginfo.exe', '\\bitsadmin
.exe', '\\cdb.exe', '\\certutil.exe', '\\cmd.exe', '\\cmst
p.exe', '\\control.exe', '\\cscript.exe', '\\csi.exe', '\\
dnx.exe', '\\dsget.exe', '\\dsquery.exe', '\\forfiles.exe'
, '\\fsi.exe', '\\ftp.exe', '\\gpresult.exe', '\\hostname.
exe', '\\ieexec.exe', '\\iexpress.exe', '\\installutil.exe
', '\\ipconfig.exe', '\\mshta.exe', '\\msxsl.exe', '\\nbts
tat.exe', '\\net.exe', '\\net1.exe', '\\netsh.exe', '\\net
stat.exe', '\\nltest.exe', '\\odbcconf.exe', '\\ping.exe',
'\\powershell.exe', '\\pwsh.exe', '\\qprocess.exe', '\\qu
ser.exe', '\\qwinsta.exe', '\\rcsi.exe', '\\reg.exe', '\\r
egasm.exe', '\\regsvcs.exe', '\\regsvr32.exe', '\\sc.exe',
'\\schtasks.exe', '\\systeminfo.exe', '\\tasklist.exe', '
\\tracert.exe', '\\whoami.exe', '\\wmic.exe', '\\wscript.e
xe', '\\xwizard.exe', '\\explorer.exe', '\\rundll32.exe',
'\\hh.exe']}, 'condition': 'selection1 and selection2'}
Log Source

Title Description
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1566 , XTA0001 , XT1002 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/02/18 medium N/A
Microsoft Build Engine Started It is unusual for Explorer or the WMI (Windows Management Instrumentation) subystem to
by a System Process launch MSBuild, the Microsoft Build Engine.
More details
Rule ID
parent_child_60
Query
{'selection1': {'Image|endswith': '\\MSBuild.exe'}, 'selec
tion2': {'ParentImage|endswith': ['\\explorer.exe', '\\wmi
prvse.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1127 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Title Description
Matur Creatio Risk False Positives
ity n Date Level
produ 2020/03/ mediu
The Build Engine is commonly used by Windows
ction 25 m developers but use by non-engineers is unusual.
Microsoft Build Engine Started Launch of the Microsoft Build Engine from an Office application is unusual and may indicate
by an Office Application the associated document has run a malicious script payload.
More details
Rule ID
parent_child_61
Query
{'selection1': {'Image|endswith': '\\MSBuild.exe'}, 'selec
tion2': {'ParentImage|endswith': ['\\eqnedt32.exe', '\\exc
el.exe', '\\fltldr.exe', '\\msaccess.exe', '\\mspub.exe',
'\\outlook.exe', '\\powerpnt.exe', '\\winword.exe']}, 'con
dition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1127 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urity on Leve
Date l
prod 2020/ high
The Build Engine is commonly used by Windows developers
uctio 03/25 but use by non-engineers is unusual. It is quite unusual for
n this program to be started by an Office application like Word
or Excel.
Command Execution via A SolarWinds process that launches a command-line call or PowerShell command is
SolarWinds Process considered suspicious.
More details
Rule ID
parent_child_62
Query

Title Description
{'selection1': {'Image|endswith': ['\\cmd.exe', '\\powersh
ell.exe']}, 'selection2': {'ParentImage|endswith': ['\\Con
figurationWizard.exe', '\\NetflowDatabaseMaintenance.exe',
'\\NetFlowService.exe', '\\SolarWinds.Administration.exe'
, '\\SolarWinds.Collector.Service.exe', '\\SolarwindsDiagn
ostics.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1195 , XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Matur Creatio Risk False Positives
ity n Date Level
produ 2020/12 mediu
Trusted SolarWinds child processes. Verify process
ction /14 m details such as network connections and file writes.
Suspicious .NET Code This may indicate suspicious .NET or Visual Basic compilation of downloaded code.
Compilation
More details
Rule ID
parent_child_63
Query
{'selection1': {'Image|endswith': ['\\csc.exe', '\\vbc.exe
']}, 'selection2': {'ParentImage|endswith': ['\\wscript.ex
e', '\\mshta.exe', '\\cscript.exe', '\\wmic.exe', '\\svcho
st.exe', '\\rundll32.exe', '\\cmstp.exe', '\\regsvr32.exe'
]}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1027 

Title Description
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/21 medium N/A
Conhost Spawned By The Console Window Host (conhost.exe) process being launched by a suspicious parent
Suspicious Parent Process process is indicative of code injection.
More details
Rule ID
parent_child_64
Query
{'selection1': {'Image|endswith': '\\conhost.exe'}, 'selec
tion2': {'ParentImage|endswith': ['\\svchost.exe', '\\lsas
s.exe', '\\services.exe', '\\smss.exe', '\\winlogon.exe',
'\\explorer.exe', '\\dllhost.exe', '\\rundll32.exe', '\\re
gsvr32.exe', '\\userinit.exe', '\\wininit.exe', '\\spoolsv
.exe', '\\wermgr.exe', '\\csrss.exe', '\\ctfmon.exe']}, 'c
ondition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/17 high N/A
Unusual Child Process of Such an unexpected process being launched from dns.exe may indicate activity related to
dns.exe running of remote code or other forms of exploitation.

Title Description
More details
Rule ID
parent_child_65
Query
{'selection1': {'ParentImage|endswith': '\\dns.exe'}, 'sel
ection2': {'Image|endswith': '\\conhost.exe'}, 'condition'
: 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1133 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Mat Creati Risk False Positives
urity on Leve
Date l
prod 2020/ high
Werfault.exe will legitimately spawn when dns.exe crashes,
uctio 07/16 but the DNS service is very stable and so this is a low
n occurring event. Denial of Service (DoS) attempts by
intentionally crashing the service will also cause werfault.exe
to spawn.
Script Process Child of Common A parent web process, such as httpd.exe, that runs a script process, such as
Web Processes powershell.exe, is suspicious and indicative of possible attempts for remote shell access.
More details
Rule ID
parent_child_66
Query
{'selection1': {'ParentImage|endswith': ['\\w3wp.exe', '\\
httpd.exe', '\\nginx.exe', '\\php.exe', '\\php-
cgi.exe', '\\tomcat.exe']}, 'selection2': {'Image|endswith
': ['\\cmd.exe', '\\cscript.exe', '\\powershell.exe', '\\p
wsh.exe', '\\powershell_ise.exe', '\\wmic.exe', '\\wscript
.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Title Description
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0003 , T1505 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Matu Creatio Risk False Positives
rity n Date Level
produ 2021/0 high
Security audits, maintenance, and network administrative
ction 8/24 scripts may trigger this alert when run under web
processes.
Suspicious Endpoint Security A suspicious Endpoint Security parent process was detected, which may indicate process
Parent Process hollowing or other form of code injection.
More details
Rule ID
parent_child_67
Query
{'selection1': {'Image|endswith': ['\\esensor.exe', '\\ela
stic-
endpoint.exe']}, 'selection2': {'ParentImage': ['C:\\Progr
am Files\\Elastic\\*', 'C:\\Windows\\System32\\services.ex
e', 'C:\\Windows\\System32\\WerFault*.exe', 'C:\\Windows\\
System32\\wermgr.exe']}, 'condition': 'selection1 and (not
selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036 
References
N/A
Severity
49

Title Description
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/24 medium N/A
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  