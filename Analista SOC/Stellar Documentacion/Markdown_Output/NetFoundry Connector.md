Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring NetFoundry Connectors

This connector allows Stellar Cyber to ingest logs from NetFoundry and add the records to the
data lake. This connector integrates with the NetFoundry API  to query API session events and
audit logs.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: NetFoundry

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

API Session Events

Audit Logs

Index

Syslog

Locating Records

msg_class:

netfoundry_api_ses
sion_event

netfoundry_audit_l
og

msg_origin.source:

netfoundry

msg_origin.vendor:

netfoundry

Content Type

Index

Locating Records

msg_origin.category:

sase

Domain

<Auth URL> and <Base URL>

where <Auth URL> and <Base URL> are variables from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Auth URL, Base URL, Client ID, Password, Network Group ID, and Network ID

Adding a NetFoundry Connector
To add a NetFoundry connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining NetFoundry Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following NetFoundry
credentials that map to the Stellar Cyber fields:

NetFoundry

Definition

Stellar Cyber Fields

NETFOUNDRY_OAUTH_URL

Authentication URL.

BASE_URL

Base URL:

Auth URL

Base URL

https://gateway.production.netfoundry.io/ 

NETFOUNDRY_CLIENT_ID

Unique identifier used to authenticate a

Client ID

NetFoundry client application.

NETFOUNDRY_PASSWORD

Secret key used with the client ID.

Password

NETWORK_GROUP_ID

Collection of networks grouped together for

Network Group ID

administrative purposes.

NETWORK_ID

Unique identifier for a specific network in your

Network ID

NetFoundry account. A network belongs to one

network group and is identified by its unique

network ID within that group.

Get an API Account

To get an API account, follow the guidance in the NetFoundry documentation in the
Authentication section for Get an API Account . The following information is in the
credentials.json file you download:

"clientId": "xxxx",

"password": "xxxxxxxxx",

"authenticationUrl": "https://xxxxxxx/oauth2/token"

Get the Network ID

To get the Network ID:

1. Log in to the NetFoundry web console at console.netfoundry.io  and log in with your

credentials.

2. Navigate to the Networks tab to see a list of all the networks associated with your

account.

3. Locate the Network ID in the list of networks. You should see details like Network

Name, Network ID, and other relevant information. The Network ID is usually displayed
alongside the network's name or in the network details page.

Get the Network Group ID

To get the Network Group ID:

1. Log in to the NetFoundry web console at console.netfoundry.io  and log in with your

credentials.

2. Navigate to Network Groups in the dashboard under the Networks tab, depending on

your account permissions and console version.

3. Locate the Network Group ID in the list of network groups. The Network Group ID is

often displayed alongside each group's name or within its detailed view.

Adding the Connector in Stellar Cyber
To add a NetFoundry connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SASE from the Category dropdown.

5. Choose NetFoundry from the Type dropdown.

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

12. Enter the Auth URL you noted above in Obtaining NetFoundry Credentials.

13. Enter the Base URL you noted above.

14. Enter the Client ID you noted above.

15. Enter the Password you noted above.

16. Enter the Network Group ID you noted above.

17. Enter the Network ID you noted above.

18. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

19. Choose the Interval (min). This is how often the logs are collected.

20. Choose the Content Type you would like to collect. The logs for API Session Events

and Audit Logs are supported.

21. Click Next. The final confirmation tab appears.

22. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the NetFoundry connector tests that
the Auth URL, Client ID, and Password are correct and an access token can be created. The
data requests for the requested content types return successful responses, which verifies
that the granted access token has the correct permissions and the provided Network Group
ID is valid.

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

