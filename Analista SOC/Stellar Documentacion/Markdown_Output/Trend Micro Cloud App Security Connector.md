Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Trend Micro Cloud App Security
Connectors

This connector allows Stellar Cyber to ingest logs from Trend Micro Cloud App Security  and
add the records to the data lake. This connector integrates with the Log Retrieval API  to get
events for the Exchange, OneDrive, Sharepoint Log, and Teams content types.

Cloud App Security (CAS) provides advanced protection for the following cloud applications and
services: Microsoft Office 365 services (Exchange Online, SharePoint Online, OneDrive, and
Microsoft Teams), Box, Dropbox, and Google Workspace (Google Drive and Gmail). CAS
searches for security risks and undesirable data sent through email services, or saved in cloud
storage applications by performing real-time scanning on files in supported cloud applications
and services.



Trend Micro Cloud App Security has a rate limit of approximately 20 requests per minute.
The rate limit will impact ingestion of data by this connector when the following occurs:

There is a data spike

The connector is set to ingest too many log event types

The connector stopped and needs to do a long backfill*

Two or more connectors were created with the same credential

*Due to the rate limit, the initial backfill will only get data for the last 10 minutes.

The rate limit is tied to the API key. The workaround is to create multiple connectors with
different API keys.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Trend Micro Cloud App Security

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: 5 minutes

Collected Data

Content Type

Exchange

OneDrive

Sharepoint Log

Teams

Index

Syslog

Locating Records

msg_class:

trendmicro_cas_log

s_exchange

trendmicro_cas_log

s_onedrive

trendmicro_cas_log
s_sharepoint

trendmicro_cas_log

s_teams

msg_origin.source:

trendmicro_cloud_a
pp_security

msg_origin.vendor:

trendmicro

msg_origin.category:

cloudsecurity

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Trend Micro Cloud App Security to get the raw alerts that are stored in
the Syslog index. Select the Exchange, OneDrive, Sharepoint Log, and Teams content types.

Stellar Cyber maps Trend Micro Cloud App Security events. The events are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by trendmicro_cloud_app_security.log_item_id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Base URL and API Key

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class:(trendmicro_cas_logs_sharepoint OR trendmicro_cas_logs_exchange OR
trendmicro_cas_logs_onedrive OR trendmicro_cas_logs_teams) AND
trendmicro_cloud_app_security.event:(\"virtual_analyzer\" OR \"security_risk_scan\"
OR \"ransomware\" OR \"data_protection\") AND NOT
trendmicro_cloud_app_security.message.risk_level.keyword:(\"No Risk\" OR \"Safe\")
AND NOT trendmicro_cloud_app_security.message.threat_type.keyword:(\"\" OR
\"Unscannable files/URLs\" OR \"Unusual signal\" OR \"Spam/Graymail\")

Adding a Trend Micro Cloud App Security Connector
To add a Trend Micro Cloud App Security connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Trend Micro Cloud App Security Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Trend Micro
Cloud App Security credentials:

Base URL—The base URL for API access. Refer to the Trend Micro documentation for
Understanding the URL Structure .

The full format is <serviceURL>/v1/siem/security_events. For the Base URL value,
you must input the value for <serviceURL>, which identifies the root of the Cloud App
Security service. For example, <serviceURL> in the US is
https://api.tmcas.trendmicro.com.

API Key—To generate an API Key, follow the guidance in the Trend Micro
documentation for Generating an Authentication Token .

Adding the Connector in Stellar Cyber
To add a Trend Micro Cloud App Security connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Cloud Security from the Category dropdown.

5. Choose Trend Micro Cloud App Security from the Type dropdown

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

12. Enter the Base URL you noted above in Obtaining Trend Micro Cloud App Security

Credentials.

13. Enter the API Key you noted above.

14. Choose the Content Type you would like to collect. The logs for Exchange, OneDrive,

Sharepoint Log, and Teams are supported.

15. Choose the Log Event Type you would like to collect. This is the event type for
ingesting logs data. The event types for Data Loss Prevention, Ransomware,
Security Risk, and Virtual Analyzer are supported.

16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Trend Micro Cloud App Security

connector tests that the Base URL and API Key are correct and data requests for the
requested content type returns successful responses.

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

