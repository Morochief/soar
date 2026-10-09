Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Recorded Future Connectors

This connector allows Stellar Cyber to ingest logs from Recorded Future and add the records to
the data lake. It integrates with Recorded Future APIs to ingest alerts data.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Recorded Future

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alert

Playbook Alert

Index

Syslog

Locating Records

msg_class:

recorded_future_al
ert

recorded_future_pl
aybook_alert

msg_origin.source:

recorded_future

msg_origin.vendor:

Content Type

Index

Locating Records

recorded_future

msg_origin.category:

cloudsec

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Recorded Future to get the raw alerts that are stored in the Syslog
index. Select the Alert and Playbook Alert content types.

Stellar Cyber maps Recorded Future alerts. The alerts are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by the following fields:

Alert—tenantid and recorded_future.id.

Playbook Alert: tenantid and recorded_future.playbook_alert_id.

For Playbook Alert, there are the following categories of alerts:

Domain Abuse

Novel Identity Exposure

Data Leakage on Code Repository

Cyber Vulnerability

Third Party Risk

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Base URL and API Token

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, for Alert, use the
query: msg_class: recorded_future_alert AND _exists_: event.threat.name

To search the alerts in the Alerts index or the Original Records in the Syslog index, for Playbook Alert, use
the query: msg_class: recorded_future_playbook_alert AND _exists_: event.threat.name

Adding a Recorded Future Connector
To add a Recorded Future connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector

4. Verify ingestion

Obtaining Recorded Future Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Recorded
Future credentials:

Base URL—The base URL for API access. The default is
https://api.recordedfuture.com.

API Token—The credential for the Recorded Future API.

Follow the guidance in the Recorded Future documentation  to set up the API Token.

Adding the Connector in Stellar Cyber
To add a Recorded Future connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Cloud Security from the Category dropdown.

5. Choose Recorded Future from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.

    Notes:

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

12. Enter the Base URL you noted above in Obtaining Recorded Future Credentials.

13. Enter the API Token you noted above.

14. Choose the Content Type you would like to collect. The logs for Alert and Playbook

Alert are supported.

 The Playbook Alert has the following six categories: domain_abuse,

cyber_vulnerability, code_repo_leakage, third_party_risk,
identity_novel_exposures, and geopolitics_facility.

15. Choose the Interval (min). This is how often the logs are collected.

16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Recorded Future connector
tests that the Base URL and API Token are correct and data requests for the requested
content type returns successful responses.

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

