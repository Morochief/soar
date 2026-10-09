Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring HYAS Protect Connectors

This connector allows Stellar Cyber to ingest logs from HYAS Protect and add the records to the
data lake. This connector integrates with the HYAS Protect API to query for DNS log reports. It
supports ingesting records, generating assets, and alerting on data from HYAS Protect to
monitor DNS logs using the Stellar Cyber platform.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: HYAS Protect

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Agents

DNS Log Reports

Syslog

Assets (for
Agents)

msg_class:

hyas_protect_agent

hyas_protect_dns_l
og_report

msg_origin.source:

hyas_protect

msg_origin.vendor:

hyas

Content Type

Index

Locating Records

msg_origin.category:

dnssec

 If there is asset information in the logs for Agents, the detected assets are reported in the Assets

Index.

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from HYAS Protect to get the raw alerts that are stored in the Syslog index.
Select the DNS Log Reports content type.

Stellar Cyber maps HYAS Protect passthrough alerts. The incidents are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

The following types of passthrough alerts are supported: Domain tagged with Suspicious Registrar,
Domain tagged as blocked by HYAS Engine, and Domain tagged as Highly Suspicious.

Deduplication is by tenantid, dns.question.name, and srcip.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Base URL and API Key

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
queries:

msg_class:hyas_protect_dns_log_report AND hyas_protect.verdictStatus: block
AND _exists_: dns.question.name

msg_class:hyas_protect_dns_log_report AND hyas_protect.verdictStatus: bad AND
_exists_: dns.question.name

msg_class:hyas_protect_dns_log_report AND hyas_protect.verdictStatus:
suspicious AND _exists_: dns.question.name

Adding a HYAS Protect Connector
To add a HYAS Protect connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining HYAS Protect Credentials

Before you configure the connector in Stellar Cyber, you must obtain the following HYAS Protect
credentials:

Base URL—The base URL for API access. The default is https://api.hyas.com .

API Key

(Optional) Client ID

Obtaining API Key

The API Key is emailed to you when you create a user account.

To create a user:

1. Log in as an Administrator to the HYAS Protect UI.

2. Click the Settings (gear) icon, and then select Manage User Accounts.

3. Select + and then add the user email and other selections.

4. From the API Key drop down, select Generate Key.

5. Click Save.

6. The user will receive an email with login instructions, such as the following:

 Store the API Key in a safe location. It cannot be retrieved later although you can

request a new one.

Obtaining Client ID

The client ID is a unique identifier for each organization. API endpoints may require the client ID
to identify for which organization the data is being requested.

To obtain the Client ID:

1. In the HYAS Protect UI, click the Settings (gear) icon, and then select Protect Agent.

2. In the HYAS Protect Agent Dashboard, select Install.

3. Copy your Install Key.

 Install Key = Client ID.

Adding the Connector in Stellar Cyber
To add a HYAS connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose DNS Security from the Category dropdown.

5. Choose HYAS Protect from the Type dropdown.

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

12. Enter the Base URL you noted above in Obtaining HYAS Protect Credentials. The

default is https://api.hyas.com.

13. Enter the API Key you noted above.

14. (Optional) Enter the Client ID you noted above.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Agents and DNS Log

Reports are supported.

  The Agents content type is always selected and cannot be removed from the

configuration as it is required for host information.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

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

For Agents and DNS Log Reports, change the Indices to Syslog.

For Agents only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

