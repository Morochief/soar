Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Changes
to Privileged Account Alert

The following rules are used to identify suspicious Microsoft Entra changes to privileged account.
Any one or more of these will trigger the Microsoft Entra Changes to Privileged Account Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

Description

Temporary Access Pass
Added to an Account

Detects when a temporary access pass (TAP) is added to an account. TAPs added to privileged
accounts should be investigated

More details

Rule ID

azure_36

Query

{'selection': {'ResultReason': 'Admin registered temporary acce
ss pass method for user', 'properties_message': 'Admin register
ed security info'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,fa84aaf5-8142-43cd-9ec2-78cfebf878ce

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0003 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#changes-to-privileged-accounts 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id

Title

Description

azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity

experiment
al

Creation
Date

Risk
Level

2022/08/10

high

False Positives

Administrator adding a legitimate temporary
access pass

Privileged Account
Creation

Detects when a new admin is created.

More details

Rule ID

azure_37

Query

{'selection': {'Result': 'Success', 'properties_message|contain
s|all': ['Add user', 'Add member to role']}, 'condition': 'sele
ction'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,f7b5b004-dece-46e4-a4a5-f6fd0e1c6947

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H', Tim Shelton

Tactics, Techniques, and Procedures

TA0003 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#changes-to-privileged-accounts 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity

Creation Date Risk Level False Positives

experimental 2022/08/11

medium

A legitimate new admin account being created

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

