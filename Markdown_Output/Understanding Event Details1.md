Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Understanding Event Details

One of the most fundamental and useful tools in Stellar Cyber is the Event Details panel which provides
analysis on the event, options to perform assorted actions, and access to the Interflow record. This panel
can be accessed anywhere a table of events is found. You can access these event tables from assorted
locations as follows:

Threat Hunting includes a table of events.  Select a row of interest, and then click More Info to
display the Event detail panel.

Cases includes a table of associated alerts; locate an alert and click the More Info button.

Alerts is a table of all discovered alerts, organized by type. Select an alert type of interest, then
click the View button to display a page with charts and a table of the events. As above, click
More Info to display details on the individual event.

Click More Info to view a panel with information on the selected event. The panel is organized into three
sections:

A header on top

A menu for different event details

A panel to display the selected menu item

Use the information below to understand how to use the Event Details display:

Header
Key Fields
Cases
Details
JSON
Actions
Action History
Rules
Related Events
InSyncs

Header Section
The first section provides a high-level summary of the event, with analysis. Note that some components
appear only if they are relevant to the type of data record being displayed.

Example 1:

Example 2:

Alert Type – The name of the alert type is displayed, along with a help button linking to more
information about that alert type.

Link to Knowledge Base Description – To the right of the alert name, click the  button to view
the alert type details.

Forwarding Link – To the right of the alert name, click the forwarding link button to copy a direct
URL to access this detail page independently of the event list.

Alert Subtype – The name of the alert subtype, if any.

Date/Time – This is the date and time the event occurred.

Kill Chain Categorization – When applicable for the selected event, the following are populated
(Refer to:Understanding the XDR Kill Chain for more detail on these attributes).

Stage

Tactic: If there are many tactics, click Show More to expand the list or Show Less to
collapse it.

Technique: If there are many techniques, click Show More to expand the list or Show
Less to collapse it.

Sub-technique: If there are many sub-techniques, click Show More to expand the list
or Show Less to collapse it.

Alert description – A description of the alert type is also provided. For alerts generated based
on Stellar Cyber's Machine Learning model, details specific to the event are embedded in this
description, to aid in interpretation. If the description is long, click More to expand the description
or Less to collapse it.

Alert Score – This number appears in a circle that is color-coded for severity, to match its
position on the kill chain. The higher the score, the more important it is. The score is also based
on Stellar Cyber's Machine Learning model, which compute the Fidelity, Severity, and Threat Intel
scores that contribute to this overall score.

Machine Learning – This orange rectangular block is displayed for events other than raw data or
straightforward traffic events. Alert types handled by Stellar Cyber Machine Learning may include
this block to highlight key triggers, such as actual versus typical, that contributed to the alert
scoring. Note the difference in key triggers illustrated in the example images above.

The remaining fields in this block are additional attributes produced through Machine Learning,
that contribute to the overall scoring:

Fidelity– our confidence in our analysis. The higher the Fidelity Score, the higher our
confidence that we correctly observed a malicious event. If this is high, it drives the Alert

Score higher. If this and the Threat Intel score are low, they reduce the Alert Score.
Severity– the importance of the category of the event. The higher the Severity Score,
the more dangerous the possible consequences of the event. In general, later-stage
events have a higher severity.
Threat Intel – the reputation of the IP addresses and URLs as assessed by the threat
intel sources. The higher the Threat Intel Score, the worse the reputation. If this is high,
it drives the Alert Score higher. If this and the Fidelity Score are low, they reduce the
Alert Score.
Data Period – This is the duration of the observed event, which affects analysis of
anomalous events (it is not the duration of the event itself).

Event Status – Use this drop down to assign an operational status to the event. The options
include:

New – Observed but no action has yet been taken.

In Progress – Investigations involving this event are being conducted.

Ignored – It has been determined that no further investigation with regard to this event
are needed.

Closed – All investigations have been concluded.

Assignee – If there is an assigned user.

Tags – If a user has assigned tags to the event, the tags appear in this section. (You can add
tags in the Actions section, described next.)

Rule-Based Alerts Link to Knowledge Base

To get the Knowledge Base description for rule-based alerts, in the Key Fields, click the Stellar Rule ID
link, for example, powershell_scriptblock_151.

