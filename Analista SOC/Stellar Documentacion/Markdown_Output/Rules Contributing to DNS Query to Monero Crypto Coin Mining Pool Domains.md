Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to DNS Query to Monero
Crypto Coin Mining Pool Domains

The following rules are used to identify DNS queries to Monero crypto coin mining pool domains.
Any one or more of these will trigger the DNS Query to Monero Crypto Coin Mining Pool
Domains Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

DNS Query to Monero Crypto
Coin Mining Pool Domains

DNS query to Monero crypto coin mining pool domains.

More details

Rule ID

dns_4

Query

{'selection_domain': {'DnsQuestionName|endswith': ['pool.min
exmr.com', 'fr.minexmr.com', 'de.minexmr.com', 'sg.minexmr.c
om', 'ca.minexmr.com', 'us-
west.minexmr.com', 'pool.supportxmr.com', 'mine.c3pool.com',
 'xmr-eu1.nanopool.org', 'xmr-eu2.nanopool.org', 'xmr-us-
east1.nanopool.org', 'xmr-us-west1.nanopool.org', 'xmr-
asia1.nanopool.org', 'xmr-jp1.nanopool.org', 'xmr-
au1.nanopool.org', 'xmr.2miners.com', 'xmr.hashcity.org', 'x
mr.f2pool.com', 'xmrpool.eu', 'pool.hashvault.pro']}, 'condi
tion': 'selection_domain'}

Log Source

Stellar Cyber Network Events configured.

Rule Source

SigmaHQ,b593fd50-7335-4682-a36c-4edcb68e4641

Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures

TA0040 , T1496 , TA0010 , T1567 

References

Title

Description

https://github.com/SigmaHQ/sigma/blob/598d29f811c1859ba18e05b8c419cc94410
c9a55/rules/network/dns/net_dns_pua_cryptocoin_mining_xmr.yml 

https://www.nextron-systems.com/2021/10/24/monero-mining-pool-fqdns/ 

Severity

50

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

stabl
e

2021/1
0/24

high

False Positives

Legitimate access to Monero mining pools. Rarely happens
unless legitimate programs contain crypto mining functions.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

