Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Acronis Cyber Protect Cloud
Connectors

This connector allows Stellar Cyber to ingest logs from Acronis Cyber Protect Cloud and add the
records to the data lake. This connector integrates with the Acronis API to query alerts, agents,
and incidents.

In addition, you can use Acronis responders to configure Webhook actions that can be triggered
manually or that can enhance Automated Threat Hunting (ATH) actions.

Acronis responders use Webhook templates that support actions. Each action is one responder,
there are three actions, and hence there are three Acronis responders: Acronis Workload Isolate,
Acronis Workload Restart, and Acronis Workload Shutdown.

This document describes how to configure an Acronis responder using the Universal Webhook
Responder, how to add the respond function to an Acronis connector and how to manually trigger
an action and perform ATH actions with an Acronis responder.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Acronis Cyber Protect Cloud

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

Agents (automatically set)

Incidents

Syslog

Assets (for
Agents)

msg_class:

acronis_cyber_prot
ect_alert

acronis_cyber_prot
ect_agent

acronis_cyber_prot
ect_incidents

msg_origin.source:

acronis_cyber_prot
ect

msg_origin.vendor:

acronis

msg_origin.category:

endpoint

Domain

<Host URL>

where <Host URL> is a variable from the configuration of this connector

Response Actions

Webhook action templates:

Acronis Workload Isolate

Acronis Workload Restart

Acronis Workload Shutdown

Third Party Native Alert Integration Details

This connector ingests logs from Acronis Cyber Protect Cloud to get the raw alerts that are stored in the
Syslog index. Select the Alerts content type.

Stellar Cyber maps Acronis Cyber Protect Cloud alerts. The alerts are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

The following four alert types are supported: Email security, EDR, Antimalware protection, and URL
filtering. Tactic and Technique are based on alert type.
Deduplication is by tenantid, event.threat.name, host.name, user.name, url, process.pid,
file.hash.sha1, email.from.address, and acronis_cyber_protect.details.edrAlertId.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Host URL (data center URL), Client ID, Client Secret

Locating Records

