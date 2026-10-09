Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Universal Webhook Responder
Connectors

Use the Universal Webhook Responder connector to configure a Webhook action that can be
triggered manually or that can enhance Automated Threat Hunting (ATH) actions.

You can configure the Universal Webhook Responder in two ways, either by using predefined
templates or by configuring your own Custom type. Each Universal Webhook Responder
supports a single response action.

The Universal Webhook Responder can be customized for API integrations with various vendors.
Using the Custom type, you can define your own responder. For example, if you want to
configure a firewall with a Block IP action, you define an API request for the action.

Universal Webhook templates can be used to dynamically create new responders. Contact
Stellar Cyber Customer Support to assist with templates. There are predefined templates
available for ESET, WithSecure Elements, Blackberry Cylance, WatchGuard Firebox, Acronis,
Proofpoint on Demand, Netskope, and Trend Micro Vision One.

You can also reuse a Universal Webhook Responder in ATH rules.

This document describes how to configure the Universal Webhook Responder connector. To
manually trigger an action with the Universal Webhook Responder, refer to External
Actions: Webhook on the Threat Hunting page. To perform ATH actions with the Universal
Webhook Responder, refer to Webhook Responder Action on the ATH Playbook page.

For the best practices, refer to Best Practices for Universal Webhook Responder.

Connector Overview: Universal Webhook Responder

Capabilities

Collect: No

Respond: Webhook actions

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: N/A

Collected Data

N/A

Domain

N/A

Response Actions

Webhook actions: created from a Custom type or predefined from a template file:

For ESET, refer to ESET Responder Connectors.

For WithSecure Elements, refer to WithSecure Elements Connectors.

For Blackberry Cylance, refer to BlackBerry Cylance Connectors.

For WatchGuard Firebox, refer to WatchGuard Firebox Responder Connectors

For Acronis, refer to Acronis Cyber Protect Cloud Connectors

For Proofpoint on Demand, refer to Proofpoint on Demand Connectors

For Netskope, refer to Netskope Connectors

For Trend Micro Vision One, refer to Trend Micro Vision One Connectors

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname, Port, Protocol, and Authentication Type, for all authentication methods (including None), plus:

For Basic authentication: Username and Password

For Header authentication: Header Name and Header Value

For OAuth2 authentication: Token URL, Client ID, and Client Secret

For Stellar Cyber API Token authentication: Platform URL and API Token

Adding a Webhook Connector
To add a Webhook connector:

1. Have authentication credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Use actions

Authentication Credentials
Depending on the Authentication Type that is used in a predefined template or that you plan to
configure with Custom, you need to have the credentials for that type of authentication, (Basic,
OAuth2, Header, or Stellar Cyber API Token), handy for the next section.

Adding the Connector in Stellar Cyber
To add a Universal Webhook connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose Custom from the Type dropdown. If there are template files, the dropdown

may also contain predefined template options that you can choose.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name. This is both the responder name and the action name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector. In
addition to specific tenants, this connector supports All Tenants, which means that the
Universal Webhook Responder connector can be used across tenants.

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

 The configuration differs depending on the Type you selected in the General tab.

11. When the Type selected is a predefined template:

a. Enter the Hostname.

 Do not enter http or https in the Hostname field.

b. (Optional) Enter the Port.

c. Choose a Protocol. The HTTP and HTTPS protocols are supported. If you

select HTTPS as the Protocol, depending on the Authentication Type for the
predefined template, another field may be available: Disable SSL Certificate
Verification.

d. (Optional) Click Disable SSL Certificate Verification if you want to disable

SSL certificate verification. Only disable SSL certificates if you have a
necessary reason to, otherwise, it is not a good security practice and may
expose the connection to security risks.

e. The Authentication Type for a predefined template is preselected. Enter the

credentials for that Authentication Type: Basic, OAuth2, or Header. Refer to
the next step for details of each authentication type.

f. Click Next. When the Type selected is a predefined template, the Done tab

appears.

g. Skip to the last step in this procedure. (Click Submit.)

