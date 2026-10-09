✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra ID
Discovery using Azurehound Alert
The following rules are used to identify Microsoft Entra ID discovery using Azurehound. Any one
or more of these will trigger the Microsoft Entra ID Discovery using Azurehound Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Title Description
Discovery Using Detects AzureHound (A BloodHound data collector for Microsoft Azure) activity via the default User-Agent
AzureHound that is used during its operation after successful authentication.
More details
Rule ID
azure_1
Query
{'selection': {'userAgent|contains': 'azurehound', 'login_result': '
success'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,35b781cc-1a08-4a5a-80af-42fd7c315c6b
Author: Janantha Marasinghe
Tactics, Techniques, and Procedures
TA0007 , T1087.004 , T1526 
References
https://github.com/BloodHoundAD/AzureHound 
Severity
75
Suppression Logic Based On
srcip_username
stellar.rule_id

Title Description
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2022/11/27    | high       |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        