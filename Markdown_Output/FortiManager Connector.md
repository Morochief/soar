Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring FortiManager Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. For either action you
must already have your firewall connected.

Use FortiManager to manage multiple FortiGate firewalls.

Connector Overview: FortiManager

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: N/A

Collected Data

N/A

Domain

N/A

Response Actions

Action

Block IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Host Name, User Name, Password, Administrative Domain, Source IP Group Name, Destination
IP Group Name, and Policy Package Name

Adding a FortiManager Connector
To add a FortiManager connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector

Obtaining FortiManager Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following FortiManager
credentials.

Host Name—The IP address, FQDN, or subnet, for example, 10.1.1.5 or mysite.com.

User Name and Password—The authentication credentials.

Administrative Domain (ADOM)—The logical partition in FortiManager. By default, the
ADOM is root.

Source IP Group Name—The collection of source IP address objects.

Destination IP Group Name—The collection of destination IP address objects

Policy Package Name—The set of firewall rules (policies), address objects, groups, and
settings. The policies can be installed on target devices or device groups.

Ensure the following:

The source/destination IP groups exist and are associated with some blocking policy in
FortiManager. Stellar Cyber checks if the address group or policy exists, but will not
create one if the group is not found. The Policy Package must include policies that use
Source IP Group as src address and Destination IP Group as dst address.

The policy package exists. Also, ensure there is a policy inside the policy package that
references the source/destination IP group.

Adding a FortiGate to FortiManager

To add a FortiGate to the FortiManager, follow the guidance in the Fortinet documentation for
Adding a model device .

1. In FortiManager, navigate to Device Manager > Device & Groups.

2. Click Add Device. The wizard opens.

3. To add a model device, enter a Name and provide the model device info.

4. Click Next in the wizard to continue adding the device.

Creating a Source Address Group

To add a source address group, follow the guidance in the Fortinet documentation to Create or
edit an address group .

1. Navigate to Create New > Address Group.

2. In the New Address Group window, enter a group name. In this example, it is

Stellar_Src_Group.

3. For Members, select the addresses to add to the source address group.

4. Click OK.

Creating a Destination Address Group

To add a destination address group, follow the guidance in the Fortinet documentation to Create
or edit an address group .

1. Navigate to Create New > Address Group.

2. In the New Address Group window, enter a group name. In this example, it is

Stellar_Dst_Group.

3. For Members, select the addresses to add to the destination address group.

4. Click OK.

Creating a Device Group

To create a device group and add the FortiGate firewalls to it, follow the guidance in the Fortinet
documentation to Add device groups .

1. Navigate to Device Manager > Device & Groups > Device Group > Create New.

2. Enter a Group Name. In this example, it is Device-Group-Stellar.

3. Click OK.

Creating a Policy Package

To create a policy package, follow the guidance in the Fortinet documentation to Create new
policy packages .

1. Navigate to Policy & Objects > Policy Packages > Policy Package > New Package.

2. Enter a policy package Name. In this example, it is Policy-Package-0.

3. Click OK.

Creating a Firewall Policy for Source

To create a deny firewall policy for source, follow the guidance in the Fortinet documentation to
Create New Firewall Policy .

1. Navigate to Policy & Objects > Policy Packages and select Firewall Policy.

2. Enter a firewall policy Name. In this example, it is FW-policy-stellar-deny-src.

3. Specify the Source. In this example, it is Stellar_Src_Group.

4. Specify the Action. In this example, it is Deny.

5. Provide the remaining required information.

6. Click OK.

Creating a Firewall Policy for Destination

To create a deny firewall policy for destination, follow the guidance in the Fortinet documentation
to Create New Firewall Policy .

1. Navigate to Policy & Objects > Policy Packages and select Firewall Policy.

2. Enter a firewall policy Name. In this example, it is FW-policy-stellar-deny-dst.

3. Specify the Source. In this example, it is Stellar_Dst_Group.

4. Specify the Action. In this example, it is Deny.

5. Provide the remaining required information.

6. Click OK.

Creating an Installation Target

To create an installation target, follow the guidance in the Fortinet documentation for Policy
package installation targets .

1. Navigate to Policy & Objects > Policy Packages and select Installation Targets.

2. Select the device group created previously. In this example, it is Device-Group-Stellar.

Creating a Local API User

To create a local API user, follow the guidance in the Fortinet documentation for Creating
administrators .

1. Navigate to System Settings > Admin > Administrators and click Create New.

2. Enter a User Name, select an Admin Type, for example, LOCAL, enter and confirm a

Password.

3. Provide the remaining required information.

4. Click OK.

Adding the Connector in Stellar Cyber
To add a new FortiManager connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose FortiManager from the Type dropdown.

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

11. Enter the Host Name you noted above in Obtaining FortiManager Credentials.

12. Enter the User Name you noted above.

13. Enter the Password you noted above.

14. Enter the Administrative Domain you noted above.

 Administrative Domain (ADOM) is a logical partition in FortiManager. By default,

the ADOM is root.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Enter the Source IP Group Name you noted above.

17. Enter the Destination IP Group Name you noted above.

18. Enter the Policy Package Name you noted above.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new firewall connector is immediately active.

Testing the Connector

 In addition to testing for connectivity, the Test button for the FortiManager connector tests
that the ADOM exists, the Source and Destination IP groups exist, the Policy Package
exists, and the Policy Package includes policies that use Source IP Group as src address
and Destination IP Group as dst address.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

