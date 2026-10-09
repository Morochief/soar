Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Steal or Forge Kerberos
Tickets Alert

The following rules are used to identify suspicious activity to steal or forge kerberos tickets. Any
one or more of these will trigger the Steal or Forge Kerberos Tickets Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Windows Events Required: 4104, 4611, 4673, 4769

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Register new Logon Process by
Rubeus

Detects potential use of Rubeus via registered new trusted logon process

More details

Rule ID

windows_security_16

Query

{'selection': {'EventID': 4611, 'LogonProcessName': 'User3
2LogonProcesss'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,12e6d621-194f-4f59-90cc-1959e21e69f7

Author: Roberto Rodriguez (source), Ilyas Ochkov (rule), oscd.community

Tactics, Techniques, and Procedures

TA0006 , T1558.003 

References

https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-
forests-trusts-71f2b33688e1 

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

2019/10/24

high

Unknown

User Couldn't Call a Privileged
Service
'LsaRegisterLogonProcess'

The 'LsaRegisterLogonProcess' function verifies that the application making the function
call is a logon process by checking that it has the SeTcbPrivilege privilege set. Possible
Rubeus tries to get a handle to LSA.

More details

Rule ID

windows_security_116

Query

{'selection': {'EventID': 4673, 'Service': 'LsaRegisterLog
onProcess()', 'Keywords': '0x8010000000000000'}, 'conditio
n': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,6daac7fc-77d1-449a-a71a-e6b4d59a0e54

Author: Roberto Rodriguez (source), Ilyas Ochkov (rule), oscd.community

Tactics, Techniques, and Procedures

TA0006 , T1558.003 

References

https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-
forests-trusts-71f2b33688e1 

Severity

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

2019/10/24

high

Unknown

PowerShell Kerberos Ticket
Request

Detects PowerShell scripts that have the capability of requesting kerberos tickets, which is
a common step in Kerberoasting toolkits to crack service accounts.

More details

Rule ID

powershell_scriptblock_154

Title

Description

Query

{'selection1': {'ScriptBlockText|contains': 'KerberosReque
storSecurityToken'}, 'selection2': {'UserId': ['S-1-5-
18', 'S-1-5-
20']}, 'selection3': {'ScriptBlockText|contains': 'sentine
lbreakpoints'}, 'selection4': {'ScriptBlockText|contains':
 ['Set-PSBreakpoint', 'Set-
HookFunctionTabs']}, 'selection5': {'ScriptBlockText|conta
ins|all': ['function global', '\\windows\\sentinel\\4']},
'condition': 'selection1 and (not selection2) and (not ((s
election3 and selection4) or selection5))'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring PowerShell scripts

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0002 , T1059.001 , TA0006 , T1003 , T1558 

References
N/A

Severity

49

Suppression Logic Based On
computer_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2022/01/24

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

