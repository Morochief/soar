Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Windows
Network Connection Alert

The following rules are used to identify suspicious Windows network connection activities. Any
one or more of these will trigger the Suspicious Windows Network Connection Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Windows Events Required: 3

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Network Activity From
MSBuild

MSBuild is a powerful tool used to compile and package code. If the MSBuild utility is accessing
network resources, it might be using code from a third party or even downloading malicious code
or executables. Malicious executables can even run inside of MSBuild with little indication it is
doing so.

More details

Rule ID

windows_network_connection_1

Query

{'selection': {'EventImage|endswith': '\\MSBuild.exe'}, 'condi
tion': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring Windows network connection events

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1127 

References
N/A

Severity

Title

Description

50

Suppression Logic Based On
computer_name
event_data.Image
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

Network Activity From
mshta

Mshta is the Microsoft HTML Application Host and allows the execution of .hta files. If the mshta
utility is accessing network resources, it might be using code from a third party or even
downloading malicious code or executables.

More details

Rule ID

windows_network_connection_2

Query

{'selection': {'EventImage|endswith': '\\mshta.exe'}, 'conditi
on': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring Windows network connection events

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
event_data.Image
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

Network Activity From
msxsl

Msxsl allows you to perform command line Extensible Stylesheet Language (XSL)
transformations. If the msxsl utility is accessing network resources, it might be using code from a
third party or even downloading malicious code or executables.

More details

Rule ID

windows_network_connection_3

Query

{'selection': {'EventImage|endswith': '\\msxsl.exe'}, 'conditi
on': 'selection'}

Title

Description

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring Windows network connection events

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
event_data.Image
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

Network Activity From
verclsid

Verclsid allows you to validate shell extensions before they are instantiated by the Windows shell
or Windows Explorer. If the verclsid utility is accessing network resources, it might be using code
from a third party or even downloading malicious code or executables.

More details

Rule ID

windows_network_connection_4

Query

{'selection': {'EventImage|endswith': '\\verclsid.exe'}, 'cond
ition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring Windows network connection events

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
event_data.Image
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

Unexpected Network
Activity from Microsoft Tool

A Microsoft tool was executed with suspicious network connection activity. This could be an
indication of malicious activity.

More details

Rule ID

windows_network_connection_5

Query

{'selection': {'EventImage|endswith': ['\\bginfo.exe', '\\rcsi
.exe', '\\control.exe', '\\odbcconf.exe']}, 'condition': 'sele
ction'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring Windows network connection events

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
event_data.Image
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

