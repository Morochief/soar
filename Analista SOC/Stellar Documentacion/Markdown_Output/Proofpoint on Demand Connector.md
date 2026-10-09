Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Proofpoint on Demand Connectors

Use this Stellar Cyber connector to ingest Proofpoint on Demand email logs to the data lake.
This connector uses Proofpoint's streaming API. It keeps an open WebSocket connection to get
streaming data.

The following license is required: Proofpoint On Demand’s Remote Syslog.

 If your Stellar Cyber deployment is configured to use an HTTP proxy, be advised that this
connector relies on Proofpoint’s API, which uses the WebSocket protocol for log collection
(WebSocket is not reliable over HTTP proxy connections).

In addition, you can use Proofpoint on Demand responders to configure Webhook actions that
can be triggered manually or that can enhance Automated Threat Hunting (ATH) actions.

Proofpoint on Demand responders use Webhook templates that support actions. Each action is
one responder, there are four actions, and hence there are four Proofpoint on Demand
responders: Proofpoint on Demand Add to Org Block List, Proofpoint on Demand Add to Org
Safe List, Proofpoint on Demand Delete From Org Block List, and Proofpoint on Demand Delete
From Org Safe List.

This document describes how to configure a Proofpoint on Demand responder using the
Universal Webhook Responder, how to add the respond function to a Proofpoint on Demand
connector and how to manually trigger an action and perform ATH actions with a Proofpoint on
Demand responder.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Proofpoint on Demand

Capabilities

Collect: Yes

Respond: Webhook actions

Native Alerts Mapped: No

Runs on: DP

Interval: Every hour

Collected Data

Content Type

Mail Log

Message

Index

Syslog

Locating Records

msg_class:

proofpoint_on_dema
nd_maillog

proofpoint_on_dema
nd_message

msg_origin.source:

proofpoint_on_dema
nd

msg_origin.vendor:

proofpoint

msg_origin.category:

email

Domain

logstream.proofpoint.com:443

Response Actions

Webhook action templates:

Proofpoint on Demand Add to Org Block List

Proofpoint on Demand Add to Org Safe List

Proofpoint on Demand Delete From Org Block List

Proofpoint on Demand Delete From Org Safe List

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

For Collect: Cluster ID and API Key

For Respond: Hostname, Protocol, Token URL, Client ID, Client Secret, and Cluster ID

Adding a Proofpoint on Demand Connector

To add a Proofpoint on Demand connector:

1. Obtain credentials (Collect)
2. Obtain credentials (Respond)
3. Adding the connector in Stellar Cyber (Collect)
4. Add the connector in Stellar Cyber (Respond)
5. Test the connector
6. Verify ingestion
7. Use actions

Obtaining Proofpoint on Demand Credentials (Collect)

 If your Stellar Cyber deployment is configured to use an HTTP proxy, be advised that this
connector relies on Proofpoint’s API, which uses the WebSocket protocol for log collection
(WebSocket is not reliable over HTTP proxy connections).

Configuration of this connector requires your Proofpoint deployment be licensed for Proofpoint
On Demand’s Remote Syslog.

Before you configure the connector in Stellar Cyber, you must obtain and verify the following
from your POD deployment:

Cluster ID The Proofpoint Cluster ID. See Locating Cluster ID.

API Keys as follows:

To configure collection of maillog and message together in one
connector: One API key is needed.

To configure collection of maillog or message in two separate
connectors: The same API key can be used for the two connectors.

To configure collection of maillog in more than one connector: You need a
different API key for each connector.

To configure collection of message in more than one connector: You need a
different API key for each connector.

See Generating API Keys.

Locating Cluster ID

The Cluster ID is assigned by Proofpoint. It is located at the top of the Proofpoint on Demand
deployment management interface.

Generating API Keys

To configure API keys:

1. Log in to the Proofpoint Admin portal at https://admin.proofpoint.com .

2. Navigate to Settings > API Key Management.

3. Click Create New.

4. On the Create New API Key dialog, enter any unique Name for the key.

5. Generate the API Key.

6. Click the new API Key and select View Details from the ellipsis menu.

7. Copy the API Key.

Obtaining Proofpoint on Demand Credentials (Respond)
Before you configure the connector in Stellar Cyber, you must obtain the following Proofpoint on
Demand credentials:

Hostname—The Hostname for API access. The default is: threatprotection-
api.proofpoint.com. Do not include http or https in the Hostname.

Protocol—The protocol used by the hostname. The options are HTTP or HTTPS.

Token URL—The URL for the token. The default is: Default:
https://auth.proofpoint.com/v1/token.

Client ID and Client Secret—The generated API key and secret key. Follow the
guidance in the Proofpoint documentation for API Key Management . Also refer to
Generating API Keys.

Cluster ID—The Proofpoint Cluster ID. See Locating Cluster ID.

Adding the Connector in Stellar Cyber (Collect)
To add a Proofpoint on Demand connector with the Collect function in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose Proofpoint on Demand from the Type dropdown.

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

12. Enter the Cluster ID you noted above in Locating Cluster ID.

13. Enter the API Key you noted above in Generating API Keys.

14. Choose the Content Type you would like to collect. The logs for Mail Log and

Message are supported.

15. Click Next. The final confirmation tab appears.

16. Click Submit.

The new connector is immediately active.

 A new Proofpoint on Demand connector automatically collects logs for the last 7 days. It can

take a few days for the logs to be current.

Adding the Connector in Stellar Cyber (Respond)
To add the respond function for a Proofpoint on Demand connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: Proofpoint on
Demand Add to Org Block List, Proofpoint on Demand Add to Org Safe List,
Proofpoint on Demand Delete From Org Block List, or Proofpoint on Demand
Delete From Org Safe List.

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
Proofpoint on Demand responder can be used across tenants.

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

11. Enter the Hostname. The default is threatprotection-api.proofpoint.com.

 Do not include http or https in the Hostname.

12. Select the Protocol, either HTTP or HTTPS, which is used by the Hostname. If you
select HTTPS, another field is available: Disable SSL Certificate Verification.

13. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

14. Enter the Token URL. The default is https://auth.proofpoint.com/v1/token.

15. Enter the Client ID and Client Secret you noted above in Generating API Keys.

16. Enter the Cluster ID you noted above in Locating Cluster ID.

17. Click Next. The final confirmation tab, Done, appears.

18. Click Submit.

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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Using Actions
With a Proofpoint on Demand responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with a Proofpoint on Demand responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Syslog.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab. Webhook actions appear under External Actions.

5. Click a Proofpoint on Demand Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. You can modify the JSON Body by entering string values or curly brace expressions.

Fill in any empty fields, such as value.

7. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with a Proofpoint on Demand responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured Proofpoint on Demand responder from the dropdown

menu for the Webhook Responder.

The template populates the fields in the Path and Query and JSON Body.

8. You can modify the JSON Body by entering string values or curly brace expressions.

9. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

10. Click Submit

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

