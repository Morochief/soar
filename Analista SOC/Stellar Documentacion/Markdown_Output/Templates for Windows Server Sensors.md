✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Templates for Windows Server Sensors
Stellar Cyber provides predefined templates for Windows Server Sensor settings. These
templates have been carefully configured to match common deployment scenarios. Once you
have reviewed the settings in a template and seen how it operates in your environment, you can
tailor the settings in individual channels to fit your needs using the instructions in Configuring
Standard Sensor Profiles
The following templates are available for options in the Windows tab of the ADD/EDIT
SENSOR PROFILE window:
Windows Detect Profile (Low Volume). The selection covers the minimal events
required for all native detections in Stellar Cyber.
Windows Context Profile (Medium Volume). Adds events commonly used by third-
party detection rules.
Windows Compliance Profile (High Volume). Covers all Windows events.
Each of these profiles collects a different set of logs/events and results in a progressively higher
volume of data ingestion from Low to Medium to High.
 If you find that you are ingesting a higher volume of data than you would like relative to your
license limits, you may want to reconfigure these settings, keeping in mind that the Low
Volume profile provides enough coverage for all native Stellar Cyber detections.
The settings for each template are summarized in the table below:
Windo
ws
Note
Channel Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Security
Collect Windows Account
advanced Logon
security audit Events

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
| policy settings |     |     |    |     |    |    |
| --------------- | --- | --- | --- | --- | --- | --- |
Credenti For
| events. |   al | UEB |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- |

|     |   Validatio | A   |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- |
n alert
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     | s.  |     |     |     |     |
|     |     |     |    |     |    |    |
Kerberos For
|     | Authenti | UEB |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- |
cation A

Service alert

s

|     | Kerberos |     |    |     |    |    |
| --- | -------- | --- | --- | --- | --- | --- |

Service

Ticket

Operatio

ns

|     |     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- |
Other

Account

Logon
  Events

|     | Account   |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
|     | Manage    |     |     |     |     |     |
|     | Applicati |     |     |     |     |    |
ment

on
Events

Group

  Manage

  ment

|     |         |     |     |     |     |    |
| --- | ------- | --- | --- | --- | --- | --- |
|     | Compute |    |     |    |     |     |

  r

  Account

Manage

ment

|     |            |     |     |     |     |    |
| --- | ---------- | --- | --- | --- | --- | --- |
|     | Distributi |     |     |     |     |     |
  on
Group

Manage

ment

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
|     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- |
Security   

  Group
  Manage
ment

|     | User |    |     |     |    |
| --- | ---- | --- | --- | --- | --- |

  Account
Manage

ment

|     |       |    |     |    |    |
| --- | ----- | --- | --- | --- | --- |
|     | Other |     |     |     |     |
Account

Manage

ment

Events

|     | Detailed   |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |

Tracking
|     | DPAPI A |    |     |     |    |
| --- | ------- | --- | --- | --- | --- |
|     | Events  |     |    |     |     |
ctivity
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |   PNP |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |
  Activity

|     |   Process | For |     |     |    |
| --- | --------- | --- | --- | --- | --- |
|     |           |    |    |     |     |

|     |   Creation | alert |     |     |     |
| --- | ---------- | ----- | --- | --- | --- |
|     |            | s     |     |     |     |

relat

ed to

proc

ess

creat
|     |     | ion |     |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     | ano |     |     |     |
malie

s.


|     | Process |     |    |     |     |
| --- | ------- | --- | --- | --- | --- |
Terminati

on
|     | RPC Eve |     |     |     |    |
| --- | ------- | --- | --- | --- | --- |
nts

Windo
ws
Note
Channel Windows Detect Profile Windows Context Profile Compli
s
ance
Profile

Token
Right
Adjustm
ent
Events
DS
Access

Detailed
Events
Directory
Service
Replicati
on
Directory   
Service
Access
  
Directory
Service
Changes

Directory
Service
Replicati
on
Logon/L
ogoff

Account
Events
Lockout

