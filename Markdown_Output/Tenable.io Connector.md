Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Tenable.io Connectors

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M03 Modular Sensor Concepts and Configuration (08h:56m)  

Modular Sensor Tenable Nessus Scanner (30m:00s)

Explore how the Stellar Cyber Modular Sensor includes a built-in Tenable Nessus
vulnerability scanner. Learn how integrated vulnerability scanning simplifies deployment
and enables efficient collection of vulnerability data for enhanced security monitoring
and analysis.

Modular Sensor Platform Connector with Tenable (50m:00s)

Explore how to configure the Stellar Cyber Platform connector for Tenable.io. Learn to
integrate Tenable.io with the Stellar Cyber Platform to automate collection of
vulnerability scan and asset data for enhanced threat analysis and reporting.

The first time you access a link on the portal during a session, you must log in to access
content.

Vulnerability scanners examine hosts for known and possible security vulnerabilities. You can
use this connector to ingest scan reports to the Stellar Cyber data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Tenable.io

Capabilities

Collect: Yes

Locating Records

msg_class:

security_scan

security_scan_re
ports

msg_origin.source:

tenableio

tenableio_report
s

msg_origin.vendor

tenable

msg_origin.category:

security_scan

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Vulnerabilities

Scans (reports and events)

Index

Scans

Assets (for
Vulnerabilities)

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Access Key and Secret Key

Adding a Tenable.io Connector
To add a Tenable.io connector:

1. Obtain Tenable.io credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Tenable.io Credentials
The following credentials are required:

Create a user with Administrator privileges.

Log in as that user to accept the license agreement.

Add that user to a group with the following permissions: Can View and Can Scan, and
the following access object: All Assets.

Generate API keys.

Create a User

To create a user:

1. Navigate to Settings.

2. Choose Access Control.

3. Choose Users | Create User.

4. Enter the FULL NAME, USERNAME, EMAIL, PASSWORD, and VERIFY PASSWORD.

5. Select Administrator from the ROLE dropdown.

6. Select API Key for AUTHENTICATION.

7. Click Next.

8. Select All Users from the USER GROUPS dropdown.

9. Click Next.

10. Click Save.

11. Log in to Tenable.io as that user and accept the license agreement.

Add Permissions

To add permissions and groups for the user:

1. Navigate to Settings | Access Control.

2. Choose Permissions | Create Permission.

3. Enter a PERMISSION NAME and select the user from the USERS drop down.

4. Select the All Users group from the GROUPS dropdown.

5. Select Can View and Can Scan from the PERMISSIONS dropdown.

6. Select All Assets from the OBJECTS dropdown.

7. Click Save.

Generate API Keys

To generate API keys:

1. Navigate to Settings and choose My Account.

2. Select API KEYS.

3. Click Generate.

4. Click Continue.

5. Copy the ACCESS KEY and SECRET KEY, which will be used to add the connector in

Stellar Cyber.

 Store the API keys in a safe location. They cannot be retrieved later although they

can be regenerated.

Adding the Connector in Stellar Cyber
See Tenable   for information on configuring a Tenable.io scanner.

To add a new Tenable.io vulnerability scanner connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose Tenable.io from the Type dropdown.

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

12. Enter the Access Key you noted above.

13. Enter the Secret Key you noted above.

14. Enter the Interval, which is the time between polls of the scanner.

15. Choose Asset Synchronization to share information bi-directionally. If you enable this,

Stellar Cyber shares MAC-identified assets with Tenable.io.

16. Choose the Content Type. The logs for Scans and Vulnerabilities are supported.
Select Scans to collect Security Scan Reports and Security Scan Events.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

The new connector is immediately active and collects logs for the previous 30 days.

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

2. Change the Indices for the type of content you collected:

For Scans and Vulnerabilities, change the Indices to Scans.

For Vulnerabilities only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Search for the msg_class values listed in Locating Records at the top of this page.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

