Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Microsoft Graph Security API Connectors

This connector allows Stellar Cyber to ingest logs from Microsoft Graph Security API and add the records to
the data lake. It integrates with the Microsoft Graph API to ingest alert data.

Refer to the rate limit information in the Microsoft documentation . The global usage rate limit is 130,000
requests per 10 seconds.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data when the

ingestion volume is large, which potentially can lead to data loss. This can happen when the processing
capacity of the collector is exceeded.

Connector Overview: Microsoft Graph Security API

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alert

Attack Simulation

Incident

Index

Locating Records

Windows Events

msg_class:

microsoft_graph_securi
ty_api_alert

microsoft_graph_securi
ty_api_attack_simulati

on

microsoft_graph_securi
ty_api_incident

msg_origin.source:

microsoft_graph_securi
ty_api

msg_origin.vendor:

Content Type

Index

Locating Records

microsoft_graph_securi
ty_api

msg_origin.category:

xdr

email (used for normalization
of the Attack Simulation

content type only)

Domain

https://graph.microsoft.com/

Response Actions

N/A

Third Party Native Alert Integration Details

Microsoft Defender XDR

This connector ingests logs from Graph Security API to get the raw alerts that are stored in the Syslog index. Select the
Alert content type.

Stellar Cyber maps Microsoft Defender XDR alerts. The alerts are read from the Syslog index, enriched with Stellar
Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication uses the microsoft_graph_security_api.id field.

For details, see Integration of Third Party Native Alerts.