User/De
vice
Claims

Group
Member
ship

IPsec
Extende
d Mode

IPsec
Main

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Mode
| IPSec   |     |     |     |    |
| ------- | --- | --- | --- | --- |
Quick
Mode

| Logoff    |     |     |     |     |
| --------- | --- | --- | --- | --- |
| Logon For |     |     |     |    |
|           |    |    |     |     |
UEB
A
alert
s

| Network   |     |     |     |     |
| --------- | --- | --- | --- | --- |
Policy
Server

| Special   |     |     |    |     |
| --------- | --- | --- | --- | --- |
Logon
| Other   |    |     |    |    |
| ------- | --- | --- | --- | --- |
Logon/L
ogoff
Events
Object
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Access

| Applicati   |     |     |     |     |
| ----------- | --- | --- | --- | --- |
Events
on

Generat

ed


| Certificat   |    |    |     |     |
| ------------ | --- | --- | --- | --- |

ion

Services


| Detailed   |    |     |    |     |
| ---------- | --- | --- | --- | --- |

File

Share


| File   |    |    |     |     |
| ------ | --- | --- | --- | --- |

Share

| File   |    |     |     |    |
| ------ | --- | --- | --- | --- |
  
System

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
  
| Filtering   |    |     |    |     |
| ----------- | --- | --- | --- | --- |
Platform
Connecti
on
| Filtering   |     |     |     |    |
| ----------- | --- | --- | --- | --- |
Platform
Packet
Drop

| Handle   |     |     |     |     |
| -------- | --- | --- | --- | --- |
Manipula
tion
| Kernel   |    |    |     |    |
| -------- | --- | --- | --- | --- |
Object

| Registry   |    |    |     |     |
| ---------- | --- | --- | --- | --- |
| Remova     |     |     |     |    |
ble
Storage

| SAM       |     |    |     |     |
| --------- | --- | --- | --- | --- |
| Central   |     |     |     |    |
Access
Policy
Staging
|         |    |    |     |    |
| ------- | --- | --- | --- | --- |
| Other   |     |     |     |     |
Object
Access
Events
Policy
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Change

| Audit   |    |     |     |     |
| ------- | --- | --- | --- | --- |
Events 
Policy

Change


| Authenti   |    |    |     |     |
| ---------- | --- | --- | --- | --- |

cation

Policy

Change

Windo
ws
Note
Channel Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Authoriz   
ation
Policy
Change

Filtering
Platform
Policy
Change

MPSSV
C Rule-
Level
Policy
Change

Other
Policy
Change
Events
Privilege
Use

Events
Non-
Sensitive
Privilege
Use
Sensitive   
Privilege
Use

Other
Privilege
Use
Events
System
Events

IPsec
Driver
Security   
State
Change

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
|     |     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- |
Security   

  System
  Extensio
n

|     | System |    |     |    |     |    |
| --- | ------ | --- | --- | --- | --- | --- |
Integrity

|     | Log |    |     |    |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Clear
|     | Other |    |     |    |     |    |
| --- | ----- | --- | --- | --- | --- | --- |
System
Events
|     | Specify |     |    |     |    |     |
| --- | ------- | --- | --- | --- | --- | --- |
Exclude
|     | Event or | Include Only: |     | Include Only: |     |     |
| --- | -------- | ------------- | --- | ------------- | --- | --- |
IDs
Include 1102, 1104, 4611, 4616, 4624-4625, 1102, 1104, 4611, 4616, 4624-
Only 4648-4649, 4656-4658, 4660-4662, 4625, 4648-4649, 4656-4658,
|     |     | 4663, 4673-4674, 4688, 4768, 4692, |     | 4660-4663, 4672-4674, 4688-4689, |     |     |
| --- | --- | ---------------------------------- | --- | -------------------------------- | --- | --- |
|     |     | 4697-4699, 4701-4702, 4704, 4706,  |     | 4692, 4697-4699, 4701-4702,      |     |     |
|     |     | 4713-4714, 4720, 4722, 4725-4732,  |     | 4704, 4706, 4713-4714, 4718-     |     |     |
|     |     | 4734, 4738, 4741-4743, 4754, 4756- |     | 4720, 4722, 4724-4734, 4738-     |     |     |
|     |     | 4758, 4765-4767, 4769, 4771, 4776, |     | 4743, 4754, 4756-4758, 4765-     |     |     |
|     |     | 4781-4782, 4794, 4799, 4825, 4898- |     | 4767, 4768-4769, 4771, 4776,     |     |     |
|     |     | 4899, 4905, 5030, 5034-5035, 5038, |     | 4781-4782, 4794, 4799, 4825,     |     |     |
|     |     | 5136, 5140, 5145, 5156, 5379,      |     | 4898-4899, 4905, 5030, 5034-     |     |     |
|     |     | 6281, 6416, 6423                   |     | 5035, 5038, 5136, 5140, 5145,    |     |     |
5156, 5379, 6281, 6416, 6423

