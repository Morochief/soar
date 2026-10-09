Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Trellix MVISION Connectors

This connector allows Stellar Cyber to ingest logs from Trellix MVISION and add the records to
the data lake. It integrates with the Trellix MVISION EDR API to query for Insight events and
devices.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Trellix MVISION

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

Alerts

Devices

Insight Events

Threats

Syslog

Assets (for
Devices)

msg_class:

trellix_mvision_ed

r_alerts

trellix_mvision_in
sight_devices

trellix_mvision_in
sight_events

trellix_mvision_ed

r_threats

Content Type

Index

Locating Records

msg_origin.source:

trellix_mvision

msg_origin.vendor:

trellix_mvision

msg_origin.category:

endpoint

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Trellix MVISION to get the raw alerts that are stored in the Syslog index.
Select the Alerts content type.

Stellar Cyber maps Trellix MVISION alerts. The alerts are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and trellix_mvision.id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

API Key, Client ID, Client Secret, and Scopes

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query:

msg_class: trellix_mvision_edr_alerts AND _exists_: event.threat.name

Adding a Trellix MVISION Connector
To add a Trellix MVISION connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Trellix MVISION Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Trellix
MVISION credentials:

API Key

Client ID

Client Secret

The client credentials are available in your Trellix on-boarding email, or see Generating
Credentials.

Generating Credentials

To generate credentials for the APIs needed for the Trellix MVISION connector:

1. Logon to the Trellix Developer  portal.

2. Navigate to Self Service > API Access Information and click Configure.

3. In API Access Information, select the following APIs and Method Types:

a. For Devices, select GET.

b. For Events, select GET.

c. For Insights Events, select GET.

d. For EDR Threats, select GET.

4. Select Client Credentials.

5. Click Add.

6. Select the Scopes (permissions) for the APIs.

7. Click Create.

8. Your Client ID and Secret are generated.

 Copy the Client ID and Secret and store them in a safe location. Also copy the
Trellix API Key. These credentials are used in the configuration of the Trellix
MVISION connector.

Adding the Connector in Stellar Cyber

To add a Trellix MVISION connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Trellix MVISION Endpoint Security from the Type dropdown.

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

12. Enter the API Key you noted above in Obtaining Trellix MVISION Credentials.

13. Enter the Client ID you noted above.

14. Enter the Client Secret you noted above.

15. Enter the Scopes, which determine the APIs you are authorized to access. It is a list of

permissions for your application. The following is the default scope: epo.device.r
mi.user.investigate soc.hts.r soc.rts.r soc.act.tg mi.user.config ins.user ins.suser
ins.ms.r

16. Choose the Interval (min). This is how often the logs are collected.

 Trellix MVISION is a rate limited API. An interval of at least 30 minutes is

recommended to avoid rate limiting.

17. Choose the Content Type you would like to collect. The logs for Devices, Alerts,

Insight Events, and Threats are supported.

  The Devices content type is always selected and cannot be removed from the

configuration as it is required for host information.

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

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Insight Events and Devices, change the Indices to Syslog.

For Devices only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

