Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring F5 BIG-IP Firewall Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. For either action you
must already have your firewall connected.

Connector Overview: F5 BIG-IP Firewall

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

User Name, Password, Device IP Address, Source Address List, Destination Address List, and
Device Port

Adding an F5 BIG-IP Firewall Connector
To add a new F5 BIG-IP firewall connector:

1. Create firewall rules
2. Add the connector in Stellar Cyber
3. Test the connector

You can also send F5 BIG-IP telemetry data to a sensor using API calls.

Creating Firewall Rules
To trigger firewall actions you must have rules on your F5 BIG-IP firewall that you can trigger. We
suggest two rules, one to block outgoing destinations and one to block incoming.

On your F5 BIG-IP firewall:

1. Create two address lists. You will use these when adding the connector in Stellar Cyber.
When a firewall action is triggered, Stellar Cyber adds the IP address to one of these
lists. For our examples, we used dst_group and src_group.

2. Create a deny policy to all destinations with the src_group as the source.

3. Create a deny policy with the dst_group as the destination and all sources.

 The Block IP action adds an IP address to the corresponding address list. The Unblock IP

action removes the IP address from the corresponding address list.

Adding the Connector in Stellar Cyber
To add a new F5 BIG-IP firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose F5 BIG-IP Firewall from the Type dropdown.

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

11. Enter the User Name to log in to the firewall. This user must have access rights to

modify a rule.

12. Enter the Password to log in to the firewall.

 The password should not include non-ASCII special characters.

13. Enter the Device IP Address. This is the management IP address for the firewall.

14. Enter the Source Address List to which to add the IP address. This is the source

address list you created that is used to include IP addresses that should be blocked as
source.

15. Enter the Destination Address List to which to add the IP address. This is the

destination address list you created that is used to include IP addresses that should be

blocked as destination.

16. Enter the Device Port. This is the API port.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

