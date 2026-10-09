✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Bitdefender Connectors
A Stellar Cyber Bitdefender connector allows you to Contain hosts (Isolate Endpoints) using an
API call to the Bitdefender server managing those hosts.
Connector Overview: Bitdefender
Capabilities
Collect: No
Respond: Yes
Native Alerts Mapped: Yes
Runs on: DP
Interval: N/A (applies only to Collect)
Collected Data
Bitdefender's API does not support pull of data, so that option is not offered in the Stellar Cyber
Bitdefender connector. For collection, you set up Bitdefender to push data to a Stellar Cyber sensor
configured to ingest httpjson over TLS. (Bitdefender's PUSH event JSON RPC messages are listed in
their online documentation).  The received logs are is ingested to the Syslog index. From there, Stellar
Cyber runs alert integrations and maps certain records (see below) to the Alert Index. A detailed list of
how to locate the ingested event types is provided in the section below on Locating Records.
Domain
<Access URL>
where <Access URL> is a variable from the configuration of this connector
Response Actions
Action Required API
Fields
Contain computer_i https://< Access URL>/api/v1.0/jsonprc/incidents {params}
(Isolate) d or
Host endpointId, where
and endpoint Access URL is the value obtained from your Bitdefender
is type GravityZone Control Center API configuration page.
Parameters are:

Action Required API
Fields
bitdefende endpointId value
r
jsonprc version (2.0)
action to perform (either createIsolateEndpointTask or
createRestoreEndpointFromIsolationTask)
uuid of the request
Example:
https://cloud.gravityzone.bitdefender.com/api/v
1.0/jsonrpc/incidents
with params:
{ "endpointId" : "62ba2eeafb978f545505e687"
},"jsonrpc": "2.0","method":
"createIsolateEndpointTask","id": "301f7b05-
ec02-481b-9ed6-c07b97de2b7b"}'
Third Party Native Alert Integration Details
Of the different record types you can configure to push to Stellar Cyber's httpjson parser, the 11 below are
normalized and enriched as they are added to the Syslog index. The records are evaluated against
existing records in the Alert index. Those that do not already exist are directly and mapped to the XDR
Kill Chain and the Alert Index. For details, see Integration of Third Party Native Alerts.
The other records are run through the ML/SA pipeline, which may generate alerts based on those
algorithms. They are assigned a description of The Bitdefender endpoint agent reported an anomaly
along with the indicated fields below.
Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
Advanced Threat Control 1 module, computer_fqdn, computer_ip, exploit_type e
(ATC)  v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
h
o
st
.i
p,
th
r
e
at
.n
a
m
e
Antiexploit Event  1 module, computer_fqdn, computer_ip, e
detection_threatName v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
th
r
e
at
.n
a
m
e
Antimalware  1 module, computer_fqdn, computer_ip, malware_name e
v
e
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
th
r
e
at
.n
a
m
e
Hyper Detect event  1 module, computer_fqdn, host.ip, malware_name e
v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
p,
th
r
e
at
.n
a
m
e
Sandbox Analyzer 1 module, computerName, computerIp, threatType e
Detection  v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
th
r
e
at
.n
a
m
e
User Control / Content 2 module, computer_fqdn, computer_ip, url e
Control  v
e
nt
.t
y
p
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
u
rl
Data Protection  3 module, computer_fqdn, computer_ip, url e
v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
u
rl
Storage Antimalware  3 module, computer_name, malware_name e
v
e
nt
.t
y
p
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
th
r
e
at
.n
a
m
e
Ransomware activity 4 module, computer_fqdn, computer_ip, attack_source e
detection  v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
sr
ci
p
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
Antiphishing  5 module, computer_name, computer_fqdn, aph_type e
v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
u
rl
Firewall  6 module, computer_name, computer_ip, source_ip e
v
e
nt
.t
y
p
e,
h
o
st
.n
a
m
e,
h
o
st
.i
p,
sr
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly

Bitdefender Event Stellar Bitdefender Fields R
Stellar Cyber Label Cyber ep
TTP* or
te
d
Fi
el
ds
ci
p
*TTP mapping legend
XDR Malware; XDR Misc Malware
Execution; Exploitation for Client Execution
Impact; Data Manipulation
Impact; Data Encrypted for Impact
Initial Access; Phishing
XDR NBA; XDR Firewall Anomaly
Required Credentials and Configurations
To Respond, an Access URL and API key are required from an administrative account in the Bitdefender
GravityZone CLOUD Control Center. The API key must be enabled for the following settings: Network
API, Reports API, Incidents API, Quarantine API, and Event Push Service API. The account must have
licensing that supports Bitdefender's Isolate action .
Locating Records
Use the following fields as a guide to query for records.
Field details
msg_origin.source: bitdefender
 All of the indicated modules contain endpoint data; those that are alert-related are additionally
