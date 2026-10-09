Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Azure New CloudShell
Created Alert

The following rules are used to identify events when an Azure new Cloud Shell is changed. Any
one or more of these will trigger the Azure New CloudShell Created Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Title

Azure New
CloudShell Created

Identifies when a new cloudshell is created inside of Azure portal.

Description

More details

Rule ID

azure_56

Query

{'selection': {'operationName': 'MICROSOFT.PORTAL/CONSOLES/WRITE'}
, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,72af37e2-ec32-47dc-992b-bc288a2708cb

Author: Austin Songer

Tactics, Techniques, and Procedures

TA0002 , T1059 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Title

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2021/09/21 medium

Description

False Positives

A new cloudshell may be created by a system
administrator.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