See Rule-Based Alert Details for additional information on rule-based alerts.

Key Fields
This section summarizes additional essential information regarding an event. Most of the information is
related to the source and the destination of the network packet that generated this event.

For details on Key Fields, see Key Fields for Alert Types.

The Key Fields includes a global map on which the geolocation of the source and destination IP
addresses are plotted with a connecting arc. For applicable alerts such as User Login Location Anomaly,
the map includes data points for the closest typical login locations of that user.

 If an IP address does not have corresponding geolocation information, it displays unknown or empty.

Important other information that may be included in this section:

Tenant – the tenant associated with the sensor
Sensor – the sensor device that collected the event data
Username – the user name associated with this event
Src Username – the user name that Stellar Cyber associates with the source IP address
Dst Username – the user name that Stellar Cyber associates with the destination IP address
Src Reputation – reputation of the source host
Dst Reputation – reputation of the destination host

 Only key fields with values are displayed.

To help explain the different user names, if you log in to Admin A's computer with Admin B's credentials,
they will be:

Username – Admin B
Src Username – You
Dst Username – Admin A

See Reputation Definitions for definitions of the values in the Src Reputation and Dst Reputation fields.

When you open Event Details from alerts based on correlated events, links to the raw data are also
provided in this section. Click the link to open a window displaying the raw data for the corresponding
event (the example below shows two events - recent domain and email traffic that were correlated to
trigger an alert). In this case the alert was Possible Phishing Site Visit from Email.

Certain fields, as illustrated below, allow operations on fields such as URL, host, user names, and
IP addresses. In this section, fields that allow actions are indicated with the more button  to the right of
the field value. Click the button to display the list of available actions, described in: Performing Field
Actions.

Cases
Cases associated with the event are listed here in descending order by score, up to a maximum of five.
Typically, only one or two cases are associated with a given alert. Use the Cases list as follows:

Click the View All (x) link at the upper right of the list to open a new tab with a filtered view of the
Cases summary page showing just those cases associated with the selected alert.

Click an individual case's entry in the list to open its associated Case details page.

 The Cases tab in the Event Details display is not affected by the value specified for the Minimum
Number of Alerts display filter in the Global Case Settings. The Cases tab shows all associated
cases, regardless of the number of alerts for the case.

Details
The Details menu option lists the Interflow object in table form. Refer also to the Metadata Dictionary or
the Metadata Dictionary Subset.

