Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Jamf Protect Connectors

This connector allows Stellar Cyber to ingest logs from Jamf Protect and add the records to the
data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Jamf Protect

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alerts

Index

Syslog

Computers (automatically
collected)

Assets (for Alerts and
Computers)

Locating Records

msg_class:

jamf_alerts

jamf_computers

msg_origin.source:

jamf_protect

msg_origin.vendor:

jamf

msg_origin.category:

Content Type

Index

Locating Records

endpoint

Domain

https://<Hostname>

where <Hostname> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname portion of your Jamf Protect console login

Client ID and password for API client having at least the Read Only role

Adding a Jamf Protect Connector
To add a Jamf Protect  connector:

1. Obtain Jamf Protect API credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Jamf Protect API Credentials
Follow guidance on the Jamf documentation site  to obtain the credentials for your connector.

1. Access the Jamf | PROTECT Console as an administrative user.

2. Navigate to Administrative > API Clients.

3. Click the button to Create API Client.

4. In the page that displays, enter a Name for the API client.

5. Add one or more Roles to configure permissions for the API client (Read Only is

sufficient)

6. Click Save.

7. From the dialog that displays next, copy the API Client Password. Save this value for

later use.

 The password cannot be retrieved or reset after this dialog is closed.  Clicking the
button to Copy to Clipboard also closes the dialog. Be sure to take care when
saving this value.

8. After the password dialog closes, the new API client configuration and endpoint

information displays. Make note of the Client ID and also the hostname portion of the
API URL.

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Jamf Protect connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Jamf Protect from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Hostname using the information you noted above in Obtaining Jamf Protect

API Credentials.

 Do not include https in the Hostname field.

Example: your-organization.protect.jamfcloud.com

13. Enter the Client ID you noted above.

14. Enter the Password for that client.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type. The logs for Alerts are supported.

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

For Alerts and Computers, change the Indices to Syslog.

For Alerts and Computers, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

