Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Google Workspace Connectors

This connector allows Stellar Cyber to collect data from external sources and add the records to
the data lake.

Integrating Google Workspace with Stellar Cyber provides real-time visibility into security events
and alerts across cloud and on-premise environments, enabling organizations to effectively
monitor and respond to security incidents. Stellar Cyber's advanced security analytics and
machine learning algorithms provide real-time threat detection and response capabilities, while
also providing advanced identity and access management capabilities to manage user access
and security policies.

You must have one connector for every Google Workspace account to be monitored.

 This connector is improved to use less memory. Under certain scenarios if there is an error

reaching the third-party API, some duplicate messages may be sent.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Google Workspace

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

Admin

Linux Events

msg_class:

Content Type

Index

Locating Records

AWS Events (Cloudtrail)

gsuite

gsuite_alert

msg_origin.source:

gsuite

msg_origin.vendor:

gsuite

msg_origin.category:

office_suite (for
alerts, for all content
types on SaaS)

Alert

Calendar

Chat

Drive

Gplus

Groups

Login

Mobile

Rules

SAML

Token

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests alerts from Google Workspace to get the raw alerts that are stored in the Linux
Events index. Select the Alert content type.

Stellar Cyber maps Google Workspace alerts . The alerts are read from the Linux Events index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by org_id, tenantid, metadata.customerId, source, type, and metadata.alertId.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

API Scopes and Service Account Key File

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Linux Events index, use
the query: msg_class:gsuite_alert AND _exists_: source

Adding a Google Workspace Connector
To add a Google Workspace connector:

1. Enable the Google Admin SDK
2. Create a Google service account
3. Create an API key
4. Add the client ID with OAuth scopes
5. Add the connector in Stellar Cyber
6. Test the connector
7. Verify ingestion

Enabling the Google Admin SDK
Before you create a service account, you must enable the Admin SDK:

 Use our example as a guideline, as you might be using a different software version.

1. Go to https://console.cloud.google.com .

2. Click  to display the menu.

3. Choose APIs & Services > Library. The API Library page appears.

4. Search for admin sdk. The Admin SDK page should be at the top of the results.

5. Click Admin SDK. The Admin SDK page appears.

6. Click Enable. The SDK is enabled.

7. Search again, this time for alert center api. and enable that.

Creating a Google Service Account
With the SDK enabled, you can create a service account:

1. Navigate back to the main menu of https://console.cloud.google.com. 

2. Click  to display the navigation pane.

3. Choose IAM & Admin > Service Accounts. The service accounts appear.

4. Click Create Service Account. The Service account details page appears.

5. Enter a name for the account.

6. Enter a description.

7. Click Create.

8. Optionally, grant permissions.

9. Click Continue.

10. Optionally, grant access.

11. Click Done. The account is created and displayed on the Service account details

page.

12. Copy the Oath2 Client ID You will use this as the Client ID when adding API scopes in

the Stellar Cyber connector.

Creating an API Key
With a service account, you can now create an API key:

1. Go to https://console.cloud.google.com .

2. Click  to display the menu.

3. Choose IAM & Admin > Service Accounts. The service accounts appear.

4. Select the service account you created.

5. Click  for that account.

6. Select Manage keys from the menu. The Keys screen appears.

7. Click the Add Key menu and select Create new key.

8. Select JSON.

9. Click Create. The JSON file is downloaded. Keep this file safe, as you cannot recover
the key if this file is lost. You will upload this file to Stellar Cyber when configuring the
connector.

10. Click Close.

11. Exit the Keys screen and return to the Service Account Details page.

12. Click  for the account again, and select Manage Details.

13. The Service Account details screen appears.

14. Make note of the Unique ID. You will use this as the Client Name when adding the

service account to Google Workspace.

Adding the Client ID with OAuth Scopes
To add the Client ID with OAuth scopes:

1. Go to https://admin.google.com/ac/home .
2. Click  to display the menu.

3. Choose Security > API Controls > Domain-wide Delegation . The API

clients appear.

4. Click Add New. The Add a new client ID screen appears.

5. Enter the Unique ID that you copied earlier from the service account as the Client ID.

6. Enter the OAuth scopes to be used with the Stellar Cyber connector.

For Alert reports, include this
scope: https://www.googleapis.com/auth/apps.alerts

For Application reports, include this
scope: https://www.googleapis.com/auth/admin.reports.audit.reado

nly

(The application types are listed in the Stellar Cyber connector configuration
dialog.)

7. Click Authorize.

You now have an authorized Client ID with OAuth scopes.

Adding the Connector in Stellar Cyber
With the Google service account set up and the API key ready, you can add a Google
Workspace connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SaaS from the Category dropdown.

5. Choose Google Workspace (Gsuite) from the Type dropdown.

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

12. Enter the Admin Email for the account administrator (not the email created by Google

for the service account).

13. For API Scopes, enter the OAuth scopes you added in Adding the Client ID with OAuth

Scopes. Stellar Cyber provides the following scopes by default:

For Alert reports, include this
scope: https://www.googleapis.com/auth/apps.alerts

 The alert scope is required if you would like Stellar Cyber to integrate the

Gmail Phishing alert to the XDR Kill Chain.

For Application reports, include this
scope: https://www.googleapis.com/auth/admin.reports.audit.reado
nly

Separate additional scopes with commas.

14. Upload the Service Account Key File, which is the API file you downloaded in Creating

an API Key.

15. Choose the Interval (min). This is how often the logs are collected.

16. (Optional) Choose the Query Delay (min).

17. Choose the App you want to collect by selecting them from the dropdown menu.

Content Type

(App Name)

Admin

Report type

Required Scope

Admin Console activities of all

of your account's administrator

https://www.googleapis.com/

auth/admin.reports.audit.rea

activity

donly

https://www.googlea

pis.com/auth/apps.al

erts

Content Type

(App Name)

Alert

Calendar

Chat

Drive

Gplus

Groups

Login

Mobile

Rules

SAML

Token

Report type

Required Scope

Google Alert Center reports

Google Calendar application's

activity audit reports

Chat activity audit reports

Google Drive application's

activity reports

Google+ / Currents application

activity reports

Google Groups audit reports

Login audit events

Device audit events

Reports for rule related events

SAML audit reports

OATH Token Audit events

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active. It does not collect any historical logs.

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

 An error displays If you use an email address that doesn't have privileges to add the

connector, or if you created the service account but it is not yet authorized.

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Linux Events or AWS Events.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

