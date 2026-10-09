Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Possible PetitPotam
Coerce Authentication Attempt Alert

The following rules detect suspicious SMB traffic related to PetitPotam coerced authentication.
Any one or more of these will trigger the Possible PetitPotam Coerce Authentication Attempt
Alert. Details for each rule can be viewed by clicking the More Details link in the description.

Title

Description

Possible PetitPotam Coerce
Authentication Attempt

Detect PetitPotam coerced authentication activity.

More details

Rule ID

network_security_4

Query

{'selection': {'appid_name': 'smb', 'metadata|contains|all': [
'IPC$', 'lsarpc', 'ANONYMOUS LOGON']}, 'condition': 'selection
'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network
traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1187 

References

https://github.com/topotam/PetitPotam 

https://github.com/splunk/security_content/blob/0dd6de32de2118b2818550df9e65255
f4109a56d/detections/endpoint/petitpotam_network_share_access_request.yml 

Severity

75

Suppression Logic Based On

Title

Description

appid_name
srcip
dstip
dstip_host
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2024/07/05

high

Unknown.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