mapped to the Alert index.
Bitdefender Bitdefender Event / Stellar Stellar Cyber msg_class Stellar Mapped to
Module / Cyber Label Cyber Alert Index
Stellar Cyber msg_origin.
event.type category
adcloud Cloud AD Integration bitdefender_cloud_ad_ endpoint
integration
antiexploit Antiexploit Event bitdefender_antiexplo endpoint yes
it_event
aph Antiphishing bitdefender_antiphish endpoint yes
ing
av Antimalware bitdefender_antimalwa endpoint yes
re
avc Advanced Threat Control bitdefender_advanced_ endpoint yes
(ATC) threat_control
device-control Device Control bitdefender_device_co endpoint
ntrol

Bitdefender Bitdefender Event / Stellar Stellar Cyber msg_class Stellar Mapped to
| Module /      | Cyber Label     |                       | Cyber       | Alert Index |
| ------------- | --------------- | --------------------- | ----------- | ----------- |
| Stellar Cyber |                 |                       | msg_origin. |             |
| event.type    |                 |                       | category    |             |
| dp            | Data Protection | bitdefender_data_prot | endpoint    | yes         |
ection
| endpoint- | Endpoint moved in | bitdefender_endpoint_ | endpoint |     |
| --------- | ----------------- | --------------------- | -------- | --- |
| moved-in  |                   | moved_in              |          |     |
endpoint- Endpoint moved out bitdefender_endpoint_ endpoint
| moved-out |                  | moved_out             |       |     |
| --------- | ---------------- | --------------------- | ----- | --- |
| exchange- | Exchange Malware | bitdefender_exchange_ | email |     |
| malware   | Detection        | malware_detection     |       |     |
exchange- Exchange License Usage bitdefender_exchange_ endpoint
| organization- | Limit Has Been Reached | organization_info |     |     |
| ------------- | ---------------------- | ----------------- | --- | --- |
info
| exchange- | Exchange User | bitdefender_exchange_ | endpoint |     |
| --------- | ------------- | --------------------- | -------- | --- |
| user-     | Credentials   | user_credentials      |          |     |
credentials
| fw  | Firewall           | bitdefender_firewall  | endpoint |     |
| --- | ------------------ | --------------------- | -------- | --- |
| hd  | Hyper Detect event | bitdefender_hyper_det | endpoint | yes |
ect_event
hwid-change Hardware ID Change bitdefender_hardware_ endpoint
id_change
| install | Install Agent | bitdefender_install_a | endpoint |     |
| ------- | ------------- | --------------------- | -------- | --- |
gent
modules Product Modules Status bitdefender_product_m endpoint
odules_status
| network-     | Network Attack Defense | bitdefender_network_a | ndr      |     |
| ------------ | ---------------------- | --------------------- | -------- | --- |
| monitor      | Event                  | ttack_defense_event   |          |     |
| network-     | Sandbox Analyzer       | bitdefender_sandbox_a | endpoint | yes |
| sandboxing   | Detection              | nalyzer_detection     |          |     |
| new-incident | New Incident           | bitdefender_new_incid | xdr      |     |
ent
ransomware- Ransomware activity bitdefender_ransomwar endpoint yes
| mitigation | detection | e_activity_detection |     |     |
| ---------- | --------- | -------------------- | --- | --- |
registration Product Registration bitdefender_product_r endpoint
egistration
storage- Storage Antimalware Event bitdefender_storage_a endpoint yes
| antimalware |     | ntimalware_event |     |     |
| ----------- | --- | ---------------- | --- | --- |
supa-update- Outdated Update Server bitdefender_outdated_ endpoint
| status |     | update_server |     |     |
| ------ | --- | ------------- | --- | --- |

