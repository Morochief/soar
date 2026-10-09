Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Trend Micro Vision One Connectors

The Trend Micro Vision One connector allows you to collect alert details and observed attack
techniques from your Trend Micro deployment, and add that to the Stellar Cyber data lake for
analysis and threat hunting.

This topic refers to configuring a Trend Micro Vision One connector. Also see:

Configuring Trend Micro Apex Central Connectors
Configuring Trend Micro Cloud One Connectors

For API rate limits, refer to the Trend Micro Vision One documentation for API Rate Limit .

In addition, you can use Trend Micro Vision One responders to configure Webhook actions that
can be triggered manually or that can enhance Automated Threat Hunting (ATH) actions.

Trend Micro Vision One responders use Webhook templates that support actions. Each action is
one responder, there are five actions, and hence there are five Trend Micro Vision One
responders: Trend Vision One Add To Block List, Trend Vision One Isolate Endpoint, Trend
Vision One Quarantine Email Message, Trend Vision One Remove From Block List, and Trend
Vision One Restore Endpoint Connection.

This document describes how to configure a Trend Micro Vision One responder using the
Universal Webhook Responder, how to add the respond function to a Trend Micro Vision One
connector and how to manually trigger an action and perform ATH actions with a Trend Micro
Vision One responder.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Trend Micro Vision One

Capabilities

Collect: Yes

Respond: Webhook actions

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Alerts

Audit Logs

Observed Attack Techniques

Syslog

msg_class:

trendmicro_visionon
e_alerts

trendmicro_visionon
e_audit_logs

trendmicro_visionon
e_observedattacktec
hniques

msg_origin.source:

trendmicro_visionon
e

msg_origin.vendor:

trendmicro

msg_origin.category:

endpoint

Domain

<API base URL>

where <API base URL> is a variable from the configuration of this connector

Response Actions

Webhook action templates:

Trend Vision One Add To Block List

Trend Vision One Isolate Endpoint

Trend Vision One Quarantine Email Message

Trend Vision One Remove From Block List

Trend Vision One Restore Endpoint Connection

Third Party Native Alert Integration Details

This connector ingests logs from Trend Micro Vision One to get the raw alerts that are stored in the
Syslog index. Select the Alerts content type.

Stellar Cyber maps Trend Micro Vision One alerts. The alerts are read from the Syslog index, enriched
with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and trendmicro_visionone.workbenchId.

Tactic and Technique are provided by the Trend Micro Vision One raw alerts field
trendmicro_visionone.matchedRules.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

For Collect: API base URL and Bearer token value

For Respond: Hostname, Protocol, and API Key

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_class: trendmicro_visionone_alerts.

Adding a Trend Micro Vision One Connector
To add a Trend Micro Vision One connector:

1. Obtain credentials (Collect)
2. Obtain credentials (Respond)
3. Add the connector in Stellar Cyber (Collect)
4. Add the connector in Stellar Cyber (Respond)
5. Test the connector
6. Verify ingestion
7. Use actions

Obtaining Credentials (Collect)
Before you configure the connector in Stellar Cyber, you must obtain the following Trend Micro
Vision One credentials:

API Base URL—The base URL for API access. Note the API URL from the location that
corresponds to your environment.

Region

Australia

FQDN

api.au.xdr.trendmicro.com

European Union

api.eu.xdr.trendmicro.com

India

Japan

api.in.xdr.trendmicro.com

api.xdr.trendmicro.co.jp

Singapore

api.sg.xdr.trendmicro.com

United States

api.xdr.trendmicro.com

Bearer token value—The unique, user-generated string of characters required in the
Authorization header for API authentication. Refer to the Trend Vision One API

Reference document in the following sections: First steps toward using the APIs  and
Obtain authentication tokens .

Obtaining Credentials (Respond)
Before you configure the connector in Stellar Cyber, you must obtain the following Trend Micro
Vision One credentials:

Hostname—The Hostname for API access. The default is: api.xdr.trendmicro.com. Do
not include http or https in the Hostname.

Protocol—The protocol used by the hostname. The options are HTTP or HTTPS. If you
select HTTPS, another field is available: Disable SSL Certificate Verification.

API Key—The authentication credential. Follow the guidance in the Trend Vision One
API Reference document in the following sections: First steps toward using the APIs 
and Obtain authentication tokens .

Adding the Connector in Stellar Cyber (Collect)
After you have noted the authentication information from the Trend Micro app integration, you
can add the Trend Micro Vision One connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Trend Micro Vision One from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name for the tenants who will have access to this connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the API base URL. Use the table noted in Obtaining Credentials (Collect) to add

the appropriate URL for your region.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Enter the Bearer token value. This is the authentication token you noted in the

previous section.

14. Choose the Interval (min). This is how often the logs are collected.

 The logs for Audit Logs are queried every 24 hours.

15. Choose the Content Type you would like to collect. The logs for Alerts, Audit Logs,

and Observed Attack Techniques are supported.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active.

Adding the Connector in Stellar Cyber (Respond)
To add the respond function for a Trend Micro Vision One connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: Trend Vision One

Add To Block List, Trend Vision One Isolate Endpoint, Trend Vision One
Quarantine Email Message, Trend Vision One Remove From Block List, and Trend
Vision One Restore Endpoint Connection.

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
Trend Micro Vision One responder can be used across tenants.

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

11. Enter the Hostname. The default is api.xdr.trendmicro.com.

 Do not include http or https in the Hostname.

12. Select the Protocol, either HTTP or HTTPS, which is used by the Hostname. If you
select HTTPS, another field is available: Disable SSL Certificate Verification.

13. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

14. Enter the API Key you noted above in Obtaining Credentials (Respond).

15. Click Next. The final confirmation tab, Done, appears.

16. Click Submit.

Testing the Connector


The Test button for the Trend Micro Vision One connector is unable to distinguish between
an expired and a non-expired authentication token. As a result, the test will succeed for
expired tokens but the connector will fail.

Note that the test button will correctly fail in other cases, such as incorrectly formatted
authentication tokens.

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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Using Actions
With a Trend Micro Vision One responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with a Trend Micro Vision One responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Syslog.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab. Webhook actions appear under External Actions.

5. Click a Trend Micro Vision One Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. You can modify the JSON Body by entering string values or curly brace expressions.

7. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with a Trend Micro Vision One responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured Trend Micro Vision One responder from the dropdown

menu for the Webhook Responder.

The template populates the fields in the Path and Query and JSON Body.

8. You can modify the JSON Body by entering string values or curly brace expressions.

9. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

10. Click Submit

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

