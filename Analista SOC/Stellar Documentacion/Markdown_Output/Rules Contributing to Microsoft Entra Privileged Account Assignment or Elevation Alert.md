Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Privileged
Account Assignment or Elevation Alert

The following rules are used to identify suspicious Microsoft Entra privileged account assignment
or elevation. Any one or more of these will trigger the Microsoft Entra Privileged Account
Assignment or Elevation Alert. Details for each rule can be viewed by clicking the More Details
link in the description.

Title

Description

Azure Subscription
Permission Elevation via
AuditLogs

Detects when a user has been elevated to manage all Azure Subscriptions. This change should
be investigated immediately if it isn't planned. This setting could allow an attacker access to
Azure subscriptions in your environment.

More details

Rule ID

azure_35

Query

{'selection': {'Category': 'Administrative', 'OperationName':
 'Assigns the caller to user access admin'}, 'condition': 'se
lection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,ca9bf243-465e-494a-9e54-bf9fc239057d

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0004 , T1078 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#assignment-and-elevation 

Severity

75

Title

Description

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity Creation Date Risk Level False Positives

test

2021/11/26

high

If this was approved by System Administrator.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

