Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Perception Point X-Ray Connectors

This connector allows Stellar Cyber to ingest logs from Perception Point X-Ray and add the
records to the data lake. This connector integrates with the Perception Point X-Ray APIs to query
scans.

Note the following rate limit in the Perception Point API documentation:

Throttling is based on the commercial agreement, with a default maximum of 100 API
calls per minute.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Perception Point X-Ray

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Scans

Index

Syslog

Locating Records

msg_class:

perception_point_x
_ray_scans

msg_origin.source:

Content Type

Index

Locating Records

perception_point_x
_ray

msg_origin.vendor:

perception_point

msg_origin.category:

email

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL and API Token

Adding a Perception Point X-Ray Connector
To add a Perception Point X-Ray connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Perception Point X-Ray Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Perception
Point X-Ray credentials:

Base URL—The base URL for API access, which you can select from the dropdown
menu. The default is https://api.perception-point.io. There are also two other URLs,
https://api.eu.perception-point.io and https://api.aus. perception-point.io, as well as
Custom URL.

Custom URL—The custom URL, which you can enter in the Custom URL field if a URL
is not available in the Base URL dropdown menu.

API Token—The authentication credentials. To generate an API Token Key, follow the
guidance in the Perception Point API  documentation or in Getting the API Token.

 You need to sign in to see the Perception Point documentation.

Getting the API Token

To get the API token:

1. Log in to the Perception Point X-Ray portal.

2. Click Account and then click Profile.

3. Locate the Security section and the API Key field.

4. Copy the API Key.

Adding the Connector in Stellar Cyber
To add a Perception Point X-Ray connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose Perception Point X-Ray from the Type dropdown.

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

12. Select the Base URL from the drop-down.

13. Or, select Custom URL from the Base URL dropdown menu and enter a URL in the

Custom URL field.

14. Enter the API Token you noted above in Obtaining Perception Point X-Ray Credentials.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Choose the Interval (min). This is how often the logs are collected.

17. Choose the Content Type you would like to collect. The logs for Scans is supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Perception Point X-Ray

connector tests that the Base URL and API Token are correct and data requests for the
requested content types return successful responses.

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

