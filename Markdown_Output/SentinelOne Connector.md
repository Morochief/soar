✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring SentinelOne Connectors
This connector allows Stellar Cyber to collect data from external sources and add the records to
the data lake.
SentinelOne integration with Stellar Cyber provides advanced threat detection and response
capabilities, combining AI-powered endpoint protection with real-time threat intelligence and
automated response workflows to improve incident response and threat mitigation.
A SentinelOne connector allows you to collect logs, discover assets, and see vulnerabilities. If
you enable Respond options on this connector, with the correct type of user account, you can
perform the following endpoint response actions:
Contain (Isolate) Host
Initiate Scan
Kill Threat
Quarantine Threat
Remediate Threat
Rate limits for the SentinelOne connector are detailed in Guidance on SentinelOne Connector
Rate Limits.
 The following error from SentinelOne, 503 Service Temporarily Unavailable, is treated by
Stellar Cyber as the following error, 429 Too Many Requests, and is not shown on the DP
connector list. This will be addressed in a later release.
 This connector is improved to use less memory. Under certain scenarios if there is an error
reaching the third-party API, some duplicate messages may be sent.
 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.
Connector Overview: SentinelOne
Capabilities

Collect: Yes
Respond: Yes
Native Alerts Mapped: Yes
Runs on: DP
Interval: Configurable
Collected Data
Content Type Index API Ma
pp
ed
to
Al
ert
In
de
x
Assets
Host (Agents) https://<s
entinelon
e region
url>/web/
api/v2.1/a
gents
Syslog, Alerts
Threats https://<s Y
entinelon e
e region s
url>/web/
api/v2.1/t
hreats
Scan
Vulnerabilities Three
related
 This content type needs the Applications API calls
View Risks permission. See Obtaining are used
SentinelOne Credentials for details. for this
data:
https://<s
entinelon
e region
url>/web/
api/v2.1/a
gents
https://<s
entinelon
e region
url>/web/
api/v2.1/i
nstalled-
applicatio
ns
https://<s
entinelon
e region
url>/web/
api/v2.1/p
rivate/inst
alled-
applicatio

| Content Type | Index | API | Ma  |
| ------------ | ----- | --- | --- |
pp
ed
to
Al
ert
In
de
x
ns/<app
id>/cves
| Support added for the following in v4.3.5: |     |     |     |
| ------------------------------------------ | --- | --- | --- |
 The following content types require an upgraded subscription (STAR), as well as
permissions. See Obtaining SentinelOne Credentials for details.
|        | Syslog | https://<se |     |
| ------ | ------ | ----------- | --- |
| Alerts |        |             |     |
ntinelone
region
url>/web/a
pi/v2.1/clo
ud-
detection/a
lerts
|                         | Syslog | https://<se |     |
| ----------------------- | ------ | ----------- | --- |
| Deep Visibility(Events) |        |             |     |
ntinelone
region
url>/web/a
pi/v2.1/dv/
events?
queryId=
{query_id}
|                        | Syslog | https://<se |     |
| ---------------------- | ------ | ----------- | --- |
| Events (Threat Events) |        |             |     |
ntinelone
region
url>/web/a
pi/v2.1/thre
ats/{threat
id}/explore/
events?
limit=1000
|        | Syslog | https://<se |     |
| ------ | ------ | ----------- | --- |
| Rogues |        |             |     |
ntinelone
region
url>/web/a
pi/v2.1/
rogues/tabl
e-view
|              | Syslog | https://<se |     |
| ------------ | ------ | ----------- | --- |
| Threat Notes |        |             |     |
ntinelone
region
url>/web/a
pi/v2.1/thre
ats/{threat
id}/notes?
limit=1000
| Support added for the following in v5.3.0: |     |     |     |
| ------------------------------------------ | --- | --- | --- |

| Content Type |     | Index | API | Ma  |
| ------------ | --- | ----- | --- | --- |
pp
ed
to
Al
ert
In
de
x
|            |     | Syslog | https://<se |     |
| ---------- | --- | ------ | ----------- | --- |
| Activities |     |        |             |     |
ntinelone
region
url>/web/a
pi/v2.1/acti
vities