12. When the Type selected is Custom:

a. Enter the Hostname.

 Do not enter http or https in the Hostname field.

b. (Optional) Enter the Port.

c. Choose a Protocol. The HTTP and HTTPS protocols are supported. If you

select HTTPS as the Protocol, another field is available: Disable
SSL Certificate Verification.

d. (Optional) Click Disable SSL Certificate Verification if you want to disable

SSL certificate verification. Only disable SSL certificates if you have a
necessary reason to, otherwise, it is not a good security practice and may
expose the connection to security risks.

e. Choose an Authentication Type. The Basic, OAuth2, Header, Stellar Cyber
API Token, and None authentication types are supported. The authentication
fields differ depending on the selection of Authentication Type.

i. If you choose None, there are no more fields on the Configuration tab

to configure, so you can click Next to go to the next step in this
procedure.

The asterisk (*) indicates a required field.

ii. If you choose Basic, in addition to Hostname, Port, and Protocol:

Enter a Username.

Enter a Password.

 The password should not include non-ASCII special

characters.

The asterisk (*) indicates a required field.

iii. If you choose Header, in addition to Hostname, Port, and Protocol:

Enter a Header Name.

Enter a Header Value.

The asterisk (*) indicates a required field.

iv. If you choose OAuth2, in addition to Hostname, Port, and Protocol:

Enter a Token URL.

Enter a Client ID.

Enter a Client Secret.

(Optional) Enter API Scopes.

The asterisk (*) indicates a required field.

v. If you choose Stellar Cyber API Token, in addition to Hostname,

Port, and Protocol:

Enter a Platform URL. This is the public Application
Programming Interface (API) endpoint.

Enter a API Token. This is the user-scoped API key.

The asterisk (*) indicates a required field.

13. Click Next. When the Type selected is Custom, the Customized tab appears.

The asterisk (*) indicates a required field.

a. (Optional) Enter Custom Headers. Enter Name and Value. Click the  button

to add multiple pairs of Name and Value.

 The Name must be unique. For example, you cannot configure two

Content-Type header names with different values.

b. Choose a Method. The GET, POST, PUT, PATCH, and DELETE methods are

supported.

The asterisk (*) indicates a required field.

c. Enter a Path and Query. The notation for double curly braces is supported.

Use the notation as a placeholder for fields that are later replaced with values.

d. (Optional) Enter the JSON Body in JSON body format. You can leave the

JSON Body empty or you can enter string values or curly brace expressions.

The notation for double curly braces is supported. Use the notation as a
placeholder for fields that are later replaced with values. For example, use
double curly braces as follows, "name": "{{name}}", to fetch the name field
from a log. The name can be complex, such as nameA.nameB.nameC.
Complex name searches in nested JSON objects are supported. For example,
use {{microsoft_defender.id}} in the path to retrieve the nested id field from
{"microsoft_defender": {"id": "123456"}}.

