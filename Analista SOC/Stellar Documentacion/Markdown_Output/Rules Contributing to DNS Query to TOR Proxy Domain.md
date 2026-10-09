Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to DNS Query to TOR Proxy
Domain

The following rules are used to identify DNS queries to onion domains and proxy domains for
TOR network. Any one or more of these will trigger the DNS Query to TOR Proxy Domain Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

DNS Query to TOR
Proxy Domain

DNS query to onion domains and proxy domains for TOR network.

Description

More details

Rule ID

dns_1

Query

{'selection_domain': {'DnsQuestionName|endswith': ['.onion', '.tor2
web.org', '.tor2web.com', '.torlink.co', '.onion.to', '.onion.ink',
 '.onion.cab', '.onion.nu', '.onion.link', '.onion.it', '.onion.cit
y', '.onion.direct', '.onion.top', '.onion.casa', '.onion.plus', '.
onion.rip', '.onion.dog', '.tor2web.fi', '.tor2web.blutmagie.de', '
.onion.sh', '.onion.lu', '.onion.pet', '.t2w.pw', '.tor2web.ae.org'
, '.tor2web.io', '.tor2web.xyz', '.onion.lt', '.s1.tor-
gateways.de', '.s2.tor-gateways.de', '.s3.tor-
gateways.de', '.s4.tor-gateways.de', '.s5.tor-
gateways.de', '.hiddenservice.net']}, 'condition': 'selection_domai
n'}

Log Source

Stellar Cyber Network Events configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0010 , T1048 , TA0011 , T1090.003 

References

https://github.com/Azure/Azure-
Sentinel/blob/f99542b94afe0ad2f19a82cc08262e7ac8e1428e/Detections/ASimDNS/imDNS_

Title

Description

TorProxies.yaml 

Severity

30

Suppression Logic Based On

srcip
dns.question.name
stellar.rule_id

Additional Information

Maturi
ty

Creatio
n Date

Risk
Level

experi
mental

2024/0
5/15

mediu
m

False Positives

Legitimate access to TOR network. TOR network is rarely used for
normal daily use unless your services have special anonymity
needs.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

