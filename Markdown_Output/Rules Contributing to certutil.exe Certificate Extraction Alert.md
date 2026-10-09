Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to certutil.exe Certificate
Extraction Alert

The following rules are used to identify certutil.exe certificate extraction activity. Any one or more
of these will trigger the certutil.exe Certificate Extraction Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

certutil.exe
Certificate
Extraction

Description

The following analytic identifies the use of certutil.exe with arguments indicating the manipulation or
extraction of certificates. This activity is significant because extracting certificates can allow attackers to
sign new authentication tokens, particularly in federated environments like Windows ADFS. If confirmed
malicious, this could enable attackers to forge authentication tokens, potentially leading to unauthorized
access and privilege escalation within the network.

More details

Rule ID

certutil_exe_certificate_extraction

Query

{'selection1': {'Image|endswith': '\\certutil.exe'}, 'selection2':
{'CommandLine|contains': '-
exportPFX'}, 'condition': 'selection1 and selection2'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1649 

References

https://blog.sygnia.co/detection-and-hunting-of-golden-saml-attack 

https://strontic.github.io/xcyclopedia/library/certutil.exe-
09A8A29BAA3A451713FD3D07943B4A43.html 

Severity

Title

Description

90

Suppression Logic Based On
computer_name
process_name
event_data.CommandLine
stellar.rule_id

Additional Information

Matur
ity

Creati
on
Date

Risk
Level

2025/0
8/18

critic
al

experi
menta
l

False Positives

Unless there are specific use cases, manipulating or exporting
certificates using certutil is uncommon. Extraction of certificate has
been observed during attacks such as Golden SAML and other
campaigns targeting Federated services.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

