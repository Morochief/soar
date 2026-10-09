Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Prisma Cloud Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Prisma Cloud

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alert

Audit

Index

Linux

Syslog

Locating Records

msg_class:

paloalto_prisma

msg_origin.source:

paloalto_prisma

msg_origin.vendor:

N/A

msg_origin.category:

cloudsec

Domain

<Prisma Cloud API URL>

where <Prisma Cloud API URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Palo Alto Networks Prisma Cloud to get the raw alerts that are stored in
the Syslog index. Select the Alert content type.

Stellar Cyber maps Palo Alto Networks Prisma Cloud alerts. The alerts are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid, .palo_alto_networks_prisma_cloud.type,
palo_alto_networks_prisma_cloud.audit_id, palo_alto_networks_prisma_cloud.incident_id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Prisma Cloud API URL, Username, and Password

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_origin.source:palo_alto_networks_prisma_cloud AND
palo_alto_networks_prisma_cloud.effect:alert AND
palo_alto_networks_prisma_cloud.type:(incident OR admission_audit OR
container_runtime_audit OR host_runtime_audit)

Adding a Prisma Cloud Connector
To add a Palo Alto Networks Prisma Cloud connector:

1. Add the connector in Stellar Cyber
2. Test the connector
3. Verify ingestion

Adding the Connector in Stellar Cyber
To add a Palo Alto Networks Prisma Cloud connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Cloud Security from the Category dropdown.

5. Choose Prisma Cloud from the Type dropdown.

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

12. Enter the Prisma Cloud API URL.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Enter the Username of a user with API permissions.

14. Enter the Password for that user.

 The password should not include non-ASCII special characters.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Alert and Audit are

supported.

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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

