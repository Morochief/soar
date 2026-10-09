✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious Microsoft 365
Mail Transport Rule Alert
The following rules are used to identify suspicious Microsoft 365 mail transport rules. Any one or
more of these will trigger the Suspicious Microsoft 365 Mail Transport Rule Alert. Details for each
rule can be viewed by clicking the More Details link in the description.
Title Description
Office365 Mail Redirect via Identifies when an Exchange Online transport rule is configured to forward emails. This could be
ExO Transport Rule an adversary mailbox configured to collect mail from multiple user accounts.
More details
Rule ID
office365_mail_1
Query
{'selection1': {'Operation': ['new-transportrule', 'set-
transportrule']}, 'selection2': {'BlindCopyTo': ''}, 'selectio
n3': {'RedirectMessageTo': ''}, 'condition': 'selection1 and (
not selection2 or not selection3)'}
Log Source
Stellar Cyber Microsoft 365 configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1114 , TA0010 , T1020 
References
N/A
Severity
50
Suppression Logic Based On
office365.Operation
office365.ObjectId
office365.Name

Title Description
user.name
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/06/09    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        