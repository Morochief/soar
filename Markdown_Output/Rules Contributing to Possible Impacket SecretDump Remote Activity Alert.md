✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Possible Impacket
SecretDump Remote Activity Alert
The following rules detect suspicious SMB traffic related to credential dumping using Impacket.
Any one or more of these will trigger the Possible Impacket SecretDump Remote Activity Alert.
Details for each rule can be viewed by clicking the More Details link in the description.
Title Description
Possible Impacket Detect AD credential dumping using Impacket SecretDump HKTL
SecretDump Remote
More details
Activity
Rule ID
network_security_2
Query
{'selection': {'appid_name': 'smb', 'metadata|contains|all': ['
ADMIN$', 'SYSTEM32\\', '.tmp']}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network
traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
N/A
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host

Title Description
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2024/07/01    | high       |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        