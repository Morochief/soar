✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to T1047 Wmiprvse
Wbemcomn DLL Hijack Alert
The following rules detect suspicious SMB traffic related to WMI DLL Hijack activities. Any one or
more of these will trigger the T1047 Wmiprvse Wbemcomn DLL Hijack Alert. Details for each rule
can be viewed by clicking the More Details link in the description.
Title Description
T1047 Wmiprvse Detects a threat actor creating a file named `wbemcomn.dll` in the `C:\Windows\System32\wbem\`
Wbemcomn DLL Hijack directory over the network for a WMI DLL Hijack scenario.
More details
Rule ID
network_security_13
Query
{'selection': {'appid_name': 'smb', 'metadata|contains': ['\\\\w
bem\\\\wbemcomn.dll']}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1047 , TA0008 , T1021.002 
References
https://threathunterplaybook.com/hunts/windows/201009-
RemoteWMIWbemcomnDLLHijack/notebook.html 
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip

Title Description
dstip_host
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2024/07/13    | high       |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        