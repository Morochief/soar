Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Phishing Domain with File
Extension TLD

The following rules are used to identify DNS queries to TLDs that resemble file extensions. Any
one or more of these will trigger the Phishing Domain with File Extension TLD Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Phishing Domain With
File Extension TLD

DNS query to TLDs that resemble file extensions. Attackers may use these TLDs for phishing.

More details

Rule ID

dns_2

Query

{'selection_domain': {'DnsQuestionName|endswith': ['.zip', '.mov
']}, 'condition': 'selection_domain'}

Log Source

Stellar Cyber Network Events configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0001 , T1566 

References

https://arstechnica.com/information-technology/2023/05/critics-say-googles-new-zip-and-
mov-domains-will-be-a-boon-to-scammers/ 

https://www.trendmicro.com/en_us/research/23/e/future-exploitation-vector-file-
extensions-as-top-level-domains.html 

Severity

30

Suppression Logic Based On

srcip
dns.question.name
stellar.rule_id

Title

Description

Additional Information

Maturit
y

Creation
Date

Risk
Level

experim
ental

2024/05/
15

low

False Positives

Legitimate domains with .zip or .mov TLDs. These new
TLDs are rarely seen in common websites.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

