Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Juniper Mist Connectors

This connector allows Stellar Cyber to ingest logs from Juniper Mist Wireless and add the
records to the data lake. It integrates with the Juniper Mist API  to query for alarms, logs, and
system events.

Note the following rate limit in the Juniper Mist documentation (Mist API Introduction ):

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Juniper Mist

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alarms

Logs

System Events

Index

Syslog

Locating Records

msg_class:

juniper_mist_alarm
s

Content Type

Index

Locating Records

juniper_mist_logs

juniper_mist_syste
m_events

msg_origin.source:

juniper_mist

msg_origin.vendor:

juniper_networks

msg_origin.category:

wireless

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL and API Token

Adding a Juniper Mist Connector
To add a Juniper Mist connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Juniper Mist Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Juniper Mist
credentials:

Base URL—The base URL for API access, for example, https://api.mist.com.

API Token—Juniper Mist API token used to authenticate your account.

Generating an API Token

To generate a Juniper Mist API token, follow the guidance in the Juniper documentation for an
Organization Token :

1. Log in to the Juniper Mist portal.

2. From the menu on the left, select Organization > Admin > Settings.

3. Scroll down to API Token and click Create Token.

4. Select an Access Level to define the permissions for the token.

5. Click Generate.

6. Click the copy button next to the Key field.

 Store the API Key in a safe location. It cannot be retrieved later although you can

create a new one.

7. Click Done.

8. Click Save near the top-right corner of the page.

Adding the Connector in Stellar Cyber
To add a Juniper Mist connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose NDR from the Category dropdown.

5. Choose Juniper Mist from the Type dropdown

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

12. Enter the Base URL, for example, https://api.mist.com.

13. Enter the API Token you noted above in Obtaining Juniper Mist Credentials.

14. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

15. Choose the Interval (min). This is how often this connector retrieves data from Juniper

Mist. The default is 5 minutes.

16. Choose the Content Type you would like to collect. The logs for Alarms, Logs, and

System Events are supported.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Juniper Mist connector tests
that the Base URL and API Token are correct and data requests for the requested content
types return successful responses.

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

is exceeded.

query.

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

