Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Password Reset By User
Account Alert

The following rules are used to identify events when a password is reset by a user account. Any
one or more of these will trigger the Password Reset By User Account Alert Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Password Reset by
User Account

Detect when a user has reset their password in Microsoft Entra ID

Description

More details

Rule ID

azure_34

Query

{'selection': {'Category': 'UserManagement', 'Result': 'Success', '
ActivityDisplayName|contains': 'Password reset'}, 'self_service_act
ivity': {'ActivityDisplayName|contains': 'flow activity progress'},
 'self_service_reason': {'ResultReason': 'User successfully reset p
assword'}, 'filter': {'initiatedBy_user_userPrincipalName': ''}, 'c
ondition': 'selection and not filter and (not self_service_activity
 or self_service_reason)'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,340ee172-4b67-4fb4-832f-f961bdc1f3aa

Author: YochanaHenderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0003 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-operations-
privileged-accounts 

Severity

Title

Description

30

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity Creation

Date

Risk
Level

experimen
tal

2022/08/03 medium

False Positives

If this was approved by System Administrator or
confirmed user action.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