Support added for the following in v6.0.0:
|                   |     | Syslog | /web/api/v |     |
| ----------------- | --- | ------ | ---------- | --- |
| Misconfigurations |     |        |            |     |
2.1/xspm/fi
ndings/mis
configurati
ons/graph
ql
|                |     | Syslog | /web/api/v |     |
| -------------- | --- | ------ | ---------- | --- |
| Unified Alerts |     |        |            |     |
2.1/unified
alerts/grap
hql
Domain
<Host URL>
where <Host URL> is a variable from the configuration of this connector
Response Actions
| Action | Required Fields | API |     |     |
| ------ | --------------- | --- | --- | --- |
Contain
|     | agentRealtimeInfo | https://<sentinelone region |     |     |
| --- | ----------------- | --------------------------- | --- | --- |
(Isolate)
|      | and                  | url>/web/api/v2.1/agents/actions/dis |     |     |
| ---- | -------------------- | ------------------------------------ | --- | --- |
| Host | agentRealtimeInfo.ag | connect                              |     |     |
entId
revert:
https://<sentinelone region
url>/web/api/v2.1/agents/actions/con
nect
| Initiate Scan | agentRealtimeInfo    | https://<sentinelone region          |     |     |
| ------------- | -------------------- | ------------------------------------ | --- | --- |
|               | and                  | url>/web/api/v2.1/agents/actions/ini |     |     |
|               | agentRealtimeInfo.ag | tiate-scan                           |     |     |
entId

Action Required Fields API
Kill Threat msg_origin.source is https://<sentinelone region
'Sentinel_endpoint' url>/web/api/v2.1/threats/mitigate/k
or ill
msg_origin.source is
'Sentinel' and
threatInfo and
threatInfo.threatId
are valid
Quarantine msg_origin.source is https://<sentinelone region
Threat 'Sentinel_endpoint' url>/web/api/v2.1/threats/mitigate/q
or uarantine
msg_origin.source is revert:
'Sentinel' and
https://<sentinelone region
threatInfo and
url>/web/api/v2.1/threats/mitigate/u
threatInfo.threatId
n-quarantine
are valid
Remediate msg_origin.source is https://<sentinelone region
Threat 'Sentinel_endpoint' url>/web/api/v2.1/threats/mitigate/r
or emediate
msg_origin.source is revert:
'Sentinel' and
https://<sentinelone region
threatInfo.detection
url>/web/api/v2.1/threats/mitigate/r
Type is 'dynamic'
ollback-remediation
and the following
fields are present
and valid:
threatInfo,
threatInfo.threatId
The endpoint must also be
either a Mac OS or
Windows host. if it is not,
then a Quarantine is
performed instead.
Third Party Native Alert Integration Details
SentinelOne Cloud
SentinelOne's threat dataset includes a variety of fields that enable Stellar Cyber to map the native
SentinelOne alerts to the Stellar Cyber Alert index. For example, threatInfo.classification
describes the event (such as Trojan). That and other fields in the threatInfo record support direct
mapping of SentinelOne's MITRE | ATT&CK Tactic and Technique fields to Stellar Cyber's XDR Kill Chain.
Of the assorted collected data types noted above, only the Threat (msg_class:
sentinelone_threat_detection) are directly mapped to the Alert index. Select the Threat content type.
For details, see Integration of Third Party Native Alerts.
SentinelOne Singularity Identity
This connector ingests logs from SentinelOne to get the raw alerts that are stored in the Syslog index.
Select the Unified Alerts content type.
Stellar Cyber maps SentinelOne alerts. The alerts are read from the Syslog index, enriched with Stellar
Cyber fields, and mapped (with deduplication) to the Alerts index.
Deduplication is by tenantid and sentinelone.external_id.
For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations
Host URL and API Key (token).
To Collect, the SentinelOne User Account can have either the Viewer or Admin role. To
Respond, the user Role must be Admin.
Locating Records
Use the following fields as a guide to query for records:
msg_origin.source: sentinelone_endpoint
msg_origin.vendor: sentinelone
msg_origin.category: endpoint
msg_class:
Events (Threat Events) Hosts (Agents) Deep Visibility
sentinelone_threat_events sentinelone_host sentinelone_deep_visib
ility
Alerts Rogues Threat
sentinelone_cloud_detection_alersentinelone_rogues_table sentinelone_threat_det
ts ection
Threat Notes Vulnerabilities Activities
sentinelone_threat_notes sentinelone_vulnerabilities sentinelone_activities
Misconfigurations Unified Alerts
sentinelone_misconfigurations sentinelone_unified_alerts
For SentinelOne Cloud, to search the Original Records in the Syslog index, use the query:
msg_class:sentinelone_threat_detection
For SentinelOne Singularity Identity, to search the alerts in the Alerts index or the Original Records in the
Syslog index, use the query: msg_class:sentinelone_unified_alerts AND
sentinelone.detectionSource.product: Identity AND (NOT event.severity_str: INFO)
Adding a SentinelOne Connector
To add a SentinelOne connector:
1. Obtain SentinelOne credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion
 You can also configure SentinelOne to send logs to the Stellar Cyber parser. However, the
