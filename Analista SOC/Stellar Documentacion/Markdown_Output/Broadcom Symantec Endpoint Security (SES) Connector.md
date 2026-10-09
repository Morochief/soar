Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Broadcom Symantec Endpoint
Security (SES) Connectors

This connector allows Stellar Cyber to ingest logs from Broadcom SES and add the records to
the data lake.

This connector requires the Broadcom Symantec Endpoint Security Enterprise subscription,
except for Incidents, which requires the Broadcom Symantec Endpoint Security Complete
subscription.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Broadcom SES

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Devices

Events

Incidents

Index

Syslog

Locating Records

msg_class:

Assets (for Devices)

broadcom_devices

broadcom_events

broadcom_ses_inc
idents

Content Type

Index

Locating Records

msg_origin.source:

broadcom_ses

msg_origin.vendor:

broadcom

msg_origin.category:

endpoint

Domain

https://<Hostname>

where <Hostname> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Broadcom Symantec Endpoint Security (SES) to get the raw alerts that
are stored in the Syslog index. Select the Incidents content type.

Stellar Cyber maps Broadcom SES incidents. The incidents are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and broadcom.incident_uid.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

OAuth credentials

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class: broadcom_ses_incidents AND _exists_: event.threat.name

Adding a Broadcom SES Connector
To add a Broadcom SES connector:

1. Obtain Broadcom SES credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Broadcom SES Credentials
Follow guidance on Broadcom documentation pages  to generate a bearer token used for
Stellar Cyber API calls and set minimum privileges.

1. Login to your Symantec Endpoint Security console.

2. Navigate to Integration > Client Applications.

3. Select Add Client Application.

4. Enter a Name for the application, then click the Add button.

5. Within the client application details screen that displays, ensure the following minimum

privileges are enabled.

Devices: View

Alerts & Events: View

Investigation (Incident and Incident Rules): View

Policies: View

6. Click Save.

7. Click the ellipsis and then select Client Secret.

8. Click the copy icon for the OAuth Credentials value for the Stellar Cyber connector to

generate a bearer token.

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Broadcom SES connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Broadcom Symantec Endpoint Security from the Type dropdown.

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

12. Enter the Hostname for example: api.sep.securitycloud.symantec.com.

 Do not include the https prefix or a trailing "/" symbol.

13. In the OAuth Credentials field, enter the value you copied in Obtaining

Broadcom SES Credentials.

14. Enter the Interval (min). This is how often the logs for Events and Incidents are

collected.

 The interval for Devices is always 24 hours.

15. Choose the Content Type. The logs for Devices, Events, and Incidents are

supported.

  The Devices content type is always selected and cannot be removed from the

configuration as it is required for host information.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

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

Connection Test Failure

For this Broadcom SES connector, the credential and connection test may not work for all
content types. But even it it fails for one content type, it will still get the logs for the other content
types.

For example, if the connection test fails for the Incident content type, the following message
displays with the Show More button:

Fail to collect Broadcom SES logs for content type of incidents: <error
message>
Please make sure the token has complete subscription.

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Devices, Events, and Incidents, change the Indices to Syslog.

For Devices only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

