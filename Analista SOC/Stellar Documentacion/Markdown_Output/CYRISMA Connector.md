Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring CYRISMA Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.
Review the content in this topic to understand what type of data can be collected and acted upon
for this connector type.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: CYRISMA

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Vulnerabilities

Index

Syslog, Linux

API

https://msp.c
yrisma.com/
app/vulnerab
ility/report/te
nants
(fetches
tenant IDs,
tenant
access URL,
and
temporary
access
token)

https://tenant
_access_url/

Content Type

Index

API

Hosts

Syslog, Assets

app/vulnerab
ility/report/js
on (fetches
vulnerabilitie
s)

Automaticall
y extracted
with
Vulnerabilitie
s

Domain

https://msp.cyrisma.com/

https://<customer_instance_URL>.cyrisma.com

 The <customer_instance_URL> is not provided in the configuration of this connector, but is

returned from previous API calls.

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

API Name and API Key

Locating Records

Use the following to query for records:

msg_origin.source: cyrisma

msg_origin.vendor: cyrisma

msg_origin.category: security_scan

msg_class: cyrisma_host, cyrisma_vulnerability

Adding a CYRISMA Connector
To add a CYRISMA connector:

1. Obtain credentials and prepare CYRISMA
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Credentials and Preparing CYRISMA
CYRISMA is a SaaS service with MSSP accounts managing data for multiple organizations.
Each organization is considered a “tenant” to Stellar Cyber.

 Set up one connector for each CYRISMA tenant from which you want to pull data.

To support this connector configuration and function:

Obtain the MSSP API Name and API Key: These are provided to the MSSP by
CYRISMA Customer Support.

Add Stellar Cyber Tenant IDs: For any organization that the MSSP wants to retrieve
data from CYRISMA, the MSSP must do the following:

1. Set up a tenant in Stellar Cyber corresponding to each of the organizations in

CYRISMA for which they want to collect data.

2. Access the Stellar Cyber Tenant screen and make note of the ID number

associated with each of the organizations.

3. Access the CYRISMA console (https://msp.cyrisma.com).

4. Display each organization page and locate the field labeled MDR/XDR Tenant,

as shown below.

5. Click the field and add the tenant ID you obtained from Stellar Cyber.

Adding the Connector in Stellar Cyber
To add the CYRISMA connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose CYRISMA from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. The connector will pull data for this tenant. The Interflow

records created by this connector include this tenant name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the API Name you obtained from CYRISMA Customer Support.

13. In the API Key you obtained from CYRISMA Customer Support.

14. Enter the Interval (hour). This is how often Stellar Cyber collects information.

 Note that the typical interval for connectors is in minutes. The CYRISMA

API supports intervals in hours.

15. Choose the Content Type. The logs for Vulnerabilities are supported.

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

2. Set the Indices to match the type of content you collected:

For Vulnerabilities, change the Indices to Scans.

For Host data, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

