Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cato Networks Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.
You create one instance of this connector for each Cato Networks account you want to monitor.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Cato Networks

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Audit Log

Connectivity

Routing

Security

Sockets Management

Stories

System

Index

Traffic

IDPS/Malware Sandbox
Events (if
cato_networks.event_s
ub_type has one of these
values: IPS, Suspicious
Activity, or Anti Malware)

Locating Records

msg_class
:

cato_aud
it

cato_con
nectivit
y

cato_rou
ting

cato_sec
urity

cato_soc
kets_man

Content Type

Index

Locating Records

agement

cato_sto
ries

cato_sys
tem

msg_origi
n.source:

cato_net
works

msg_origi
n.vendor:

cato_net
works

msg_origi
n.category
:

sase

Domain

https://api.catonetworks.com/

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Cato Networks to get the raw alerts that are stored in the Syslog index.
Select the Security content type.

Stellar Cyber maps Cato Networks events. The events are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by event_id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Account ID and API Key

The account must also be enabled to Enable integration with Cato events

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class: cato_security AND cato_networks.event_sub_type.keyword: (\"NG Anti
Malware\" OR \"Anti Malware\") AND _exists_: file.name AND NOT
cato_networks.threat_verdict: \"clean\"

Adding a Cato Networks Connector
To add a Cato Networks connector:

1. Enable Cato API access
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Enabling Cato API Access
Before you configure the connector in Stellar Cyber, you must obtain a Cato Networks API key.
Follow the guidance in the Cato API documentation .

Enable Event Integration

To send Cato events data to a third party application, follow the guidance in the note in the Cato
API documentation :

 If you are using the eventsFeed API to ingest event data, make sure to select Enable

integration with Cato events in the Resources > Event Integrations page.

Adding the Connector in Stellar Cyber
To add the Cato Networks connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SASE from the Category dropdown.

5. Choose Cato Networks from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name to specify which tenant is permitted to use this connector on

Stellar Cyber.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Account ID you obtained from the Cato Networks login.

13. In the API Key field, enter the value you noted above in Enabling Cato API Access.

14. Enter the Interval (min). This is how often the logs are collected.

15. Select the Content Type:

Audit Log
Connectivity
Routing
Security
Sockets Management

Stories
System

16. (Optional) The Initial Marker field is used to adjust the ingestion start point in cases
where the volume of Event data to retrieve is extremely large. (The default duration

Cato Network’s API retrieves is 7 days of Event data.) The API supporting this field
requires an encoded base64 string (combining topic, partition, and offset) that is unique
to your active events queue. Stellar Cyber has provided this field for use only by
advanced API users of Cato Networks who are already familiar with retrieving this
marker value in their environment. (This marker does not apply to Audit Log data.)

17. (Optional) For the Security content type, you can select the Enable Security Filter

checkbox to specify a customized security event filter.

18. (Optional) Enter a customized security event filter in the Customized Security Event

Filter field. This field allows you to specify a customized filter for the security events'
event_sub_type. Define filters using the following format:

{"fieldName":"event_sub_type","operator":"in","values":["NG Anti
Malware","Anti Malware","SaaS Security API Anti Malware"]}

For this filter:

fieldName should be event_sub_type

operator supports in, not_in, is, and is_not

Use the following link for more information on the event_sub_type under the Security
content type:

Cato API - EventsFeed (Large Scale Event Monitoring) 

19. Click Next. The final confirmation tab appears.

20. Click Submit.

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
using the X button. If the test fails, you can select the   button from the same row to review and
correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

400

Bad

This error occurs when there is an error in the

Request

connector configuration.

Did you configure the connector correctly?

401

Unauthorize

d

This error occurs when an authentication credential is

Did you enter your credentials correctly?

invalid or when a user does not have sufficient

privileges to access a specific API.

Are your credentials expired?

Are your credentials entitled or licensed for that

specific resource?

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

403

Forbidden

This error occurs when the permission or scope is not

correct in a valid credential.

Did you enter your credentials correctly?

Do you have the required role or permissions for

that credential?

404

Not Found

This error occurs when a URL path does not resolve

Did you enter your API URL correctly?

to an entity.

429

Too Many

Requests

This error occurs when the API server receives too

The server or user license/quota will eventually

much traffic or if a user’s license or entitlement quota

recover. The connector will periodically retry the

is exceeded.

query.

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Traffic.

or

Change the Indices to IDPS/Malware Sandbox Events.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

