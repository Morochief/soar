Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Handle
Request to Sensitive Object Alerts

The following rules are used to identify suspicious activity with handle requests to sensitive
Windows objects. Any one or more of these will trigger a Suspicious Handle Request to Sensitive
Object Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Windows Events Required: 4656

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

SAM Registry Hive
Handle Request

Detects handles requested to SAM registry hive

Description

More details

Rule ID

windows_security_147

Query

{'selection': {'EventID': 4656, 'ObjectType': 'Key', 'ObjectName|e
ndswith': '\\SAM'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,f8748f2c-89dc-4d95-afb0-5a2dfdbad332

Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures

TA0007 , T1012 , TA0006 , T1552.002 

References

https://threathunterplaybook.com/hunts/windows/190725-
SAMRegistryHiveHandleRequest/notebook.html 

Severity

Title

Description

75

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2019/08/12

high

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

