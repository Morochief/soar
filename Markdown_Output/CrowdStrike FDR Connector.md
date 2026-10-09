Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring CrowdStrike FDR Connectors

This connector allows Stellar Cyber to ingest logs from CrowdStrike Falcon Data Replicator
(FDR) and add the records to the data lake. This connector supports ingestion of secondary
events as attachments. It requires the Falcon Insight XDR license.

CrowdStrike FDR uses S3 buckets and Simple Queue Service (SQS) queues for data streaming.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: CrowdStrike FDR

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Aid Master

App Info

Managed Assets

Not Managed Assets

User Info

Index

Syslog

Locating Records

msg_class:

crowdstrike_fdr_ai
dmaster

crowdstrike_fdr_ap
pinfo

crowdstrike_fdr_ma
nagedassets

crowdstrike_fdr_no
tmanagedassets

Content Type

Index

Locating Records

crowdstrike_fdr_us
erinfo

msg_origin.source:

crowdstrike_fdr

msg_origin.vendor:

crowdstrike

msg_origin.category:

endpoint

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Access Key, Secret Key, and SQS Queue URL, plus Region

Adding a CrowdStrike FDR Connector
To add a CrowdStrike FDR connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining CrowdStrike FDR Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following CrowdStrike
FDR credentials. Follow the guidance in the CrowdStrike FDR documentation, for example,
Falcon Data Replicator (FDR) schema API.

Access Key—The unique identifier for an API client, used for authentication and also
known as a client ID.

Secret Key—The secret key used for authentication and also known as a client secret.

SQS Queue URL—The unique identifier for an Amazon Simple Queue Service (SQS)
queue. The URL is a specific address that points to the SQS queue.

The API client credentials must have the following scope enabled:

Create the client ID and client secret from the CrowdStrike platform:

1. Log in to CrowdStrike Falcon at https://falcon.crowdstrike.com/ .

2. Click Support and resources.

3. Click Resources and tools.

4. Click API Clients and Keys.

5. Click Add new API client.

6. Enter the Client Name.

7. Select API Scopes, including Falcon Data Replicator: Read.

8. Click Add.

9. Copy the Client ID and Secret.

For the SQS Queue URL, refer to the following section in the CrowdStrike Falcon Data
Replicator (FDR): SQS Add-on for Splunk Installation and Configuration Guide.

Adding the Connector in Stellar Cyber
To add a CrowdStrike FDR connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose CrowdStrike FDR from the Type dropdown.

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

12. Enter the Access Key you noted above in Obtaining CrowdStrike FDR Credentials.

13. Enter the Secret Key you noted above.

14. Choose the Region from the dropdown.

15. Enter the SQS Queue URL you noted above.

16. Choose the Interval (min). This is how often the logs are collected.

17. Choose the Content Type you would like to collect. The logs for Aid Master, App Info,

Managed Assets, Not Managed Assets, and User Info are supported.

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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