| System |     |     |    |    |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
Collect Windows
system events.
| Application |     |     |    |    |     |    |
| ----------- | --- | --- | --- | --- | --- | --- |
Collext Windows
application
events.
|           |     |     |    |    |     |    |
| --------- | --- | --- | --- | --- | --- | --- |
| Forwarded |     |     |     |     |     |     |
Events

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Collect Windows
events
forwarded from
other Windows
machines.
| DHCP Client |     |     |    |    |     |    |
| ----------- | --- | --- | --- | --- | --- | --- |
Collect Windows
DHCP client
events
| Windows |     |     |    |    |     |    |
| ------- | --- | --- | --- | --- | --- | --- |
Firewall
Collect Windows
advanced
security firewall
events.
| Windows |     |     |     |     |     |    |
| ------- | --- | --- | --- | --- | --- | --- |
|         |     |    |     |    |     |     |
Defender
|     | Specify   |     |    |     |    |     |
| --- | --------- | --- | --- | --- | --- | --- |
Collect specified
Event
|     |     | Include Only: |     | Include Only: |     |     |
| --- | --- | ------------- | --- | ------------- | --- | --- |
Windows
IDs
|     |     | 1006-1008, 1015, 1116-1119, 2013 |     | 1006-1008, 1013, 1015, 1116-1119, |     |     |
| --- | --- | -------------------------------- | --- | --------------------------------- | --- | --- |
Defender
| events. |     |     |     | 1121, 2013, 5001, 5010, 5012- |     |     |
| ------- | --- | --- | --- | ----------------------------- | --- | --- |
5013, 5101


| Sysmon |     |    |     |    |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
Collect specified
Windows
|     | Specify   |     |    |     |    |     |
| --- | --------- | --- | --- | --- | --- | --- |
sysmon events
Event
|     |     | Include Only: |     | Include Only: |     |     |
| --- | --- | ------------- | --- | ------------- | --- | --- |
for process
|     | IDs | 1, 3, 10, 13 |     | 1, 3, 5, 7-8, 10-13, 15, 17, 20-21, |     |     |
| --- | --- | ------------ | --- | ----------------------------------- | --- | --- |
anomaly
23
detections.


| PowerShell |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- |
|            |     |    |     |    |     |     |
Collect specified
Windows
PowerShell
operational logs.

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile

|     | Specify   |     |    |     |    |     |
| --- | --------- | --- | --- | --- | --- | --- |
Event
|               |         | Include Only: |     | Include Only:          |     |     |
| ------------- | ------- | ------------- | --- | ---------------------- | --- | --- |
|               | IDs     | 4104          |     | 4103-4104, 40961-40962 |     |     |
| FIM           | Not     |               |     |                        |     |     |
| Configure and | enabled |               |     |                        |     |     |
by
enable file
default in
integrity
| monitoring. | any |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
template.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
|     |     |     |     | Support |   |  Contact Us   |    |         |
| --- | --- | --- | --- | ------- | ----------------------- | -------- |