In the Details, there are tooltips on the icons when you hover over them showing their type, that is, if they
), as well as highlighting on the icons showing the fields that are
are a number (

), or string (

), array (

enriched, which are also in the tooltip, for example,  string | enriched or

 number | enriched. For

details, see Enrichment Details.

Stellar Cyber provides several options to help you more quickly find the information you're looking for in
the Details section: quick filters and a search field.

The quick filters let you hide key-value pairs that do not interest you so you can more quickly see those
that do. You can apply quick filters to display only detections, only TI (Threat Intelligence) enrichments,
or both. When you don't apply a filter, you see all the key-value pairs for an alert.

When you apply the detections filter, Stellar Cyber displays only the key-value pairs with field names that
begin with xdr_event.

When you apply the TI enrichments filter, Stellar Cyber displays the following fields if the alert has been
enriched with this information:

srcip_reputation

dstip_reputation

srcip_reputation_source

dstip_reputation_source

srcip_geo and all its subproperties

srcip_geo.city

srcip_geo.countryCode

srcip_geo.countryName

srcip_geo.latitude

srcip_geo.longitude

srcip_geo.region

dstip_geo.region and all its subproperties

dstip_geo.city

dstip_geo.countryCode

dstip_geo.countryName

dstip_geo.latitude

dstip_geo.longitude

dstip_geo.region

 If the above fields for an alert have not been enriched with information, Stellar Cyber does not display

them.

When you apply both the detections filter and TI enrichments filter, Stellar Cyber displays key-value
pairs that match either filter.

You can search for any term that appears in a field key, name, or value and use commas to separate
multiple terms. Stellar Cyber displays all results that match any of the search terms you enter. If you're
applying a filter at the time of a search, then Stellar Cyber limits its search to just the filtered data. If no
filter is applied, then it searches through all unfiltered data.

JSON
The Interflow object can be displayed in JSON form and copied to a clipboard for pasting elsewhere.

JavaScript Object Notation (JSON) is a lightweight data interchange format that's easy for humans to read
and write, and easy for machines to parse and generate. It consists of two primary structures: a collection
of name/value pairs and an ordered list of values. If you're interested in learning more about JSON, here
are some useful resources:

For an introduction to JSON, see Introducing JSON .

For a basic reference, see JSON .

For a JSON error correction and validation tool, see JSONLint Validator and Formatter .

Actions Section
This section contains controls that can be used to alter the event's status in the system and add new data.
Some controls might not appear depending on the type of event record being displayed.

The Search box allows you to look for an External Action by name.

The buttons allow you to:

View Action History
Add a Filter
Add a Tag
Add a Comment
Trigger An Email
Sync to ServiceNow

Perform External Actions

External actions vary based on configuration and content in the Interflow record. If an option is
not applicable it is grayed out in the menu, as shown below. This may occur if the required data is
not present in the Interflow record, or an appropriate connector is not configured.

The following table indicates which connector respond actions are applicable for each external
action, along with the requirements to enable that action. Specifically, certain connectors must be
configured and the indicated fields in the Interflow must contain non-null, valid data.

E

x

t

e

r

n

a

l

A

c

ti

o

n

Bl

o

c

k

IP

/

Bl

o

c

k

o

n

Fi

Connector and Data Requirement*

for Action Availability

At least one firewall or security switch connector is configured and required fields are populated

dstip or

srcip

Applicable

Connector

s

AWS, Azure

NSG,

Barracuda

Firewall,

Check

Point,

Check Point

Smart-1

Cloud

,

re

w

al

l

D

is

a

bl

e

U

s

er

C

o

nf

Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field

userPrincipalName

Microsoft Entra ID (formerly Azure AD) connector required field

Cisco FMC,

Cisco

Meraki, F5

BIG-IP

ASM, F5

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

Active

Directory,

Microsoft

Entra ID

(formerly

Azure

Active

Directory)

Microsoft

Entra ID

(formerly

msg_class of Content Type

User ID on Which to Perform Action

azure_ad_audit

azure_ad_signin

azure_ad_risk_detection

azure_ad_risky_user

user_profile

initiatedBy.user.id

userId

userId

azure_ad.id

user_profile.id

Microsoft Entra ID (formerly Azure AD) connector required field

msg_class of Content Type

User ID on Which to Perform Action

azure_ad_audit

azure_ad_signin

azure_ad_risk_detection

azure_ad_risky_user

user_profile

initiatedBy.user.id

userId

userId

azure_ad.id

user_profile.id

Azure

Active

Directory)

Microsoft

Entra ID

(formerly

Azure

Active

Directory)

Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field

 user_id and group_id Microsoft

Entra ID

(formerly

Azure

Active

Directory)

Microsoft

Entra ID

(formerly

Azure

Active

Directory)

Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field

userPrincipalName

ir

m

C

o

m

pr

o

m

is

e

d

D

is

m

is

s

R

is

k

R

e

m

o

v

e

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

e

v

o

k

e

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

d

d

U

s

er

to

G

ro

u

p

Active Directory or Microsoft Entra ID (formerly Azure AD) connector required field

 user_id and group_id Microsoft

Entra ID

(formerly

Azure

Active

Directory)

R

Always available

SSH Host

u

n

a

S

cr

ip

t

C

o

nt

ai

n

H

o

st

(I

s

ol

at

e

E

n

d

p

oi

nt

)

Is

ol

at

One of the following connectors is configured. The required data varies based on connector to be used for

Bitdefender,

response.

Bitdefender required fields

 One of bitdefender.computer_id or bitdefender.endpointId

CrowdStrike required fields

dstip or srcip or hostip

Cybereason required fields

 cybereason.pylumId

Cylance required fields
device and device.deviceID or
cylance and one of cylance.device_id or srcmac or dstmac or ( host and host.mac)

Cynet required fields
srcip_host, computer_name or host.name

 are any value other than an IP Address in at least one of these: hostip_host,

Deep Instinct:  required fields
deep_instinct_asset and deep_instinct.id or
deep_instinct_suspiciousevent and deep_instinct.device_id or
deep_instinct_maliciousevent and deep_instinct.device_id

Microsoft Defender for Endpoint required fields
microsoft_defender.machineId

microsoft_defender.id and

SentinelOne required fields
sentinelone.agentId

sentinelone and sentinelone.agentRealtimeInfo and

Sophos Central required fields

sophos.hostip_assetid

VMware Carbon Black Cloud required fields

device_id

Palo Alto Networks CORTEX XDR required fields

endpoint_id

CrowdStrik

e,

Cybereason

, Deep

Instinct,

BlackBerry

Cylance,

Cynet,

Microsoft

Defender

for

Endpoint,

SentinelOn

e, Sophos

Central,

VMware

Carbon

Black

Palo Alto

Networks

CrowdStrike required fields

dstip or srcip or hostip

CORTEX

XDR

CrowdStrik

e

Forescout required fields

srcip, dstip, srcmac, dstmac

Forescout

SentinelOne required fields

sentinelone.agentRealtimeInfo and sentinelone.agentId

SentinelOn

SonicWall Capture Client required fields

device.deviceId and device.InstallToken

SentinelOne required fields

msg_origin.source is 'SentinelOne_endpoint' or msg_origin.source

is SentinelOne and the following fields are present and valid: sentinelone.threatInfo,

sentinelone.threatInfo.threatId

SentinelOne required fields

msg_origin.source is 'SentinelOne_endpoint' or msg_origin.source

is SentinelOne and the following fields are present and valid: sentinelone.threatInfo,

sentinelone.threatInfo.threatId

e,

SonicWall

Capture

Client

SentinelOn

e

SentinelOn

e

e

E

n

d

p

oi

nt

H

id

e

H

o

st

U

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

iti

at

e

S

c

a

n

Ki

ll

T

hr

e

at

Q

u

ar

a

nt

in

e

T

hr

e

at

SentinelOne required fields

msg_origin.source is SentinelOne_endpoint or msg_origin.source is

SentinelOne and the following fields are present and valid: sentinelone.threatInfo,

sentinelone.threatInfo.detectionType, sentinelone.threatInfo.threatId and

sentinelone.threatInfo.detectionType is dynamic

SentinelOn

e

The endpoint must also be either a Mac OS or Windows host. if it is not, then a Quarantine is performed instead

SonicWall Capture Client required fields

device.deviceId and device.InstallToken

SonicWall Capture Client required fields

device.deviceId and device.InstallToken

SonicWall Capture Client required fields

device.deviceId and device.InstallToken

Cynet required fields

 are any value other than an IP Address in at least one of these: hostip_host,

srcip_host, computer_name or host.name.

SonicWall

Capture

Client

SonicWall

Capture

Client

SonicWall

Capture

Client,

Cynet

R

e

m

e

di

at

e

T

hr

e

at

D

is

c

o

n

n

e

ct

H

o

st

R

e

st

ar

t

M

a

c

hi

n

e

S

h

ut

D

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

Barracuda Email Security Service required fields

barracuda.account_id and barracuda.subject

Barracuda

and barracuda.env_from and barracuda.hdr_from

o

st

)