connector allows you to assign a tenant, while the parser does not.
Obtaining SentinelOne Credentials
As part of this procedure, you specify the credentials of an account on the SentinelOne server
that will be used to retrieve data. This account must have read/view permissions or better on

the SentinelOne server. To perform response actions, the account must have an
administrative role.
1. Log into your SentinelOne Management Console as an administrative user (for
example: https://usea1-partners.sentinelone.net/login).
2. From the Management Console navigation pane, select Settings.
3. Navigate to Site Info.
4. Make sure that Licenses is Complete for the site.

Some content types require an upgraded subscription (STAR), as well as
permissions, otherwise the connector will not produce expected results. If that is
the case, select Add-ons STAR.
5. In the tab for Users, choose Roles.
To support the collect only function in Stellar Cyber, choose either Viewer or
Admin.
To support the respond function in Stellar Cyber, choose Admin.
6. To support the Vulnerabilities content type, with the Admin role, choose Applications,
and select Permissions including View Risks.

7. For the role, set the following permissions for certain content types:
To support the Deep Visibility content type, choose Deep Visibility View.
To support the Threats content type, choose Threats View.
To support the Rogues content type, choose Rogues View.
 If these features are Not allowed (greyed out), contact SentinelOne.
8. Click Save.
9. Choose the Users tab and select the option to add a New User for the account you will
use with the Stellar Cyber connector.
10. In the User Details, enter the information for the new user.

11. Make sure to assign a role to the account, either Viewer or Admin.
12. Log out of the SentinelOne Management Console and then log back in with the
username you created. You are prompted to create a password for that user. Create
the password and complete the login.
13. When logged into the SentinelOne online console as an administrative user, you need
to generate an API token for the connector configuration. The token can be generated
from a console user or from a service user.
The following steps are to generate the API token from a console user:
a. Click the username from the top right of the console and select My User.
b. In the dialog that displays, click the link to Generate an API Token.
c. This displays the token with a warning to copy it. If you forget the token, you
will need to regenerate it. Download it now or Copy it and save it to a file for
later use in the connector you configure in Stellar Cyber.
d. Exit the console and proceed to the next section.
The following steps are to generate the API token from a service user:
a. Click the USERS tab and choose Service Users. Then select Create New
Service User from the Actions menu.

b. Enter the Name of the New Service User and choose an Expiration
Date.Then click Next.
c. You can set the Scope of Access for the Account or the Site.
d. To set the Scope of Access for the Account, select Account. Choose Admin
or Viewer from the dropdown menu for the role. Choose Admin for respond
actions.
e. To set the Scope of Access for the Site, select Site. Choose Admin or
Viewer from the dropdown menu for the role. Choose Admin for respond
actions.
f. Click Create User.
g. Copy the API Token.

 Store the API key in a safe location. It cannot be retrieved later although it
can be regenerated.
h. Click Close.
Adding the Connector in Stellar Cyber
To add a SentinelOne connector in Stellar Cyber:
1. Log in to Stellar Cyber.
2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.
3. Click Create and select Connector.
The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.
4. Choose Endpoint Security from the Category dropdown.
5. Choose SentinelOne from the Type dropdown.
The asterisk (*) indicates a required field.
6. Enable the Function for Collect and/or Respond.
7. Enter a Name.

 Notes:
This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.
8. Choose a Tenant Name. The Interflow records created by this connector include this
tenant name.
9. Choose the device on which to run the connector.
10. (Optional) When the Function is Collect, you can apply Log Filters. For information,
see Managing Log Filters.
11. Click Next. The Configuration tab appears.
The asterisk (*) indicates a required field.
12. Enter the Host URL. This is the address of your SentinelOne server.
 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"
symbol.
13. Enter the API Key (token) you created above.
 In earlier releases, Stellar Cyber supported use of a Username / Password
combination. However, SentinelOne now enforces use of 2FA, which necessitates
use of a token with API communications.
14. (Optional) Enter Site. This is a string and can be either a site ID or a site name. In the
SentinelOne management console, navigate to Settings > Sites, click the site, and
click Site Info for the value. A site ID is a long numeric string, for example:
775505036300366067.
15. Choose the Content Type. The following logs are supported:
Vulnerabilities
 This content type requires a permission. See Obtaining SentinelOne
Credentials for details.
 T he SentinelOne connector only supports single scope for the
Vulnerabilities API. If multiple scopes are needed:
create multiple users: one scope per user
create multiple connectors: one connector per user

Hosts (Agents)
Threats
The following logs are supported for v4.3.5, and later.
 These content types require an upgraded subscription, as well as
permissions. See Obtaining SentinelOne Credentials for details.
Alerts
Events (Threat Events)
Threat Notes
Rogues
Deep Visibility
The following logs are supported for v5.3.0, and later.
Activities
Misconfigurations
Unified Alerts
16. Click the Advanced Settings checkbox to enter the interval, in minutes, for each
content type selected. The interval is how often the logs are collected. There are default
values for the interval, based on the content type. Most content types have a 5 minute
default interval, but Deep Visibility has a 30 minute default interval.
Also for Deep Visibility, you can specify the number of items retrieved in the interval.
The default is 20000. Use caution when adjusting the limit. If it is too high, there are
risks, for example, the SentinelOne API might not support the high number.
17. Click Next. The final confirmation tab appears.
18. Click Submit.
The new connector is immediately active.
Guidance on SentinelOne Connector Rate Limits

Some customers using the SentinelOne connector in Stellar Cyber may occasionally experience
API rate limit issues when retrieving data from SentinelOne endpoints. Limits are enforced by
SentinelOne to ensure fair use and platform stability across tenants.
Why This Happens
SentinelOne applies API rate limits at the tenant or console level. For larger MSSP environments
or those running multiple integrations, these limits can sometimes be reached during periods of
high activity or large data pulls.
Recommended Customer Actions
The following are recommended actions you can take:
1. Contact SentinelOne Support or Your TAM
If you encounter rate limit issues, please reach out to your SentinelOne Technical
Account Manager (TAM) or SentinelOne Support to request a rate limit increase.
SentinelOne’s official guidance on rate limiting can be found here: API rate
limits 
Rate limit increases are reviewed and approved by SentinelOne
2. Review Your API Usage
Review how frequently your SentinelOne data is being queried. In some cases,
reducing the query frequency or adjusting collection intervals can help avoid rate limit
thresholds.
3. Dedicated Consoles (for MSSPs)
MSSPs operating on shared SentinelOne consoles may not be able to request IP
whitelisting or dedicated rate limit adjustments.
However, if your organization operates a dedicated SentinelOne console, you can
contact SentinelOne Support to ask about potential configuration options specific to
your tenant.
Summary
While rate limits are controlled by SentinelOne, our integration is designed to ensure reliable
data collection even under constrained conditions.
If you continue to experience interruptions, please contact Stellar Cyber Support for assistance.
Providing your SentinelOne case number (if you have opened one) will help us coordinate more
effectively with the SentinelOne team.
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

HTTP E HTTP Stan
rror dard Error Explanation Recommendation
Code Name
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
is exceeded. query.
If this occurs unexpectedly or too often, work with
your API provider to investigate the server limits,
user licensing, or quotas.
For a full list of codes, refer to HTTP response status codes .
Verifying Ingestion
To verify ingestion:
1. Select Threat Hunting. The Interflow Search tab appears.
2. Set the Indices for the type of content you collected:
For Threats, change the Indices to Syslog or Alerts.
For Hosts, change the Indices to Assets. Note that hosts discovered through
this connector show SentinelOne as a data source.
For Vulnerabilities, change the Indices to Scans.
For all other data types, change the Indices to Syslog.
3. Search for the msg_class corresponding to the data type you want to view:
Vulnerabilities: sentinelone_vulnerabilities
Hosts (Agents): sentinelone_host
Threats: sentinelone_threat_detection
Alerts: sentinelone_cloud_detection_alerts
Events (Threat Events): sentinelone_threat_events
Threat Notes: sentinelone_threat_notes
Rogues: sentinelone_rogues_table
Deep Visibility: sentinelone_deep_visibility
Activities: sentinelone_activities
Misconfigurations: sentinelone_misconfigurations

Unified Alerts: sentinelone_unified_alerts
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  