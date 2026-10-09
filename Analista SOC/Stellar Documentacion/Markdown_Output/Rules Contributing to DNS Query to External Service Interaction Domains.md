Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to DNS Query to External
Service Interaction Domains

The following rules are used to identify DNS queries to external service interaction domains often
used for out-of-band interactions after successful RCE. Any one or more of these will trigger the
DNS Query to External Service Interaction Domains Alert. Details for each rule can be viewed by
clicking the More Details link in the description.

Title

Description

DNS Query to External
Service Interaction Domains

DNS query to external service interaction domains often used for out-of-band interactions after
successful RCE.

More details

Rule ID

dns_3

Query

{'selection_domain': {'DnsQuestionName|endswith': ['.interact
.sh', '.oast.pro', '.oast.live', '.oast.site', '.oast.online'
, '.oast.fun', '.oast.me', '.burpcollaborator.net', '.oastify
.com', '.canarytokens.com', '.requestbin.net', '.dnslog.cn']}
, 'condition': 'selection_domain'}

Log Source

Stellar Cyber Network Events configured.

Rule Source

SigmaHQ,aff715fa-4dd5-497a-8db3-910bea555566

Author: Florian Roth (Nextron Systems), Matt Kelly (list of domains)

Tactics, Techniques, and Procedures

TA0001 , T1190 , TA0043 , T1595.002 

References

https://github.com/SigmaHQ/sigma/blob/598d29f811c1859ba18e05b8c419cc94410c9
a55/rules/network/dns/net_dns_external_service_interaction_domains.yml 

https://twitter.com/breakersall/status/1533493587828260866 

Title

Description

Severity

30

Suppression Logic Based On

srcip
dns.question.name
stellar.rule_id

Additional Information

Matu
rity

Creatio
n Date

Risk
Level

test 2022/0

6/07

mediu
m

False Positives

Legitimate external service access. May be initiated by
internal security engineers for out-of-band application security
testing.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

