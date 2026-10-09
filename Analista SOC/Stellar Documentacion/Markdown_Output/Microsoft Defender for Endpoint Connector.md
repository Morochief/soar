Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Microsoft Defender for Endpoint Connectors

Microsoft Defender for Endpoint connectors allow Stellar Cyber to ingest logs or issue response actions with
Microsoft Defender for Endpoint and add the records to the data lake. There can be any number of Microsoft
Defender for Endpoint connectors active.

This connector requires one of the following Microsoft endpoint security plans: Microsoft Defender for Endpoint Plan 1
(P1) or Microsoft Defender for Endpoint Plan 2 (P2). To learn about plans, refer to Compare Microsoft endpoint
security plans .



There may be two data sources for third party native alerts if you have integrated both Microsoft Defender for
Endpoint (this connector) and Windows Defender Antivirus (free version).

If a tenant is using the Microsoft Defender for Endpoint connector and the status of the connector in System |
INTEGRATIONS | Connectors is green, alerts from Windows Defender Antivirus will be suppressed in order to
remove duplicate logs. If the status of the connector is not green, alerts from Windows Defender Antivirus will
not be suppressed.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data when the ingestion
volume is large, which potentially can lead to data loss. This can happen when the processing capacity of the
collector is exceeded.

Connector Overview: Microsoft Defender for Endpoint

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alerts

Host

Vulnerabilities

Index

Syslog

Locating Records

msg_class:

Assets (for Host)

microsoft_defender_alerts

Scans (for
Vulnerabilities)

microsoft_defender_host

microsoft_defender_vulnerabilities

msg_origin.source:

microsoft_defender

msg_origin.vendor:

microsoft

msg_origin.category:

endpoint

Domain

https://login.microsoftonline.com

<API Endpoint URL>

where <API Endpoint URL> is a variable from the configuration of this connector

Response Actions

Action

Contain Host

(for Host and Alerts)

Required Fields

microsoft_defender.id (for Host data)

microsoft_defender.machineId (for Alerts data)

The required permission for response actions is Machine.Isolate.

Third Party Native Alert Integration Details

The Microsoft Defender ATP alerts are mapped to the Stellar Cyber Syslog Index. Select the Alerts content type.

Deduplication is by tenantid, host.ip, host.name, and microsoft_defender.id.

For details, see Integration of Third Party Native Alerts.

For full alert integration of Microsoft Defender for Endpoint, the following licenses are required:

Microsoft Defender for Endpoint Plan 1 (P1)

Microsoft Defender for Business

Required Credentials and Configurations

Office 365 Subscription Plan, API Endpoint URL, Client ID with permissions enabled (for permissions see, Creating an
App in Microsoft Entra ID), Directory ID, and Client Secret

Locating Records

Use the following to query for records:

msg_origin.source: microsoft_defender

msg_class: microsoft_defender_alerts

To search the alerts, use the query: msg_class: microsoft_defender_alerts AND
(microsoft_defender.detectionSource: WindowsDefenderAv OR microsoft_defender.detectionSource:
WindowsDefenderAtp)

Adding a Microsoft Defender for Endpoint Connector
To add a Microsoft Defender for Endpoint connector:

1. Create an app
2. Gather information
3. Add the connector in Stellar Cyber
4. Test the connector
5. Verify ingestion

Creating an App in Microsoft Entra ID
You must create an app in Microsoft Entra ID (formerly Azure Active Directory) that can access Microsoft Defender for
Endpoint. Refer to the following article: https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-
defender-atp/exposed-apis-create-app-webapp .

Enable the following role for the API:

Vulnerability.Read.All

Also enable the following roles for the application:

Machine.Isolate

Event.Write

Machine.Scan

Url.Read.All

Ip.Read.All

Ti.ReadWrite

User.Read.All

Machine.ReadWrite.All

Machine.StopAndQuarantine

Alert.Read.All

File.Read.All

Machine.Read.All

Alert.ReadWrite.All

AdvancedQuery.Read.All

Gathering the Microsoft Entra ID Information
The following is the Microsoft Entra ID (formerly Azure AD) information to gather as you create the app:

API Endpoint URL—this is the API URL for the server closest to your region:

https://api-us.securitycenter.microsoft.com

https://api-eu.securitycenter.microsoft.com