R

e

m

e

di

at

e

E

m

ai

l

W

N/A

e

b

h

o

o

k

Email

Security

Universal

Webhook

Responder,

ESET

Responders

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

Add a Filter

Depending on the type of event, you may have the option to create an alert filter or a log filter.

Add a Tag

You can tag events to group them and make them easier to find later. The tag can be anything that helps
you identify the events tagged. To tag an event:

1. From the event display, select the Actions tab, and click Add a Tag.

2. Choose a tag from the Tag This Event dropdown. You can also enter a new tag.
3. Click Submit. The tag is immediately added to the event.

You can now filter by tag, and use a query to find events with the tag.

Add a Comment

You can add comments to any event.

1. From the event display, select the Actions tab, and click Add a Comment.

2. Enter your comment.

3. When you click Submit, the comment is added, along with your name and a timestamp.

Trigger An Email

To send an email about this security event:

1. From the event display, select the Actions tab, and click Trigger An Email. The email is

automatically "from" the email address specified in System | ORGANIZATION MANAGEMENT |
Mail Server options.

2. You can add recipients by directly typing a full email address, or selecting them from the

dropdown list that appears when you click in the Recipients field.

3. Change the Subject, Priority, or Email Body, if desired.

4. You can choose whether to include the Interflow data as an attachment or append it to the email

