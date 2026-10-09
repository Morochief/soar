Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Proofpoint TAP Connectors

This connector allows Stellar Cyber to ingest logs from Proofpoint Targeted Attack Protection (TAP) and add the
records to the data lake. This connector integrates with the SIEM API and the Threat API to provide information from
Proofpoint TAP.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data when the ingestion
volume is large, which potentially can lead to data loss. This can happen when the processing capacity of the
collector is exceeded.

Connector Overview: Proofpoint TAP

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Events

Threats

Index

Syslog

Locating Records

msg_class:

proofpoint_tap_event

proofpoint_tap_threat

msg_origin.source:

proofpoint_tap

msg_origin.vendor:

proofpoint

msg_origin.category:

email

Domain

<Host URL>

where <Host URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Proofpoint Targeted Attack Protection (TAP) to get the raw alerts that are stored in the Syslog
Index. Select the Events content type.

Stellar Cyber maps Proofpoint TAP alerts. The alerts are read from the Syslog Index, enriched with Stellar Cyber fields, and
mapped (with deduplication) to the Alerts Index.

Deduplication is by email.from.address and email.sender.address.

There are the following event types:

Proofpoint TAP messageBlocked

Proofpoint TAP messageDelivered

Proofpoint TAP clickBlocked

Proofpoint TAP clickDelivered

For details, see Integration of Native Third Party Alerts.

Required Credentials and Configurations

Host URL, Service Principal, and Secret

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
proofpoint_tap_event

Adding a Proofpoint TAP Connector
To add a Proofpoint TAP connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

You can also Disable Users.

Obtaining Proofpoint TAP Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Proofpoint TAP credentials:

Service Principal

Secret

Follow guidance on Proofpoint TAP  documentation.

To generate Proofpoint TAP service credentials.

1. Log in as an administrative user to https://threatinsight.proofpoint.com .

2. Navigate to Settings | Connected Applications.

3. Click Create New Credential.

4. Enter a name for the new credential set and click Generate.

5. Copy the Service Principal and the Secret. You need these for the Stellar Cyber connector configuration.

 Make sure to copy these credentials as they will not be available after the following dialog is closed.

Adding the Connector in Stellar Cyber
To add a Proofpoint TAP connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab cannot be changed
after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose Proofpoint Targeted Attack Protection from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this tenant name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information, see Managing Log

Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Host URL, for example, https://tap-api-v2.proofpoint.com .

13. Enter the Service Principal you noted above in Obtaining Proofpoint TAP Credentials.

14. Enter the Secret you noted above.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Events and Threats are supported.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active.

Testing the Connector
When you add (or edit) a connector, we recommend that you run a test to validate the connectivity parameters you
entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60 seconds for new or

modified configuration details to be propagated to the sensor before performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure result. A successful
test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by using the X button. If the
test fails, you can select the   button from the same row to review and correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the connector status, but if

issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP Er

HTTP Standar

ror Code

d Error Name

Explanation

Recommendation

400

Bad Request

This error occurs when there is an error in the connector

Did you configure the connector correctly?

configuration.

401

Unauthorized

This error occurs when an authentication credential is invalid or

Did you enter your credentials correctly?

when a user does not have sufficient privileges to access a

Are your credentials expired?

specific API.

403

Forbidden

This error occurs when the permission or scope is not correct in a

valid credential.

Are your credentials entitled or licensed for that specific

resource?

Did you enter your credentials correctly?

Do you have the required role or permissions for that

credential?

404

429

Not Found

This error occurs when a URL path does not resolve to an entity. Did you enter your API URL correctly?

Too Many

Requests

This error occurs when the API server receives too much traffic or

The server or user license/quota will eventually recover. The

if a user’s license or entitlement quota is exceeded.

connector will periodically retry the query.

If this occurs unexpectedly or too often, work with your API

provider to investigate the server limits, user licensing, or

quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

(Optional) Disabling Users
You can disable an associated Active Directory (AD) user account that is listed in the Recipient Address(es) key
field in a Proofpoint TAP alert.

To configure the disabling an AD user account:

1. Configure the Proofpoint TAP connector as described in this document.

2. Configure the Active Directory connector as described in Configuring Active Directory Connectors. For

Function, select both Collect and Respond.

3. Configure the Disable User action as described in External Actions: Disable User. In the Disable User field,

enter email.recipient.addresses.

The Disable User action will be applied to data that has a value in the Email Recipient Addresses for a
msg_class of proofpoint_tap_event.

You can click the JSON tab to see the email.recipient.addresses.

Or you can navigate to Threat Hunting to see the Email Recipient Addresses. You may have to add the
column to the table.

4. On the AD Server, make sure you have a user with the same email address. In this example, it is

ceo@exec.vogon.science.

 The email.recipient.addresses can be a list. When there are multiple recipients in the list, the AD

response action, Disable User, will be applied to all recipient addresses in the list.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