To search the alerts in the Alerts index, use the query: msg_class: acronis_cyber_protect_alert
AND event.category: ('URL filtering' OR 'EDR' OR 'Antimalware protection' OR 'Email
security')

To search the Original Records in the Syslog index, use the query: msg_class:
acronis_cyber_protect_alert

Adding an Acronis Cyber Protect Cloud Connector
To add an Acronis Cyber Protect Cloud connector:

1. Obtain credentials
2. Adding the connector in Stellar Cyber (Collect)
3. Add the connector in Stellar Cyber (Respond)
4. Test the connector
5. Verify ingestion

For a limitation on filtering APIs, see Filtering APIs on Acronis Connectors.

Obtaining Acronis Cyber Protect Cloud Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Acronis Cyber
Protect Cloud credentials:

Client ID

Client Secret

Host URL (data center URL), for example, https://eu2-cloud.acronis.com or https://eu8-
cloud.acronis.com.

Getting the Client ID and Client Secret

Follow the guidance in Acronis Cyber Protect Cloud documentation for Creating an API client .

1. Using an administrator account role, log in to the management portal.

2. Click Settings | API clients | Create API client.

3. Enter a name for the API client.

4. Click Next.

5. Copy and save the ID and secret value of the client and the data center URL.

 Store the ID and secret value in a safe location. The secret value cannot be

retrieved later although it can be reset.

6. Click Done.

Adding the Connector in Stellar Cyber (Collect)
To add an Acronis Cyber Protect Cloud connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Acronis Cyber Protect Cloud from the Type dropdown.

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

12. Enter the Host URL you noted above in Obtaining Acronis Cyber Protect Cloud

Credentials, for example, https://eu2-cloud.acronis.com.

13. Enter the Client ID you noted above.

14. Enter the Client Secret you noted above.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Agents, Alerts, and

Incidents are supported.

  The Agents content type is always selected and cannot be removed from the
configuration as it is required for host information. The logs for Agents are set
automatically.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Adding the Connector in Stellar Cyber (Respond)
To add the respond function for an Acronis connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Webhook from the Category dropdown.

5. Choose one of the predefined templates from the Type dropdown: Acronis Workload

Isolate, Acronis Workload Restart, or Acronis Workload Shutdown.

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
Acronis responder can be used across tenants.

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

11. Enter the Hostname you noted above in Obtaining Acronis Cyber Protect Cloud

Credentials.

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
The Test button for Acronis shows success with a valid credential.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

For Alerts and Agents, change the Indices to Syslog.

For Agents only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Filtering APIs on Acronis Connectors
Some vendor APIs integrated through Stellar Cyber connectors do not support time-bounded
querying (for example, using start_time, end_time, or equivalent filters), and may lack time-series
metadata on records. As a result, Stellar Cyber is required to pull the entire dataset during each
polling cycle, regardless of whether the data has changed.

Potential Impact

Performance Overhead: The absence of time-based filtering may lead to increased load
on the Stellar Cyber ingestion pipeline and degrade collection performance over time.

Inefficient Polling: The connector must fetch and process all available records each
cycle, leading to longer collection durations and higher resource usage.

Scalability Limitations: For large or growing datasets (for example, alerts, logs, or
assets), this limitation may result in delayed data availability or collection timeouts.

Data Inconsistency: Data may be duplicated or missed due to the quantity of data.

When working with connectors that have this limitation, consider the potential impact on
performance and collection efficiency.

Recommendation

Where possible, we recommend working with your vendor to improve or add time range filtering
capabilities to their APIs.

Acronis Connector Content Types

The Acronis connector content types impacted by this limitation are as follows:

Agents

Alerts

Incidents (filter by date)

For the Incidents content type, an internal filter is implemented that filters the response by a date
field (datetime or timestamp). The Acronis internal filter supports a second level filter.

Using Actions
With an Acronis responder, you can:

Manually trigger an action

View action status

Perform an ATH action

Manually Triggering an Action

To manually trigger an action with an Acronis responder:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the record type, for example, Syslog.

3. Scroll down the page and click the icon for More Info in the Actions column.

4. Click the Actions tab. Webhook actions appear under External Actions.

5. Click an Acronis Webhook action.

The template populates the fields in the Path and Query and the JSON Body.

6. Verify the Path and Query. Enter your Acronis Cyber Protect Incident ID in the
{{acronis_cyber_protect.incident_id}} parameter and your Acronis Cyber Protect
Customer ID in the {{acronis_cyber_protect.customer_id}} parameter in the path, for
example: /api/mdr/v1/incidents/f32a6e51-7c84-4a39-9b76-

3a52b6c1942d/response_action?
action=WORKLOAD_ISOLATE&customer_id=9c47a6f2-84d5-4e33-9f11-52f70a6e9b28

Refer to the Acronis documentation for Performing and monitoring response actions .

7. The JSON Body does not need to be modified.

8. To perform the action, click Submit.

Viewing Action Status

To view action status:

1. Click Automation | Action History.

2. Click Webhook Actions.

You can view the action status or error message in the table.

Performing an ATH Action

To perform an ATH action with an Acronis responder:

1. Click Automation | Automation.

2. Click Create.

3. Scroll down to Actions.

4. Click the  button to add an action. Another action appears below the existing action.

5. Select the Trigger on condition.

6. Select Webhook Responder for the Type.

7. Select a previously configured Acronis responder from the dropdown menu for the

Webhook Responder.

The template populates the fields in the Path and Query and JSON Body.

8. The Path and Query do not need to be modified.

9. The JSON Body does not need to be modified.

10. (Optional) Click Override Default Settings to override the playbook's mute settings and

mute just this action.

11. Click Submit.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

