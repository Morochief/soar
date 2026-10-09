✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Using the Response Tab in the Case Details
View
The Case Details Response tab is where you take action on a case based on your triage and
analysis in the Detection and Analysis tabs. Stellar Cyber automatically recommends actions to
you based on the case's specifics and the connectors providing data for the observables in the
case. For example, if a firewall provided the data for a host in your case, the Response tab
typically includes a Block IP action for that host.
The figure below summarizes the main features of the Response tab:
Keep in mind the following when using the Response tab:
The actions available in the Response tab depend on the connectors providing data for
the observables in the case. As described below, different connectors provide different
response actions depending on their configuration and the data seen.
 Because of this, the recommended actions provided by Stellar Cyber can and will
vary from case to case.
If multiple Case Actions are listed, you can use the Search actions field to locate the
one you're looking for.
If multiple connectors contributed data to a case, Stellar Cyber intelligently selects the
connector that is most relevant to the target of your Case Action.
Stellar Cyber prepopulates the configuration wizards for case actions with the data
corresponding to the case. For example, when configuring a Block IP action, the IP
drop-down list automatically lists just those IP addresses associated with the case. You

can always type in your own address, but the most relevant ones are already listed for
you.
Once you've submitted an action, you can keep track of feedback for the action in the
Automation | Action History pages.
The standard Identification, Evidence Locker, and Case Activity panels all remain
persistent in the Response tab.
Recommended Actions in the Response Tab
When AI Case Analysis is enabled in Global Settings, you can run AI Case Analysis to accelerate
investigations with AI-generated narratives, insights, and suggested incident responses in the
Detection, Analysis, and Response tabs in the Case Detail view.
After running AI Case Analysis on a case, the Response tab in the Case Detail view provides
case-specific guidance for containment and investigation. As shown in the figure below, this
guidance helps you move quickly from analysis to action with recommendations tailored to the
specific case:
Recommendations in the Response tab can include:
Immediate Attention – High-priority entities such as accounts, hosts, or IPs that require
urgent focus.
Validation Steps – Actions to confirm or disprove the working hypothesis (e.g., audit
account activity, verify credential use).
Recommended Investigations – Follow-up steps such as forensic analysis, timeline
reviews, or enhanced monitoring of suspicious sources.
Next Steps with AI Case Analysis
To return to the case's high-level summary, you can click on the Detection tab.
To explore analytical details for the case, see the Hypothesis, Timeline, and
Observables panels in the Analysis tab.
Available Case Actions
This section lists the possible Case Actions together with the information necessary to configure
them. In general, the available Case Actions are the same as the External Actions found in Event
Details displays.
 Refer to Case Actions by Connector for details on which connectors are required for
different Case Actions.

Block IP
You can immediately respond to a case by creating a new firewall rule:
1. From the Case Response tab, select Block IP.
2. The Action Parameters | Block IP section appears.
 To add a new firewall or switch, see Configuring Connectors.
3. Choose the IP address to be blocked.
The drop-down list contains all addresses associated with the case.
4. Choose the connector you want to use to perform the action.
Stellar Cyber automatically attempts to select the best connector for the IP address.
5. Set the Direction:
For all firewalls, select Incoming, Outgoing, or Any.
When Incoming is selected, an Inbound firewall rule is created to
match the Source IP address.
When Outgoing is selected, an Outbound firewall rule is created to
match the Destination IP address.
If you select a Security Switch, the Direction setting is not applicable.
 These actions are reported in Automation | Action History | Security
Switch actions.
6. Choose a Duration.
You can choose Minutes, Hours, Days, or even Forever.
7. Select Submit.
The new firewall rule is submitted to the firewall.
8. The status is reported in the Firewall Actions tab on the Action History page
(Automation | Action History | Firewall Actions).

 For Firewall actions, if you block an IP host that is already blocked or if you unblock
an IP host that is already unblocked, the action is marked as Succeeded. You can
view status details in the Status Message.
Disable User
You can immediately respond to a case by disabling a user:
1. From the Case Response tab, select Disable User.
The Action Parameters | Disable User section appears.
2. Choose which user to disable.
Depending on the case, you might have only one option.
3. Choose the Connector.
4. Set the Duration.
You can choose Minutes, Hours, Days, or even Forever.
5. Select Submit.
The user is immediately disabled.
 To enable a user after disabling, visit the User Actions tab (Automation | Action History |
User Actions) to revert the disable action.
Run a Script
You can immediately respond to a case by running a saved script or creating a new script:
1. From the Case Response tab, select Run a Script.
The Action Parameters | Run a Script section appears.
2. Choose the Target remote host from the drop-down list.
The connection information is automatically filled in. The dropdown also includes the
option to add a new remote host. If needed, select "create new remote host" as the
target:
Specify the host name, address, port to connect to and the user credentials.

