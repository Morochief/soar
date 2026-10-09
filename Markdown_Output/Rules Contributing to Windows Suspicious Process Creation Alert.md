Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Windows Suspicious
Process Creation Alert

The following rules are used to identify suspicious activity associated with process creation. Any
one or more of these will trigger the Suspicious Process Creation Alert. Details for each rule can
be viewed by clicking the More Details link in the description.

Windows Events Required: 1, 4688

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Powershell Process Created by
Internet Explorer

A Powershell process has been created by Internet Explorer. This can indicate a
malicious website has successfully launched an exploit.

More details

Rule ID

process_creation_image_1

Query

{'selection3': {'ParentImage|contains': 'iexplore.exe'},
'selection4': {'Image|contains': 'powershell.exe'}, 'cond
ition': 'selection3 and selection4'}

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

Title

Description

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Powershell Process Created by
Office PowerPoint

A Powershell process has been created by Microsoft Office PowerPoint. This can indicate
a malicious document containing a macro or an exploit has been opened by the user.

More details

Rule ID

process_creation_image_2

Query

{'selection3': {'ParentImage|contains': 'POWERPNT.EXE'},
'selection4': {'Image|contains': 'powershell.exe'}, 'cond
ition': 'selection3 and selection4'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Executable with Suspicious
Extension

An executable was launched with a well-known extension preceding the executable
extension. This could be an indication that a user was tricked into executing a malicious
program.

More details

Rule ID

process_creation_image_5

Query

{'selection3': {'Image|re': '\\.
(jpeg|jpg|png|gif|tiff|ico|zip|rar|pdf)\\.
(exe|msi|scr|hta|bat|hta)$'}, 'selection4': {'CurrentDire

Title

Description

ctory|re': '(?:\\\\Program Files(?:\\(x86\\))?
|\\\\PROGRA~
(?:1|2))'}, 'condition': 'selection3 and not selection4'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Process created by dbgsrv
debugger

A known signed debugger software has been detected creating a remote process. This
could be used by an attacker trying to bypass whitelisted applications.

More details

Rule ID

process_creation_image_6

Query

{'selection3': {'ParentImage|contains': '\\dbgsrv.exe'},
'selection4': {'ParentCommandLine|contains': 'clicon='},
'selection5': {'ParentCommandLine|contains': 'port='}, 'c
ondition': 'selection3 and selection4 and selection5'}

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

Title

Description

computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Powershell Process Created by
Office Word

A Powershell process has been created by Microsoft Office Word. This can indicate a
malicious document containing a macro or an exploit has been opened by the user.

More details

Rule ID

process_creation_image_8

Query

{'selection3': {'ParentImage|contains': 'WINWORD.EXE'}, '
selection4': {'Image|contains': 'powershell.exe'}, 'condi
tion': 'selection3 and selection4'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Java Process Spawning Scripting
Process

A suspicious process has been created by Java Software. This could be an indication of
malicious activity.

More details

Rule ID

process_creation_image_10

Query

{'selection3': {'ParentImage|re': '\\\\java[w]?
\\.exe'}, 'selection4': {'Image|re': '(?:powershell|wscri
pt|cscript|mshta)\\.exe'}, 'condition': 'selection3 and s
election4'}

Log Source

Title

Description

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1216 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Title

Description

Potential LSASS Clone Creation
via PssCaptureSnapShot

Identifies the creation of an LSASS process clone via PssCaptureSnapShot where the
parent process is the initial LSASS process instance. This may indicate an attempt to
evade detection and dump LSASS memory for credential access.

More details

Rule ID

windows_security_11

Query

{'selection1': {'Image': '?:\\Windows\\System32\\lsass.ex
e'}, 'selection2': {'ParentImage': '?:\\Windows\\System32
\\lsass.exe'}, 'condition': 'selection1 and selection2'}

Log Source

Stellar Cyber Windows Server Sensor configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003 

References
N/A

Severity

75

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

production

2021/11/27

high

N/A

Powershell Process Created by
webserver process

A webserver process has created a Powershell session. This could be the result of a
successful exploitation of the webserver or the installation of a webshell.

More details

Rule ID

process_creation_image_11

Query

{'selection3': {'Image|contains': 'powershell.exe'}, 'sel
ection4': {'ParentImage|contains': 'w3wp.exe'}, 'selectio
n5': {'ParentImage|contains': 'httpd.exe'}, 'selection6':
 {'ParentImage|contains': 'tomcat6.exe'}, 'selection7': {
'ParentImage|contains': 'nginx.exe'}, 'selection8': {'Par
entImage|contains': 'php-
cgi.exe'}, 'selection9': {'ParentImage|contains': 'tomcat
.exe'}, 'condition': 'selection3 and (selection4 or selec
tion5 or selection6 or selection7 or selection8 or select
ion9)'}

Log Source

Title

Description

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Process Execution Using pcwutl.dll A process has been launched using the pcwutl.dll library. This can indicate an attacker is

trying to bypass whitelisting technologies.

More details

Rule ID

process_creation_image_12

Query

{'selection3': {'ParentImage|contains': '\\rundll32.exe'}
, 'selection4': {'ParentCommandLine|contains': 'pcwutl.dl
l'}, 'condition': 'selection3 and selection4'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1218.011 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Title

Description

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Windows Hacking Tool Detected

A common hacking tool was detected being used on this machine. While hacking tools
can be used for System diagnostics during routine maintenance it is also a common
indicator of malware performing additional reconnaissance or privilege escalation.

More details

Rule ID

process_creation_image_13

Query

{'selection3': {'Image|re': '\\\\(?:(?:
(?:win32dd|win64dd|wce|mailpv|rdpv|logreader|netpass|iepv
|routerpass|pstpass|vncpass|mspass)\\.exe)|WebBrowserPass
View|VNCPassView|Cachedump|Fgdump|gsecdump|Lslsass|mimika
tz|pwdump|getlsasrvaddr|timestomp|BulletsPassView|WebBrow
serPassView|WirelessKeyView|Chromepass|dialupass|lookpass
|Fluxay5Beta1|pstpassword|OperaPassView|routerpassview|Pa
sswordFox)'}, 'condition': 'selection3'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Executable launched using
Windows PresentationHost tool

Windows Presentation Foundation Host (PresentationHost.exe) enables applications to
be hosted in compatible browsers. This tool can bypass code integrity enforcement in
Windows Defender Application Control.

More details

Rule ID

process_creation_image_14

Query

{'selection3': {'ParentImage|contains': '\\PresentationHo
st.exe'}, 'selection4': {'Image|re': '\\\\

Title

Description

(?:iexplore|chrome|firefox)\\.exe'}, 'condition': 'select
ion3 and not selection4'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Executable Launched from System
Volume Information

Running executables from the System Volume Information folder is a common technique
used by malware in order to hide itself. This could be an indication of malicious activity.

More details

Rule ID

process_creation_image_15

Query

{'selection3': {'Image|contains': ':\\System Volume Infor
mation\\'}, 'condition': 'selection3'}

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
process_name
stellar.rule_id

Title

Description

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Powershell Process Created by
Office Excel

A Powershell process has been created by Microsoft Office Excel. This can indicate a
malicious document containing a macro or an exploit has been opened by the user.

More details

Rule ID

process_creation_image_16

Query

{'selection3': {'ParentImage|contains': 'EXCEL.EXE'}, 'se
lection4': {'Image|contains': 'powershell.exe'}, 'conditi
on': 'selection3 and selection4'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Detected scripting process
spawned by WinRAR

A scripting process executed with wscript.exe, cscript.exe or mshta.exe was directly
executed from WinRAR. This behavior is commonly executed by packed malware.

More details

Rule ID

process_creation_image_17

Query

{'selection3': {'ParentImage|contains': '\\WinRAR.exe'},
'selection4': {'Image|re': '\\\\
(wscript|cscript|mshta)\\.exe$'}, 'condition': 'selection
3 and selection4'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Title

Description

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0002 , T1059 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

RDP process spawning a
suspicious process

An unauthenticated attacker could connect to the target system using RDP and send
specially crafted requests. This vulnerability could execute arbitrary code on the target
system.

More details

Rule ID

process_creation_image_18

Query

{'selection3': {'ParentImage|contains': '\\svchost.exe'},
 'selection4': {'ParentCommandLine|contains': 'svchost.ex
e -
k termsvcs'}, 'selection5': {'Image|contains': '\\rdpclip
.exe'}, 'condition': 'selection3 and selection4 and not s
election5'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0008 , T1210 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Title

Description

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Windows UAC bypass - UACME
tool

User Account Control Bypass activity was detected. This can be due to either a regular
operation or because an attacker is trying to escalate privileges.

More details

Rule ID

process_creation_image_19

Query

{'selection3': {'ParentImage|contains': '\\dism.exe'}, 's
election4': {'ParentCommandLine|contains': '.xml'}, 'sele
ction5': {'Image|re': '\\\\appdata\\\\.*\\\\dismhost\\.ex
e'}, 'selection6': {'Image|contains': '\\wusa.exe'}, 'sel
ection7': {'CommandLine|contains': '/quiet'}, 'selection8
': {'ParentImage|contains': '\\explorer.exe'}, 'selection
10': {'ParentImage|contains': 'dccw.exe'}, 'selection11':
 {'ParentImage|contains': '\\slui.exe'}, 'condition': '((
selection3 and selection4 and not selection5) or (selecti
on6 and selection7 and not selection8) or selection10 or
selection11)'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

MS Exchange transport agent
backdoor

Transport agents let you install custom software on an Exchange server. This could be
used by malware to gain persistence and install backdoors.

More details

Rule ID

process_creation_image_20

Query

{'selection3': {'ParentImage|contains': '\\EdgeTransport.
exe'}, 'condition': 'selection3'}

Title

Description

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0002 , T1129 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Executable launched using
Synaptics Touchpad
Enhancements tool

Synaptics Touchpad Enhancements utility allows you to run binaries in the system. This
tool can bypass code integrity enforcement in Windows Defender Application Control.

More details

Rule ID

process_creation_image_21

Query

{'selection3': {'ParentImage|contains': '\\SynTPEnh.exe'}
, 'selection4': {'ParentCommandLine|contains': '/SHELLEXE
C'}, 'selection5': {'Image|contains': '\\SynTPHelper.exe'
}, 'selection6': {'Image|contains': '\\WerFault.exe'}, 'c
ondition': 'selection3 and selection4 and not (selection5
 or selection6)'}

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

Title

Description

process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

SharPyShell Process Execution
Detected

SharPyShell is a known hacking tool that is able to deploy a shell into the ASP.NET
server. This shell can be controlled remotely from a malicious server. A process with
these characteristics has been detected, what is an indicator of compromise by
SharPyShell.

More details

Rule ID

process_creation_image_22

Query

{'selection3': {'SubjectDomainName': 'IIS APPPOOL'}, 'sel
ection4': {'SubjectUserName': 'sharpy'}, 'condition': 'se
lection3 and selection4'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1505.003 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Suspicious Process Created by
mshta.exe

A suspicious process process has been created by mshta.exe. This can indicate an
attacker is using built-in Windows functionality to perform malicious activity.

More details

Rule ID

process_creation_image_24

Query

{'selection3': {'ParentImage|contains': '\\mshta.exe'}, '
selection4': {'Image|re': '\\\\(?:powershell|
(?:w|c)script|cmd)\\.exe'}, 'selection5': {'CurrentDirect
ory|re': '(?:\\\\Program Files(?:\\(x86\\))?|\\\\PROGRA~

Title

Description

(?:1|2))'}, 'condition': 'selection3 and selection4 and n
ot selection5'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1218.005 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Java Process Spawning WMIC

The wmic.exe process was executed by Java Software. This could be an indication of
malicious activity.

More details

Rule ID

process_creation_image_25

Query

{'selection3': {'ParentImage|re': '\\\\java[w]?
\\.exe'}, 'selection4': {'Image|contains': '\\wmic.exe'},
 'condition': 'selection3 and selection4'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0002 , T1047 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name

Title

Description

stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Process Spawning Fodhelper

A process has spawned Fodhelper.exe. There is a known UAC bypass that can be used
to escalate privileges.

More details

Rule ID

process_creation_image_26

Query

{'selection3': {'ParentImage|re': '\\\\(?:powershell|
(?:w|c)script|cmd)\\.exe'}, 'selection4': {'Image|contain
s': '\\fodhelper.exe'}, 'condition': 'selection3 and sele
ction4'}

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Executable Launched from Recycle
Bin

Running executables from the Recycle Bin folder is a common technique used by
malware in order to hide itself. This could be an indication of malicious activity.

More details

Rule ID

process_creation_image_28

Query

{'selection3': {'Image|contains': ':\\$Recycle.Bin\\'}, '
selection4': {'Image|contains': ':\\Recycler\\'}, 'condit
ion': '(selection3 or selection4)'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Title

Description

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
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Suspicious Process Created by
Notepad or Calculator

A potentially suspicious process was started by either Notepad or Calculator. This could
be the result of malicious file being opened by the user or a proof-of-concept being
tested.

More details

Rule ID

process_creation_image_31

Query

{'selection3': {'ParentImage|contains': '\\NOTEPAD.EXE'},
 'selection4': {'Image|re': '\\\\
(?:notepad|ctfmon|Microsoft\\.Uev\\.SyncController)\\.exe
'}, 'selection5': {'CommandLine|contains': '\\DRIVERS\\'}
, 'selection6': {'ParentImage|contains': '\\CALC.EXE'}, '
selection7': {'Image|contains': 'CALC.EXE'}, 'selection8'
: {'Image|contains': ':\\Program Files'}, 'selection9': {
'Image|contains': '":\\Windows\\splwow64.exe"'}, 'conditi
on': '((selection3 and not (selection4 or selection5)) or
 (selection6 and not selection7)) and not (selection8 or
selection9)'}

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

50

Title

Description

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Suspicious Process Created by
Microsoft Office Application

A potentially suspicious process was started by a Microsoft Office application. This can
indicate a malicious document containing a macro or an exploit has been opened by the
user.

More details

Rule ID

process_creation_image_32

Query

{'selection3': {'ParentImage|re': '(?:winword|excel|power
pnt|msaccess|infopath)\\.exe'}, 'selection6': {'Image|re'
: '(?:cmd|svchost|wscript|notepad|rundll32|schtasks|ntvdm
|bitsadmin|msiexec|regsvr32|certutil|mshta|[A-
Z]:\\\\Users\\\\.*)\\.exe$'}, 'selection4': {'Image|conta
ins': '\\AppData\\'}, 'selection5': {'CommandLine|contain
s': '\\DRIVERS\\'}, 'condition': 'selection3 and selectio
n6 and not (selection4 or selection5)'}

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

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Windows mofcomp with suspicious
file extension

The Managed Object Format (MOF) compiler parses a file containing MOF statements
and adds the classes and class instances defined in the file to the WMI repository.
Attackers could use this tool to compile malicious WMI classes.

More details

Rule ID

process_creation_image_33

Title

Description

Query

{'selection3': {'Image': '\\mofcomp.exe'}, 'selection5':
{'CommandLine|re': '\\.mof'}, 'condition': 'selection3 an
d not selection5'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0002 , T1047 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/05/01

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

