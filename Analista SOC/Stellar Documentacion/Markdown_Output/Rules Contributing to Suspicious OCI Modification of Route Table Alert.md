Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI
Modification of Route Table Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious modification of route tables in OCI. Any one or
more of these will trigger the Suspicious OCI Modification of Route Table Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

OCI Route Table
Created

Identifies when an OCI Route Table has been created for the specified VCN.

Description

More details

Rule ID

oci_audit_5

Query

{'selection1': {'eventName': 'createroutetable'}, 'selection2': {'
status': '200'}, 'condition': 'selection1 and selection2'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1098 

References
N/A

Severity

25

Suppression Logic Based On

oracle.data.resourceId

Title

Description

oracle.data.eventName
stellar.rule_id

Additional Information

Risk
Leve
l

low

Creati
on
Date

2025/0
2/24

Matur
ity

experi
menta
l

False Positives

Routine infrastructure updates or deployments may trigger route
table creation events. To manage this, establish a baseline of
expected behavior during scheduled maintenance windows and
exclude these from alerts.

Automated cloud management tools often create route tables as part
of their operations. Identify these tools and create exceptions for their
known activities to reduce noise.

Development and testing environments frequently undergo changes,
including the creation of route tables. Consider excluding these
environments from alerts or applying a different set of monitoring
rules.

Legitimate changes by authorized personnel can be mistaken for
suspicious activity. Implement a process to verify and document
authorized changes, allowing for quick exclusion of these events
from alerts.

Multi-account setups might have centralized networking teams that
create route tables across accounts. Coordinate with these teams to
understand their activities and exclude them from triggering alerts.

OCI Route Table
Modified or Deleted

Identifies OCI events where a route table has been modified or deleted. Route table can be used by
attackers to disrupt network traffic, reroute communications, or maintain persistence in a compromised
environment.

More details

Rule ID

oci_audit_6

Query

{'selection': {'eventName': ['deleteroutetable']}, 'condition': 's
election'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1098 

References
N/A

Severity

25

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Title

Description

Risk
Level

low

Creati
on
Date

2025/0
2/24

Matur
ity

experi
menta
l

False Positives

Route table modifications are often part of routine administrative
tasks, such as creating new routes, updating associations, or
removing unused resources.

Automated workflows may trigger these events. Verify whether the
source IP matches known automation tools.

Confirm whether these actions align with maintenance activities or
scaling events (e.g., adding or removing subnets).

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

