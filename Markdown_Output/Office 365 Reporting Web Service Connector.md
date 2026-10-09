Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Office 365 Reporting Web Service
Connectors

This connector allows Stellar Cyber to ingest logs from Office 365 Reporting Web Service and
add the records to the data lake. It integrates with the Microsoft Reporting Web Service to query
Message Trace data.

 Microsoft has announced the deprecation of the legacy Message Trace Reporting Web

Service on April 8, 2026 and announced the General Availability of the New Message Trace
in Exchange Online . It is recommended that you migrate any existing Office 365 Reporting
Web Service connectors in Stellar Cyber to Microsoft Graph Message Trace connectors.

Note the following:

This connector is set to start retrieving data from 24 hours ago due to a limitation from
Microsoft that data may be delayed by up to 24 hours before they appear in a report.
The connector ingestion interval is every 5 minutes.

This connector gets 2000 records for each time window query. (By default, the window
is 10 minutes range.)

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Office 365 Reporting Web Service

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Message Trace

Windows Events

msg_class:

office365_reportin
gwebservice_messag
e_trace

msg_origin.source:

office365_reportin
gwebservice

msg_origin.vendor:

microsoft

msg_origin.category:

saas

Domain

<Authentication Endpoint>

where <Authentication Endpoint> is a variable from the configuration of this connector and
will be one of the following, based on the Subscription Plan:

https://login.microsoftonline.us

https://login.microsoftonline.de

https://login.partner.microsoftonline.cn

https://login.microsoftonline.com

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Authentication Endpoint, Directory ID, Application ID, and API Access Key

Adding an Office 365 Reporting Web Service Connector
To add an Office 365 Reporting Web Service connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Office 365 Reporting Web Service Credentials

Before you configure the connector in Stellar Cyber, you must obtain the following Office 365
Reporting Web Service credentials:

Authentication Endpoint—The authentication endpoint, which you can select from the
dropdown menu.

Directory ID—The tenant from which to request permission, also known as the Tenant
ID.

Application ID—The ID that the app registration portal assigned when the app was
registered, also known as the Client ID.

API Access Key—The API access key or client secret that you generated for your app in
the app registration portal, also known as the Client Secret.

For details, see Registering the Application and Obtaining Permissions.

Registering the Application

Follow the guidance in the Microsoft documentation  to get started with Reporting Web
Service.

To register the application in Microsoft Entra ID (formerly Azure Active Directory) and obtain the
Tenant ID, Client ID, and Client Secret:

1. Log in as an administrative user to the Azure Management Portal at

https://portal.azure.com  and sign in with the credentials for the tenant subscribed to
Office 365.

2. From Azure services, select Microsoft Entra ID.

3. In the navigation pane, select App registrations.

4. Click New registration.

5. In Register an application, enter a Name.

6. Choose a supported account type. For Single tenant, select Accounts in this

organizational directory only.

7. For Redirect URI (optional), select Web, and enter http://localhost as the Web

URL.

8. Click Register.

9. Copy the Application (client) ID and Directory (tenant) ID. You will use them to

configure the connector in Stellar Cyber.

10. In the navigation pane, click Certificates & secrets.

11. Click New client secret.

12. In Add a client secret, enter a Description and choose an expiration.

13. Click Add.

14. Copy the Value. You will use this as the API Access Key to configure the connector in

Stellar Cyber.

 Store the value in a safe location. It cannot be retrieved later.

Obtaining Permissions

First, assign the Security Reader role to the created application.

1. Log in to the Microsoft Entra ID admin center.

2. Navigate to Identity > Roles & admins > Roles & admins.

3. Search or scroll for the Security Reader role in the Administrative roles and select it.

4. Click Add assignments and select the users or groups you want to assign to this role.

5. Click Add to assign the role.

Next, add API permissions for your application.

1. In the navigation pane, select API Permissions.

2. Click Add a permission.

3. In Request API permissions, select the APIs my organization uses tab.

4. Search or scroll for Office 365 Exchange Online, and select it.

Next, select Application Permissions:

1. Select Application Permissions to allow the application to run as a background

service without a signed-in user.

2. Search for and select ReportingWebService.Read.All.

3. Click Add permissions.

Then, grant admin consent.

1. After adding permissions, there is a banner at the top of the API Permissions page that

says the permissions require admin consent.

2. In the API permissions window, go to the Grant admin consent section.

3. If you are the Office 365 super admin, grant the permissions. Select the checkmark to

Grant admin consent for <tenant name>.

4. Confirm the consent by clicking Yes.

Finally, verify the permissions.

1. After granting admin consent, the status for the permissions will update to Granted for <

tenant name>.

2. Ensure that the Application permission (ReportingWebService.Read.All) is correctly

listed and granted.

Adding the Connector in Stellar Cyber
To add an Office 365 Reporting Web Service connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SASE from the Category dropdown.

5. Choose Office 365 Reporting Web Service from the Type dropdown.

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

12. Enter the Authentication Endpoint you noted above in Obtaining Office 365 Reporting

Web Service Credentials.

13. Enter the Directory ID you noted above.

14. Enter the Application ID you noted above.

15. Enter the API Access Key you noted above.

16. Choose the Interval (min). This is how often the logs are collected.

17. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

18. Choose the Content Type you would like to collect. The logs for Message Trace are

supported.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Office 365 Reporting Web

Service connector tests that the Authentication Endpoint, Directory ID, Application ID, and
API Access Key are correct and data requests for the requested content type returns
successful responses.

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

