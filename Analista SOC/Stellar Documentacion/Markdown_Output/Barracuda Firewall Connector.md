Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Barracuda Firewall Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. For either action you
must already have your firewall connected.

Connector Overview: Barracuda Firewall

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: N/A

Collected Data

N/A

Domain

https://<Device IP Address>:<Device Port>

where <Device IP Address> and <Device Port> are variables from the configuration of this
connector

Response Actions

Action

Block IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

API Token, Device IP Address, Device Port, Source Network Object, and Destination Network
Object

Adding a Barracuda Firewall Connector
To add a new Barracuda firewall connector:

1. Create firewall rules
2. Enable the firewall API
3. Add the connector in Stellar Cyber
4. Test the connector

Creating Firewall Rules
To trigger firewall actions you must have rules on your Barracuda firewall that you can trigger.
Those rules must have network objects. You must:

1. Create a rule for blocking inbound IP addresses.

2. Configure a source network object  . The Name of this object is the Source Network

Object you will use when configuring the connector in Stellar Cyber.

3. Create a rule for blocking outbound IP addresses.

4. Configure a destination network object  . The Name of this object is the Destination

Network Object you will use when configuring the connector in Stellar Cyber.

Enabling the Firewall API
You must enable the Barracuda firewall API  for HTTPS. When you do, note:

the HTTPS Port

the API Token

You'll need both of these when configuring the connector in Stellar Cyber.

Adding the Connector in Stellar Cyber
To add a Barracuda firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Barracuda Firewall from the Type dropdown.

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

11. Enter the API Token to access the firewall.

12. Enter the Device IP Address or FQDN.

13. Enter the Device Port you noted above.

14. Enter the name of the Source Network Object that you created above.

15. Enter the name of the Destination Network Object that you created above.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new firewall connector is immediately active.

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

