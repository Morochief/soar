Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Barracuda WAF Connectors

This connector allows Stellar Cyber to ingest logs from Barracuda Web Application Firewall
(WAF) Cloud and add the records to the data lake. It integrates with the Barracuda WAF-as-a-
Service API  to query for WAF and access logs.

This connector enhances visibility into web application security events, providing better
protection against web-based threats such as SQL injection, cross-site scripting, and DDoS
attacks.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Barracuda WAF

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Access Logs

WAF Logs

Index

Syslog

Locating Records

msg_class:

barracuda_waf_acce
ss_log

barracuda_waf_waf_
log

msg_origin.source:

Content Type

Index

Locating Records

barracuda_waf

msg_origin.vendor:

barracuda_waf

msg_origin.category:

waf

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL, Email, and Password

Adding a Barracuda WAF Connector
To add a Barracuda WAF connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Barracuda WAF Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Barracuda
WAF credentials:

Base URL—The base URL for API access, for example,
https://api.waas.barracudanetworks.com.

Email and Password—Create a new user. See Creating a New User.

Creating a New User

To create a new user with an email address and password:

1. As an administrative user, go to Barracuda Cloud Control at

https://login.barracudanetworks.com/ .

2. Enter your Admin username and password.

3. Click Log In.

4. On the Barracuda Cloud Control dashboard, navigate to Home > Admin > Users.

5. Click Add User.

6. Enter the required information for a user:

Name: Enter a username for the new user.

Email: Provide a valid email address for the user.

 The user will automatically be sent an email to configure their password.

7. You will need to assign a role (for example, Admin). In Product Entitlements, select

WAF as a Service (Admin).

8. Click Save User at the top of the page.

9. Log out of the current session if you are still logged in as the administrative user.

10. Log in to Barracuda Cloud Control using the credentials of the new user.

11. Access the WAF audit logs under Application Protection.

12. Select AUDIT LOGS to see the audit logs of the newly created user.

Adding the Connector in Stellar Cyber
To add a Barracuda WAF connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Web Security from the Category dropdown.

5. Choose Barracuda WAF from the Type dropdown

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

12. Enter the Base URL you noted above in Obtaining Barracuda WAF Credentials.

13. Enter the Email you noted above in Creating a New User.

14. Enter the Password you noted above.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Choose the Interval (min). This is how often the logs are collected.

17. Choose the Content Type you would like to collect. The logs for Access Logs and

WAF Logs are supported.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The new connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the Barracuda WAF connector tests
that the Base URL, Email, and Password are correct and data requests for the requested
content types return successful responses.

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

