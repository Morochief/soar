Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AD Machine
Account Creation Alert

The following rules are used to identify suspicious machine account creation activity in Active
Directory. Any one or more of these will trigger the Suspicious AD Machine Account Creation
Alert. Details for each rule can be viewed by clicking the More Details link in the description.

Title

Description

Active Directory
MachineAccountQuota
Compromise

MachineAccountQuota is an attribute in Active Directory that specifies how many machine
accounts a user can create in the domain. Compromise of MachineAccountQuota occurs when
an attacker abuses this privilege to create unauthorised machine accounts. Machine accounts
are assigned credentials, just like user accounts. Attackers can extract the credentials
(password hashes) for further use. These accounts can then be used for other malicious
purposes, often bypassing standard account monitoring mechanisms.

More details

Rule ID

ad_machineAccountQuota_compromise

Query

{'selection': {'EventID': [4741, 4720], 'TargetUserName|endsw
ith': '$'}, 'condition': 'selection |
 count() by SubjectUserName > 3', 'timeframe': '15m'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1136 

References

https://rootguard.gitbook.io/cyberops/detection-engineering/ad-attack-detections-and-
mitigations/machineaccountquota-compromise 

Severity

Title

Description

50

Suppression Logic Based On

event_data.SubjectUserName
stellar.rule_id

Additional Information

Creati
on
Date

Risk
Leve
l

2025/
06/13

medi
um

Matur
ity

experi
ment
al

False Positives

False positives are possible if multiple machine accounts are
created by legitimate users. We recommend excluding trusted
service accounts or administrators. However, limiting the ability
of non-privileged users to register devices is highly
recommended.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

