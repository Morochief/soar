Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring ConnectSecure V4 Connectors

This connector allows Stellar Cyber to ingest logs from ConnectSecure V4 and add the records
to the data lake. It integrates with the ConnectSecure V4 API  to get Asset, Asset Wise
Vulnerabilities, Remediation Plan, and Vulnerability Suppression data.



Note the following rate limits in the ConnectSecure documentation :

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: ConnectSecure V4

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Asset

Asset Wise Vulnerabilities

Remediation Plan

Vulnerability Suppression

Syslog

Assets (for
Asset)

Scans (for Asset
Wise
Vulnerabilities
and Vulnerability
Suppression)

msg_class:

connectsecurev4_as
set

connectsecurev4_as
set_wise_vulnerabi

lity

connectsecurev4_re
mediation

connectsecurev4_vu
lnerability_suppre
ssion

msg_origin.source:

connectsecurev4

msg_origin.vendor:

connectsecure

msg_origin.category:

security_scan

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL, Tenant Name, Client ID, and Client Secret

Adding a ConnectSecure V4 Connector
To add a ConnectSecure V4 connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

For a limitation on filtering APIs, see Filtering APIs on ConnectSecure V4 Connectors.

Obtaining ConnectSecure V4 Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following
ConnectSecure V4 credentials.

Base URL—The base URL for API access. There is no default URL. Each user will have
a different pod. An example of a Base URL is https://pod106.myconnectsecure.com.
See Finding the API URL.

Tenant Name—The name of the ConnectSecure V4 tenant for authentication. See
Finding the Tenant Name.

Client ID and Client Secret—The authentication credentials. See Getting the Client ID
and Client Secret.

Getting the Client ID and Client Secret

Follow the guidance in the ConnectSecure documentation for User Management and
Security .

 The following procedure is a summary.

To obtain the Client ID and Client Secret:

1. Log in to the portal and navigate to Global > Settings > Users.

2. Click Add.

3. Enter the user information, such as First Name, Last Name, and Email, then select the

roles, and choose the Company Level Access for that role.

4. For an existing user, select Action > API Key.

5. Copy your Client ID and Client Secret.

6. Click Close.

Finding the API URL

To find the API URL:

1. Log in to the portal and navigate to Global Settings > Users.

2. Click API Documentation.

3. Locate the URL, which in this case is https://pod106.myconnectsecure.com.

Finding the Tenant Name

Locate the tenant name in your welcome email as follows:



The Stellar Cyber configuration uses the ConnectSecure V4 tenant name for authentication

only. The connector does not perform client-side filtering by company. Instead, the scope of
data ingestion is determined by the permissions assigned to the ConnectSecure V4 user
associated with the API key as follows:

If the user has global or administrator-level access, the connector can ingest data
for all companies within that tenant.

If the user is restricted to specific companies, only data for those companies will
be returned and ingested.

Adding the Connector in Stellar Cyber
To add a ConnectSecure V4 connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose ConnectSecure V4 from the Type dropdown.

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

12. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

13. Enter the Base URL you noted above in Obtaining ConnectSecure V4 Credentials.

14. Enter the ConnectSecure V4 Tenant Name you noted above.

15. Enter the Client ID you noted above.

16. Enter the Client Secret you noted above.

17. Choose the Interval (min). This is how often the logs are collected.

18. Choose the Content Type you would like to collect. The logs for Asset, Asset Wise
Vulnerabilities, Remediation Plan, and Vulnerability Suppression are supported.

  The Asset content type is always selected and cannot be removed from the

configuration as it is required for host information.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the ConnectSecure V4 connector
tests that the Base URL, Tenant Name, Client ID, and Client Secret are correct and data
requests for the requested content types return successful responses.

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

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For all content types, change the Indices to Syslog.

 The Asset content type is sent to the Syslog index first, then a host log

sends the data to the Assets index.

For Asset change the Indices to Assets.

For Asset Wise Vulnerabilities and Vulnerability Suppression change the
Indices to Scans.

The table immediately updates to show ingested Interflow records.

Filtering APIs on ConnectSecure V4 Connectors

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

ConnectSecure V4 Connector Content Types

The ConnectSecure V4 connector content types impacted by this limitation are as follows:

Asset

Asset Wise Vulnerabilities

Remediation Plan

Vulnerability Suppression

For the listed content types, an internal filter is implemented that filters the response by a date
field (datetime or timestamp). The internal time filter in the ConnectSecure V4 connector
supports a second level filter.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

