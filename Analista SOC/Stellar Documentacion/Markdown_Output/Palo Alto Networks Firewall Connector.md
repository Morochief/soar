Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Palo Alto Networks Firewall
Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. For either action you
must already have your firewall connected.

Connector Overview: Palo Alto Networks Firewall

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

User Name, Password, Device IP Address, Source IP Group, Destination IP Group, and Virtual
System Name

Adding a Palo Alto Networks Firewall Connector
To add a new Palo Alto Networks firewall connector:

1. Create firewall rules
2. Add the connector in Stellar Cyber
3. Test the connector

Creating Firewall Rules
To trigger firewall actions from Stellar Cyber, you must already have firewall rules. To create Palo
Alto firewall rules:

1. Create an address group called Stellar_src_group. You must include at least one IP

address.

2. Create an address group called Stellar_dst_group. You must include at least one IP

address.

3. Create an outbound deny policy with the following:

Name: Stellar_Outbound_Deny

Source:

Zone: Any

Address: Stellar_src_group

User: any

Device: any

Destination:

Zone: Any

Address: Any

User: any

Device: any

Application: any

Service: any

Action: DENY

4. Create an inbound deny policy with the following:

Name: Stellar_Inbound_Deny

Source:

Zone: Any

Address: any

User: any

Device: any

Destination:

Zone: Any

Address: Stellar_dst_group

User: any

Device: any

Application: any

Service: any

Action: DENY

5. Commit all of your changes.

You now have firewall rules that you can trigger from Stellar Cyber.

Adding the Connector in Stellar Cyber

With the firewall rules in place, you can add the Palo Alto Networks firewall connector in Stellar
Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Palo Alto Networks from the Type dropdown.

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

11. Enter a User Name with permissions to edit address groups and commit the changes to

the firewall.

12. Enter the Password for that user name.

 The password should not include non-ASCII special characters.

13. Enter the Device IP Address.

14. (Optional) Enter the Device Port. The default is 443.

15. Enter the Source IP Group you created (for example, Stellar_src_group).

16. Enter the Destination IP Group you created (for example, Stellar_dst_group).

17. Enter the Virtual System Name. If the firewall is not configured to use multi-vsys, use

vsys1.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

