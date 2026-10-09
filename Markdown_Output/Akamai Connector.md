Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Akamai Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Akamai

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

Admin Events Reports

Syslog

msg_class:

Audit Logs Reports

Connectors

Users

Assets (for
Connectors)

akamai_eaa_admin_ev
ents_reports

akamai_eaa_audit_lo
gs_reports

akamai_eaa_connecto
rs

akamai_eaa_users

msg_origin.source:

akamai_eaa

msg_origin.vendor:

Content Type

Index

Locating Records

akamai

msg_origin.category:

endpoint

Domain

https://<Hostname>

where <Hostname> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname, Access Token, Client Token, Client Secret, and Contract ID

Adding an Akamai Connector
To add an Akamai connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Akamai Credentials
To create the Akamai API credentials:

 Use our example as a guideline, as you might be using a different software version.

1. Log in to your Akamai Control Center account (https://control.akamai.com).

2. Navigate to Identity & Access > New API Client for Me.

3. Select which roles, contracts, and groups you are using with the Stellar Cyber API

client. You will need to note the Contract ID for use with the connector.

4. Select HTTPie for the tool you will use for the API requests.

5. Select the permissions as read-only.

6. Click Submit.

7. When displayed, copy the base URL.

8. Click on the New Credential button and copy or download your Access Token, Client

Token, and Client Secret.

9. Save all of the above information before proceeding to the next section.

Adding the Connector in Stellar Cyber
After completing the previous section, with the required credentials noted, you can add the
Akamai connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Akamai from the Type dropdown.

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

12. Enter the Hostname.

 Do not include https in the hostname.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Enter the Access Token you noted above in Obtaining Akamai Credentials.

14. Enter the Client Token you noted above.

15. Enter the Client Secret you noted above.

16. Enter the Contract ID you noted above.

17. Choose the Interval (min). This is how often the logs are collected.

18. Choose the Content Type you would like to collect. The supported content types are:

Admin Events Reports

Audit Logs Reports

Connectors

Users

19. Click Next. The final confirmation tab appears.

20. Click Submit.

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

For all content types, change the Indices to Syslog.

For Connectors only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

