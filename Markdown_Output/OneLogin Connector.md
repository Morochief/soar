Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring OneLogin Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.
This topic describes the OneLogin connector. The OneLogin connector allows you to ingest user
and event data.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: OneLogin

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Events

Users

Index

Syslog

Traffic

Locating Records

msg_class:

one_login_events

one_login_users

msg_origin.source:

one_login

msg_origin.vendor:

one_login

msg_origin.category:

Content Type

Index

Locating Records

iam

Domain

https://<API Domain>

where <API Domain> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Client ID, Client Secret, and API Domain

Adding a OneLogin Connector
To add a OneLogin connector:

1. Create the OneLogin API token to use in Stellar Cyber
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Creating the OneLogin API Token
To create the OneLogin API token you'll use to configure the connector:

1. Log in to your OneLogin as an account owner or an account with administrative

privileges.

2. Navigate to Developers > API Credentials.

3. On the API Access Page, click New Credential.

4. On the dialog that displays, enter the Name of the token to be used with Stellar Cyber

and make note of it.

5. Select a scope that fits your plan for the Stellar Cyber connector. If you want to disable
users, you will need to select the option for Manage All (this will allow you to disable
users, if needed).

6. Click Save.

7. A dialog displays your new keys. At this point, make note of the Client secret and

Client ID for use later.

8. Click Done.

Adding the Connector in Stellar Cyber
To add a OneLogin connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose IdP from the Category dropdown.

5. Choose OneLogin from the Type dropdown.

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

12. Enter the Client ID you noted above in Creating the OneLogin API Token.

13.  Enter the Client Secret you noted above.

14. Select the OneLogin API Domain from the dropdown, for example: api.us.onelogin.com

or api.eu.onelogin.com.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Events and Users are

supported.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 If you've just added this connector, wait 5–10 minutes before testing.

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

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Syslog or Traffic to check ingestion.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

