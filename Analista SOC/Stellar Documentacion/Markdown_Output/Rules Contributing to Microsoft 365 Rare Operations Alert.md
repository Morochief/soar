Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft 365 Rare
Operations Alert

The following rules are used to identify rare and suspicious Microsoft 365 mailbox operations.
Any one or more of these will trigger the Microsoft 365 Rare Operations Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

Description

Rare and Potentially High-
Risk Office365 Operations

Identifies Office365 operations that are typically rare and can provide capabilities useful to
attackers.

More details

Rule ID

office365_mail_5

Query

{'selection1': {'Operation': ['add-
mailboxfolderpermission', 'new-
managementroleassignment', 'new-inboxrule', 'set-
inboxrule', 'set-
transportrule']}, 'selection2': {'Operation': ['add-
mailboxpermission', 'set-
mailbox']}, 'selection3': {'UserId|contains': ['nt authority\
\system (microsoft.exchange.servicehost)', 'nt authority\\sys
tem (microsoft.exchange.adminapi.netcore)', 'nt authority\\sy
stem (w3wp)', 'devilfish-
applicationaccount']}, 'condition': 'selection1 or (selection
2 and not selection3)'}

Log Source

Stellar Cyber Microsoft 365 configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1098 , TA0009 , T1114 

References

Title

Description

N/A

Severity

25

Suppression Logic Based On

office365.Operation
user.name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2025/06/09

low

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