https://api-uk.securitycenter.microsoft.com

https://au.api.securitycenter.microsoft.com

https://swa.api.securitycenter.microsoft.com

Client ID—this is the Application (client) ID

Directory ID—this is the Directory (tenant) ID

Client Secret—this is the token you generated

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Microsoft Defender for Endpoint connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab cannot be changed
after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Microsoft Defender for Endpoint from the Type dropdown.

The asterisk (*) indicates a required field.

6. Choose the Function: Collect to collect logs; Respond to contain hosts. If you want Respond, choose both
Collect and Respond because Respond uses fields present in Alerts and Host data to perform the Contain
Host action.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this tenant name. If you

create an automated response action, note that the Tenant for this connector (Collect and Respond) must be
within the Tenant for the action. You can use All Tenants or match specific tenants.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information, see Managing Log

Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Select the applicable Office 365 Subscription Plan from the menu and the API Endpoint URL:

Enterprise Plan—Select the API Endpoint URL for the server closest to your region for the best
performance as listed in Gathering the Microsoft Entra ID Information

GCC Government Plan—Select the API Endpoint URL (the URL is: https://api-
gcc.securitycenter.microsoft.us)

GCC High Government Plan—Select the API Endpoint URL (the URL is: https://api-
gov.securitycenter.microsoft.us)

DoD Government Plan—Select the API Endpoint URL (the URL is: https://api-
gov.securitycenter.microsoft.us)

To learn about Office 365 government plans, refer to the following documentation:
https://learn.microsoft.com/en-us/defender-endpoint/gov?view=o365-worldwide 

13. Enter the Client ID you noted above.

14. Enter the Directory ID you noted above.

15. Enter the Client Secret you noted above.

16. Enter the Interval (min). This is how often the logs are collected.

 If data is not being pulled, you can increase the interval, for example, to 10 minutes.

17. (Optional) Choose the Lookback Time (hr). This is how far back in time, in hours, the connector will pull
data when it either starts or restarts. (Configuring this field has no impact when the connector is running,
only when the connector is started for the first time or when it is stopped and restarted.) This field is for the
Alerts and Vulnerabilities content types since the Host content type already looks back in time. The default

is 720 hours, or one month. The minimum is 1 and maximum has no limit.

 Use caution if setting the Lookback Time to a high value. It may take a long time to pull the data and

may result in old alert types being retriggered.

18. Choose the Content Type you would like to collect. The logs for Alerts, Host, and Vulnerabilities are

supported.

 The Vulnerabilities content type is sent to the Assets | Asset Analytics page, which shows the

relationship between assets and vulnerabilities.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Testing the Connector
When you add (or edit) a connector, we recommend that you run a test to validate the connectivity parameters you
entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60 seconds for new or

modified configuration details to be propagated to the sensor before performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure result. A successful
test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by using the X button. If the
test fails, you can select the   button from the same row to review and correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the connector status, but if

issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP Er

HTTP Standar

ror Code

d Error Name

Explanation

Recommendation

400

Bad Request

This error occurs when there is an error in the connector

Did you configure the connector correctly?

configuration.

401

Unauthorized

This error occurs when an authentication credential is invalid or

Did you enter your credentials correctly?

when a user does not have sufficient privileges to access a

Are your credentials expired?

specific API.

403

Forbidden

This error occurs when the permission or scope is not correct in a

valid credential.

Are your credentials entitled or licensed for that specific

resource?

Did you enter your credentials correctly?

Do you have the required role or permissions for that

credential?

404

429

Not Found

This error occurs when a URL path does not resolve to an entity. Did you enter your API URL correctly?

Too Many

Requests

This error occurs when the API server receives too much traffic or

The server or user license/quota will eventually recover. The

if a user’s license or entitlement quota is exceeded.

connector will periodically retry the query.

If this occurs unexpectedly or too often, work with your API

provider to investigate the server limits, user licensing, or

quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Alerts, change the Indices to Syslog.

For Host, change the Indices to Assets. Hosts discovered through this connector show Microsoft
Defender for Endpoint as a data source.

For Vulnerabilities, change the Indices to Scans.

The table immediately updates to show ingested Interflow records.

If you configured the connector Respond actions, refer to External Actions: Contain Host to understand how to
work with the Contain Host feature.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

