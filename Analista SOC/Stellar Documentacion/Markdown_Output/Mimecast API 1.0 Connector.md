Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Mimecast API 1.0 Connectors

This connector allows Stellar Cyber to ingest Mimecast logs and add the records to the data
lake.

Mimecast integration with Stellar Cyber provides advanced threat detection and response
capabilities, combining Mimecast's email security solutions with real-time threat intelligence and
automated response workflows to improve incident response and threat mitigation.

There can be any number of Mimecast connectors active.

 This connector uses Mimecast API 1.0.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Mimecast API 1.0

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: 5 minutes

Collected Data

Content Type

Index

Locating Records

MTA Log

Syslog

msg_class:

mimecast_email

mimecast_email_attachme
nt_protect_log

mimecast_email_av_log

Content Type

Index

Locating Records

mimecast_email_imperson
ation_protect_log

mimecast_email_internal
_email_protect_log

mimecast_email_url_prot
ect_log

msg_origin.source:

mimecast_email

msg_origin.vendor

mimecast

msg_origin.category:

email

Domain

https://api.mimecast.com/api/login/discover-authentication

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Mimecast (API version 1.0) to get the raw alerts that are stored in the
Syslog index. Select the MTA Log content type.

Stellar Cyber maps Mimecast alerts. The alerts are read from the Syslog index, enriched with Stellar
Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by the following fields:

Attachment Protect and AV/AntiVirus—tenantid, srcip, file.hash.md5,
email.sender.address, and email.recipient.addresses

Impersonation Protect, Internal Email , and Malicious Receipt Log—tenantid and
mimecast.aCode

URL Protect—tenantid, srcip, url, email.sender.address, and
email.recipient.addresses

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

App ID, App Key, Access Key, Secret Key, and Administrator Email

Locating Records

To search the alerts in the Alerts index, use the query msg_class: mimecast_*

To search the Original Records in the Syslog index, use the msg_class and alert key fields (refer to Key
Fields for Third Party Native Alert Types):

Attachment Protect logs: msg_class.keyword: mimecast_email_attachment_protect_log

AV logs: msg_class.keyword: mimecast_email_av_log

Impersonation Protect logs: msg_class.keyword: mimecast_impersonation_protect_log

Internal Email Protect logs: msg_class.keyword:
mimecast_email_internal_email_protect_log

Receipt logs: _exists_: mimecast.Virus AND _exists_: mimecast.aCode AND
msg_class.keyword: mimecast_email

URL Protect logs: msg_class.keyword: mimecast_email_url_protect_log

Other logs: msg_class.keyword: mimecast_email

Adding a Mimecast Connector
To add a Mimecast connector:

1. Configure Mimecast logs
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Configuring Mimecast Logs
You must configure Mimecast logs before you add the connector in Stellar Cyber.

To configure Mimecast logs:

1. Log in to Mimecast.
2. Follow the Mimecast online instructions to Enable logging for your account .
3. Refer to the following site (https://community.mimecast.com/s/article/Managing-API-
Applications-505230018 ) for guidance preparing for use of the Mimecast API and
gathering the info below:
App ID
App Key
Access Key
Secret Key



Refer to the following recommendations:

Generate the Access Key and Secret Key before adding the user to any Basic
Administrator role.

If the Access Key and Secret Key need to be generated, first remove the user from
any Basic Administrator role and add the user back after obtaining the new keys.

Adding the Connector in Stellar Cyber
To add a Mimecast connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose Mimecast API 1.0 from the Type dropdown.

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

12. Enter the App ID you noted above in Configuring Mimecast Logs.

13. Enter the App Key you noted above.

14. Enter the Access Key you noted above.

15. Enter the Secret Key you noted above.

16. Enter the Administrator Email.

17. Choose the Content Type you would like to collect. The logs for MTA Log are

supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active.

 A new Mimecast connector automatically collects logs for the last 7 days. It can take a few

days for the logs to be current.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

