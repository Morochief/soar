Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Manage Engine Endpoint Central
Connectors

This connector allows Stellar Cyber to ingest logs from Manage Engine Endpoint Central and
add the records to the data lake. It integrates with the Audit Logs API to retrieve audit events.

Note the following Manage Engine Endpoint Central rate limit: APIs can be used to a maximum
of 30 times per 5 minutes per technician.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Manage Engine Endpoint Central

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Audit Logs

Index

Syslog

Locating Records

msg_class:

manage_engine_endp
oint_central_audit
_logs

msg_origin.source:

manage_engine_endp
oint_central

Content Type

Index

Locating Records

msg_origin.vendor:

manage_engine

msg_origin.category:

it_mgmt

Domain

<Auth URL> and <Base URL>

where <Auth URL> and <Base URL> are variables from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Auth URL, Base URL, Client ID, and Client Secret

Adding a Manage Engine Endpoint Central Connector
To add a Manage Engine Endpoint Central connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Manage Engine Endpoint Central Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Manage
Engine Endpoint Central credentials:

Auth URL—The authentication URL. The default is https://accounts.zoho.com. Refer to
the Manage Engine Endpoint Central  documentation for the domains available in the
Multiple data centres section.

Base URL—The base URL for API access. The default is
https://endpointcentral.manageengine.com. Refer to the Manage Engine Endpoint
Central  documentation for the domains available in the Multiple data centres section.

Client ID and Client Secret—The generated credentials. Follow the guidance in the
Manage Engine Endpoint Central  documentation in the Authentication section for
generating the Client ID and Client Secret.

Adding the Connector in Stellar Cyber

To add a Manage Engine Endpoint Central connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose IT Management from the Category dropdown.

5. Choose Manage Engine Endpoint Central from the Type dropdown.

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

12. Enter the Auth URL, you noted above in Obtaining Manage Engine Endpoint Central

Credentials. For example: https://accounts.zoho.com.

13. Enter the Base URL,you noted above. For

example: https://endpointcentral.manageengine.com.

14. Enter the Client ID and Client Secret you noted above.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Choose the Interval (min). This is how often the logs are collected.

 The API requires the difference between startTime and endTime to be at least five
(5) minutes. Setting the connector’s Interval (min) below 5 minutes causes errors.
The error resolves automatically when the range between start_time and end_time
exceeds 5 minutes.

17. Choose the Content Type you would like to collect. The logs for Audit Logs are

supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Manage Engine Endpoint
Central connector tests that the Auth URL, Base URL, Client ID, and Client Secret are
correct and data requests for the requested content types return successful responses.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