To send the raw Interflow record as the payload of the webhook request as a
JSON object, use the following syntax in the JSON Body: {"source": "
{{interflow_raw}}"}.

 The {{interflow_raw}} syntax is supported in ATH and external actions.

See Using Actions.

The Interflow contains the _source, _index, and _id fields in the Elasticsearch
record. For field definitions, refer to Metadata fields .

To send the Interflow record as the payload of the webhook request as a JSON
string, use the following syntax in the JSON Body: {"source": "
{{interflow_str}}"}.

 The {{interflow_str}} syntax is supported in ATH and external actions.

See Using Actions.

 If the JSON format is incorrect, an error message, Invalid JSON Body, is
displayed. In the following example, there is a semi-colon (;) instead of a
comma (,) at the end of the "comment" line.

 When the Universal Webhook Responder is triggered manually or

through the ATH Playbook, you can edit the Path and Query and the
JSON Body when you issue the action.

14. Click Next. The final confirmation tab, Done, appears.

15. Click Submit.

Testing the Connector
When you define a Universal Webhook Responder, we recommend that you run a test to validate
the connectivity parameters you entered. The test validates authentication / connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60

seconds for new or modified configuration details to be propagated to the sensor before
performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

4. When you click Test, the Webhook Test dialog box opens. It is pre-populated with the
original configuration of the custom webhook responder. You can modify the Path and
Query and the JSON Body for testing purposes. You can replace a field in double curly
braces, {{ }}, with a real value.

Click Test in the Webhook Test dialog.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure
result. A successful test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by
using the X button. If the test fails, you can select the   button from the same row to review and
correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.

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
With the Universal Webhook Responder, you can:

Manually trigger an action

View a performed action

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with the Universal Webhook Responder, refer to External
Actions: Webhook on the Threat Hunting page:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Syslog.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab. Webhook actions appear under External Actions.

5. Click a configured Webhook action.

6. (Optional) Modify the Path and Query or JSON Body.

7. To perform the action, click Submit.

Viewing a Performed Action

To view a performed action, refer to Viewing Webhook Actions.

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with the Universal Webhook Responder, refer to Webhook Responder
Action on the Automated Threat Hunting page:

1. Select Automation | Automation and then select Create.

2. Configure the ATH playbook and scroll down to Actions.

3. Select the  button to add an action.

Another action appears below the existing action.

4. Select the Trigger on condition.

5. Select Webhook Responder for the Type.

6. Choose a previously configured Custom Webhook, Acronis, Cylance, ESET, Netskope,

Proofpoint on Demand, Trend Vision One, WatchGuard Firebox, or WithSecure
Elements Responder from the drop-down menu.

The Path and Query and JSON Body fields populate.

7. (Optional) Modify the Path and Query or JSON Body.

When you select a preconfigured Custom Webhook Responder, the system
prepopulates the JSON Body field with a structure designed to match the expectations
of the receiver. You can modify this body to include additional fields if needed.

When you do modify it, use direct field references with Mustache syntax. Do not use
iteration tags such as {{#ctx.payload.filtered}} and
{{/ctx.payload.filtered}}. Webhook Responders process one result at a time and
do not require iteration. The system automatically flattens field names, so you do not
include _source. in any field reference.

The Webhook Responder differs from other playbook actions that operate on a list of
results. This action triggers once per result, typically one alert at a time, such as when
used from the Alerts page. Because Stellar Cyber already loops through each record
automatically, you do not iterate over ctx.payload.filtered. Instead, reference fields
from the current record directly using Mustache syntax, like {{dstip}} or
{{stellar_uuid}}.

You can reference event fields such as {{dstip}}, {{dstip_host}},
{{appid_name}}, and {{metadata.request.server_name}}, and enriched fields
such as {{_id}}, {{_index}}, and {{stellar_uuid}}.

The system deduplicates webhook requests. If multiple results render the same JSON
body, the responder sends only the first and skips the rest.

Example: Basic Custom Format

Use this format when defining a simple JSON payload:

{
  "DST-IP": "{{dstip}}",
  "Host": "{{dstip_host}}",
  "Reputation": "{{dstip_reputation}}",
  "Link": "https://your-
tenant.stellarcyber.cloud/alerts/alert/{{_index}}/_doc/{{_id}}",
  "UniqueID": "{{stellar_uuid}}"
}

Example: Adding Fields to a Prepopulated Ticket Structure

If the prepopulated JSON defines a helpdesk ticket structure, you can insert
additional event data into the comment body:

{
  "ticket": {
    "comment": {
      "body": "Alert link: https://poc-
eu.stellarcyber.cloud/alerts/alert/{{_index}}/_doc/{{_id}}. Unique ID:
{{stellar_uuid}}. DST-IP: {{dstip}}. Host: {{dstip_host}}. Reputation:
{{dstip_reputation}}."
    },

    "priority": "urgent",
    "subject": "Criticality: Critical {{xdr_event.display_name}}"
  }
}

Use this format when enriching a service ticket with alert details while preserving the
expected structure of the receiving system.

8. Select the Override Default Settings option to override the playbook mute settings and

mute just this action.

9. Select Submit.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

