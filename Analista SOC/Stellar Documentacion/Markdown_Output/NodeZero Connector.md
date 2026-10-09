Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring NodeZero Connectors

This connector allows Stellar Cyber to ingest logs from NodeZero and add the records to the data lake. It integrates
with the Horizon3.ai API  to query penetration tests and related action logs, weaknesses, and hosts.

NodeZero is an autonomous penetration testing platform developed by Horizon3.ai, designed to help organizations
proactively identify, exploit, and remediate security vulnerabilities across their IT environments.

By default, archived pentests are excluded from the API's pentest page. If you archive a pentest before it is collected,
this connector will note be able to ingest it.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data when the ingestion
volume is large, which potentially can lead to data loss. This can happen when the processing capacity of the
collector is exceeded.

Connector Overview: NodeZero

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Action Logs

Hosts

Pentests

Weaknesses

Index

Syslog

Scans

Assets

Locating Records

msg_class:

horizon3ai_nodezero_actio
n_logs

horizon3ai_nodezero_hosts

horizon3ai_nodezero_pente
sts

horizon3ai_nodezero_weakn
esses

msg_origin.source:

horizon3ai_nodezero

msg_origin.vendor:

horizon3ai

msg_origin.category:

penetration_testing_tool

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL and API Key

Adding a NodeZero Connector
To add a NodeZero connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining NodeZero Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following NodeZero credentials. Follow the
guidance in the Horizon3.ai documentation .

Base URL—The base URL for API access. The default is https://api.horizon3ai.com.

API Key—The API key for authorization.

You can obtain the API Key from the Horizon3.ai Portal .

Adding the Connector in Stellar Cyber
To add a NodeZero connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab cannot be changed
after you add the connector.

4. Choose Penetration Testing from the Category dropdown.

5. Choose NodeZero from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this tenant name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information, see Managing Log

Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Base URL, for example: https://api.horizon3ai.com

13. Enter the API Key you noted above in Obtaining NodeZero Credentials.

14. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL certificate verification. Only
disable SSL certificates if you have a necessary reason to, otherwise, it is not a good security practice and
may expose the connection to security risks.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Pentests, Hosts, Action Logs, and

Weaknesses are supported.

  The Pentests content type is always selected and cannot be removed from the configuration as it is
the default. The Hosts content type is always selected and cannot be removed from the configuration
as it is required for host information.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the NodeZero connector tests that the Base URL and

API Key are correct and data requests for the requested content types return successful responses.

When you add (or edit) a connector, we recommend that you run a test to validate the connectivity parameters you
entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60 seconds for new or

modified configuration details to be propagated to the sensor before performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure result. A successful
test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by using the X button. If the
test fails, you can select the   button from the same row to review and correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the connector status, but if

issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP Er

HTTP Standar

ror Code

d Error Name

Explanation

Recommendation

400

Bad Request

This error occurs when there is an error in the connector

Did you configure the connector correctly?

configuration.

401

Unauthorized

This error occurs when an authentication credential is invalid or

Did you enter your credentials correctly?

when a user does not have sufficient privileges to access a

Are your credentials expired?

specific API.

403

Forbidden

This error occurs when the permission or scope is not correct in a

valid credential.

Are your credentials entitled or licensed for that specific

resource?

Did you enter your credentials correctly?

Do you have the required role or permissions for that

credential?

404

429

Not Found

This error occurs when a URL path does not resolve to an entity. Did you enter your API URL correctly?

Too Many

Requests

This error occurs when the API server receives too much traffic or

The server or user license/quota will eventually recover. The

if a user’s license or entitlement quota is exceeded.

connector will periodically retry the query.

If this occurs unexpectedly or too often, work with your API

provider to investigate the server limits, user licensing, or

quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For all content types, change the Indices to Syslog.

For Weaknesses only, change the Indices to Scans.

For Hosts only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

