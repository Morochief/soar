Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring WatchGuard Firebox Responder
Connectors

Use a WatchGuard Firebox Responder to configure a Webhook action that can be triggered
manually or that can enhance Automated Threat Hunting (ATH) actions.

WatchGuard Firebox Responders use Webhook templates that support actions. Each action is
one responder, there are two actions, and hence there are two Responders: WatchGuard
Firebox Add Allowed Sites and WatchGuard Firebox Add Blocked Sites.

This document describes how to configure a WatchGuard Firebox Responder using the
Universal Webhook Responder, how to manually trigger an action with a WatchGuard Firebox
Responder, and how to perform ATH actions with a WatchGuard Firebox Responder.

Note the following rate limit :

Connector Overview: WatchGuard Firebox Responder

Capabilities

Collect: No

Respond: Webhook actions

Native Alerts Mapped: No

Runs on: DP

Interval: N/A

Collected Data

N/A

Domain

<Hostname>

where <Hostname> is a variable from the configuration of this connector

Response Actions

Webhook action templates:

WatchGuard Firebox Add Allowed Sites

WatchGuard Firebox Add Blocked Sites

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname, Protocol, Access ID, Password, and WatchGuard-API-Key

Adding a WatchGuard Firebox Responder
To add a WatchGuard Firebox Responder:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Use actions

Obtaining Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following WatchGuard
Firebox credentials:

Hostname—The base URL for API access. The default (for United States) is
api.usa.cloud.watchguard.com. Locate the Base URL for other regions at WatchGuard
API documentation .

Protocol—The options for Protocol are HTTP and HTTPS.

Access ID and Password—The authentication credentials. To obtain an Access ID and
password, follow the guidance in the WatchGuard API documentation to Get Started
with WatchGuard APIs . Specify the Read-write credential.

WatchGuard-API-Key—The API Key associated with your WatchGuard Cloud account.
Locate it on the Managed Access page in WatchGuard Cloud. Specify the API Key as
the value of the WatchGuard-API-Key header parameter.

Adding the Connector in Stellar Cyber
To add a WatchGuard Firebox Responder in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: WatchGuard

Firebox Add Allowed Sites or WatchGuard Firebox Add Blocked Sites.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector. In
addition to specific tenants, this connector supports All Tenants, which means that a
WatchGuard Firebox Responder can be used across tenants.

9. Choose the device on which to run the connector.



Certain connectors can be run on either a Sensor or a Data Processor.
The available devices are displayed in the Run On menu. If you want to
associate your collector with a sensor, you must have configured that
sensor prior to configuring the connector or you will not be able to select
it during initial configuration.

If the device you're connecting to is on premises, we recommend you run
on the local sensor. If you're connecting to a cloud service, we
recommend you run on the DP.

10. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

11. Enter the Hostname you noted above in Obtaining Credentials.

12. Select the Protocol, either HTTP or HTTPS. If you select HTTPS, another field is

available: Disable SSL Certificate Verification.

13. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

14. Enter the Access ID and Password you noted above.

15. Enter the WatchGuard-API-Key you noted above.

16. Click Next. The final confirmation tab, Done, appears.

17. Click Submit.

Testing the Connector
When you define a WatchGuard Firebox Responder, we recommend that you run a test to
validate the connectivity parameters you entered. The test validates authentication / connectivity.
The Test button shows success with a valid credential.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success
or failure result. A successful test indicates that you entered all of the connector
information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close
it by using the X button. If the test fails, you can select the   button from the same row
to review and correct issues.

 The connector status is updated every five (5) minutes. A successful test clears
the connector status, but if issues persist, the status reverts to failed after a
minute.

Repeat the test as needed.

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

Using Actions
With a WatchGuard Firebox Responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with a WatchGuard Firebox Responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Alerts.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab.

Webhook actions appear under External Actions.

5. Click a WatchGuard Firebox Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. Modify the Path and Query by entering your WatchGuard Cloud account ID in the

{{account_id}} parameter in the path. Locate your account ID on the My Account page in
the WatchGuard Cloud, then enter it in place of {{account_id}} in the path, for
example: /rest/firebox/management/v1/configuration/{{account_id}}/exceptions/blockeds
ite

7. Modify the JSON Body by entering string values or curly brace expressions. Fill in any

empty fields.

8. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with a WatchGuard Firebox Responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured WatchGuard Firebox Responder from the dropdown

menu for the Webhook Responder. The template populates the fields in the Path and
Query and JSON Body.

8. Modify the Path and Query by entering your WatchGuard Cloud account ID in the

{{account_id}} parameter in the path. Locate your account ID on the My Account page in
the WatchGuard Cloud, then enter it in place of {{account_id}} in the path, for
example: /rest/firebox/management/v1/configuration/{{account_id}}/exceptions/blockeds
ite

9. Modify the JSON Body by entering string values or curly brace expressions. Fill in any

empty fields.

10. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

11. Click Submit

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

