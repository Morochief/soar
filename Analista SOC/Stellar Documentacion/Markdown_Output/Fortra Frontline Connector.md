Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Fortra Frontline Connectors

This connector allows Stellar Cyber to ingest logs from Fortra Frontline Vulnerability Manager
(VM) and add the records to the data lake. It integrates with the Fortra Frontline VM Quick
Connect API  to query for hosts and vulnerabilities.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Fortra Frontline

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Hosts

Vulnerabilities

Syslog (for
Hosts)

Scans (for
Vulnerabilities)

Assets (for
Hosts)

msg_class:

fortra_frontline_h
osts

fortra_frontline_v
ulnerabilities

msg_origin.source:

fortra_frontline

msg_origin.vendor:

fortra

Content Type

Index

Locating Records

msg_origin.category:

security_scan

Domain

<Router URL>

where <Router URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Router URL and API Token

Adding a Fortra Frontline Connector
To add a Fortra Frontline connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Fortra Frontline Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Fortra
Frontline credentials:

Router URL—regional URL with which your API key is associated, for example,
https://api/frontline.cloud/api/router/

API Token—Fortra VM API key used to authenticate your account. The key is valid only
with the specific Fortra VM region of the account.

To generate a Fortra VM API key, follow the guidance in the Fortra VM documentation :

1. Log in to Fortra VM .

2. In the site header, select your name and then select My profile.

3. On the API Tokens tab, select Create new token.

4. In the Add New Token dialog, enter the token name and then select OK.

5. Below your token name, select Click to show key to display your API Key.

 Store the API Key in a safe location. It cannot be retrieved later although you can

create a new one.

Adding the Connector in Stellar Cyber
To add a Fortra Frontline connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose Fortra Frontline from the Type dropdown

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

12. Enter the Router URL, for example, https://api/frontline.cloud/api/router/.

13. Enter the API Token you noted above in Obtaining Fortra Frontline Credentials.

14. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

15. Choose the Interval (min). This is how often this connector retrieves data from Fortra

Frontline. The default is 15 minutes.

16. Choose the Content Type you would like to collect. The logs for Hosts and

Vulnerabilities are supported.

 The Hosts content type is always selected and cannot be removed from the

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

2. Change the Indices for the type of content you collected:

For Hosts only, change the Indices to Syslog.

For Vulnerabilities only, change the Indices to Scans.

For Hosts only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

