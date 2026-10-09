Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring 1Password Connectors

This connector allows Stellar Cyber to ingest logs from 1Password and add the records to the
data lake. This connector integrates with the 1Password API to query endpoints.

The Events API allows 1Password Business customers to send account activity to another tool,
such as a SIEM tool.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: 1Password

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Audit Events

Item Usage Events

Sign-in Attempts

Index

Syslog

Locating Records

msg_class:

onepassword_audit

onepassword_itemus
age

onepassword_signin
attempt

msg_origin.source:

onepassword

Content Type

Index

Locating Records

msg_origin.vendor:

onepassword

msg_origin.category:

pw_mgmt

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL and API Token

Adding an 1Password Connector
To add an 1Password connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining 1Password Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following 1Password
credentials:

Base URL—The base URL for API access.

API Token—The authentication credential.

The Base URL is determined by the server that hosts your 1Password account.

If your account is on:

Your Base URL is:

http://1Password.com 

https://events.1password.com (for 1Password Business)

https://events.ent.1password.com (for 1Password Enterprise)

http://1Password.ca 

https://events.1password.ca

http://1Password.eu 

https://events.1password.eu

Getting an API Token

To obtain the API token, follow the guidance in the 1Password documentation:
https://support.1password.com/events-reporting/. 

1. Login as an administrative user to your 1Password account.

2. Select Integrations and under Events Reporting, select Stellar Cyber.

3. On the Events Reporting page, enter a System Name.

4. Click Add Integration.

5. To set up a token, enter a Token Name, select an Expires After option, and select the

Events to Report, which are the event types to which the token has access.

6. Click Issue Token.

7. To save your token, use the Copy icon to copy it.

 Store the token in a safe location. It cannot be viewed later.

8. To save the token in 1Password, click Save in 1Password and select the vault to which

to save your token.

Adding the Connector in Stellar Cyber

To add an 1Password connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Password Management from the Category dropdown.

5. Choose 1Password from the Type dropdown.

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

12. Enter the Base URL you noted above in Obtaining 1Password Credentials.

 Do not include the https prefix or a trailing "/" symbol.

13. Enter the API Token you noted above.

14. Choose the Interval (min). This is how often the logs are collected.

15. Choose the Content Type you would like to collect. The logs for Audit Events, Item

Usage Events, and Sign-in Attempts are supported.

16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

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

For the Audit Events, Item Usage Events, and Sign-in Attempts content
types, change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

