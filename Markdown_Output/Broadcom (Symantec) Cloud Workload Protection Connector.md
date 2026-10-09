Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Broadcom (Symantec) Cloud
Workload Protection Connectors

The Broadcom (Symantec) Cloud Workload Protection connector allows you to ingest event and
alert logs to the Stellar Cyber data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Broadcom (Symantec) Cloud
Workload Protection

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

Alert

Event-CWP

Event-CWP-S

Event-CWP-SPE

Syslog

msg_class:

symantec_cloud_work
load_alert

symantec_cloud_work
load_event_cwp

symantec_cloud_work
load_event_cwp_s

symantec_cloud_work
load_event_cwp_spe

Content Type

Index

Locating Records

msg_origin.source:

symantec_cloud_work
load_protection

msg_origin.vendor:

symantec

msg_origin.category:

cloudsec

Domain

https://scwp.securitycloud.symantec.com

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Customer ID, Domain ID, Client ID, and Client Secret

Adding a Broadcom (Symantec) Cloud Workload
Protection Connector
To add the Broadcom (Symantec) Cloud Workload Protection connector:

1. Obtain the required credentials
2. Add the connector in Stellar Cyber
3. Test the connector

Obtaining the Required Credentials
To configure this connector in Stellar Cyber, you will need the following information from your
Broadcom (Symantec) Cloud Workload Protection deployment:

Customer ID

Domain ID

Client ID

Client Secret

Adding the Connector in Stellar Cyber
With the configuration information handy, you can add the Broadcom (Symantec) Cloud
Workload Protection connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Cloud Security from the Category dropdown.

5. Choose Symantec Cloud Workload Protection from the Type dropdown.

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

9. Choose the device on which to run the connector .

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Customer ID you noted above in Obtaining the Required Credentials.

13. Enter the Domain ID you noted above.

14. Enter the Client ID you noted above.

15. Enter the Client Secret you noted above.

16. Choose the Interval (min). This is how often the logs are collected.

17. Select the Content Type you want to collect:

Alert

Event CWP

Event CWP-S

Event CWP-SPE

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

1. Select Threat Hunting. The Interflow Search tab appears.

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