Specify whether to run the script on the Data Processor or a device sensor.
Note that the host is saved
3. Choose a script to execute from the drop-down list.
The script is automatically added to the Script Body field. To create a new saved script,
see Creating a New Script.
You can also choose Custom and create a new script.
This new script will not be saved.
4. Select Submit.
The script is executed.
The script action appears in the Script Actions tab on the Action History page (Automation |
Action History | Script Actions).
Contain Host
You can immediately contain (lock down or isolate) a host managed by certain services such as
Bitdefender, Cynet, Cybereason, BlackBerry Cylance, SentinelOne, CrowdStrike Falcon, or
Microsoft Defender for Endpoint. You must have previously configured a connector to that service
in order to perform this action.
1. From the Case Response tab, select Contain Host.
The Action Parameters > Contain Host section appears.
2. Choose the Target.
This menu option allows you to specify the source or destination host associated with
the event as the host you want to isolate or lock down. For Cybereason connectors, the
Target Value is automatically populated with the ID of the Cybereason sensor. For all
other connectors, the value is the IP address or MAC ID of that host.
The Connector field is automatically filled in with the connector that manages the
chosen host.
3. Choose a Duration.
4. Select Submit.
The Contain Host action is reported in the Endpoint Actions tab (Automation | Action
History | Endpoint Actions).
 Depending on the originating connector, you may be able to revert a host containment from
Stellar Cyber. If this is supported, a Revert button is displayed in the row for the containment
action of the Automation | Action History | Endpoint Actions table. For supported connectors,
using Revert triggers a Lift Containment action that is displayed in the same table. If the

API for the managing service does not support a revert option then you need to use that
product's UI to manage the host state.
 Blackberry Cylance connector's Contain Host action automatically expires upon the
requested duration but this action is not reported back to Stellar Cyber. The Endpoint Actions
table reports that the containment was successful, but not expired.
 If you use a Cynet connector to perform a response action on a host that is not in your Cynet
list of hosts, the Automation | Action History | Endpoint Actions row for the action will indicate
that with an error message such as: The remote server returned an
error: (422) Unprocessable Entity.
Hide Host
The Hide Host response for CrowdStrike Falcon is not available from Case Management. It is still
available from Event Details.
Disconnect Host
You can immediately disconnect a host managed by SonicWall Capture:
1. From the Case Response tab, select Disconnect Host.
The Action Parameters > Disconnect Host section appears.
2. Choose your SonicWall Capture service from the drop-down list.
You can add a SonicWall Capture connector from System | INTEGRATIONS |
Connectors.
3. Choose a Duration.
4. Select Submit.
The host is disconnected from the network.
The action appears in the Endpoint Actions tab on the Action History page (Automation | Action
History | Endpoint Actions).
Initiate Scan
You can immediately scan an asset managed by SonicWall Capture or SentinelOne.
1. From the Case Response tab, select Initiate Scan.
The Action Parameters > Initiate Scan section appears.
2. Choose the target (asset, device, or agent) from the available list.
The Connector field is automatically filled in based on the chosen target.

3. Select Submit.
A vulnerability scan of your selection is triggered immediately from the service
associated with your connector.
The action appears in the Endpoint Actions page tab on the Action History page (Automation |
Action History | Endpoint Actions).
Restart Machine
You can immediately restart a host managed by SonicWall Capture:
1. From the Case Response tab, select Restart Machine.
The Action Parameters > Restart Machine Configuration section appears.
2. Choose your SonicWall Capture service from the dropdown.
You can add a SonicWall Capture connector from System | INTEGRATIONS |
Connectors.
3. Select Submit.
The host is immediately restarted.
The action appears in the Endpoint Actions tab on the Action History page (Automation | Action
History | Endpoint Actions).
Shutdown Host
You can immediately shut down a host managed by SonicWall Capture or Cynet:
1. From the Case Response tab, select Shutdown Host.
The Action Parameters > Shutdown Configuration section appears.
2. Specify the target device on which you want to perform the action.
The Connector field is automatically filled in based on the chosen target.
3. Select Submit.
The host is immediately shut down.
The action appears in the Endpoint Actions tab on the Action History page (Automation | Action
History | Endpoint Actions).
Update Device
You can upload JSON to run actions on a device known to a Forescout connector:
1. From the Case Response tab, select Update Device.
The Action Parameters > Update Device section appears.
2. Select the Target on which you want to run the Forescout connector update action.
The target can be one of these: Source Host, Destination Host, Source MAC, or
Destination MAC.
The Connector field is automatically filled in based on the chosen target.
3. If your connector was created with default JSON, customize it now or skip this step.

