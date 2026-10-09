Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Barracuda Email Connectors

If your environment includes integration with Barracuda's Email Security Service, you can
configure a connector in Stellar Cyber to create an external email remediation incident in a
Barracuda Forensics And Incident Response deployment, based on Stellar Cyber alerts.

Connector Overview: Barracuda Email

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP

Interval: N/A

Collected Data

N/A

Domain

https://api.barracudanetworks.com

Response Actions

Action

Remediate Email

Required Fields

barracuda.account_id and barracuda.subject and
barracuda.env_from and barracuda.hdr_from

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Client ID and Client Secret

Adding a Barracuda Email Connector
To add a new Barracuda email connector:

1. Verify the Barracuda configuration
2. Enable API Access / Obtain Credentials
3. Add the connector in Stellar Cyber
4. Test the connector

Verifying the Barracuda Configuration
This connector is intended to support deployments with Barracuda already integrated. The
following are needed before you proceed:

1. You must already have a Barracuda Cloud Control / Email Protection account set up.

(https://ess.barracudanetworks.com/ )

2. Your email service must already be integrated with Barracuda Email Security as a

gateway. (Steps are provided on the Barracuda documentation website .)

3. Configure SYSLOG parsing for port 5559 on the Barracuda email server and on your

Stellar Cyber sensor.

Enabling API Access

1. Use the Barracuda token service to register an application for communication between

Stellar Cyber and the Barracuda Email Gateway Defense system. Log in to:
https://login.bts.barracudanetworks.com/register . (Steps are also provided  on
Barracuda's documentation site.)

2. Click Add Application.

3. Ensure you select the option to permit read/write, which allows you to submit response

actions from Stellar Cyber.

4. After you save the application, make note of the Client ID and Client Secret. If you

forget these, you can retrieve the ID but not the secret, you would need to use the token
web page to reset the secret.

Adding the Connector in Stellar Cyber
To add a Barracuda Email Security connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Email from the Category dropdown.

5. Choose Barracuda Email Security from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this

tenant name.

9. Choose the device on which to run the connector.

10. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

11. Enter the Client ID and Client Secret noted in the previous section.

12. Click Next. The final confirmation tab appears.

13. Click Submit.

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

