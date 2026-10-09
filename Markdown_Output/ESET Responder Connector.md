Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring ESET Responder Connectors

Use an ESET Responder to configure a Webhook action that can be triggered manually or that
can enhance Automated Threat Hunting (ATH) actions. This responder only supports cloud.

ESET Responders use Webhook templates that support actions. Each action is one responder,
there are four actions, and hence there are four ESET Responders: ESET Isolate computer from
network, ESET End computer isolation from network, ESET On-Demand Scan, and ESET Run
command.

This document describes how to configure an ESET Responder using the Universal Webhook
Responder, how to manually trigger an action with an ESET Responder, and how to perform ATH
actions with an ESET Responder.

Connector Overview: ESET Responder

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

ESET End computer isolation from network

ESET Isolate computer from network

ESET On-Demand Scan

ESET Run command

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname, Protocol, Username, and Password

Adding an ESET Responder
To add an ESET Responder:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Use actions

Obtaining Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following ESET
credentials:

Hostname: The default is: us.automation.eset.systems.
For Europe, modify the default to: eu.automation.eset.systems.
For other regions, such as Japan and Canada, refer to
https://help.eset.com/eset_connect/en-US/use_api_with_swagger.html .

Protocol: The options are HTTP and HTTPS.

Username and Password: To obtain a username and password, create an API user
account following the guidance in the ESET documentation for Create API User
account. 

Adding the Connector in Stellar Cyber
To add an ESET Responder in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: ESET End

computer isolation from network, ESET Isolate computer from network, ESET On-
Demand Scan, or ESET Run command.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector. In
addition to specific tenants, this connector supports All Tenants, which means that an
ESET Responder can be used across tenants.

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

14. Enter the Username and Password you noted above.

15. Click Next. The final confirmation tab, Done, appears.

16. Click Submit.

Testing the Connector
When you define an ESET Responder, we recommend that you run a test to validate the
connectivity parameters you entered. The test validates authentication / connectivity.

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

Using Actions
With an ESET Responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with an ESET Responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Alerts.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab.

Webhook actions appear under External Actions.

5. Click an ESET Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. You can modify the JSON Body by entering string values or curly brace expressions.

Fill in any empty fields as follows:

Enter the targets for devicesUuids.

(Optional) For manual, you can enter customized settings such as expireTime
and createTime. Follow the guidance in the ESET documentation for Swagger
UI .

7. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with an ESET Responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured ESET Responder from the dropdown menu for the

Webhook Responder. The template populates the fields in the Path and Query and
JSON Body.

8. You can modify the JSON Body by entering string values or curly brace expressions.

Fill in any empty fields as follows:

Enter the targets for devicesUuids.

(Optional) For manual, you can enter customized settings such as expireTime
and createTime. Follow the guidance in the ESET documentation for Swagger
UI .

9. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

10. Click Submit

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