Populate the JSON field with the action you want the connector to transmit to the
Forescout app configured in the beginning of this procedure. Note that Stellar Cyber
verifies general format of the JSON, not the logic. Following is an example based on
ActionAPI-supported JSON properties:
{
"connect_actionapi_vlan_assign":true,
"connect_actionapi_vlan_assign_id":"vlan233"
}

Do not include the IP or MAC address, as that is added automatically based on
your selection in the previous step. The JSON that is transmitted to Forescout will
include the IP or MAC and the property tag, similar to the sample below.
{
"mac":"009027390a7c",
"properties":{
"connect_actionapi_vlan_assign":true,
"connect_actionapi_vlan_assign_id":"vlan233"
}
}
Refer to Forescout documentation for supported fields and syntax details.
4. Select Submit.
The connector runs the update action one time.
Kill Threat
For assets managed by a SentinelOne service, if you have configured your connector for
Respond actions, you can use this action to kill a threat.
1. From the Case Response tab, select Kill Threat.
The Action Parameters > Kill Threat section appears.
2. Then select the Target from the available list that is populated based on your connector
selection.
The Connector field is automatically filled in based on the chosen target.
3. Select Submit.
A kill threat signal on the target is immediately triggered from the SentinelOne service
associated with your connector.
The action appears in the Endpoint Actions tab on the Action History page (Automation | Action
History | Endpoint Actions).
Quarantine Threat
For assets managed by a SentinelOne service, if you have configured your connector for
Respond actions, you can use this action to quarantine a threat.

1. From the Case Response tab, select Quarantine Threat.
The Action Parameters > Quarantine Threat section appears.
2. Choose the Target from the drop-down menu.
The Connector field is automatically populated based on the chosen target.
3. Use the duration fields to specify the length of time to put the target in quarantine.
4. Select Submit.
A quarantine on the target is immediately triggered from the SentinelOne service
associated with your connector.
The action appears in the Endpoint Actions tab on the Action History page (Automation | Action
History | Endpoint Actions).
Remediate Threat
For assets managed by a SentinelOne service, if you have configured your connector for
Respond actions, you can use this action to remediate a threat.
1. From the Case Response tab, select Remediate Threat.
The Action Parameters > Remediate Threat Configuration section appears.
2. Choose the Target from the drop-down list.
The Connector field is automatically populated based on the chosen target.
3. Select Submit.
A remediation signal on the target is immediately triggered from the SentinelOne service
associated with your connector.
The action appears in the Endpoint Actions tab on the Action History page (Automation | Action
History | Endpoint Actions).
Remediate Email
For deployments integrated with the Barracuda Email Security Service, you can use Stellar
Cyber to create an incident in a Barracuda Forensics And Incident Response system.
1. From the Case Response tab, select Remediate Email.
The Action Parameters > Create Remediate Email section appears with some
sections pre-populated from the JSON associated with the selected event.
2. Choose the applicable connector from the drop-down menu.
3. Optionally, specify whether to search for the email in previously Quarantined and Sent
categories.

