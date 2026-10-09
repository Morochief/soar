Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Automox Connectors

This connector allows Stellar Cyber to ingest logs from Automox and add the records to the data
lake. It integrates with Automox APIs to query several content types.

Note the following rate limit in the Automox documentation :

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Automox

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: 8 hours

Collected Data

Content Type

Index

Locating Records

Audit Logs

Devices

Events

Policies

Syslog

Assets (for
Devices)

msg_class:

automox_audit_logs

automox_devices

automox_events

Content Type

Index

Locating Records

Prepatch Report

Users

automox_policies

automox_prepatch_r
eport

automox_users

msg_origin.source:

automox

msg_origin.vendor:

automox

msg_origin.category:

it_mgmt

 The Automox Audit Logs API may occasionally experience reliability issues. In cases where
endpoint problems occur, data retrieval can be delayed for extended periods. As a result, the
connector may temporarily stall and have difficulty catching up on missed data.

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL and API Token

Adding an Automox Connector
To add an Automox connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

For a limitation on filtering APIs, see Filtering APIs on Automox Connectors.

Obtaining Automox Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Automox
credentials. Follow the guidance in the Automox documentation .

Base URL—The base URL for API access. The default is https://console.automox.com.

API Token—The API token for Authorization, for example:

"Authorization": "Bearer <API_TOKEN>"

where you replace <API_TOKEN> with the token value

(Optional) Organization ID—The ID for the organization, which is the last part of your
console URL, for example, 0000:

https://console.automox.com/dashboard?o=0000

 The Organization ID is a number, not a UUID. When an Organization ID is
provided, the connector will only collect data for the specified organization.

Adding the Connector in Stellar Cyber
To add an Automox connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose IT Management from the Category dropdown.

5. Choose Automox from the Type dropdown.

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

12. Enter the Base URL, for example: https://console.automox.com.

13. Enter the API Token you noted above in Obtaining Automox Credentials.

14. (Optional) Enter the Organization ID you noted above.

15. Choose the Content Type you would like to collect. The logs for Devices, Audit Logs,

Events, Policies, Prepatch Report, and Users are supported.

  The Devices content type is always selected and cannot be removed from the

configuration as it is required for host information.

16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Automox connector tests that

the Base URL and API Token are correct and data requests for the requested content types
return successful responses.

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

Change the Indices to Syslog.

For Devices only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Filtering APIs on Automox Connectors
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

Automox Connector Content Types

The Automox connector content types impacted by this limitation are as follows:

Device (asset)

Users

Policies

PrePatch Report

Events (filter by date only)

Audit Logs (filter by date only)

The Device, Users, Policies, and PrePatch Report content types can only be pulled for their
entire dataset (no time range filter).

For the Events and Audit Logs content types, each time the connector is sent a request to get
data, it will request it with full a day filter (for example, 2025/07/22) instead of an hour/minute
time range (for example, 2025/07/21 23:50 ~ 2025/07/22 00:00).

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

