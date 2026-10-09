✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Firewall Requirements
Several components in the Stellar Cyber product require certain ports and domains be
accessible through your firewall. Use the legend and tables below to understand which are
appropriate for your environment.
Also see: Log Parser Ports.
Legend
CM: Configuration Manager (runs in the DL)
DA: Data Analyzer*
DL: Data Lake*
DP: Data Processor
LAS: Linux Server (Agent) Sensor
MS: Modular Sensor
WAS: Windows Server (Agent) Sensor
*Although these are part of the DP, they have unique IP addresses so are listed independently in the tables below.

General Purpose Ports
| Source | Destination | Port | Protocol Required | Purpose |
| ------ | ----------- | ---- | ----------------- | ------- |
?
| Stellar Cyber | LAS, MS | 22  | TCP Optional | Management access |
| ------------- | ------- | --- | ------------ | ----------------- |
user's SSH client
| Sensors | DNS Server  | 53  | UDP Required | Name service for:                     |
| ------- | ----------- | --- | ------------ | ------------------------------------- |
|         | Environment |     |              | Downloading third-party libraries     |
|         | specific    |     |              | Support of customer configured Active |
Directory
CM communication (if CM is by name
vs IP)
All sensors NTP Server 123 UDP Required Performing time synchronization
Stellar Cyber DL 443 TCP Required Viewing the Stellar Cyber user interface
user's web
browser
WAS, LAS, MS <org>.stellarcybe 443 HTTPS Required Communicating with the CM.
|     | r.cloud |     | with |     |
| --- | ------- | --- | ---- | --- |
The dn-<org>.stellarcyber.cloud port is used
|     |     |     | TLS 1.2 | when fast path communications between |
| --- | --- | --- | ------- | ------------------------------------- |
dn-
|     | <org>.stellarcybe |     |     | sensors and the CM are enabled. This |
| --- | ----------------- | --- | --- | ------------------------------------ |
happens automatically when either a Sensor
r.cloud
CLI session is initiated from the user interface
or a response is configured on the sensor.
WAS, LAS, MS  receiver- 8889 TCP Required Downloading software and files from the DP,
|     | <org>.stellarcybe |     | (HTTPS   | including custom log parsers. |
| --- | ----------------- | --- | -------- | ----------------------------- |
|     | r.cloud           |     | with TLS |                               |
1.2)
WAS, LAS, MS  receiver- 8889 TCP Required Receiver ports for communicating with the
|     | <org>.stellarcybe |     | (HTTPS   | DA  |
| --- | ----------------- | --- | -------- | --- |
|     | r.cloud           |     | with TLS |     |
1.2)
MS with 8080 HTTP Pr Required Must be open for communications between
WAS, LAS, MS
|     | Aggregator |     | oxy | sensor and aggregator. |
| --- | ---------- | --- | --- | ---------------------- |
Enabled
Domains
All of the following domains are required.
| Source | Destination      | Port | Protocol Purpose      |     |
| ------ | ---------------- | ---- | --------------------- | --- |
| MS     | archive.ubuntu.c | 443  | TCP Software updates. |     |
om
80
security.ubuntu.c
om
esm.ubuntu.com
ppa.launchpad.n
et
LAS For Environment TCP Customer configured port for accessing the OS
centos/redhat
specific provider's server (repository) for application updates
servers:

Source Destination Port Protocol Purpose
domains
included
in the
repositor
y
configura
tion files
(/etc/yum
.repo.d/.r
epo)
dl.fedora
project.or
g
mirrors.fe
doraproje
ct.org
LAS For Environment TCP Customer configured port for accessing the OS
SUSE servers: specific provider's server (repository) for application updates
domains
in the
repositor
y
configura
tion files
/etc/zypp/
repos.d/*.
repo
LAS For Ubuntu Environment TCP Customer configured port for accessing the OS
servers: specific provider's server (repository) for application updates
hosts in
the
ubuntu
/etc/apt/s
ource.list
LAS launchpadlibraria 80 TCP Software updates
n.net
LAS http://download. 80 TCP Software updates
webmin.com
Stellar Cyber doc- 443 TCP Accessing online help on the Stellar Cyber
user's web server.stellarcyb documentation server
browser er.ai
Stellar Cyber 443 TCP Dynamically enabling Early Access Program functionality,
https://cli
user's web entsdk- features, and fixes in the Stellar Cyber Platform
browser ld.stellarc
yber.ai
https://cli
entstrea
m-
ld.stellarc
yber.ai
https://ev
ents-
ld.stellarc
yber.ai
WAS live.sysinternals. 443 TCP Optional. Domain is required if the customer wants to
com/sysmon.exe install feature
MS sandbox.stellarc 443 TCP (Optional) Domain is required if the customer wants
yber.ai Malware Sandbox capability
MS Environment Environment TCP (Optional) Customer configured host and port for Tenable
specific specific vulnerability scanning support
Machine with *.oraclecloud.co 443 TCP For download of upgrade packages from Oracle Cloud
User's Browser m Infrastructure.

Connector/Parser-specific
In addition to the general requirements above, review the following for your specific connector
and parser choices:
For any connector, you must also allow access between the sensor (or DP if applicable)
and the API hosts/URLs you specify during configuration.
In most cases, connector communication is over port TCP 443. Connectors with unique
requirements are shown below.
The configuration of firewall rules for connector Collect and Respond functions depends
on the deployment type:
On-premises: For connectors running on the DP, configure the firewall with the DA IP
address for Collect functions and the DL IP address for the Respond functions.
SaaS: The egress IP address used for both Collect and Respond connector functions is
unique to each SaaS instance. To add this address to an allow-list on your perimeter
firewall, contact Stellar Cyber Support to confirm the egress IP address assigned to
your SaaS environment.
For the ports to open for sensors receiving logs from devices on your network see Log
Parser Ports Also, refer to Using the Port Relay Feature to Minimize Open Ports for
information on relaying traffic sent to the generic syslog port to its appropriate vendor-
specific parser.
Source Destination Port Protocol Connector
MS AD Server and LDAP/S: 389 or TCP/UD Active Directory
domain specified 636 (TCP) P
in connector Kerberos: 88 (if
configuration used) (TCP/UDP
)
DP api.barracudanet 443 TCP Barracuda Email server
works.com
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  