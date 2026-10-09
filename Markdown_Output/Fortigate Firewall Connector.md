Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Fortigate Firewall Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. For either action you
must already have your firewall connected.

Connector Overview: Fortigate Firewall

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

For API Token Auth Method: API Token, Device IP Address, Source IP Group, Destination IP
Group, and Virtual Domain Name

For User Name / Password Auth Method: User Name, Password, Device IP Address,
Source IP Group, Destination IP Group, and Virtual Domain Name

Adding a Fortigate Firewall Connector
To add a Fortigate firewall connector:

1. Create API user
2. Create firewall rules
3. Obtain an API Token
4. Add the connector in Stellar Cyber
5. Test the connector

Creating API User
To create an API user, first create an Admin Profile, then create the API user either for a single
VDOM or multiple VDOMs.

Creating Admin Profile

1. Navigate to Admin Profiles under System.

2. Click Create New.

3. For the Access Permissions, next to Firewall, click Custom.

4. For the Firewall Address, click Read/Write.

5. Click OK.

Creating an API User for a Single VDOM

To create an API user for a single VDOM:

1. Navigate to Administrators under System.

2. Click Create New and select Administrators.

3. In the New Administrator window, enter a Username, Password, and Confirm

Password.

4. For the Administrator Profile, select the profile you previously created.

5. Click OK.

Creating an API User for Multiple VDOMs

To create an API user for multiple VDOMs, follow the initial steps in Creating an API User for a
Single VDOM:

1. In the New Administrator window, in addition to selecting the Administrator Profile you

previously created, also select Virtual Domains.

2. Click OK.

Creating Firewall Rules
To trigger firewall actions, you must have rules on your Fortigate firewall that you can trigger.
Create the rules with a user that has access rights to modify rules.

Login to Fortigate with a user that you have previously logged in with. Or, if you have created a
new user, log in to Fortigate as that user and accept the license agreement before starting this
procedure.

To create the firewall rules:

1. Create two address groups. You will use these when adding the connector in Stellar

Cyber. When a firewall action is triggered, Stellar Cyber adds the IP address to one of
these groups.

 Do not use non-ASCII characters in IP address names. When blocking an IP

address, there cannot be an existing address in the IP address group in which the
IP address name has non-ASCII characters in it.

The following is an example of the source address group named Stellar-Src-Group:

The following is an example of the destination address group named Stellar-Dst-
Group:

2. Click OK to save each address group.

3. Create two deny policies. The first policy is an example of an Inbound Deny rule named

Stellar_Inbound with the following settings:

Incoming Interface: Internet (wan1)
Outgoing Interface: internal
Source = Stellar-Src-Group
Destination = all
Action = DENY

When there is a Block IP action from an alert and the direction is inbound, the IP
address will be added in the Source address group to the firewall (Stellar-Src-Group in
this example).

4. The second policy is an example of an Outbound Deny rule named Stellar_Outbound

with the following settings:

Incoming Interface: internal
Outgoing Interface: Internet (wan1)
Source = all
Destination = Stellar-Dst-Group
Action = DENY

When there is a Block IP action from an alert and the direction is outbound, the IP
address will be added in the Destination address group to the firewall (Stellar-Dst-Group
in this example).

5. Click OK to save each rule.

Obtaining an API Token
There are two ways to authenticate with the Stellar Cyber connector: API Token or User Name /
Password. The API Token Auth Method is recommended.

You generate an API token when you create a REST API administrator in the GUI or the CLI.
Refer to the FortiOS Administration Guide for REST API administrator .

Adding the Connector in Stellar Cyber
To add a new Fortigate firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Fortigate from the Type dropdown.

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

11. Choose the Auth Method to use API Token or User Name / Password.

 The API Token Auth Method is recommended.

For API Token Auth Method, enter the API Token you noted above in Obtaining an
API Token.

For User Name / Password Auth Method:

The asterisk (*) indicates a required field.

a. Enter the User Name to log in to the firewall. This user must have access

rights to modify a rule.

b. Enter the Password to log in to the firewall.

 The password should not include non-ASCII special characters.

12. Enter the Device IP Address. This is the management IP address for the firewall.

13. (Optional) Enter the Device Port. The default is 443.

14. Enter the Source IP Group to which to add the IP address. This is the source address

group you created above in Creating Firewall Rules.

15. Enter the Destination IP Group to which to add the IP address. This is the destination

address group you created above in Creating Firewall Rules.

16. Enter the Virtual Domain Name. This is where the rules were created.

 Virtual Domains (VDOMs) are used to divide a Fortigate into two or more virtual
units that function independently. By default, the management VDOM is root.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

