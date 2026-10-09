Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cyble Connectors

This connector allows Stellar Cyber to ingest logs from the Cyble Threat Intelligence Platform
and add the records to the data lake. It integrates with the Cyble API to query alerts.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Cyble

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alerts

Index

Syslog

Locating Records

msg_class:

cyble_alerts

msg_origin.source:

cyble

msg_origin.vendor:

cyble

msg_origin.category:

Content Type

Index

Locating Records

threat_intel_vendo
r

Domain

<API URL>

where <API URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Cyble to get the raw alerts that are stored in the Syslog index. Select the
Alerts content type.

Stellar Cyber maps Cyble alerts. The alerts are read from the Syslog index, enriched with Stellar Cyber
fields, and mapped (with deduplication) to the Alerts index.

The following alert types are supported: leaked_credentials, stealer_logs, darkweb_data_breaches,
darkweb_marketplaces, suspicious_domains, vulnerability, new_vulnerability ip_risk_score, and
ssl_expiry.

Deduplication is by cyble.id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

API URL and Token

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class:cyble_alerts AND (event.threat.name:(leaked_credentials OR
stealer_logs OR darkweb_data_breaches OR darkweb_marketplaces OR suspicious_domains
OR vulnerability OR new_vulnerability OR ip_risk_score OR ssl_expiry) OR
event.severity_str:HIGH)

Adding a Cyble Connector
To add a Cyble connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Cyble Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Cyble
credentials.

API URL—The URL for API access. The example is https://example.cyble.ai. Your
URL will have your customer name instead of the word example. Obtain your specific

URL from Cyble.

Token—The authentication credential. You can view and manage API keys in the
platform under your Cyble account.

Adding the Connector in Stellar Cyber
To add a Cyble connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Threat Intel Vendor from the Category dropdown.

5. Choose Cyble from the Type dropdown.

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

12. Enter the API URL, you noted above in Obtaining Cyble Credentials.

13. Enter the Token you noted above.

14. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Alerts are supported.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Cyble connector tests that the
API URL and Token are correct and data requests for the requested content types return
successful responses.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

403

Forbidden

This error occurs when the permission or scope is not

correct in a valid credential.

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

