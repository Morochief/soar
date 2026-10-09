✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Azure Event Hub Connectors
Azure Event Hub connectors allow Stellar Cyber to ingest Azure events and add them to the data
lake.
 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.
Connector Overview: Azure Event Hub
Capabilities
Collect: Yes
Respond: No
Native Alerts Mapped: Yes
Runs on: DP
Interval: Continuous
Collected Data
| Content Type       | Index              | Locating Records   |
| ------------------ | ------------------ | ------------------ |
| Azure Activity Log | Syslog             | msg_class:         |
| Azure Bastion      | Traffic (for Azure | azure_activity_log |
Firewall and
| Azure Firewall |     | azure_bastion_log |
| -------------- | --- | ----------------- |
Structured Azure
| Azure Keyvault | Firewall Log) | azure_firewall (for |
| -------------- | ------------- | ------------------- |
Azure Firewall and
| Azure Security Center | Windows Events |     |
| --------------------- | -------------- | --- |
Structured Azure Firewall
(for Microsoft
| Azure Security Groups |     | Log) |
| --------------------- | --- | ---- |
Defender for
| Azure SQL Server | Cloud) | azure_keyvault_log  |
| ---------------- | ------ | ------------------- |
| Azure Storage    |        | azure_security_cent |
er
Azure Synapse Workspace
azure_security_grou
Azure Web Application Firewall
ps
Microsoft Defender for Cloud
azure_sql_server

Content Type Index Locating Records
Microsoft Graph Activity Log azure_storage
azure_synapse_works
pace
Microsoft Sentinel
azure_web_applicati
Structured Azure Firewall Log on_firewall
microsoft_defender_
cloud
microsoft_graph_act
ivity_log
microsoft_sentinel
msg_origin.source:
azure_eventhub
microsoft_azure (for
azure_activity_log)
msg_origin.vendor:
microsoft
msg_origin.category:
saas
Domain
N/A
Response Actions
N/A
Third Party Native Alert Integration Details
Microsoft Defender for Cloud
This connector ingests logs from the content type, Microsoft Defender for Cloud, to get the raw alerts that
are stored in the Windows Events index.
Stellar Cyber maps Microsoft Defender for Cloud alerts. The alerts are read from the Windows Events
index, enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.
Deduplication is by tenantid and microsoft_defender_cloud.SystemAlertId.
For details, see Integration of Third Party Native Alerts.
Microsoft Sentinel
This connector also ingests logs from the content type, Microsoft Sentinel, to get the raw alerts that are
stored in the Syslog index.
 The integration focuses exclusively on Microsoft Sentinel Incident data and only supports data
transferred through Azure Event Hub.
Stellar Cyber maps Microsoft Sentinel incidents. The alerts are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.
Deduplication is by tenantid and microsoft_sentinel.IncidentName.

For details, see Integration of Third Party Native Alerts.
Required Credentials and Configurations
Event Hub Name, Connection String, Consumer Group
Locating Records
Microsoft Defender for Cloud
To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_class: (microsoft_defender_cloud OR AzureSecurityCenter).
Microsoft Sentinel
To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_class: microsoft_sentinel AND microsoft_sentinel.Type: SecurityIncident.
Adding an Azure Event Hub Connector
To add an Azure Event Hub connector:
1. Gather the Event Hub information
2. Stream logs to Event Hub
3. Add Azure Monitor logs to Event Hub
4. Add the connector in Stellar Cyber
5. Test the connector
6. Verify ingestion
Gathering the Event Hub Information
Gather the following Event Hub information.
 The subscription plan needed for the Azure Event Hub connector is Basic.
Azure Event Hub Name: The name of the Azure Event Hub.
Connection String: Find the connection string in Azure . You must use a unique
connection string for each of your Stellar Cyber Azure Event Hub connector instances.
 The connection string must include the Listen permission for shared access
policies.
Consumer Group: The consumer group for the Event Hub.
Event Source: The source of the events you want to ingest (you must configure these
sources to send data to your Event Hub):
Azure Activity Log
Azure Bastion
Azure Firewall
Azure Keyvault
Azure Security Center

Azure Security Groups
Azure SQL Server (includes AuditEvent log)
Azure Storage
Azure Synapse Workspace
Azure Web Application Firewall
Microsoft Defender for Cloud
Microsoft Graph Activity Log
Microsoft Sentinel
Structured Azure Firewall Log
Custom Event Source
Streaming Logs to Event Hub
To stream logs to an Event Hub, refer to the Microsoft documentation .
1. Log in as a Security Administrator to Microsoft Entra ID.
2. Scroll down to Monitoring and click Diagnostic settings.
3. Click General and then click Add diagnostic setting.
4. In the Diagnostic setting window:
a. Enter a Diagnostic setting name.
b. Select the Logs you want to stream.
c. Select the check box for Stream to an event hub.

d. For where you want to route the logs, select the Subscription, Event hub
namespace, optional Event hub name, and Event hub policy name.
5. Click Save.
 Make sure the Subscription and Event hub namespace are associated with the Microsoft