4. Specify which remediation actions to perform on the Barracuda response system.
Message Actions: Select None, Delete, or Quarantine.
Enable continuous quarantine: (Visible only when the message action is set
to Delete or None) Select this option to request that the action continue for 72
hours after the initial remediation has completed.
Notify: Select this option to also send a warning email alert to the affected
user.
Send summary: Select this to copy an incident summary to the configured
security team.
5. Select Submit.
An incident is sent to the Barracuda Forensics And Incident Response associated
with your connector.
The action appears in the Email Actions tab on the Action History page (Automation | Action
History | Email Actions).
Case Actions by Connector
The available Case Actions depend on the connectors providing data on the observables in the
case.
The following table indicates which connector respond actions are applicable for each external
action, along with the requirements to enable that action. Specifically, certain connectors must be
configured and the indicated fields in the Interflow must contain non-null, valid data.
E
x
t
e
r
n Applicable
Connector and Data Requirement*
a Connector
for Action Availability
l s
A
c
ti
o
n
Bl AWS, Azure
At least one firewall or security switch connector is configured and required fields are populated dstip or
o NSG,
srcip
c
k
Barracuda
I
Firewall,
P
Check
/
Point,
Bl
Check Point

o Smart-1
c Cloud
k
o
,
n
Cisco FMC,
Fi
Cisco
re
Meraki, F5
w
BIG-IP
al
ASM, F5
l
BIG-IP
Firewall, F5
Silverline,
Fortigate,
FortiManag
er
,
HanDreamn
et Security
Switch, Hills
tone, Palo
Alto
Networks
Firewall,
Palo Alto
Networks
Panorama,
SonicWall
Firewall,
Sophos XG
Firewall,
Stormshield
Network
Security
(SNS) Fire
wall
, Versa
Networks
Firewall
D
Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field userPrincipalName Active
is
Directory,
a
Microsoft

| bl  |     | Entra ID   |
| --- | --- | ---------- |
| e   |     | (formerly  |
| U   |     | Azure      |
| s   |     | Active     |
| er  |     | Directory) |
C
Microsoft Entra ID (formerly Azure AD) connector required field Microsoft
o
Entra ID
| msg_class of Content Type | User ID on Which to Perform Action |     |
| ------------------------- | ---------------------------------- | --- |
nf
(formerly
| ir azure_ad_audit | initiatedBy.user.id |     |
| ----------------- | ------------------- | --- |
Azure
| m azure_ad_signin | userId |     |
| ----------------- | ------ | --- |
Active
C
| azure_ad_risk_detection | userId | Directory) |
| ----------------------- | ------ | ---------- |
o
| azure_ad_risky_user | azure_ad.id |     |
| ------------------- | ----------- | --- |
m
| user_profile | user_profile.id |     |
| ------------ | --------------- | --- |
pr
o
m
is
e
d
D
Microsoft Entra ID (formerly Azure AD) connector required field Microsoft
is
Entra ID
m msg_class of Content Type User ID on Which to Perform Action
(formerly
| is azure_ad_audit | initiatedBy.user.id |     |
| ----------------- | ------------------- | --- |
Azure
s
| azure_ad_signin | userId | Active |
| --------------- | ------ | ------ |
R
| azure_ad_risk_detection | userId | Directory) |
| ----------------------- | ------ | ---------- |
is
| azure_ad_risky_user | azure_ad.id |     |
| ------------------- | ----------- | --- |
k
| user_profile | user_profile.id |     |
| ------------ | --------------- | --- |
R
Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field  user_id and group_id Microsoft
e
Entra ID
m
(formerly
o
Azure
v
Active
e
Directory)
U
s
er
fr
o
m
G
ro
u
p

R
Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field userPrincipalName Microsoft
e
Entra ID
v
(formerly
o
Azure
k
Active
e
Directory)
E
xi
st
in
g
Si
g
n-
In
S
e
s
si
o
n
s
A
Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field user_id and group_id Microsoft
d
Entra ID
d
(formerly
U
Azure
s
Active
er
Directory)
to
G
ro
u
p
R Always available SSH Host
u
n
a
S
cr
ip
t
C
One of the following connectors is configured. The required data varies based on connector to be used for Bitdefender,
o
response. CrowdStrik
nt
e,
Bitdefender required fields One of bitdefender.computer_id or bitdefender.endpointId
ai
Cybereason
n CrowdStrike required fields dstip or srcip or hostip

