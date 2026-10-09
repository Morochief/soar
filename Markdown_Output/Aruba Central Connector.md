Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Aruba Central Connectors

This connector allows Stellar Cyber to ingest logs from Aruba Central and add the records to the
data lake. It integrates with the Aruba Central API to query for Audit Logs and Monitoring Events.

There is a base API rate limit of 5,000 API calls per day for all accounts. The rate limit can be
dynamically increased with Foundation or Advanced Licenses.

 Due to a vendor API limitation, this connector can only retrieve the first 10,000 records per

request.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Aruba Central

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Audit Logs

Monitoring Events

Index

Syslog

Locating Records

msg_class:

aruba_central_audi
t_log

aruba_central_moni
toring

msg_origin.source:

Content Type

Index

Locating Records

aruba_central

msg_origin.vendor:

hpe

msg_origin.category:

netmgmt

Domain

<Base URL> or <Custom URL>

where <Base URL> or <Custom URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL or Custom URL, Username, Password, Client ID, Client Secret, and Customer ID

Adding an Aruba Central Connector
To add an Aruba Central connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Aruba Central Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Aruba Central
credentials:

Base URL—The base URL for API access, which you can select from the dropdown
menu. Refer to the table in the Aruba Central documentation . This URL is
determined by the geographical cluster in which you registered the account of HPE
Aruba Networking Central.

Custom URL—The custom URL, which you can enter in the Custom URL field if a URL
is not available in the Base URL dropdown menu.

Username and Password—The credentials used to authenticate a user on the Aruba
Central Portal. Follow the guidance in the Aruba Central documentation .

Client ID and Client Secret—The credentials used to authenticate with the Aruba
Central API.

Customer ID—The unique identifier for your Aruba Central account.



With the authentication mechanism for this connector, it is easy to be locked out. Be cautious

of the following scenarios:

Sharing credentials among Stellar Cyber connectors or with any third party.

Attempting to authenticate with the wrong credentials consecutively.

Clicking the Test button and then immediately enabling the collector. (The amount
of time between successful logins (cooldown time) is 30 minutes for each
successful login attempt.)

Disabling and enabling the connector immediately.

Follow these procedures to:

Add a new user to HPE GreenLake

Log in with the new user to HPE GreenLake

Obtain the Base URL, Client ID, Client Secret, and Customer ID

Adding a New User to HPE GreenLake

To add a new user:

1. Login to HPE GreenLake as an administrative user.

2. Select User Management from the Quick Links.

3. In the Users page, click Invite users.

4. In the Invite User page, enter the user's Email Address and select a Role.

5. Click Send Invite.

6. To grant access for the new user, select Assign Role.

7. Select a Service manager, a Role, and select Limit Resource Access. There are view

only roles and operator roles.

8. Click Assign Role.

Logging in with the New User to HPE GreenLake

To log in with the new user:

1. The new user will receive an email, accept the invitation to activate the account, and

then login to HPE GreenLake.

2. In Getting Started, the new user can then click Launch to start using Aruba Central.

3. Note the username and password of the new user. These credentials are used in the

configuration of the Aruba Central connector.

Obtaining the Base URL, Client ID, Client Secret, and Customer ID

To obtain the base URL, client ID, client secret, and customer ID:

1. In the Aruba Central Portal, select Organization.

2. Select the Platform Integration tab and then select REST API.

3. Note the URL (the part before swagger) in the APIs tab. It will be used in the

configuration of the Aruba Central connector. In this example, the base URL is
https://apigw-uswest4.central.arubanetworks.com.

4. Select the Account Home icon at the top right of the user interface and click

API Gateway, then select the My Apps & Tokens tab.

5. Click Add Apps & Tokens.

6. In the NEW TOKEN page, click Generate.

7. Note the Client ID and Client Secret. They will be used in the configuration of the Aruba

Central connector.

8. Select the user icon at the top right of the user interface.

9. Note the Customer ID for that user. It will be used in the configuration of the Aruba

Central connector.

Adding the Connector in Stellar Cyber
To add an Aruba Central connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Network Management from the Category dropdown.

5. Choose Aruba Central from the Type dropdown.

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

12. Select the Base URL from the dropdown menu.

13. Or, select Custom URL from the Base URL dropdown menu and enter a URL in the

Custom URL field.

14. Enter the Username and Password you noted above in Obtaining Aruba Central

Credentials.

15. Enter the Client ID and Client Secret you noted above.

16. Enter the Customer ID you noted above.

17. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

18. Choose the Interval (min). This is how often the logs are collected.

19. Choose the Content Type you would like to collect. The logs for Audit Logs and

Monitoring Events are supported.

20. Click Next. The final confirmation tab appears.

21. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Aruba Central connector tests
that the Base URL and authentication credentials are correct and data requests for the
requested content types return successful responses.

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

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