Entra tenant from where the logs are streamed.
Adding Azure Monitor Logs to Event Hub
To add Azure monitor logs to an Event Hub:
1. In Microsoft Azure, portal.azure.com , search for and select the Monitor service.
2. Click Activity log and then click Export Activity Logs.
3. For the Diagnostic settings, select a Subscription and then click Add diagnostic
setting.
4. In the Diagnostic setting window:
a. Enter a Diagnostic setting name.
b. Select the Logs you want to stream.
c. Select the check box for Stream to an event hub.
d. For where you want to route the logs, select the Subscription, Event hub
namespace, optional Event hub name, and Event hub policy name.

5. Click Save.
Adding the Connector in Stellar Cyber
With the access information handy, you can add an Azure Event Hub connector in Stellar Cyber:
1. Log in to Stellar Cyber.
2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.
3. Click Create and select Connector.
The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.
4. Choose PaaS from the Category dropdown.
5. Choose Azure Event Hub from the Type dropdown.
The asterisk (*) indicates a required field.
6. For this connector, the supported Function is Collect, which is enabled already.
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
12. Enter the Azure Event Hub Name you noted above.
13. Enter the Connection String you noted above.
14. Enter the Consumer Group you noted above.
15. Select one or more Event Source. The available sources are:
Azure Activity Log
Azure Bastion
Azure Firewall
Azure Keyvault
Azure Security Center
Azure Security Groups
Azure SQL Server (includes AuditEvent log )
Azure Storage
Azure Synapse Workspace
Azure Web Application Firewall
Microsoft Defender for Cloud
Microsoft Graph Activity Log
Microsoft Sentinel
Structured Azure Firewall Log
 The order of the event sources in the above list dictates the content type
that will be matched first. The event source that was added first will match
first.
Custom Event Source (choose only if using optional Custom Event Sources)
16. (Optional) Use Custom Event Sources to set up customized event sources that pull
specific types of data from Azure Event Hub.

 For guidelines on how to create a custom content type, see Creating a Custom
Content Type.
a. Select Custom Event Source from the Event Source dropdown menu.
b. In the Custom Event Sources (optional) area, enter a name for the Event
Source Name that is unique within the connector. The name will be used for
setting the msg_class in the following format: azure_<customer defined
name>.
c. Enter a Regex, a Regular Expression that defines a unique string expected in
the data, for example, abc*. The connector looks in Azure Event Hub and pulls
any data that matches the Regex.
d. Click the + sign to add another custom event source. The recommended
maximum is 10.
 The order of the event sources in the list dictates the content type that will
be matched first. The custom event source that appears in the list at the
top will match first, meaning that the one added last will match first.
e. Click the trash can to delete a custom event source.
17. Click Next. The final confirmation tab appears.
18. Click Submit.
The new connector is immediately active.
Creating a Custom Content Type
The following are guidelines to create a custom content type using Custom Event Sources in
the Azure Event Hub connector.
Collect the log sample from Azure Event Hub directly to understand the log content,
because the Stellar Cyber data enrichment and normalization occur after the custom
parser matching of the configured Regex from the raw data retrieved from Azure Event
Hub.

If you are not able to do the above step, then you can use the AzureAllLogs content
type to study the data content.
For debugging purposes, you can optionally type AzureAllLogs into the Event Source
dropdown menu and press Enter. The content type will display as follows:
 See the following AzureAllLogs Format Limitation.
The AzureAllLogs content type collects all logs available to the configured credentials.
The logs collected this way have the msg_class: azure_all.
 Keep in mind that AzureAllLogs is a debugging content type and is not usually
used by the customer in normal cases. It may cause conflicting field types in
Elasticsearch and thus data loss, because all logs that do not match the existing
parser will send data under this content type.
To create the custom content type:
a. Select Custom Event Source from the Event Source dropdown menu.
b. In the Custom Event Sources (optional) area, enter a name for the Event
Source Name that is unique within the connector.
c. Enter a unique Regex applied to this custom event source only. It can be
either a field or value because each event is a string (body_as_str) before it
is converted to a valid JSON object. So use a unique value, a unique field, or
both, or multiple values/fields to identify the event source. For information on
body_as_str, see the Microsoft documentation .
To verify the logs ingested under the custom event source, use the msg_class as an
indicator. The msg_class for a custom event source has the following format:
azure_<customer defined name>, for example, azure_<source_name>.
AzureAllLogs Format Limitation
The data from Azure sources is expected to have the following format:
{'records': [...]}
which is an object with the key 'records' and the value as a list of objects.
The schema for data coming from another source with another format cannot be guaranteed to
be parsed correctly.
Check your source of Azure Event Hub data and use the expected format in the raw event logs.
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

HTTP E HTTP Stan
rror dard Error Explanation Recommendation
Code Name
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
is exceeded. query.
If this occurs unexpectedly or too often, work with
your API provider to investigate the server limits,
user licensing, or quotas.
For a full list of codes, refer to HTTP response status codes .
Verifying Ingestion
To verify ingestion:
1. Select Threat Hunting.
The Interflow Search tab appears.
2. Change the Indices for the type of content you collected:
For the majority of content types, change the Indices to Syslog.
For Microsoft Defender for Cloud only, change the Indices to Windows
Events.
For Azure Firewall and Structured Azure Firewall Log only, change the
Indices to Traffic.
The table immediately updates to show ingested Interflow records.
 For custom event sources, the unique name provided during configuration displays in
Threat Hunting with a msg_class containing an azure prefix. For example, if the unique
name is test, the msg_class in Threat Hunting is azure_test.

Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  