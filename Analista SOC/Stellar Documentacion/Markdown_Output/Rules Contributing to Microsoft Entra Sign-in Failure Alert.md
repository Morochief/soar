✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra Sign-in
Failure Alert
The following rules are used to identify suspicious Microsoft Entra sign-in failures. Any one or
more of these will trigger the Microsoft Entra Sign-in Failure Alert. Details for each rule can be
viewed by clicking the More Details link in the description.
Title Description
Sign-in Failure Due to Define a baseline threshold for failed sign-ins due to Conditional Access failures
Conditional Access
More details
Requirements Not Met
Rule ID
azure_3
Query
{'selection': {'ResultType': 53003}, 'condition': 'selecti
on'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,b4a6d707-9430-4f5f-af68-0337f52d5c42
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
stellar.rule_id

Title Description
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/01 high
Service Account misconfigured
Misconfigured Systems
Vulnerability Scanners
Multifactor Authentication Denied User has indicated they haven't instigated the MFA prompt and could indicate an attacker
has the password for the account.
More details
Rule ID
azure_4
Query
{'selection': {'status_additionalDetails|contains': 'MFA d
enied'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,e40f4962-b02b-4192-9bfe-245f7ece1f99
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0001 , T1078.004 , TA0006 , T1110 
References
https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-
targeting-organizations-for-data-exfiltration-and-destruction/ 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2022/03/2 medium
Users actually login but mis-click into the Deny
4 button when MFA prompt.
Multifactor Authentication Identifies user login with multifactor authentication failures, which might be an indication an
Interrupted attacker has the password for the account but can't pass the MFA challenge.
More details
Rule ID
azure_5
Query
{'selection_50074': {'ResultType': 50074}, 'selection_5001
21': {'ResultType': 500121}, 'condition': '1 of selection_
*'}

Title Description
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,5496ff55-42ec-4369-81cb-00f417029e25
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0001 , T1078.004 , TA0006 , T1110 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/10 medium
Unknown
Account Lockout Identifies user account which has been locked because the user tried to sign in too many
times with an incorrect user ID or password.
More details
Rule ID
azure_6
Query
{'selection': {'ResultType': 50053}, 'condition': 'selecti
on'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,2b7d6fc0-71ac-4cf7-8ed1-b5788ee5257a
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0006 , T1110 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information

Title Description
| Maturity | Creation Date | Risk Level | False Positives |
| -------- | ------------- | ---------- | --------------- |
| test     | 2021/10/10    | medium     |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        