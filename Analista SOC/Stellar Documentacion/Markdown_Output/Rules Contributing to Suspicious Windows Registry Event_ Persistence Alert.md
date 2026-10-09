Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Windows
Registry Event: Persistence Alert

The following rules are used to identify suspicious Windows registry events usually in the
persistence stage. Any one or more of these will trigger the Suspicious Windows Registry Event:
Persistence Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Windows Events Required: 13

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Potential Persistence Via
Microsoft office Add-in

Detect potential persistence via the creation of a Microsoft office add-in file to make it run
automatically.

More details

Rule ID

windows_registry_set_2

Query

{'selection1': {'TargetObject|contains': ['\\Software\\Microso
ft\\Office\\']}, 'selection2': {'TargetObject|contains': ['\\E
xcel\\Options\\OPEN'], 'Details|startswith': '/R ', 'Details|e
ndswith': '.xll'}, 'selection3': {'TargetObject|contains|all':
 ['\\PowerPoint\\AddIns', '\\Path'], 'Details|endswith': '.ppa
m'}, 'condition': 'selection1 and (selection2 or selection3)'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring registry events

Rule Source

SigmaHQ,961e33d1-4f86-4fcf-80ab-930a708b2f82

Author: frack113

Tactics, Techniques, and Procedures

TA0003 , T1137.006 

Title

Description

References

https://github.com/redcanaryco/atomic-red-
team/blob/4ae9580a1a8772db87a1b6cdb0d03e5af231e966/atomics/T1137.006/T1137.
006.md 

https://labs.withsecure.com/publications/add-in-opportunities-for-office-persistence 

Severity

75

Suppression Logic Based On
computer_name
event_data.TargetObject
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2023/01/15

high

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

