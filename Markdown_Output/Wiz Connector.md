Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Wiz Connectors

This connector allows Stellar Cyber to ingest logs from Wiz and add the records to the data lake.
It integrates with the Wiz API to ingest Issues and Vulnerabilities data types.

Wiz is a cloud security platform that helps organizations make their cloud environments secure
and more streamlined. They create a normalizing layer across different cloud environments, so
companies can spot and remove high-priority risks faster.

The Wiz API has a rate limit that is based per service account on tenant level. The rate limit is 10
calls per second for a service account query. Depending on the amount of data, the connector
may fail to pull data and receive a 429 response.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Wiz

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

Issues

Vulnerabilities

Syslog (for
Issues)

Scans (for
Vulnerabilities)

msg_class:

wiz_issues

wiz_vulnerabilitie
s

Content Type

Index

Locating Records

msg_origin.source:

wiz

msg_origin.vendor:

wiz

msg_origin.category:

cloudsec

Domain

<Auth URL> and <Base URL>

where <Auth URL> and <Base URL> are variables from the configuration of this

connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Wiz to get the raw alerts that are stored in the Syslog index. Select the
Issues content type.

Stellar Cyber maps Wiz events. The events are read from the Syslog index, enriched with Stellar Cyber
fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and wiz.id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Auth URL, Base URL, Client ID, and Client Secret
or

Auth URL (Custom URL), Custom Auth URL, Credential Audience, Base URL (Custom URL),
Custom Base URL, Client ID, and Client Secret

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class:\"wiz_issues\"

Adding a Wiz Connector
To add a Wiz connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Wiz Credentials

Before you configure the connector in Stellar Cyber, you must obtain the following Wiz
credentials:

Auth URL—The authentication URL. There are three URLs, based on tenant. The
values are:

https://auth.app.wiz.io for Wiz Commercial (default)

https://auth.app.wiz.us for Wiz for Gov

https://auth.gov.wiz.io for Wiz Commercial on GovCloud

Custom URL

Base URL—The base URL for API access. The base URL depends on the region.
There are four regions (us1, us2, eu1, and eu2). The values are:

https://api.us1.app.wiz.io (default)

https://api.us2.app.wiz.us

https://api.eu1.app.wiz.io

https://api.eu2.app.wiz.io

Custom URL

Client ID and Client Secret—The authentication credentials.

or

Auth URL—The same values as above. Select Custom URL to display Custom Auth
URL and Credential Audience fields.

Custom Auth URL—The default is: https://auth.app.wiz.io

Credential Audience—The credential audience may have a different value based on the
tenant URL used in authentication. When Auth URL is custom, then the Credential
Audience value is unknown, so it needs to be input by the user. The default is: wiz-api

Base URL—The same values as above. Select Custom URL to display Custom Base
URL field.

Custom Base URL—The default is https://api.us1.app.wiz.io

Client ID and Client Secret—The authentication credentials.

Adding a Service Account

Add a service account for authenticating with the Wiz API. You will need to specify the
permissions (API scopes).

Follow the guidance in your Wiz API documentation.

1. Log in as a Wiz administrative user with Write permission for Service Accounts.

2. Select Settings > Access Management > Service Accounts.

3. Click Add Service Account.

4. Enter a Name, an optional Description, and select a Type. For Type, choose Custom

Integration (GraphQL API).

5. Select the API Scopes to grant to this new service account.

For example, under Resources, select Read graph resource.

For example, under Issues, select Read an issue, list issues.

For example, under Vulnerabilities, select Read vulnerabilities.

6. Click Add Service Account.

7. The Client ID and Client Secret are displayed for the new service account. They will be

needed when configuring the connector in Stellar Cyber.

 Copy the Client ID and Client Secret and store them in a safe location.

Adding the Connector in Stellar Cyber
To add a Wiz connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Cloud Security from the Category dropdown.

5. Choose Wiz from the Type dropdown.

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

12. If you select an Auth URL from the dropdown menu:

a. Select the Auth URL you noted above in Obtaining Wiz Credentials.

b. Select the Base URL you noted above, then skip the next step.

13. If you select Custom URL from the dropdown menu in the Auth URL field:

a. Enter the Custom Auth URL or keep the default.

b. Enter the Credential Audience or keep the default.

c. For Base URL, select Custom URL.

d. Enter the Custom Base URL or keep the default.

14. Enter the Client ID you noted above.

15. Enter the Client Secret you noted above.

16. Choose the Content Type you would like to collect. The logs for Issues and

Vulnerabilities are supported.

17. Choose the Interval (min). This is how often the logs are collected.

18. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Wiz connector tests that the
Auth URL, Base URL, Client ID, and Client Secret are correct and data requests for the
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

2. Change the Indices for the type of content you collected:

For Issues, change the Indices to Syslog.

For Vulnerabilities, change the Indices to Scans.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

