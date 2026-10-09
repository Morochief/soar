Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Sensitive Windows Active
Directory Attribute Modification Alerts

The following rules are used to identify suspicious activity with sensitive Windows Active
Directory attribute modification. Any one or more of these will trigger Sensitive Windows Active
Directory Attribute Modification Alert. Details for each rule can be viewed by clicking the More
Details link in the description.

Windows Events Required: 4742, 5136

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Suspicious LDAP-Attributes Used Detects the usage of particular AttributeLDAPDisplayNames, which are known for data

exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in
companies.

More details

User account exposed to
Kerberoasting

Detects when a user account has the servicePrincipalName attribute modified. Attackers
can abuse write privileges over a user to configure Service Principle Names (SPNs) so that
they can perform Kerberoasting. Administrators can also configure this for legitimate
purposes, exposing the account to Kerberoasting.

More details

Powerview Add-DomainObjectAcl
DCSync AD Extend Right

Backdooring domain object to grant the rights associated with DCSync to a regular user or
machine account using Powerview\Add-DomainObjectAcl DCSync Extended Right cmdlet,
will allow to re-obtain the pwd hashes of any user/computer

Possible Shadow Credentials
Added

Potential Shadow Credentials
added to AD Object

More details

Detects possible addition of shadow credentials to an active directory object.

More details

Identify the modification of the msDS-KeyCredentialLink attribute in an Active Directory
Computer or User Object. Attackers can abuse control over the object and create a key
pair, append to raw public key in the attribute, and obtain persistent and stealthy access to
the target user or computer object.

Title

Description

More details

AdminSDHolder Backdoor

Detects modifications in the AdminSDHolder object. Attackers can abuse the SDProp
process to implement a persistent backdoor in Active Directory. SDProp compares the
permissions on protected objects with those defined on the AdminSDHolder object. If the
permissions on any of the protected accounts and groups do not match, the permissions
on the protected accounts and groups are reset to match those of the domain's
AdminSDHolder object, regaining their Administrative Privileges.

More details

Possible DC Shadow Attack

Detects DCShadow via create new SPN

More details

Modification of the
msPKIAccountCredentials

Identify the modification of the msPKIAccountCredentials attribute in an Active Directory
User Object. Attackers can abuse the credentials roaming feature to overwrite an arbitrary
file for privilege escalation. ms-PKI-AccountCredentials contains binary large objects
(BLOBs) of encrypted credential objects from the credential manager store, private keys,
certificates, and certificate requests.

More details

Windows AD SID History Attribute
Modified

Detects modifications to the SID History attribute in Active Directory. This detection
identifies changes to the sIDHistory attribute which can be exploited by adversaries to
inherit permissions from other accounts, potentially granting unauthorized access. If
confirmed malicious, this activity could allow attackers to maintain persistent access and
escalate privileges within the domain, posing a significant security risk.

More details

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

