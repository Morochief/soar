Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Huntress Connectors

This connector allows Stellar Cyber to ingest logs from Huntress and add the records to the data
lake. This connector integrates with the Huntress API to query for agents and incident reports.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Huntress

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

Agents

Incident Reports

Syslog

Assets (for
Agents)

msg_class:

huntress_agent

huntress_incident_
report

msg_origin.source:

huntress

msg_origin.vendor:

huntress

msg_origin.category:

Content Type

Index

Locating Records

endpoint (Agents)

mdr (Incident Reports)

Domain

<Host URL>

where <Host URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Huntress to get the raw alerts that are stored in the Syslog index. Select
the Incident Reports content type.

Stellar Cyber maps Huntress incidents. The incidents are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid, huntress_id, huntress.organization_id, and huntress.account_id.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Host URL, API Key, API Secret Key, and Organization ID

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_class: huntress_incident_report.

Adding a Huntress Connector
To add a Huntress connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Huntress Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Huntress
credentials:

Host URL—hostname of the Huntress server. The default is: https://api.huntress.io/v1.

API Key—API key associated with a user account, generated from Huntress, and used
to authenticate with Huntress

API Secret Key—API secret key associated with a user account, displayed when the
API key is created, and used to authenticate with Huntress

Organization ID—identifier of the organization

To generate an API key, refer to the Huntress documentation :

1. Log in as an administrative user to <your_account_subdomain>.huntress.io>.

2. Navigate to API Credentials.

3. Click the green Generate button.

4. Click Confirm, which generates a public and private key pair. This is your API key and

API secret key.

 Store the API key and API secret key in a safe location. It cannot be retrieved later

although it can be regenerated.

Locating the Organization ID

To locate the organization ID:

1. Navigate to Organizations.

2. Select the organization's name. The organization ID is located in the URL.

Adding the Connector in Stellar Cyber
To add a Huntress connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Huntress from the Type dropdown.

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

12. Enter the Host URL you noted above in Configuring Huntress Credentials.

13. Enter the API Key you noted above.

14. Enter the API Secret Key you noted above.

15. Enter the Organization ID you noted above.

16. Choose the Interval (min). This is how often the logs are collected.

 The logs for Agents are queried every 24 hours.

17. Choose the Content Type you would like to collect. The logs for Agents and Incident

Reports are supported.

  The Agents content type is always selected and cannot be removed from the

configuration as it is required for host information.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active.

Partial and Complete Parsing

Parsing methods are as follows:

Partial parsing—only essential header information is parsed, including the incident
report URL, host URL, organization, and security product

Complete parsing—in addition to the above, all processes, files, users, and threat
information contained in the body field are parsed

The information in this section relates to the data enrichment done by the connector where the
string under the body field is used to populate fields required for Machine Learning (ML)
purposes. But if the size of the body is too large, complete parsing may not be done.

The following threshold levels, T1 and T2, manage data flow and system performance as follows:

Threshold T1 (500KB)— set to prevent sending large data files through the Stellar
Cyber data platform

Threshold T2 (5MB)—aims to avoid performance and memory issues

The handling of data sizes in relation to these thresholds is as follows:

For data size S < T1—the body field is retained and complete data parsing is
performed

For T1 ≤ S < T2—data is fully parsed, but the body field is dropped to reduce size

For S ≥ T2—only partial parsing is conducted and the body field is dropped

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

For Agents and Incident Reports, change the Indices to Syslog.

For Agents only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

