Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Nessus Connectors

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

Vulnerability scanners examine hosts for known and possible security vulnerabilities.

Nessus integration with Stellar Cyber enables organizations to conduct vulnerability scans and
identify security risks across their network, providing real-time threat intelligence and automated
response workflows to improve incident response and threat mitigation.

You can connect Stellar Cyber to your existing vulnerability scanner and have Stellar Cyber
generate reports on the target hosts scanned.

See Tenable   for information on configuring a Nessus scanner.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Nessus

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: Sensor

Interval: Configurable

Collected Data

Content Type

N/A

Index

Scans

Assets (host data
if mac_address
and ip_address)

Locating Records

msg_class:

security_scan

msg_origin.source:

nessus_scanner

msg_origin.vendor

tenable

msg_origin.category:

security_scan

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname, Port, Username, and Password (of the scanner)

Adding a Nessus Connector
To add a Nessus scanner:

1. Add the connector in Stellar Cyber
2. Test the connector
3. Verify ingestion

Adding the Connector in Stellar Cyber

To add a new Nessus vulnerability scanner connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose Nessus Scanner from the Type dropdown.

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

12. Enter the Hostname. This is the FQDN or IP address of the scanner.

 Do not include https in the Hostname.

13. Enter the Port. The default is 8834.

14. Enter the Username to log in to the scanner.

15. Enter the Password to log in to the scanner.

 The password should not include non-ASCII special characters.

16. Choose the Interval (min). This is the time between polls of the scanner.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

Change the Indices to Scans. Allow time for the vulnerability scan to
complete.

 Data for this connector is not entered into the Scan Index until the scan is

in a "Completed" status.

For host data, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

