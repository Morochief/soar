Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring People Risk Explorer Connectors

This connector allows Stellar Cyber to ingest logs from People Risk Explorer and add the records
to the data lake. This connector integrates with the People Risk Explorer API to query
Organization Group Risk Posture, People Group Risk Posture, and People Risk Posture data.

 The data is downloaded once per day, however, because the third party generates CVS files
at inconsistent times each day, Stellar Cyber extracts only the CSV files that were generated
on the previous day. As a result, the data is delayed by one day.

People Risk Explorer gives you a unified view of your people-centric risk across the Proofpoint
platform and third-party products, assesses the impact of user risk on your organization, and lets
you scope and prioritize security projects to protect your people and data.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: People Risk Explorer

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Every day

Collected Data

Content Type

Index

Locating Records

Organization Group Risk Posture

Syslog

msg_class:

Content Type

Index

Locating Records

People Group Risk Posture

People Risk Posture

proofpoint_people_
risk_explorer_org_
group_risk_posture

proofpoint_people_
risk_explorer_peop
le_group_risk_post
ure

proofpoint_people_
risk_explorer_peop
le_risk_posture

msg_origin.source:

proofpoint_people_
risk_explorer

msg_origin.vendor:

proofpoint

msg_origin.category:

email

Domain

<Auth URL> and <Base URL>

where <Auth URL> and <Base URL> are variables from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Auth URL, Base URL, Client ID, and Client Secret

Adding a People Risk Explorer Connector
To add a People Risk Explorer connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining People Risk Explorer Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following People Risk
Explorer credentials:

Auth URL—The authentication URL for API access. The default is:
https://auth.proofpoint.com

Base URL—The base URL for API access. The default is:
https://api.peoplecentric.proofpoint.com

Client ID and Client Secret—The authentication credentials. Follow the guidance in the
People Risk Explorer User Guide to generate service credentials for the People Risk
Explorer API.

Adding the Connector in Stellar Cyber
To add a People Risk Explorer connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose People Risk Explorer from the Type dropdown.

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

12. Enter the Auth URL you noted above in Obtaining People Risk Explorer Credentials.

13. Enter the Base URL you noted above.

14. Enter the Client ID you noted above.

15. Enter the Client Secret you noted above.

16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

17. Choose the Content Type you would like to collect. The logs for Organization Group

Risk Posture, People Group Risk Posture, and People Risk Posture are supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the People Risk Explorer connector

tests that the Auth URL, Base URL, Client ID, and Client Secret are correct.

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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