body.

5. Click Submit. Stellar Cyber immediately sends the email.

Sync to ServiceNow

The manual Sync to ServiceNow button is visible in the Actions tab when an alert cannot be
synchronized to any InSync configuration automatically.

After clicking the Sync to ServiceNow button and if the manual synchronization is successful, the button
is hidden and the ServiceNow icon displays on the top of the Alert Details page.

External Actions: Block IP

You can immediately respond to an event by creating a new firewall rule:

1. From the event display, select the Actions tab, and click Block IP for a Firewall or Security

Switch.

 To add a new firewall or switch, see Configuring Connectors.

2. Choose the connector you want to use to perform the action.

3. Choose the IP address to be blocked. The dropdown contains both the source and destination

IP addresses from the event.

4. For Direction:

For all firewalls, select Incoming, Outgoing, or Any.

When Incoming is selected, an Inbound firewall rule is created to match the
Source IP address.

When Outgoing is selected, an Outbound firewall rule is created to match the
Destination IP address.

If you selected a Security Switch, the Direction setting is not applicable.

 These actions are reported in Automation | Action History | Security Switch

Actions.

5. Choose a Duration. You can choose Minutes, Hours, Days, or Forever.

6. Click Submit. The new firewall rule is submitted to the firewall.

7. The status is reported in the Event Details pane and in the Automation | Action History,

Firewall Actions tab.

 For Firewall actions, if you block an IP host that is already blocked or if you unblock an IP
host that is already unblocked, the action is marked as Succeeded. You can view status
details in the Status Message.

External Actions: Disable User

You can immediately respond to an event by disabling a user:

1. From the event display, select the Actions tab, and click Disable User.

2. Choose a Connector from the dropdown. You can select either Active Directory or Microsoft

Entra ID (formerly Azure AD) connectors.

3. Set the Duration. You can choose Minutes, Hours, Days, or Forever.

4. Set a value for the Disable User field by selecting or typing a field name to match (from the

Interflow record).

 For Microsoft Entra ID (formerly Azure Active Directory) Connectors this field is

automatically populated from the userPrincipalName field. Also, the username field is

populated from Office 365 records.

5. Choose which user to disable. Depending on the event, you might have only one option.

6. Click Submit. The user is immediately disabled.

 To enable a user after disabling, visit the User Actions tab in the Automation | Action History page to

revert the disable action.

External Actions: Confirm Compromised

You can confirm that a user is compromised:

1. From the event display, select the Actions tab, and click Confirm Compromised.

2. Choose the Connector. Only Microsoft Entra ID (formerly Azure Active Directory) connectors are

supported.

3. Set the Duration. This is how long an action is triggered. Then it is reverted by the Dismiss Risk

action. You can choose Minutes, Hours, Days, or Forever.

4. Choose a User ID. They are automatically populated from the JSON record.

5. Click Submit. It is immediately confirmed that the user was compromised.

External Actions: Dismiss Risk

For a user that was confirmed compromised, you can dismiss the risk of that user:

1. From the event display, select the Actions tab, and click Dismiss Risk.

2. Choose the Connector. Only Microsoft Entra ID (formerly Azure Active Directory) connectors are

supported.

3. Choose a User ID. They are automatically populated from the JSON record.

4. Click Submit. The user is immediately dismissed.

 There is no Duration for this action. Once a user is dismissed, they stay dismissed. In other

words, there is no Revert action that returns the user to Confirm Compromised.

External Actions: Add User to Group

You can add a user to a group.

1. From the event display, select the Actions tab and click Add User to Group.

2. Choose the Connector. Only Microsoft Entra ID (formerly Azure Active Directory) connectors are

supported.

3. Choose a Selected User. This field is automatically populated from the user_id field.

4. Choose a Group ID. This field is automatically populated from the group_id field.

5. Click Submit. The user is added to the group.

External Actions: Remove User from Group

 The Remove User from Group action is only supported for manual action. It is not supported in

Automated Threat Hunting (ATH) playbooks.

You can remove a user from a group.

1. From the event display, select the Actions tab and click Remove User from Group.

