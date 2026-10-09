Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Microsoft 365
Inbox Rule Alert

The following rules are used to identify suspicious Microsoft 365 inbox rules. Any one or more of
these will trigger the Suspicious Microsoft 365 Inbox Rule Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

Malicious Office365 Inbox
Rule

Often times after the initial compromise, the attackers create inbox rules to delete emails that
contain certain keywords. This is done so as to limit ability to warn compromised users that they
have been compromised.

More details

Rule ID

office365_mail_2

Query

{'selection1': {'Operation': 'new-
inboxrule', 'ResultStatus': ['true', 'succeeded'], 'Parameters
|contains': ['deleted items', 'junk email', 'deletemessage']},
 'selection2': {'SubjectContainsWords|contains': ['helpdesk',
' alert', ' suspicious', 'fake', 'malicious', 'phishing', 'spa
m', 'do not click', 'do not open', 'hijacked', 'fatal']}, 'sel
ection3': {'BodyContainsWords|contains': ['helpdesk', ' alert'
, ' suspicious', 'fake', 'malicious', 'phishing', 'spam', 'do
not click', 'do not open', 'hijacked', 'fatal']}, 'selection4'
: {'SubjectOrBodyContainsWords|contains': ['helpdesk', ' alert
', ' suspicious', 'fake', 'malicious', 'phishing', 'spam', 'do
 not click', 'do not open', 'hijacked', 'fatal']}, 'condition'
: 'selection1 and (selection2 or selection3 or selection4)'}

Log Source

Stellar Cyber Microsoft 365 configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1564.008 , TA0003 , T1098 

Title

Description

References

https://www.reddit.com/r/sysadmin/comments/7kyp0a/recent_phishing_attempts_my_e
xperience_and_what/ 

Severity

50

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

medium

N/A

Suspicious Office365 Inbox
MoveToFolder Rule

Identifies when the parameters of Microsoft 365 inbox MoveToFolder rules have suspicious
characteristics that move emails to the RSS folder, which attackers sometimes use to hide
incoming mail like security alerts or MFA notifications.

More details

Rule ID

office365_mail_3

Query

{'selection': {'Operation': ['new-inboxrule', 'set-
inboxrule'], 'MoveToFolder|contains': 'rss'}, 'condition': 'se
lection'}

Log Source

Stellar Cyber Microsoft 365 configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1564.008 , TA0003 , T1098 

References
N/A

Severity

50

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

medium

N/A

Suspicious Office365 Inbox
Rule Name

Identifies when the parameters of Microsoft 365 inbox rules have suspicious characteristics that
are often used in automated or attacker-created rules, specifically rule names that contain
strange strings or strings used in known attacks.

More details

Rule ID

Title

Description

office365_mail_4

Query

{'selection1': {'Operation': ['new-inboxrule', 'set-
inboxrule']}, 'selection2': {'Name|contains': ['erder', 'ddd']
}, 'selection3': [{'Name|re': '/(^|\\s+)\\.+
($|\\s+)/'}, {'Name|re': '/(^|\\s+)\\w{0,3}\\.\\w{0,3}
($|\\s+)/'}, {'Name|re': '/(^|\\s+).
($|\\s+)/'}, {'Name|re': '/(^|\\s+)\\,+,
($|\\s+)/'}, {'Name|re': '/(^|\\s+)\\W{0,4}
($|\\s+)/'}, {'Name|re': '/(^|\\s+)(.)\\1{0,3}
($|\\s+)/'}, {'Name|re': '/(^|\\s+)[a-z]{0,3}
($|\\s+)/'}], 'condition': 'selection1 and (selection2 or sele
ction3)'}

Log Source

Stellar Cyber Microsoft 365 configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1564.008 , TA0003 , T1098 

References
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

Malicious Office365 Inbox
Deletion Rule

Identifies when a Microsoft 365 inbox rule is set up such that it deletes all incoming messages,
without specifying any condition (e.g., from a specific sender, with a certain subject, etc.).
Attackers often use this to hide inbound warnings, MFA emails, or incident response
communication after compromising an account.

More details

Rule ID

office365_mail_6

Query

{'selection': {'Operation': ['new-inboxrule', 'set-
inboxrule'], 'DeleteMessage': 'true'}, 'condition': 'selection
'}

Log Source

Stellar Cyber Microsoft 365 configured.

Rule Source

Developed internally by Stellar Cyber

Title

Description

Tactics, Techniques, and Procedures

TA0005 , T1564.008 , TA0003 , T1098 

References
N/A

Severity

50

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

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

