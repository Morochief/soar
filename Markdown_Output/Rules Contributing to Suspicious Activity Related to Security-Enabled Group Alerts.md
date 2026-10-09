✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious Activity
Related to Security-Enabled Group Alerts
The following rules are used to identify suspicious activity related to security-enabled group. Any
one or more of these will trigger suspicious Activity Related to Security-Enabled Group Alert.
Details for each rule can be viewed by clicking the More Details link in the description.
Windows Events Required: 4727, 4730, 4731, 4734, 4754, 4756, 4758
The Windows Detect Profile (Low Volume)  covers these required Windows events.
Title Description
Security-Enabled Universal A Security-Enabled Universal Group has been created. This could be an indication of malicious
Group was Created activity.
More details
Rule ID
windows_itdr_4
Query
{'selection1': {'EventID': 4754}, 'selection2': {'SubjectUserN
ame': ''}, 'selection3': {'SubjectDomainName': ''}, 'condition
': 'selection1 and not selection2 and not selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50

Title Description
Suppression Logic Based On
computer_name
event_id
event_data.SubjectDomainName
event_data.SubjectUserSid
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Security-Enabled Global A Security-Enabled Global Group has been created. This could be an indication of malicious
Group was Created activity.
More details
Rule ID
windows_itdr_5
Query
{'selection1': {'EventID': 4727}, 'selection2': {'SubjectUserN
ame': ''}, 'selection3': {'SubjectDomainName': ''}, 'condition
': 'selection1 and not selection2 and not selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.SubjectDomainName
event_data.SubjectUserSid
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Security-Enabled Local A Security-Enabled Local Group has been created. This could be an indication of malicious
Group was Created activity.
More details
Rule ID
windows_itdr_8
Query
{'selection1': {'EventID': 4731}, 'selection2': {'SubjectUserN
ame': ''}, 'selection3': {'SubjectDomainName': ''}, 'condition
': 'selection1 and not selection2 and not selection3'}

Title Description
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.SubjectDomainName
event_data.SubjectUserSid
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Security-Enabled Local A Security-Enabled Local Group has been deleted. This could be an indication of malicious
Group was Deleted activity.
More details
Rule ID
windows_security_31
Query
{'selection1': {'EventID': 4734}, 'selection2': {'SubjectUserN
ame': ''}, 'selection3': {'SubjectDomainName': ''}, 'condition
': 'selection1 and not selection2 and not selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Title Description
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Security-Enabled Universal A Security-Enabled Universal Group has been deleted. This could be an indication of malicious
Group was Deleted activity.
More details
Rule ID
windows_security_87
Query
{'selection1': {'EventID': 4758}, 'selection2': {'SubjectUserN
ame': ''}, 'selection3': {'SubjectDomainName': ''}, 'condition
': 'selection1 and not selection2 and not selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Security-Enabled Global A Security-Enabled Global Group has been deleted. This could be an indication of malicious
Group was Deleted activity.
More details
Rule ID
windows_security_127
Query
{'selection1': {'EventID': 4730}, 'selection2': {'SubjectUserN
ame': ''}, 'selection3': {'SubjectDomainName': ''}, 'condition
': 'selection1 and not selection2 and not selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
| TA0003 , T1098 |    |     |     |
| --------------- | --- | --- | --- |
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |
| -------- | ------------- | ---------- | --------------- |
| test     | 2022/05/01    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        