2. Choose the Connector. Only Microsoft Entra ID (formerly Azure Active Directory) connectors are

supported.

3. Choose a Selected User. This field is automatically populated from the user_id field.

4. Choose a Group ID. This field is automatically populated from the group_id field.

5. Click Submit. The user is removed from the group.

External Actions: Revoke Existing Sign-In Sessions

 The Revoke Existing Sign-In Sessions action is only supported for manual action. It is not supported

in Automated Threat Hunting (ATH) playbooks.

You can revoke existing sign-in sessions:

1. From the event display, select the Actions tab and click Revoke Existing SIgn-In Sessions.

2. Choose the Connector. Only Microsoft Entra ID (formerly Azure Active Directory) connectors are

supported.

3. Choose a Selected User. This field is automatically populated from the userPrincipalName

field.

4. Click Submit. All active sign-in sessions for the specified user are terminated.

External Actions: Run a Script

You can immediately respond to an event by running a saved script or creating a new script:

1. From the event display, select the Actions tab, and click Run a Script.

2. Choose the Target remote host from the dropdown. The connection information is automatically
filled in. The dropdown also includes the option to add a new remote host. If needed, select
"create new remote host" as the target:

Specify the host name, IP address, port to which to connect, and the user and
password.
Specify whether to run the script on the Data Processor or a device sensor.
Note that the host is saved

3. Choose a script from the dropdown. The script is automatically added to the Script Body field. To

create a new saved script, see Creating Saved Scripts.

4. You can also choose Custom and create a new script. This new script will not be saved.
5. Click Submit. The script is executed.

The script action appears on the Script Actions page.

External Actions: Contain Host

You can immediately contain (lock down or isolate) a host managed by certain services such as
Bitdefender, BlackBerry Cylance, CrowdStrike, Cybereason, Cynet, Deep Instinct, Microsoft Defender for
Endpoint, SentinelOne, Sophos Central, VMware Carbon Black Cloud. You must have previously
configured a connector to that service in order to perform this action.

1. From the event display, select the Actions tab, and click Contain Host.

2. Choose the connector from the Connector dropdown.

 If you contain a host that is not managed by selected connector, the action status on the

Endpoint Actions page will be failed.

3. Choose the Target.  This menu option allows you to specify the source or destination host
associated with the event as the host you want to isolate or lock down. For Cybereason
connectors, the Target Value is automatically populated with the ID of a single Cybereason
machine. For all other connectors, the value is the MAC ID of that host.

4. Choose a Duration. You can choose Minutes, Hours, Days, or Forever.

5. Click Submit. The Contain Host action is reported in the Automation | Action History | Endpoint

Actions table.

 Depending on the originating connector, you may be able to revert a host containment from Stellar
Cyber. If this is supported, a Revert button is displayed in the row for the containment action of the
Automation | Action History | Endpoint Actions table. For supported connectors, using Revert triggers a
Lift Containment action that is displayed in the same table. If the API for the managing service does
not support a revert option then you need to use that product's UI to manage the host state.

 Blackberry Cylance connector's Contain Host action automatically expires upon the requested

duration but this action is not reported back to Stellar Cyber. The Endpoint Actions table reports that
the containment was successful, but not expired.

 If you use a Cynet connector to perform a response action on a host that is not in your Cynet list of
hosts, the Automation | Action History | Endpoint Actions row for the action will indicate that with an
error message such as: The remote server returned an error: (422) Unprocessable Entity.

The action appears on the Endpoint Actions page.

External Actions: Isolate Endpoint

You can isolate an endpoint on Palo Alto Networks CORTEX XDR. You must have previously configured a
connector to that service in order to perform this action. You can also unisolate an endpoint.

1. From the event display, select the Actions tab, and click Isolate Endpoint.

2. Choose the connector from the Connector dropdown.

3. Choose the Target.  This menu option allows you to specify the Endpoint ID. The Target Value is

populated.

4. Click Submit. The Isolate Endpoint action is reported in the Automation | Action History |

 Endpoint Actions table.

5. To unisolate the endpoint, use the Revert button in the Actions column of the table.

External Actions: Hide Host

You can immediately hide a host managed by CrowdStrike Falcon:

1. From the event display, select the Actions tab, and click Hide Host.

