Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Microsoft Graph Message Trace
Connectors

This connector allows Stellar Cyber to ingest logs from Microsoft Graph Message Trace and add
the records to the data lake. This connector integrates with the messageTraces API  to query
email flow data (Message Trace).

 It is recommended that you migrate any existing Office 365 Reporting Web Service
connectors in Stellar Cyber to Microsoft Graph Message Trace connectors. Refer to
Announcing General Availability (GA) of the New Message Trace in Exchange Online .

Microsoft Graph Message Trace requires a plan that includes Microsoft Exchange Online, such
as Microsoft 365 Business Basic/Standard/Premium, Office 365 E1/E3/E5, and Exchange Online
Plan 1 or 2. Refer to Exchange Online service description .

Note the following:

The messageTraces API  is currently only available on the Microsoft Graph global
service (Enterprise Plan).

The required permission is ExchangeMessageTrace.Read.All.

The Exchange message trace service limit  is 100 requests per 5 minutes.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Microsoft Graph Message Trace

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

microsoft_graph_me
ssage_trace

msg_origin.source:

microsoft_graph

msg_origin.vendor:

microsoft

msg_origin.category:

email

Domain

https://graph.microsoft.com/

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Client Secret, Microsoft Subscription Plan, Tenant ID, and Client ID

Adding a Microsoft Graph Message Trace Connector
To add a Microsoft Graph Message Trace connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Microsoft Graph Message Trace Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Microsoft
Graph Message Trace credentials. Follow the guidance in the Microsoft documentation in the
Graph-based message trace API onboarding guide .

Client Secret—The password that you generated for your app in the app registration
portal

Microsoft Subscription Plan—The available Microsoft Subscription Plan, which is
Enterprise Plan.

Tenant ID—The tenant from which to request permission, also known as the Directory
ID.

Client ID—The client ID, also known as the Application ID that the app registration
portal assigned when the app was registered.

Registering an Application

To register an application, follow the guidance in the Microsoft documentation to Register an
application with the Microsoft identity platform . Refer to the Prerequisites. You will need a
Tenant ID in Microsoft Entra.

When you complete the registration of the application, the Microsoft Entra admin center displays
the app registration's Overview pane. Make note of the Application (client) ID and Directory
(tenant) ID.

To add a client secret, follow the guidance in the Microsoft documentation to Add credentials .
Make note of the client secret's value.

Assigning API Permissions

To assign the required application permissions, follow the guidance in the Microsoft
documentation to Configure Microsoft Graph permissions . Add the
ExchangeMessageTrace.Read.All permission.

Creating the Service Principal

You can create the service principal in two ways:

Use the Microsoft Graph Explorer. Follow the guidance in the Microsoft documentation
to Create the service principal by using Microsoft Graph Explorer .

Use the Microsoft Graph PowerShell SDK. Follow the guidance in the Microsoft
documentation to Create the service principal by using Microsoft Graph PowerShell .

Adding the Connector in Stellar Cyber
To add a Microsoft Graph Message Trace connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose Microsoft Graph Message Trace from the Type dropdown.

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

12. Enter the Client Secret you noted above in Obtaining Microsoft Graph Message Trace

Credentials.

13. Select the available Microsoft Subscription Plan, which is Enterprise Plan.

14. Enter the Tenant ID you noted above.

15. Enter the Client ID you noted above.

16. Choose the Content Type you would like to collect. The logs for Message Trace are

supported.

17. Choose the Interval (min). This is how often the logs are collected.

18. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Microsoft Graph Message Trace
connector tests that the Client Secret, Tenant ID, and Client ID are correct and data requests
for the requested content type returns successful responses.

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

403

Forbidden

This error occurs when the permission or scope is not

Did you enter your credentials correctly?

correct in a valid credential.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

