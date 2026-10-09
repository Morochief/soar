Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Stormshield SNS Firewall
Connectors

You can connect Stellar Cyber to Stormshield Network Security (SNS) firewalls so that you can
block and unblock IP addresses quickly and easily from within Stellar Cyber while you're threat
hunting. You can configure firewall actions or manually trigger a firewall action from the event
display.

Stormshield firewalls use a dynamic blacklist mechanism to control network behavior in addition
to deny policy rules. When an IP address is added to the blacklist, the firewall automatically
blocks all traffic from that address, enforcing security policy without requiring manual rule
modifications.

This integration uses the Stormshield CLI  API so that Stellar Cyber can add IP addresses to
its blacklist dynamically and remove them from it.

Connector Overview: Stormshield SNS Firewall

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP

Interval: N/A

Collected Data

N/A

Domain

<Host>

where <Host> is a variable from the configuration of this connector

Response Actions

Action

Required Fields

Block IP/Unblock IP

srcip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Host or IP Address, Port, Username, and Password

Adding a Stormshield SNS Firewall Connector
To add a new Stormshield SNS Firewall connector:

1. Obtain Stormshield firewall credentials
2. Add the connector in Stellar Cyber
3. Test the connector

 Stormshield firewalls come with predefined address lists, including a blacklist. It's not
necessary to create or configure a blacklist manually. Instead, either you manually add
IP addresses to the blacklist through the Stellar Cyber interface or Stellar Cyber
automatically adds them when applying a firewall action in an Automated Threat Hunting
(ATH) playbook in response to a security threat.

Obtaining Stormshield Firewall Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Stormshield
Networks Security firewall user credentials:

FQDN or IP address of the SNS firewall management interface

Username and password for a Stormshield Networks Security (SNS) firewall user
account with Modify privileges

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Stormshield connector in Stellar Cyber.

To add the Stormshield Network Security (SNS) Firewall connector:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Stormshield Network Security (SNS) Firewall from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector.

9. Choose the device on which to run the connector.

10. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

11. Enter the Host or IP Address using the FQDN or IP address of the SNS firewall
management interface that you noted above in Obtaining Stormshield Firewall
Credentials.

12. Enter the Port number. The default is 443.

13. Enter the Username and Password of the Stormshield user account that you noted

above.

14. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

15. Click Next. The final confirmation tab appears.

16. Click Submit.

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