2. Choose your CrowdStrike Falcon service from the dropdown. You can add a CrowdStrike

connection from System | INTEGRATIONS | Connectors menu.

3. Choose the Target from the dropdown.
4. Choose a Duration. You can choose Minutes, Hours, Days, or Forever.
5. Click Submit. The host is hidden in CrowdStrike. That host now has an Unhide action, allowing

you to revert.

The action appears on the Endpoint Actions page.

 If you hide a host that is not managed by your CrowdStrike service, the action status on the

Endpoint Actions page will be failed.

External Actions: Disconnect Host

You can immediately disconnect a host managed by SonicWall Capture:

1. From the event display, select the Actions tab, and click Disconnect Host.

2. Choose your SonicWall Capture service from the dropdown. You can add a SonicWall Capture

connector from System | INTEGRATIONS | Connectors.

3. Choose the Target and Target Value.

4. Choose a Duration. You can choose Minutes, Hours, Days, or Forever.
5. Click Submit. The host is disconnected from the network.

The action appears on the Endpoint Actions page.

 If you disconnect a host that is not managed by your SonicWall Capture service, the action status on

the Endpoint Actions page will be failed.

External Actions: Initiate Scan

You can immediately scan an asset managed by SonicWall Capture or SentinelOne.

1. From the event display, select the Actions tab, and click Initiate Scan.

2. Choose the applicable connector from the dropdown menu.

3. Then select the asset / device / agent from the available list that is populated based on your

connector selection.

4. Choose the Target Value.

5. Click Submit. A vulnerability scan of your selection is triggered immediately from the service

associated with your connector.

The action appears on the Endpoint Actions page.

 If you scan a host that is not managed by your SonicWall Capture service, the action status on the

Endpoint Actions page will be failed.

External Actions: Restart Machine

You can immediately restart a host managed by SonicWall Capture:

1. From the event display, select the Actions tab, and click Restart Machine.

2. Choose your SonicWall Capture service from the dropdown. You can add a SonicWall Capture

connector from System | INTEGRATIONS | Connectors.

3. Choose the Target Value.

4. Click Submit. The host is immediately restarted.

The action appears on the Endpoint Actions page.

 If you restart a host that is not managed by your SonicWall Capture service, the action status on the

Endpoint Actions page will be failed.

External Actions: Shutdown Host

You can immediately shut down a host managed by SonicWall Capture or Cynet:

1. From the event display, select the Actions tab, and click Shut Down.

2. From the dropdown menu, select the connector you want to use to perform the shut down.

3. Specify the target device on which you want to perform the action.

 If you select a Cynet connector, the Target Value is automatically populated with related

JSON information.

4. Choose the Target Value.

5. Click Submit. The host is immediately shut down.

 If you use a Cynet connector to perform a response action on a host that is not in your Cynet list of
hosts, the Automation | Action History | Endpoint Actions row for the action will indicate that with an
error message such as: The remote server returned an error: (422) Unprocessable
Entity.

 If you shut down a host that is not managed by your SonicWall Capture service, the action status on

the Endpoint Actions page will be failed.

The action appears on the Endpoint Actions page.

External Actions: Update Device

You can upload JSON to run actions on a device known to a Forescout connector:

1. Access the Event Details Display:

a. Select Threat Hunting.

The Interflow Search tab appears.

b. Select the Indices for Traffic.

c. Select an event and click the More Info button.

2. From the event display, select the Actions tab, and click Update Device.

3. From the Connector menu, select the Forescout connector.

4. The Target menu lists the addresses associated with this event. Select the host on which you

want to run the Forescout connector update action. The target can be one of these: Source Host,
Destination Host, Source MAC, or Destination MAC. The Target Value is updated automatically
from the event data. These two fields are required default parameters for the Forescout action
and should not be specified in the JSON added in the next step.

5. If your connector was created with default JSON, you can customize it now, or skip this step.

Populate the JSON field with the action you want the connector to transmit to the Forescout app
configured in the beginning of this procedure. Note that Stellar Cyber verifies general format of
the JSON, not the logic. Following is an example based on ActionAPI's supported
JSON properties:

{

"connect_actionapi_vlan_assign":true,

"connect_actionapi_vlan_assign_id":"vlan233"

}