| H Cybereason required fields |  cybereason.pylumId   | , Deep    |
| ---------------------------- | --------------------- | --------- |
| o                            |                       | Instinct, |
Cylance required fields
device and device.deviceID or
| st  |     | BlackBerry |
| --- | --- | ---------- |
cylance and one of cylance.device_id or srcmac or dstmac or ( host and host.mac)
| (I  |     | Cylance, |
| --- | --- | -------- |
Cynet required fields  are any value other than an IP Address in at least one of these: hostip_host,
| s srcip_host, computer_name or host.name |     | Cynet,    |
| ---------------------------------------- | --- | --------- |
| ol                                       |     | Microsoft |
Deep Instinct:  required fields
deep_instinct_asset and deep_instinct.id or
| at  |     | Defender |
| --- | --- | -------- |
deep_instinct_suspiciousevent and deep_instinct.device_id or
e deep_instinct_maliciousevent and deep_instinct.device_id for
| E   |     | Endpoint, |
| --- | --- | --------- |
Microsoft Defender for Endpoint required fields  microsoft_defender.id and
microsoft_defender.machineId
| n   |     | SentinelOn |
| --- | --- | ---------- |
d SentinelOne required fields sentinelone and sentinelone.agentRealtimeInfo and e, Sophos
sentinelone.agentId
| p   |     | Central, |
| --- | --- | -------- |
Sophos Central required fields  sophos.hostip_assetid
| oi  |     | VMware |
| --- | --- | ------ |
VMware Carbon Black Cloud required fields  device_id
| nt  |     | Carbon    |
| --- | --- | --------- |
| )   |     | Black     |
| Is  |     | Palo Alto |
Palo Alto Networks CORTEX XDR required fields endpoint_id
| ol  |     | Networks |
| --- | --- | -------- |
| at  |     | CORTEX   |
| e   |     | XDR      |
E
n
d
p
oi
nt
| H                                                    |     | CrowdStrik |
| ---------------------------------------------------- | --- | ---------- |
| CrowdStrike required fields dstip or srcip or hostip |     |            |
| id                                                   |     | e          |
e
H
o
st
U
Forescout required fields srcip, dstip, srcmac, dstmac Forescout
p
d
at
e
D
e
vi
c
e
In
SentinelOne required fields sentinelone.agentRealtimeInfo and sentinelone.agentId SentinelOn
iti
e,
SonicWall Capture Client required fields device.deviceId and device.InstallToken
at
SonicWall
e

S Capture
c Client
a
n
Ki SentinelOne required fields msg_origin.source is 'SentinelOne_endpoint' or msg_origin.source SentinelOn
ll e
is SentinelOne and the following fields are present and valid: sentinelone.threatInfo,
T
sentinelone.threatInfo.threatId
hr
e
at
Q SentinelOne required fields msg_origin.source is 'SentinelOne_endpoint' or msg_origin.source SentinelOn
u e
is SentinelOne and the following fields are present and valid: sentinelone.threatInfo,
ar
sentinelone.threatInfo.threatId
a
nt
in
e
T
hr
e
at
R SentinelOne required fields msg_origin.source is SentinelOne_endpoint or msg_origin.source is SentinelOn
e e
SentinelOne and the following fields are present and valid: sentinelone.threatInfo,
m
sentinelone.threatInfo.detectionType, sentinelone.threatInfo.threatId and
e
sentinelone.threatInfo.detectionType is dynamic
di
at The endpoint must also be either a Mac OS or Windows host. if it is not, then a Quarantine is performed instead
e
T
hr
e
at
D SonicWall
SonicWall Capture Client required fields device.deviceId and device.InstallToken
is Capture
c Client
o
n
n
e
ct
H
o
st
R SonicWall Capture Client required fields device.deviceId and device.InstallToken SonicWall
e Capture

st Client
ar
t
M
a
c
hi
n
e
S SonicWall Capture Client required fields device.deviceId and device.InstallToken SonicWall
h Capture
Cynet required fields are any value other than an IP Address in at least one of these: hostip_host,
ut Client,
srcip_host, computer_name or host.name.
D Cynet
o
w
n
(
S
h
ut
d
o
w
n
H
o
st
)
R Barracuda Email Security Service required fields barracuda.account_id and barracuda.subject Barracuda
e and barracuda.env_from and barracuda.hdr_from Email
m Security
e
di
at
e
E
m
ai
l
W N/A Universal
e Webhook
b Responder,
h ESET
o Responders

o
k
,
WithSecure
Elements
(Respond)
,
BlackBerry
Cylance
(Respond)
,
WatchGuar
d Firebox
Responder
, Acronis
Cyber
Protect
Cloud
(Respond)
, Proofpoint
on Demand
(Respond)
, Netskope
(Respond),
, Trend
Micro
Vision One
(Respond)
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  