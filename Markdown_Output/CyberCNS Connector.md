Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring CyberCNS Connectors

This connector allows Stellar Cyber to ingest logs from CyberCNS and add the records to the
data lake. It integrates with the CyberCNS API to get vulnerability information.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: CyberCNS

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

Scans

Locating Records

msg_class:

cybercns_vulnerabi
lity

msg_origin.source:

cybercns

msg_origin.vendor:

cybercns

msg_origin.category:

security_scan

Domain

<Domain Name>

where <Domain Name> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Domain Name, Tenant Name, Client ID, and Client Secret

Adding a CyberCNS Connector
To add a CyberCNS connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining CyberCNS Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following CyberCNS
credentials:

Client ID

Client Secret

1. Log in to CyberCNS as an administrative user.

2. Click the

 icon.

3. Navigate to Settings | Users and click Add.

4. You can add a user to All Companies or to Specific Companies.

To add a user to All Companies:

a. Enter the First Name, Last Name, and Email.

b. Choose a Role, for example, readOnly.

c. Click All Companies.

d. Click Save.

e. Under Action, click the three vertical dots icon and choose API Key.

To add a user to Specific Companies:

a. Enter the First Name, Last Name, and Email.

b. Choose a Role, for example, readOnly.

c. Click Specific Companies.

d. Select one or more companies.

e. Click Save.

f. Under Company Access, you can select Restricted and then choose

API Key.

g. Under Action, you can click the three vertical dots icon and choose API Key.

5. Copy the API key.

 Store the API key in a safe location. It cannot be retrieved later although it can be

regenerated.

Adding the Connector in Stellar Cyber
To add a CyberCNS connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose CyberCNS from the Type dropdown.

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

12. Enter the Domain Name. For example, portaluseast2.mycybercns.com or

portaluswest2.mycybercns.com.

 Do not include the http/https prefix.

13. Enter the Tenant Name. This is the name of the CyberCNS tenant.

14. Enter the Client ID you noted above in Obtaining CyberCNS Credentials.

15. Enter the Client Secret you noted above.

16. Choose the Interval (min). This is how often this connector retrieves data from

CyberCNS.

17. Choose the Content Type you would like to collect. The logs for Vulnerabilities are

supported.

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

For Vulnerabilities change the Indices to Scans.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

