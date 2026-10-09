Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring WithSecure Elements Connectors

This connector allows Stellar Cyber to ingest logs from WithSecure Elements and add the
records to the data lake. This connector integrates with the WithSecure Elements API  to query
devices, events, incidents, and detections.

In addition, you can use WithSecure Elements responders to configure Webhook actions that
can be triggered manually or that can enhance Automated Threat Hunting (ATH) actions.

WithSecure Elements responders use Webhook templates that support actions. Each action is
one responder, there are four actions, and hence there are four WithSecure Elements
responders: WithSecure Elements Isolate From Network, WithSecure Elements Kill Process,
WithSecure Elements Kill Thread, and WithSecure Elements Release From Network Isolation.

This document describes how to configure a WithSecure Elements responder using the
Universal Webhook Responder, how to add the respond function to a WithSecure Elements
connector and how to manually trigger an action and perform ATH actions with a WithSecure
Elements responder.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: WithSecure Elements

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

Detections

Devices

Incidents

Security Events

Syslog

Assets (for
Devices)

msg_class:

withsecure_element
s_detection

withsecure_element
s_device

withsecure_element
s_incident

withsecure_element
s_event

msg_origin.source:

withsecure_element
s

msg_origin.vendor:

withsecure

msg_origin.category:

endpoint

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

Webhook action templates:

WithSecure Elements Isolate from Network

WithSecure Elements Kill Process (Beta feature)

WithSecure Elements Kill Thread (Beta feature)

WithSecure Elements Release From Network Isolation

Third Party Native Alert Integration Details

This connector ingests logs from WithSecure Elements to get the raw alerts that are stored in the Syslog
index. Select the Detections content type.

Stellar Cyber maps WithSecure Elements detections. The detections are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.
Deduplication is by tenantid, event.threat.name, user.name, process.hash.sha1,
withsecure_elements.detectionId, and withsecure_elements.description.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

For Collect: Base URL, Client ID, Client Secret, and Organization ID

For Respond: Hostname, Protocol, Client ID, and Client Secret

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class:withsecure_elements_detection AND NOT event.severity_str:info AND NOT
withsecure_elements.riskLevel:info AND NOT
event.threat.name:network_connection_discovery_by_detected_process

Adding a WithSecure Elements Connector
To add a WithSecure Elements connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber (Collect)
3. Add the connector in Stellar Cyber (Respond)
4. Test the connector
5. Verify ingestion
6. Use actions

Obtaining WithSecure Elements Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following WithSecure
Elements credentials:

Base URL—The base URL for API access. The default is:
https://api.connect.withsecure.com.

Hostname—Hostname for respond function. The default is:
api.connect.withsecure.com.

Client ID and Client Secret—Generated API Client ID and Client Secret.

Generating a Client ID and Client Secret

To generate a Client ID and Client Secret:

1. Log in to the Console .

2. Navigate to Management > Organization Settings.

3. Select the API Clients tab and click Add new.

4. On the Add new API client page, enter an Organization and a Description.

For an API key for the Collect function, check Read-only.

For an API key for the Respond function, uncheck Read-only.

5. Click Add.

6. The API client is generated. Copy the Client ID and Secret. You will need them when

configuring the connector in Stellar Cyber.

 Store the Client ID and Secret in a safe location. It cannot be retrieved later

although you can create a new one.

Adding the Connector in Stellar Cyber (Collect)
To add the collect function for a WithSecure Elements connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose WithSecure Elements from the Type dropdown.

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

12. Enter the Base URL you noted above in Obtaining WithSecure Elements Credentials.

13. Enter the Client ID you noted above.

14. Enter the Client Secret you noted above.

15. (Optional) Enter the Organization ID.

 If an Organization ID is not entered, the default organization of the authenticated

client is used.

16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a reason to, otherwise, it
is not a good security practice.

17. Choose the Interval (min). This is how often the logs are collected.

 The logs for Devices are queried every 24 hours.

18. Choose the Content Type you would like to collect. The logs for Devices, Detections,

Incidents, and Security Events are supported.

  The Devices content type is always selected and cannot be removed from the

configuration as it is required for host information.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Adding the Connector in Stellar Cyber (Respond)
To add the respond function for a WithSecure Elements connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: WithSecure

Elements Isolate From Network, WithSecure Elements Kill Process, WithSecure
Elements Kill Thread, or WithSecure Elements Release From Network Isolation.

The asterisk (*) indicates a required field.

 WithSecure Elements Kill Process and WithSecure Elements Kill Thread are

Beta features.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector. In
addition to specific tenants, this connector supports All Tenants, which means that a
WithSecure Elements responder can be used across tenants.

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

11. Enter the Hostname you noted above in Obtaining WithSecure Elements Credentials.

12. Select the Protocol, either HTTP or HTTPS. If you select HTTPS, another field is

available: Disable SSL Certificate Verification.

13. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

14. Enter the Client ID and Client Secret you noted above.

15. Click Next. The final confirmation tab, Done, appears.

16. Click Submit.

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

2. Change the Indices for the type of content you collected:

For Devices, Detections, Incidents, and Security Events, change the
Indices to Syslog.

For Devices only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Using Actions
With a WithSecure Elements responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with a WithSecure Elements responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Syslog.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab. Webhook actions appear under External Actions.

5. Click a WithSecure Elements Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. You can modify the JSON Body by entering string values or curly brace expressions.

Fill in any empty fields, such as organizationId, threadId, or targets.

7. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with a WithSecure Elements responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured WithSecure Elements responder from the dropdown

menu for the Webhook Responder.

The template populates the fields in the Path and Query and JSON Body.

8. You can modify the JSON Body by entering string values or curly brace expressions.

9. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

10. Click Submit.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