Microsoft Defender for Cloud (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts that are stored in the Windows Events index.
Select the Alert content type.

Stellar Cyber maps Microsoft Defender for Cloud alerts. The alerts are read from the Windows Events index, enriched
with Stellar Cyber fields, and mapped to the Alerts index.

There is no deduplication of alerts between Microsoft Defender for Cloud and Microsoft Defender for Cloud (Graph
Security API).

For details, see Integration of Third Party Native Alerts.

Microsoft Defender for Endpoint (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts that are stored in the Windows Events index.
Select the Alert content type.

Stellar Cyber maps Microsoft Defender for Endpoint alerts. The alerts are read from the Windows Events index, enriched
with Stellar Cyber fields, and mapped to the Alerts index.

There is no deduplication of alerts between Microsoft Defender ATP and Microsoft Defender for Endpoint (Graph
Security API).

For details, see Integration of Third Party Native Alerts.

Microsoft Defender for Cloud Apps (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft Defender for Cloud Apps alerts. The alerts are read from the Windows Events index,
enriched with Stellar Cyber fields, and mapped to the Alerts index.

There is no deduplication of alerts between Microsoft Defender for Cloud Apps and Microsoft Defender for Cloud Apps
(Graph Security API).

For details, see Integration of Third Party Native Alerts.

Microsoft App Governance (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft App Governance alerts. The alerts are read from the Windows Events index, enriched with
Stellar Cyber fields, and mapped to the Alerts index.
Deduplication is by tenantid and microsoft_graph_security_api.id.

For details, see Integration of Third Party Native Alerts.

Microsoft Data Loss Prevention (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft Data Loss Prevention alerts. The alerts are read from the Windows Events index, enriched
with Stellar Cyber fields, and mapped to the Alerts index.
Deduplication is by tenantid and microsoft_graph_security_api.id.

For details, see Integration of Third Party Native Alerts.

Microsoft Defender for Identity (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft Defender for Identity alerts. The alerts are read from the Windows Events index, enriched
with Stellar Cyber fields, and mapped to the Alerts index.
Deduplication is by tenantid and microsoft_graph_security_api.id.

For details, see Integration of Third Party Native Alerts.

Microsoft Defender for Office 365 (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft Defender for Office 365 alerts. The alerts are read from the Windows Events index,
enriched with Stellar Cyber fields, and mapped to the Alerts index.
Deduplication is by tenantid and microsoft_graph_security_api.id.

For details, see Integration of Third Party Native Alerts.

Microsoft Threat Intelligence (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft Threat Intelligence alerts. The alerts are read from the Windows Events index, enriched
with Stellar Cyber fields, and mapped to the Alerts index.
Deduplication is by tenantid and microsoft_graph_security_api.id.

For details, see Integration of Third Party Native Alerts.

Microsoft Entra ID Protection (Graph Security API)

This connector ingests logs from Graph Security API to get the raw alerts are stored in the Windows Events index. Select
the Alert content type.

Stellar Cyber maps Microsoft Entra ID Protection alerts. The alerts are read from the Windows Events index, enriched
with Stellar Cyber fields, and mapped to the Alerts index.
Deduplication is by tenantid and microsoft_graph_security_api.id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Tenant ID, Client ID, and Password

Locating Records

Microsoft Defender XDR

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the query: msg_class:
microsoft_graph_defender_xdr_alert and _exists_: event.threat.name

Microsoft Defender for Cloud (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_defender_for_cloud_alerts AND msg_origin.source: microsoft_graph_security_api AND

_exists_: event.threat.name.

Microsoft Defender for Endpoint (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_defender_for_endpoint_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name.

Microsoft Defender for Cloud Apps (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_defender_for_cloud_apps_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name.

Microsoft App Governance (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_app_governance_alerts AND msg_origin.source: microsoft_graph_security_api AND _exists_:
event.threat.name AND NOT microsoft_graph_security_api.status: resolved.

Microsoft Data Loss Prevention (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_data_loss_prevention_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name AND NOT microsoft_graph_security_api.status: resolved.

Microsoft Defender for Identity (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_defender_for_identity_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name AND NOT microsoft_graph_security_api.status: resolved.

Microsoft Defender for Office 365 (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_defender_for_office365_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name AND NOT microsoft_graph_security_api.status: resolved.

Microsoft Threat Intelligence (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
microsoft_threat_intelligence_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name AND NOT microsoft_graph_security_api.status: resolved.

Microsoft Entra ID Protection (Graph Security API)

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
azure_ad_identity_protection_alerts AND msg_origin.source: microsoft_graph_security_api AND
_exists_: event.threat.name AND NOT microsoft_graph_security_api.status: resolved.

Adding a Microsoft Graph Security API Connector
To add a Microsoft Graph Security API connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Microsoft Graph Security API Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Microsoft Graph Security
API credentials:

Tenant ID—The tenant from which to request permission, also known as the Directory ID

Client ID—The client ID, also known as the Application ID that the app registration portal assigned
when the app was registered

Password—The password that you generated for your app in the app registration portal, also known
as the Client Secret

Registering an Application

To register an application, follow the guidance in the Microsoft documentation :

1. With an administrative account, log in to Microsoft Entra admin center and select Entra ID in the

navigation pane.

2. Select App registrations. A page for adding and managing App registrations is displayed.

3. Click New registration. A pane is opened for your new parameters.

4. Enter a display Name for your application.

5. Choose a supported account type. Accounts in this organizational directory only is typical.

6. The Redirect URI setting is not required.

7. Click Register. The initial app registration is completed and a summary of it is displayed.

8. Copy the following details to a file:

Display Name

Application (client) ID, which is the Client ID you will use to add the connector in Stellar
Cyber

Directory (tenant) ID, which is the Tenant ID you will use to add the connector in Stellar
Cyber

Configuring the Application

To configure the application by setting permissions and obtaining the client secret, follow the guidance in the
Microsoft documentation :

1. To set the permissions for your application, in the navigation pane under Manage, select

API Permissions. Click Add a permission. The Request API permissions pane appears. Click
Microsoft Graph.

a. Click Application permissions.

 You can type in the Search box to find permissions.

b. Set the following permissions for the logs you want to collect.

Permission

Description

SecurityAlert.Read.All

Read all security alerts

SecurityEvents.Read.All

Read your organization's security events

SecurityIncident.Read.All

Read all security incidents

AttackSimulation.Read.All

Read attack simulation data of an organization

c. Click Add permissions. The API permissions page redisplays with your added

permissions.

d. If you are the super admin, grant the permissions. Select the checkmark to Grant admin

consent for <account name>.

Otherwise, wait for the super admin to grant them.

 Make sure that the permissions are granted. If you add the connector before

permissions are granted, the process fails.

When the permissions are granted successfully, there will be green checkmarks in the
Status column.

2. To add a client secret to the application, select Certificates & secrets and New client secret.

a. Add a Description and select an expiry.

b. Click Add. The client secret is displayed in the Client secrets list.

c. Copy the Value. This is the Password you will use to add the connector in Stellar Cyber.

Supporting Microsoft Defender for Identity

This connector also supports identity-based security alert and incident ingestion.

To get Microsoft Defender for Identity events from Microsoft Graph Security API, ensure that Microsoft
Defender for Identity is properly configured or integrated with Microsoft 365 Defender . Refer to the section
on alerts and incidents in Use the Microsoft Graph security API .

Alert ingestion needs the following permissions (refer to List alerts_v2 ):

Least privileged permissions: SecurityAlert.Read.All

Higher privileged permissions: SecurityAlert.ReadWrite.All

Incident ingestion needs the following permissions (refer to List incidents ):

Least privileged permissions: SecurityIncident.Read.All

Higher privileged permissions: SecurityIncident.ReadWrite.All

Adding the Connector in Stellar Cyber
To add a Microsoft Graph Security API connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab cannot be
changed after you add the connector.

4. Choose Extended Detection & Response from the Category dropdown.

5. Choose Microsoft Graph Security API from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as tenantname-
connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this tenant name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information, see Managing

Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Select the applicable Microsoft Subscription Plan from the menu:

Enterprise Plan

GCC Government Plan

GCC High Government Plan

DoD Government Plan

To learn about US government plans, refer to the following Microsoft documentation: Microsoft
Defender XDR for US Government customers .

13. Enter the Tenant ID you noted above in Obtaining Microsoft Graph Security API Credentials.

14. Enter the Client ID you noted above.

15. Enter the Password you noted above.

16. Choose the Content Type you would like to collect. The logs for Alert , Attack Simulation, and

Incident are supported.

17. Choose the Interval (min). This is how often the logs are collected.

18. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL certificate

verification. Only disable SSL certificates if you have a necessary reason to, otherwise, it is not a
good security practice and may expose the connection to security risks.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Microsoft Graph Security API connector

tests that the Tenant ID, Client ID, and Password are correct and data requests for the requested content
type returns successful responses.

When you add (or edit) a connector, we recommend that you run a test to validate the connectivity
parameters you entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60 seconds for new or

modified configuration details to be propagated to the sensor before performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure result. A
successful test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by using the X
button. If the test fails, you can select the   button from the same row to review and correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the connector status,

but if issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP Er

HTTP Standa

ror

rd Error

Explanation

Code

Name

Recommendation

400

Bad Request This error occurs when there is an error in the connector

Did you configure the connector correctly?

configuration.

401

Unauthorized

This error occurs when an authentication credential is invalid

Did you enter your credentials correctly?

or when a user does not have sufficient privileges to access a

Are your credentials expired?

specific API.

Are your credentials entitled or licensed for that specific

resource?

403

Forbidden

This error occurs when the permission or scope is not correct

Did you enter your credentials correctly?

in a valid credential.

Do you have the required role or permissions for that

credential?

404

Not Found

This error occurs when a URL path does not resolve to an

Did you enter your API URL correctly?

entity.

429

Too Many

Requests

This error occurs when the API server receives too much

The server or user license/quota will eventually recover.

traffic or if a user’s license or entitlement quota is exceeded.

The connector will periodically retry the query.

If this occurs unexpectedly or too often, work with your

API provider to investigate the server limits, user

licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Windows Events.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

