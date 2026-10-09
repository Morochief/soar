Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cloudflare Connectors

This connector allows you to use the Cloudlfare Logpull API to ingest retained log files to the Stellar Cyber data lake.

Cloudflare connectors use the Logpull API. Logpull is only available to Cloudflare customers on the Enterprise
plan.  Make sure that you have the following:

a Cloudflare account on an Enterprise plan

an Enterprise subscription for the zone

 For the available permissions for tokens and roles as they relate to logs, refer to Get started > Permissions .

 This connector is improved to use less memory. Under certain scenarios if there is an error reaching the third-

party API, some duplicate messages may be sent.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data when the ingestion
volume is large, which potentially can lead to data loss. This can happen when the processing capacity of the
collector is exceeded.

Connector Overview: Cloudflare

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Logs (not configurable in the user interface)

Index

Syslog

Locating Records

msg_class:

cloudflare_logpull_logs

msg_origin.source:

cloudflare_logpull

msg_origin.vendor:

cloudflare

msg_origin.category:

websec

waf

Domain

https://api.cloudflare.com

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Zone ID and API Token

Adding a Cloudflare Connector
To add a Cloudflare connector:

1. Obtain the required credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining the Required Credentials
To configure this connector in Stellar Cyber, you will need the following information from your Cloudflare deployment:

Zone ID: Specify the Zone ID, Cloudflare's unique identifier for each domain in your account. You will be
using this ID to configure the connector.

API Token: You will need to create an API token for use by the Stellar Cyber connector.

Field list: Review whether you want to collect the Default fields according to how the defaults are set in
your Cloudflare deployment, or whether you want All fields that are applicable to the dataset you have
associated with that Zone. (Refer to the Cloudflare documentation for a description of the log fields available
per dataset.) 

 Note that the applicable logs are not retained by default. To support the retrieval of logs with the Logpull API, you
must enable log retention . If enabling log retention does not work according to Cloudflare's documentation, you
may need to modify the API call using the curl command below.

1. Log into the Cloudflare dashboard  using a user with the Administrator Read only role.

2. Select the account and the domain  for which you want to collect data. This step ensures you save the

correct Zone ID.

3. From the Overview page, locate the section titled API and the field for Zone ID, then click the link Click to

copy. For example:

4. Paste that value in a file to use when you configure the connector below.

5. Click the link for Get your API Token.

6. Follow Cloudflare's guidance to Create an API token . You can create an API from a template or you can

create a custom token.

Specify the following permissions: Zone, desired dataset , Edit. (See note below about Edit versus Read
permissions).

For example, below is a custom token, with the permissions for Zone, Logs, and Edit specified:



The Edit permission is needed for the API token so that this connector can turn on log retention. If you
can turn on log retention, only Read permission is needed for the API token.

Use the following command to turn on log retention:

curl -i -H "Authorization: Bearer <API TOKEN>" POST
"https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/logs/control/retention
/flag" -d '{"flag":true}'

where <API TOKEN> and <ZONE ID> are your API token and Zone ID.

7. Save the API token in the same file in which you saved the Zone ID, then proceed to the next section.

Adding the Connector in Stellar Cyber

With the Zone ID and API token handy, you can add the Cloudflare connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab cannot be changed
after you add the connector.

4. Choose Web Security from the Category dropdown.

5. Choose Cloudflare from the Type dropdown.

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

12. Enter the Zone ID you noted above in Obtaining the Required Credentials.

13. Enter the API Token you noted above.

14. Choose the Interval (min). This is how often the logs are collected.

15. Select the Log Fields you want to collect:

All Fields: all fields applicable to the dataset associated with the Zone

Default Fields: default fields set in your Cloudflare deployment

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active.

Testing the Connector
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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