Do not include the IP or MAC address, as that is added automatically based on your
selection in the previous step. The JSON that is transmitted to Forescout will include the IP
or MAC and the property tag, similar to the sample below.

{

"mac":"009027390a7c",

"properties":{

"connect_actionapi_vlan_assign":true,

"connect_actionapi_vlan_assign_id":"vlan233"

}

}

Refer to Forescout documentation for supported fields and syntax details.

6. Click Submit. The connector runs the update action one time.

External Actions: Kill Threat

For assets managed by a SentinelOne service, if you have configured your connector for Respond
actions, you can use this action to kill a threat.

1. From the event display, select the Actions tab, and click Kill Threat.

2. Choose the SentinelOne connector from the dropdown menu.

3. Then select the Target from the available list that is populated based on your connector

selection.

4. The Target Value is automatically populated.

5. Click Submit. A kill threat signal on the target is immediately triggered from the SentinelOne

service associated with your connector.

The action appears on the Endpoint Actions page.

External Actions: Quarantine Threat

For assets managed by a SentinelOne service, if you have configured your connector for Respond
actions, you can use this action to quarantine a threat.

1. From the event display, select the Actions tab, and click Quarantine Threat.

2. Choose the SentinelOne connector from the dropdown menu.

3. Then select the Target from the available list that is populated based on your connector

selection.

4. The Target Value is automatically populated.

5. Choose a Duration. You can choose Minutes, Hours, Days, or Forever. This specifies the

length of time to put the target in quarantine.

6. Click Submit. A quarantine on the target is immediately triggered from the SentinelOne service

associated with your connector.

The action appears on the Endpoint Actions page.

External Actions: Remediate Threat

For assets managed by a SentinelOne service, if you have configured your connector for Respond
actions, you can use this action to remediate a threat.

1. From the event display, select the Actions tab, and click Remediate Threat.

2. Choose the SentinelOne connector from the dropdown menu.

3. Then select the Target from the available list that is populated based on your connector

selection.

4. The Target Value is automatically populated.

5. Click Submit. A remediation signal on the target is immediately triggered from the SentinelOne

service associated with your connector.

The action appears on the Endpoint Actions page.

External Actions: Remediate Email

For deployments integrated with Barracuda's Email Security Service you can use Stellar Cyber to
create an incident in a Barracuda Forensics And Incident Response system.

1. From the event display, select the Actions tab, and click Remediate Email. The dialog appears

with some sections pre-populated from the JSON associated with the selected event.

2. Choose the applicable connector from the dropdown menu.

3. Optionally, specify whether to search for the email in previously Quarantined and Sent

categories.

4. Specify which remediation actions to perform on the Barracuda response system.

Message Actions: Select either None, Delete, or Quarantine.

Enable continuous quarantine: (Visible only when the message action is set to Delete
or None) Select this option to request that the action continue for 72 hours after the
initial remediation has completed.

Notify: Select this option to also send a warning email alert to the affected user.

Send summary: Select this to copy an incident summary to the configured security
team.

5. Click Submit. An incident is sent to the Barracuda Forensics And Incident Response

associated with your connector.

The action appears on the Automation | Action History | Email Actions page.

External Actions: Webhook

You can manually trigger a Webhook action. The action may have been created from a customization in
the Universal Webhook Responder or from a predefined template in the Universal Webhook Responder or
ESET Responder.

1. From the event display, select the Actions tab, and click a Webhook action.

2. (Optional) When the Webhook Responder is triggered manually, you can edit the Path and

Query and the JSON Body when you issue the action.

3. Click Submit.

Action History
Any action you perform on an event is recorded in the Action History. This section appears after the first
action is performed and tracks all actions by any user. Click View Action History.

Click View Actions to exit the Action History.

Rules
The Rules tab only displays if the alert type is rule-based. See Rule-Based Alert Details for information.

Related Events
The Related Events tab only displays if the alert type is SentinelOne. The tab contains a summary of
related SentinelOne Deep Visibility events. For details, see Related Events for Alert Types.

InSyncs
If there are any integration syncs, there is a ServiceNow icon displayed at the top of the Details page.

When you hover over the ServiceNow icon, the status, Ticket ID, and Last Synced date and time are
displayed.

For details, see Using InSyncs.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

