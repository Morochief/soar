Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring SonicWall Capture Client
Connectors

A SonicWall Capture Client connector allows you to disconnect host, initiate scan, restart
machine, or shut down using Stellar Cyber (as long as those hosts are managed by SonicWall
Capture Client), and ingest SonicWall Capture Client logs, discover assets, and see
vulnerabilities.

There can be any number of SonicWall Capture Client connectors active.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: SonicWall Capture Client

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

ATP

Host

Log

Threat

Vulnerabilities

Index

Syslog

Scans

Assets (for Host)

Linux

Locating Records

msg_class:

sonicwallcc_
<content type>

msg_class
example:

sonicwallcc
_atp

Content Type

Index

Locating Records

msg_origin.sou
rce:

sonicwallcc

msg_origin.ven
dor:

N/A

msg_origin.cate
gory:

endpoint

Domain

<Host URL>

where <Host URL> is a variable from the configuration of this connector

Response Actions

Action

Initiate Scan

Disconnect Host

Restart Machine

Shut Down Host

Required Fields

device.deviceId and device.InstallToken

device.deviceId and device.InstallToken

device.deviceId and device.InstallToken

device.deviceId and device.InstallToken

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Host URL, Email, Password, and Sonicwall Tenant ID

Adding a SonicWall Capture Client Connector
To add a SonicWall Capture Client connector:

1. Configure SonicWall log management
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Configuring SonicWall Log Management
You must configure SonicWall log management before you add the connector in Stellar Cyber.
You must also have the Tenant ID for an administrative user. MySonicWall credentials are not
supported with the APIs.

To get the Tenant ID:

1. Log in to the SonicWall Capture Client console (https://captureclient.sonicwall.com) as

an administrative user.

2. Navigate to Management | TENANT SETTINGS.

3. Copy the Tenant ID.

Adding the Connector in Stellar Cyber
To add a SonicWall Capture Client connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose SonicWall Capture Client from the Type dropdown.

The asterisk (*) indicates a required field.

6. Choose the Function: Collect to collect logs; Respond to enable endpoint actions.

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

12. Enter the Host URL.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Enter the Email.

14. Enter the Password.

 The password should not include non-ASCII special characters.

15. Enter the Sonicwall Tenant ID you noted above, if you chose Collect.

16. Enter the Interval (min) if you chose Collect. This is how often the logs are collected.

17. Choose the Content Type you would like to collect, if you chose Collect. The logs for

ATP, Host, Log, Threat, and Vulnerabilities are supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

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

2. Change the Indices to Syslog if you chose the Log or Threat content type.

The table immediately updates to show ingested Interflow records.

3. Change the Indices to Assets if you chose the Host content type.

The table immediately updates to show ingested Interflow records. Also, hosts
discovered through this connector show SonicWall Capture Client as a data source.

4. Change the Indices to Linux Events if you chose the Vulnerabilities content type.

The table immediately updates to show ingested Interflow records.

5. Change the Indices to Scans if you chose the ATP content type.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

