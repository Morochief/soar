✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious AWS Login
Failure
The following rules are used to identify suspicious AWS account login failure. Any one or more of
these will trigger the AWS Cloud Account Login Failure alert. Details for each rule can be viewed
by clicking the More Details link in the description.
Title Description
AWS Console Login Failed The following analytic identifies an authentication attempt event against an AWS Console that
During MFA Challenge fails during the Multi Factor Authentication challenge.
More details
Rule ID
aws_117
Query
{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selec
tion2': {'eventName': 'ConsoleLogin'}, 'selection3': {'errorMe
ssage': 'Failed authentication'}, 'selection4': {'additionalEv
entData_MFAUsed': 'Yes'}, 'condition': 'selection1 and selecti
on2 and selection3 and selection4'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0042 , T1586 
References
https://aws.amazon.com/what-is/mfa/ 
Severity
80
Suppression Logic Based On
service_id

Title Description
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
| Maturi Creation | Risk False Positives |     |
| --------------- | -------------------- | --- |
| ty Date         | Level                |     |
| produc 2022-10- | mediu                |     |
Legitimate users may miss to reply the MFA challenge
| tion 03 | m   | within the time window or deny it by mistake. |
| ------- | --- | --------------------------------------------- |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        