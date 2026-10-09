Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Windows
Active Directory Operation Alerts

The following rules are used to identify suspicious activity with Windows Active Directory
operation. Any one or more of these will trigger Suspicious Windows Active Directory Operation
Alert. Details for each rule can be viewed by clicking the More Details link in the description.

Windows Events Required: 4662

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

DPAPI Domain
Backup Key Extraction

Detects tools extracting LSA secret DPAPI domain backup key from Domain Controllers

More details

Rule ID

windows_security_37

Query

{'selection': {'EventID': 4662, 'ObjectType': 'SecretObject', 'Ac
cessMask': '0x2', 'ObjectName|contains': 'BCKUPKEY'}, 'condition'
: 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,4ac1f50b-3bd0-4968-902d-868b4647937e

Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures

TA0006 , T1003.004 

References

https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 

Severity

Title

Description

75

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2019/06/20

high

Unknown

WMI Persistence -
Security

Detects suspicious WMI event filter and command line event consumer based on WMI and Security
Logs.

More details

Rule ID

windows_security_60

Query

{'selection': {'EventID': 4662, 'ObjectType': 'WMI Namespace', 'O
bjectName|contains': 'subscription'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,f033f3f3-fd24-4995-97d8-a3bb17550a88

Author: Florian Roth (Nextron Systems), Gleb Sukhodolskiy, Timur Zinniatullin oscd.community

Tactics, Techniques, and Procedures

TA0003 , T1546.003 

References

https://twitter.com/mattifestation/status/899646620148539397 

https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/ 

Severity

50

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2017/08/22

medium

False Positives

Unknown (data set is too small; further testing
needed)

AD Object WriteDAC
Access

Detects WRITE_DAC access to a domain object

More details

Rule ID

windows_security_77

Title

Description

Query

{'selection': {'EventID': 4662, 'ObjectServer': 'DS', 'AccessMask
': '0x40000', 'ObjectType': ['19195a5b-6da0-11d0-afd3-
00c04fd930c9', 'domainDNS']}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,028c7842-4243-41cd-be6f-12f3cf1a26c7

Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures

TA0005 , T1222.001 

References

https://threathunterplaybook.com/hunts/windows/180815-
ADObjectAccessReplication/notebook.html 

https://threathunterplaybook.com/library/windows/active_directory_replication.html 

https://threathunterplaybook.com/hunts/windows/190101-
ADModDirectoryReplication/notebook.html 

Severity

90

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2019/09/12

critical

Unknown

Access to a Sensitive
LDAP Attribute

Identify access to sensitive Active Directory object attributes that contains credentials and decryption
keys such as unixUserPassword, ms-PKI-AccountCredentials and msPKI-CredentialRoamingTokens.

More details

Rule ID

windows_security_81

Query

{'selection1': {'EventID': 4662}, 'selection2': {'SubjectUserSid'
: 'S-1-5-18'}, 'selection3': {'Properties': ['*612cb747-c0e8-
4f92-9221-fdd5f15b550d*', '*b8dfa744-31dc-4ef1-ac7c-
84baf7ef9da7*', '*b3f93023-9239-4f7c-b99c-
6745d87adbc2*', '*b7ff5a38-0818-42b0-8110-
d3d154c97f24*']}, 'selection4': {'AccessMask': ['0x0', '0x100']},
 'condition': 'selection1 and (not selection2) and selection3 and
 (not selection4)'}

Log Source

Stellar Cyber Windows Server Sensor configured.

Rule Source

Developed internally by Stellar Cyber

Title

Description

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

Maturity

Creation Date

Risk Level

False Positives

production

2022/11/09

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

