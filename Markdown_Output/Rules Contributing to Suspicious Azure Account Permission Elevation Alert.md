Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure Account
Permission Elevation Alert

The following rules are used to identify suspicious Azure account permission elevation. Any one
or more of these will trigger the Suspicious Azure Account Permission Elevation Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Azure Subscription
Permission Elevation Via
ActivityLogs

Detects when a user has been elevated to manage all Azure Subscriptions. This change
should be investigated immediately if it isn't planned. This setting could allow an attacker
access to Azure subscriptions in your environment.

More details

Rule ID

azure_71

Query

{'selection': {'operationName': 'MICROSOFT.AUTHORIZATION/ELE
VATEACCESS/ACTION'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,09438caa-07b1-4870-8405-1dbafe3dad95

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0004 , T1098.003 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations#microsoftauthorization 

Severity

75

Suppression Logic Based On

azure_activity_log.resourceId

Title

Description

azure_activity_log.operationName
stellar.rule_id

Additional Information

Maturity Creation Date Risk Level False Positives

test

2021/11/26

high

If this was approved by System Administrator.

Granting Of Permissions To
An Account

Identifies IPs from which users grant access to other users on azure resources and alerts
when a previously unseen source IP address is used.

More details

Rule ID

azure_82

Query

{'selection': {'OperationNameValue': ['Microsoft.Authorizati
on/roleAssignments/write']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,a622fcd2-4b5a-436a-b8a2-a4171161833c

Author: sawwinnnaung

Tactics, Techniques, and Procedures

TA0004 , T1098.003 

References

https://github.com/Azure/Azure-
Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureAct
ivity/Granting_Permissions_To_Account_detection.yaml 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2020/05/07

medium

Valid change

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

