Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring BlackBerry Cylance Connectors

The BlackBerry Cylance connector allows you to lock down a device that is associated with an
event reported by another connector. In Stellar Cyber, this connector is used for lock down only,
not event tracking.

 The devices you want to lock down using this connector must be configured using

BlackBerry's CylancePROTECT Console to have a policy that permits device control (or to
be in a zone configured with a policy that has device control enabled).

In addition, you can use Cylance responders to configure Webhook actions that can be triggered

manually or that can enhance Automated Threat Hunting (ATH) actions.

Cylance responders use Webhook templates that support actions. Each action is one responder,
there are four actions, and hence there are four Cylance responders: Cylance Add to
GlobalQuarantine, Cylance Add to GlobalSafe, Cylance Delete from GlobalQuarantine, and
Cylance Delete from GlobalSafe.

This document describes how to configure a Cylance responder using the Universal Webhook
Responder, how to add the respond function to a Cylance connector and how to manually trigger
an action and perform ATH actions with a Cylance responder.

Connector Overview: Blackberry Cylance

Capabilities

Collect: No

Respond: Webhook actions

Native Alerts Mapped: Yes

Runs on: DP

Interval: N/A

Collected Data

N/A

Domain

<Service Endpoint URL>

where <Service Endpoint URL> is a variable from the configuration of this connector

Response Actions

Action

Contain Host

Required Fields

deviceand device.deviceID or cylance and one of
cylance.device_id or srcmac or dstmac or (host and
host.mac)

Webhook action templates:

Cylance Add to GlobalQuarantine

Cylance Add to GlobalSafe

Cylance Delete from GlobalQuarantine

Cylance Delete from GlobalSafe

Third Party Native Alert Integration Details

For CylancePROTECT, three types of Cylance events are mapped to the XDR Kill Chain and Stellar
Cyber's Alert index: Exploit Attempts, Script Control, and Threats. The other data (Audit Log, Device,
Device Control, and Threat Classification) are ingested and mapped to the Syslog index (not Alerts
index), and are not run through the ML/SA pipeline.

For CylanceOPTICS, Detection events are evaluated with Stellar Cyber time series analysis models to
determine abnormality of the event before mapping.

 For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Service Endpoint URL, Tenant ID, App ID, and App Secret

Locating Records

Use the following to query for records:

msg_origin.source: cylance_protect or cylance_optics

msg_class: cylance_protect_alert or cylance_optics_event

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_origin.source:cylance_protect AND event.type:(ExploitAttempt OR
ScriptControl OR Threat)

Adding a Blackberry Cylance Connector
To add a Blackberry Cylance connector:

1. Set up Stellar Cyber in CylancePROTECT and obtain IDs
2. Add the connector in Stellar Cyber
3. Add the connector in (Webhook Responder)
4. Test the connector
5. Use the connector to contain a host
6. Use actions

 Use our example as a guideline, as you might be using a different software version.

Setting up the Stellar Cyber App Integration
Before you configure the connector in Stellar Cyber, you must obtain the following Cylance
credentials:

App ID and App Secret

Tenant ID

To obtain the information:

1. Log in to the CylancePROTECT Console as an administrator.

2. Select Settings > Integrations.

3. Click Add Application.

4. Type an Application Name. This must be unique within your organization.

5. Select the access privileges for a Console data type. Not selecting any checkboxes for

a data type means the application does not have access to that data type.

6. Click Save.

7. The credentials to use for the application displays. Make note of both the Application

ID and the Application Secret.

8. Click OK to return to the Integrations tab.

9. Note that your new application appears in the list. At this point, make note of the Tenant

ID that is displayed on the Integrations tab.

 The syntax of the Tenant ID must be exactly as it appears here.

You are now ready to set up your Stellar Cyber Cylance connector.

Adding the Connector in Stellar Cyber
After you have noted the configuration information, you can add the BlackBerry Cylance
connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose BlackBerry Cylance from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this

tenant name.

9. Choose the device on which to run the connector.

10. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

11. Enter the Service Endpoint URL (the URL of your regional BlackBerry Cylance portal).
Do not append any details to this URL, just the value indicated below for your region:

Region

URL

Asia-Pacific - North

https://protectapi-apne1.cylance.com/

Asia-Pacific - Southeast

https://protectapi-au.cylance.com/

Europe - Central

https://protectapi-euc1.cylance.com/

North America

https://protectapi.cylance.com/

South America

https://protectapi-sae1.cylance.com/

US Government

https://protectapi.us.cylance.com/

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

12. Enter the Tenant ID you noted above in Setting up the Stellar Cyber App Integration.

 The syntax of the Tenant ID must be exactly as it appeared in the Integration tab of

the Cylance Console.

13. Enter the App ID and App Secret you noted above.

14. Click Next. The final confirmation tab appears.

15. Click Submit.

The new connector is immediately active.

Adding the Connector in Stellar Cyber (Webhook
Respond)

To add the Webhook respond function for a BlackBerry Cylance connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: Cylance Add to

GlobalQuarantine, Cylance Add to GlobalSafe, Cylance Delete from
GlobalQuarantine, or Cylance Delete from GlobalSafe.

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
Cylance responder can be used across tenants.

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

11. Enter the Hostname you noted above (the URL of your regional BlackBerry Cylance

portal).

12. Select the Protocol, either HTTP or HTTPS. If you select HTTPS, another field is

available: Disable SSL Certificate Verification.

13. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

14. Enter the Tenant ID you noted above.

 The syntax of the Tenant ID must be exactly as it appeared in the Integration tab of

the Cylance Console.

15. Enter the App ID and App Secret you noted above.

16. Click Next. The final confirmation tab, Done, appears.

17. Click Submit.

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

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Using the Connector to Contain a Host
When an event has occurred on a host known to the BlackBerry Cylance connector, you can use
this to isolate the associated host. From the Event list in Threat Hunting, you can select the
event of interest, then click More Info.  From there, you can select Actions > External Actions >
Contain Host. In the Contain Host Configuration dialog, select the relevant connector and in
the Target, specify the Source IP, Destination IP, or host IP to lock down.

For more information on working with the events and the actions on them, refer to Understanding
Event Details.

Using Actions
With a Cylance responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with a Cylance responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Syslog.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab.

Webhook actions appear under External Actions.

5. Click a Cylance Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. You can modify the JSON Body by entering string values or curly brace expressions.

7. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with a Cylance responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured Cylance responder from the dropdown menu for the

Webhook Responder. The template populates the fields in the Path and Query and
JSON Body.

8. You can modify the JSON Body by entering string values or curly brace expressions.

9. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

10. Click Submit.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

