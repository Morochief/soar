Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Instance
Activity Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious instance activity in OCI. Any one or more of
these will trigger the Suspicious OCI Instance Activity Alert. Details for each rule can be viewed
by clicking the More Details link in the description.

Title

Description

OCI Multiple
Instances Terminated

Detects when multiple instances were terminated.

More details

Rule ID

oci_audit_21

Query

{'selection': {'eventName': 'TerminateInstance'}, 'condition': 'se
lection | count() by srcip >= 5', 'timeframe': '10m'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0040 , T1529 

References
N/A

Severity

75

Suppression Logic Based On

srcip

Title

Description

stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2025/03/03

high

N/A

OCI Multiple
Instances Launched

Detects when multiple instances were launched.

More details

Rule ID

oci_audit_22

Query

{'selection': {'eventName': 'LaunchInstance'}, 'condition': 'selec
tion | count() by srcip >= 5', 'timeframe': '10m'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0040 , T1496 

References
N/A

Severity

50

Suppression Logic Based On

srcip
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2025/03/03

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