Bitdefender Bitdefender Event / Stellar Stellar Cyber msg_class Stellar Mapped to
| Module /      | Cyber Label            |                       | Cyber       | Alert Index |
| ------------- | ---------------------- | --------------------- | ----------- | ----------- |
| Stellar Cyber |                        |                       | msg_origin. |             |
| event.type    |                        |                       | category    |             |
| sva           | Security Server Status | bitdefender_security_ | endpoint    |             |
server_status
sva-load Overloaded Security bitdefender_overloade endpoint
|             | Server      | d_security_server     |          |     |
| ----------- | ----------- | --------------------- | -------- | --- |
| task-status | Task Status | bitdefender_task_stat | endpoint |     |
us
troubleshootin Troubleshooting activity bitdefender_troublesh endpoint
| g-activity |                      | ooting_activity       |          |     |
| ---------- | -------------------- | --------------------- | -------- | --- |
| uc         | User Control/Content | bitdefender_user_cont | endpoint | yes |
|            | Control              | rol_content_control   |          |     |
| uninstall  | Uninstall Agent      | bitdefender_uninstall | endpoint |     |
_agent
Adding a Bitdefender Connector
To add a Bitdefender connector:
1. Configure Bitdefender API access
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion
Configuring Bitdefender API Access
You must configure obtain the following information from your Bitdefender GravityZone console
before you add the connector in Stellar Cyber:
Access URL
API Key
1. Log in to the Bitdefender GravityZone CLOUD Console as an administrative user.
2. Access your account settings.
3. Locate and save the Access URL information for use in the next section (for example:
https://cloud.gravityzone.bitdefender.com).

Do not include /api at the end of the URL.

4. Select the option to Add an API Key.
5. Create the key with at least these options:
Network API
Reports API
Incidents API
Quarantine API
Event Push Service API
6. Save the API key.
7. Locate the new key in the API keys table and save the value for use in the next section.
Adding the Connector in Stellar Cyber
To add a Bitdefender client connector in Stellar Cyber:
1. Log in to Stellar Cyber.
2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.
3. Click Create and select Connector.
The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.
4. Choose Endpoint Security from the Category dropdown.
5. Choose Bitdefender from the Type dropdown.
The asterisk (*) indicates a required field.
6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.
 Notes:
This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.
8. Choose a Tenant Name. This is the Stellar Cyber tenant allowed to use this connector.
9. Choose the device on which to run the connector.
10. Click Next. The Configuration tab appears.
The asterisk (*) indicates a required field.
11. Enter the Access URL you noted above in Configuring Bitdefender API Access (for
example: https://cloud.gravityzone.bitdefender.com).
 Do not include /api at the end of the URL.
12. Enter the API Key you noted above.
13. Click Next. The final confirmation tab appears.
14. Click Submit.
The new connector is immediately active.
Testing the Connector
When you add (or edit) a connector, we recommend that you run a test to validate the
connectivity parameters you entered. The test validates authentication and connectivity.
 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60
seconds for new or modified configuration details to be propagated to the sensor before
performing a test.
1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.
2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.
 Note that you may run only one test at a time.
Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure
result. A successful test indicates that you entered all of the connector information correctly.
To aid troubleshooting your connector, the dialog remains open until you explicitly close it by
using the X button. If the test fails, you can select the  button from the same row to review and
correct issues.
 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.
Repeat the test as needed.
Display sample messages...
Success ! Failure with summary of issue:
Show More example detail:
If the test fails, the common HTTP status error codes are as follows:
HTTP E HTTP Stan
rror dard Error Explanation Recommendation
Code Name
400 Bad This error occurs when there is an error in the
Did you configure the connector correctly?
Request connector configuration.
401 Unauthorize
This error occurs when an authentication credential is Did you enter your credentials correctly?
d
invalid or when a user does not have sufficient
Are your credentials expired?
privileges to access a specific API.
Are your credentials entitled or licensed for that
specific resource?
403 Forbidden This error occurs when the permission or scope is not
Did you enter your credentials correctly?
correct in a valid credential.
Do you have the required role or permissions for
that credential?
404 Not Found This error occurs when a URL path does not resolve Did you enter your API URL correctly?
to an entity.
429 Too Many
This error occurs when the API server receives too The server or user license/quota will eventually
Requests
much traffic or if a user’s license or entitlement quota recover. The connector will periodically retry the

HTTP E HTTP Stan
rror dard Error Explanation Recommendation
Code Name
is exceeded. query.
If this occurs unexpectedly or too often, work with
your API provider to investigate the server limits,
user licensing, or quotas.
For a full list of codes, refer to HTTP response status codes .
Verifying Ingestion
Use these steps to verify the records related to Bitdefender are in Stellar Cyber:
1. Select Threat Hunting.
The Interflow Search tab appears.
2. Change the Indices to Syslog.
The table immediately updates to show ingested Interflow records.
For Respond actions, refer to Understanding Event Details to understand how work with the
Contain Host feature.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  