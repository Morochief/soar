Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Windows
Registry Event: Impact Alert

The following rules are used to identify suspicious Windows registry events usually in the impact
stage. Any one or more of these will trigger the Suspicious Windows Registry Event: Impact
Alert. Details for each rule can be viewed by clicking the More Details link in the description.

Windows Events Required: 13

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Potential Ransomware Activity
Using LegalNotice Message

Detect changes to the "LegalNoticeCaption" or "LegalNoticeText" registry values where the
message set contains keywords often used in ransomware ransom messages

More details

Rule ID

windows_registry_set_1

Query

{'selection': {'TargetObject|contains': ['\\SOFTWARE\\Micros
oft\\Windows\\CurrentVersion\\Policies\\System\\LegalNoticeC
aption', '\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Po
licies\\System\\LegalNoticeText']}, 'condition': 'selection'
}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring registry events

Rule Source

SigmaHQ,8b9606c9-28be-4a38-b146-0e313cc232c1

Author: frack113

Tactics, Techniques, and Procedures

TA0040 , T1491.001 

References

Title

Description

https://github.com/redcanaryco/atomic-red-
team/blob/5c1e6f1b4fafd01c8d1ece85f510160fc1275fbf/atomics/T1491.001/T1491
.001.md 

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

2022/12/11

high

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

