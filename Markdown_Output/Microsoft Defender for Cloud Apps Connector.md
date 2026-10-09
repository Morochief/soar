Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Microsoft Defender for Cloud Apps
Connectors

This connector allows Stellar Cyber to ingest logs from Microsoft Defender for Cloud Apps and
add the records to the data lake. This connector integrates with the Microsoft Defender for Cloud
Apps API to query activities and alerts.

Microsoft Defender for Cloud Apps requires one of the following Microsoft 365 Enterprise Plan
subscriptions: E5, E5 Security, or E5 Compliance. To learn about plans, refer to Microsoft 365
licensing datasheet  under Next steps.

 GCC Government Plan and GCC High Government Plan are not supported by this

connector at this time.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Microsoft Defender for Cloud
Apps

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Activities

Windows Events

msg_class:

Content Type

Index

Locating Records

Alerts

microsoft_defender
_for_cloud_apps_ac
tivities

microsoft_defender
_for_cloud_apps_al
erts

msg_origin.source:

microsoft_defender
_for_cloud_apps

msg_origin.vendor:

microsoft_defender

msg_origin.category:

saas

 If the Audit General content type is set up in the Office 365 connector with the same account, there

may be duplicates when reporting Activities.

Domain

<API URL>

where <API URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Microsoft Defender for Cloud Apps to get the raw alerts that are stored
in the Windows Events index. Select the Alerts content type.

Stellar Cyber maps Microsoft Defender for Cloud Apps alerts. The alerts are read from the Windows
Events index, enriched with Stellar Cyber fields, and mapped (with de-duplication) to the Alerts index.

Deduplication is by tenantid and microsoft_defender_for_cloud_apps._id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

API URL, Tenant ID, Client ID, and Client Secret

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Windows Events index,
use the query: msg_class: microsoft_defender_for_cloud_apps_alerts AND
msg_origin.source: microsoft_defender_for_cloud_apps

Adding a Microsoft Defender for Cloud Apps Connector
To add a Microsoft Defender for Cloud Apps connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Microsoft Defender for Cloud Apps
Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Microsoft
Defender for Cloud Apps credentials:

API URL

Tenant ID

Client ID

Client Secret

Obtaining the API URL

To obtain the API URL for your tenant:

1. In the Microsoft Defender Portal (https://security.microsoft.com/ ), select Settings and

then select Cloud Apps.

2. Under System, select About.

3. The API URL is displayed on the right side of the About screen.

Creating an App

Follow the procedure in the link below to create an app and grant permissions to the app:

https://learn.microsoft.com/en-us/defender-cloud-apps/api-authentication-application 

Make note of the following:

Client Secret

 Store the secret value in a safe location. It cannot be retrieved later.

Directory (tenant) ID or Tenant ID

Application (client) ID or Client ID

Adding the Connector in Stellar Cyber
To add a Microsoft Defender for Cloud Apps connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SaaS from the Category dropdown.

5. Choose Microsoft Defender for Cloud Apps from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

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

12. Enter the API URL you noted above in Obtaining the API URL.

13. Enter the Tenant ID you noted above in Creating an App.

14. Enter the Client ID you noted above.

15. Enter the Client Secret you noted above.

16. Choose the Interval (min). This is how often the logs are collected.

17. Choose the Content Type you would like to collect. The logs for Activities and Alerts

are supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

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

Did you configure the connector correctly?

Request

connector configuration.

401

Unauthorize

d

This error occurs when an authentication credential is

Did you enter your credentials correctly?

invalid or when a user does not have sufficient

privileges to access a specific API.

Are your credentials expired?

403

Forbidden

This error occurs when the permission or scope is not

correct in a valid credential.

Are your credentials entitled or licensed for that

specific resource?

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

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

