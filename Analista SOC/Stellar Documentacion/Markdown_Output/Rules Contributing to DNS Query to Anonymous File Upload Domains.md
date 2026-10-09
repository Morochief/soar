Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to DNS Query to Anonymous
File Upload Domains

The following rules are used to identify DNS queries to anonymous file upload platform domains
often used for malicious purposes. Any one or more of these will trigger the DNS Query to
Anonymous File Upload Domains Alert. Details for each rule can be viewed by clicking the More
Details link in the description.

Title

Description

DNS Query to Anonymous
File Upload Domains

DNS query to anonymous file upload platform domains often used for malicious purposes.

More details

Rule ID

dns_6

Query

{'selection_domain': {'DnsQuestionName|endswith': ['.anonfiles
.com', '.api.put.io', '.upload.put.io', '.ufile.io']}, 'condit
ion': 'selection_domain'}

Log Source

Stellar Cyber Network Events configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0010 , T1567.002 

References

https://github.com/SigmaHQ/sigma/blob/29dce312bc49a9101d33e4d390a7c349c8d98
5a2/rules/windows/builtin/dns_client/win_dns_client_anonymfiles_com.yml 

https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-
spotlight-blackbyte 

https://github.com/SigmaHQ/sigma/blob/29dce312bc49a9101d33e4d390a7c349c8d98
5a2/rules/windows/builtin/dns_client/win_dns_client_put_io.yml 

https://darkatlas.io/blog/medusa-ransomware-group-opsec-failure 

https://github.com/SigmaHQ/sigma/blob/598d29f811c1859ba18e05b8c419cc94410c9a
55/rules/windows/builtin/dns_client/win_dns_client_ufile_io.yml 

Title

Description

https://thedfirreport.com/2021/12/13/diavol-ransomware/ 

Severity

20

Suppression Logic Based On

srcip
dns.question.name
stellar.rule_id

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2024/12/20

low

False Positives

Legitimate use of anonymous file sharing
services.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

