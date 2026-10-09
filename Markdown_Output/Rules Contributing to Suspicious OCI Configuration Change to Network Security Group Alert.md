Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI
Configuration Change to Network Security
Group Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious configuration changes to Network Security
Groups in OCI. Any one or more of these will trigger the Suspicious OCI Configuration Change to
Network Security Group Alert. Details for each rule can be viewed by clicking the More Details
link in the description.

Title

Description

OCI Network Security Group
Configuration Change
Detection

Identifies a change to an OCI network security group configuration. A network security group
(NSG) provides virtual firewall rules for a specific set of VNICs in a VCN. A security rule is
one of the items in a NetworkSecurityGroup; it can be for either inbound or outbound IP
packets. Modifying configurations may allow unauthorized access. Threat actors may abuse
this to establish persistence, exfiltrate data, or pivot in an OCI environment.

More details

Rule ID

oci_audit_7

Query

{'selection': {'eventName': ['createnetworksecuritygroup',
'updatenetworksecuritygroup', 'deletenetworksecuritygroup',
 'updatenetworksecuritygroupsecurityrules', 'removenetworks
ecuritygroupsecurityrules']}, 'condition': 'selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

Title

Description

TA0005 , T1562 

References
N/A

Severity

25

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Creati
on
Date

Risk
Leve
l

low

2025/
02/24

Matu
rity

exper
iment
al

False Positives

Network security group modifications may be part of regular
infrastructure maintenance. Verify if this action aligns with
known, scheduled administrative activities.

If you are using automated tools like `Terraform` or
`CloudFormation`, confirm if the change matches expected
configuration drift corrections or deployments.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

