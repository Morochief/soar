Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Microsoft Entra
Sign-in Activity Alert

The following rules are used to identify suspicious Microsoft Entra sign-in activity. Any one or
more of these will trigger the Microsoft Entra Suspicious Sign-in Activity Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

Description

Use of Legacy
Authentication Protocols

Alert on when legacy authentication has been used on an account

More details

Rule ID

azure_9

Query

{'selection': {'login_result': 'success', 'ClientApp': ['Other
 clients', 'IMAP', 'POP3', 'MAPI', 'SMTP', 'Exchange ActiveSyn
c', 'Exchange Web Services']}, 'filter': {'srcip_username': ''
}, 'condition': 'selection and not filter'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,60f6535a-760f-42a9-be3f-c9a0a025906e

Author: Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0001 , T1078.004 , TA0006 , T1110 

References

https://docs.microsoft.com/en-gb/azure/active-directory/fundamentals/security-
operations-privileged-accounts 

Severity

75

Suppression Logic Based On
srcip_username

Title

Description

stellar.rule_id

Additional Information

Maturity Creation

Date

experime
ntal

2022/06/1
7

Risk
Level

high

False Positives

User has been put in exception group so they can
use legacy authentication

Suspicious Sign-ins From a
Non-Registered Device

Detects risky authentication from a non AD registered device without MFA being required.

More details

Rule ID

azure_10

Query

{'selection': {'ResultType': 0, 'RiskState': 'atRisk', 'Device
Detail_trusttype': ''}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,572b12d4-9062-11ed-a1eb-0242ac120002

Author: Harjot Singh, '@cyb3rjy0t'

Tactics, Techniques, and Procedures

TA0001 , T1078 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-devices#non-compliant-device-sign-in 

Severity

75

Suppression Logic Based On
srcip_username
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2023/01/10

high

Unknown

Device Registration or Join
without MFA

Monitor and alert for device registration or join events where MFA was not performed.

More details

Rule ID

azure_11

Query

{'selection': {'ResourceDisplayName': 'Device Registration Ser
vice', 'conditionalAccessStatus': 'success'}, 'filter_mfa': {'
status_additionalDetails|startswith': 'MFA'}, 'condition': 'se
lection and not filter_mfa'}

Log Source

Title

Description

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,5afa454e-030c-4ab4-9253-a90aa7fcc581

Author: Michael Epping, '@mepples21'

Tactics, Techniques, and Procedures

TA0001 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-devices#device-registrations-and-joins-outside-policy 

Severity

50

Suppression Logic Based On
srcip_username
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2022/06/28

medium

Unknown

Azure Unusual
Authentication Interruption

Detects when there is an interruption in the authentication process.

More details

Rule ID

azure_12

Query

{'selection_50097': {'ResultType': 50097}, 'selection_50155':
{'ResultType': 50155}, 'selection_50158': {'ResultType': 50158
}, 'condition': '1 of selection_*'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,8366030e-7216-476b-9927-271d79f13cf3

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0001 , T1078 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 

Severity

50

Suppression Logic Based On
srcip_username
stellar.rule_id

Additional Information

Title

Description

Maturity

Creation Date

Risk Level

False Positives

experimental

2021/11/26

medium

Unknown

Login to Disabled Account

Detect failed attempts to sign in to disabled accounts.

More details

Rule ID

azure_14

Query

{'selection': {'ResultType': 50057}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,908655e0-25cf-4ae1-b775-1c8ce9cf43d8

Author: AlertIQ

Tactics, Techniques, and Procedures

TA0001 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 

Severity

50

Suppression Logic Based On
srcip_username
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2021/10/10

medium

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

