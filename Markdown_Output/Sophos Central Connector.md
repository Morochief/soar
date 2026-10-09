Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Sophos Central Connectors

This connector allows Stellar Cyber to collect data from Sophos Central and add the records to
the data lake and, optionally, to issue the contain a host response action.

Integration with Sophos enables organizations to monitor and detect security threats across their
network, including endpoints, servers, and cloud infrastructure, while providing quick incident
response capabilities. By combining Sophos' security solutions with Stellar Cyber's advanced
security analytics and machine learning algorithms, organizations can effectively defend against
cyber attacks.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Sophos Central

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable (applicable to Collect only)

Collected Data

Content Type

Index

Locating Records

Alerts

Events

Syslog

Assets (for Alerts and
Events)

msg_class:

sophos_alerts

sophos_events

msg_origin.source:

sophos_alerts

Content Type

Index

Locating Records

sophos_events

msg_origin.vendor

sophos

msg_origin.category:

endpoint

 If there is asset information in the logs for Events and Alerts, the detected assets are reported in the

Assets Index.

Domain

<API Access URL>

where <API Access URL> is a variable from the configuration of this connector

Response Actions

Action

Required Fields

Contain (Isolate) Host

sophos.hostid_assetid (endpoint_id)

Third Party Native Alert Integration Details

This connector ingests logs from Sophos Central to get the raw alerts that are stored in the Syslog index.
Select the Alerts and Events content types.

Stellar Cyber maps Sophos alerts and events. The alerts and events are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and sophos.id.

The subtype uses sophos.type. Only Endpoint-related alerts and events are integrated.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

If the Collect function only is selected, or the Respond function only, or both the Collect and Respond
functions:

API Key / Header Auth Method: API Access URL, x-api-key header value, and Authorization
header value

Client ID / Client Secret Auth Method: Account Type of Tenant, Client ID, and Client Secret

If the Collect function only is selected:

Account Type of Organization, Client ID, and Client Secret

 Respond actions are not supported with an Account Type of Organization.

Locating Records

To search the alerts or events in the Alerts index or to search the Original Records in the Syslog index,
use the queries:

msg_class: sophos_alerts AND event.type: Endpoint

msg_class: sophos_events AND event.type: Endpoint

Adding a Sophos Central Connector
To add a Sophos Central connector:

1. Enable access to Sophos Central
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Enabling Sophos Central Access
Before you create a Sophos Connector, you must create a Token and get the key values.

 Use our example as a guideline, as you might be using a different software version.

1. Login to Sophos Central Website (https://central.sophos.com ) as the user you want

to associate with your Stellar Cyber connector.

2. If you are going to configure the Stellar Cyber Sophos connector to Collect only, you
can use an API Access URL method for authentication. If you anticipate using the
Respond (with or without the Collect function), you must use Client ID/Client Secret for
authentication. Select the appropriate section below to obtain the needed credentials.

For API Access URL...



Legacy API Token Management is being retired.

a. Navigate to Global Settings > API Token Management.

b. Click Add Token.

c. In the dialog that displays, specify a Name for your new Stellar

Cyber Sophos connector.

d. Click Save.

e. When the Token Summary displays, make note of the following for

use in Stellar Cyber.

API Access URL

Headers for x-api-key and for Authorization

Use the diagram above to identify which parts of the header strings
to use. You do not need to save the API Access URL + Headers
string.

For Client Secret / Client ID...

Follow the guidance in the Sophos Central documentation for
API Credentials Management .

a. Navigate to Global Settings.

b. Go to Access Control > API Credentials Management.

c. Click Add Credential.

d. Enter a Name and optional Description to help you identify the

credential later.

e. From the Role menu, select Service Principal ReadOnly.

f. Click Add.

g. The API Credential Summary displays your Client ID and Client

Secret.

 The Client Secret is only displayed once.

h. Copy the Client ID and Client Secret.

Adding the Connector to Stellar Cyber
With the information ready, you can add a Sophos Central connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Sophos Central from the Type dropdown.

The asterisk (*) indicates a required field.

6. For Function, enable Collect. If you want to be able to contain hosts, also check the

box for Respond.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears. There is a toggle for Auth Method.
Depending on what you selected as the Function in the previous screen, the
authentication method: either API Key / Header or Client ID / Client Secret, will be
selected.

The configuration fields for the API Key / Header Auth Method are as follows:

The asterisk (*) indicates a required field.

The configuration fields for the Client ID / Client Secret Auth Method are as follows.

The asterisk (*) indicates a required field.

12. For the API Key/Header Auth Method:

a. Enter the API Access URL you obtained above.

b. Using the Headers information you noted above, enter the x-api-key header

value and the Authorization header value.

 The Authorization header value must include the string "Basic".

13. For the Client ID / Client Secret Auth Method:

    The Sophos API is a Tenant API . This Sophos Central connector pulls data for

individual Sophos tenants (not for organizations or partners).

If you have a multi-tenant instance, log in with that tenant and create the API

credential.

a. Choose an Account Type. Select either a Tenant account or an Organization

account. You can check your Sophos Central portal for the account type.

 Respond actions are not supported with an Account Type of Organization.

 If you have a multi-tenant instance, do not configure the top tenant as

Organization or Tenant.

b. Enter the Client ID and Client Secret you obtained above.

14. Set the Interval (min). This is how often the logs are collected.

15. Choose the Content Type. The logs for Alerts and Events are supported.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

18. The Connector Overview appears.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

2. Change the Indices for the type of content you collected:

For Alerts and Events, change the Indices to Syslog.

For Alerts and Events, change the Indices to Assets to view asset data
ingested from the logs for Events and Alerts.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

