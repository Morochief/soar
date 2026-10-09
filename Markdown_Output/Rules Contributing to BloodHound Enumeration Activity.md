Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to BloodHound Enumeration
Activity

The following rules are used to identify potential domain enumeration activity from BloodHound
or other Active Directory data collection tools. Any one or more of these will trigger the
BloodHound Enumeration Activity Alert. Details for each rule can be viewed by clicking the More
Details link in the description.

Title

Description

BloodHound
Enumeration Activity

Detects unusual LDAP search requests, which can be potential domain enumeration activity from
BloodHound or other Active Directory data collection tools.

More details

Rule ID

network_security_14

Query

{'selection_search': {'metadata|contains': ["'message_type': 3"]},
'selection_generic': {'metadata|contains': ['(grouptype:1.2.840.113
556.1.4.803:=2147483648)', '(grouptype:1.2.840.113556.1.4.803:=2147
483656)', '(grouptype:1.2.840.113556.1.4.803:=2147483652)', '(group
type:1.2.840.113556.1.4.803:=2147483650)', '(samaccounttype=8053063
69)', '(samaccounttype=805306368)', '(samaccounttype=536870913)', '
(samaccounttype=536870912)', '(samaccounttype=268435457)', '(samacc
ounttype=268435456)', '(objectcategory=grouppolicycontainer)', '(ob
jectcategory=organizationalunit)', '(objectcategory=computer)', '(o
bjectcategory=ntdsdsa)', '(objectcategory=server)', '(objectcategor
y=domain)', '(objectcategory=person)', '(objectcategory=group)', '(
objectcategory=user)', '(objectclass=trusteddomain)', '(objectclass
=computer)', '(objectclass=server)', '(objectclass=group)', '(objec
tclass=user)', '(primarygroupid=521)', '(primarygroupid=516)', '(pr
imarygroupid=515)', '(primarygroupid=512)', 'objectguid=', '(schema
idguid=']}, 'selection_dn_enum': {'metadata|contains': ['cn=domain
admins', 'cn=enterprise admins', 'cn=group policy creator owners']}
, 'selection_allobject': {'metadata|contains': ["'filter': '(object
class=*)'"]}, 'selection_suspicious': {'metadata|contains': ['(user
accountcontrol:1.2.840.113556.1.4.803:=4194304)', '(useraccountcont
rol:1.2.840.113556.1.4.803:=2097152)', '!
(useraccountcontrol:1.2.840.113556.1.4.803:=1048574)', '(useraccoun

Title

Description

tcontrol:1.2.840.113556.1.4.803:=524288)', '(useraccountcontrol:1.2
.840.113556.1.4.803:=65536)', '(useraccountcontrol:1.2.840.113556.1
.4.803:=8192)', '(useraccountcontrol:1.2.840.113556.1.4.803:=544)',
 '!(useraccountcontrol:1.2.840.113556.1.4.803:=2)', 'msds-
allowedtoactonbehalfofotheridentity', 'msds-
allowedtodelegateto', 'msds-
groupmanagedserviceaccount', '(accountexpires=9223372036854775807)'
, '(accountexpires=0)', '(admincount=1)', 'ms-mcs-
admpwd']}, 'filter_generic': {'metadata|contains': ['(domainsid=',
'(objectsid=', '(cn=']}, 'condition': 'selection_search and (((sele
ction_generic or (selection_dn_enum and selection_allobject)) and n
ot filter_generic) or selection_suspicious)'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0007 , T1482 , T1087.002 , T1069.002 

References

https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ldap/win_ldap_recon.ym
l 

https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/hunting-for-
reconnaissance-activities-using-ldap-search-filters/ba-p/824726 

https://github.com/PowerShellMafia/PowerSploit/blob/d943001a7defb5e0d1657085a77a0e78
609be58f/Recon/PowerView.ps1 

https://github.com/BloodHoundAD/SharpHound3/blob/7d96b991b1887ff50349ce59c80980bc
0d95c86a/SharpHound3/LdapBuilder.cs 

https://medium.com/falconforce/falconfriday-detecting-active-directory-data-collection-0xff21-
c22d1a57494c 

https://github.com/fox-
it/BloodHound.py/blob/d65eb614831cd30f26028ccb072f5e77ca287e0b/bloodhound/ad/domai
n.py#L427 

https://ipurple.team/2024/07/15/sharphound-detection/ 

Severity

74

Suppression Logic Based On

srcip
dstip
stellar.rule_id

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2024/10/28

high

False Positives

LDAP search requests sent by legitimate tools or
services

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

