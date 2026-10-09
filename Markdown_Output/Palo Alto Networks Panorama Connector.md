Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Palo Alto Networks Panorama
Connectors

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

You can integrate Stellar Cyber with Palo Alto Networks Panorama to manage all your firewalls.
While the Palo Alto Networks Firewall connector communicates with each individual firewall, the
Palo Alto Networks Panorama connector provides centralized management capabilities over
several Panorama firewalls.

You can configure firewall actions or manually trigger a firewall action from the event display.

Connector Overview: Palo Alto Networks Panorama

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

Block IP/Unblock IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

User Name, Password, Device IP Address, Software Version, Device Group, Source IP Group,
and Destination IP Group

Adding a Palo Alto Networks Panorama Connector
To add a new Palo Alto Networks Panorama connector:

1. Add a user
2. Add templates
3. Add device groups
4. Add address groups
5. Add policies
6. Add the connector in Stellar Cyber
7. Test the connector

Adding a User
To create an admin level user:

1. Under Panorama, select Administrators.

2. Click Add.

3. In the Administrator screen, enter the Name of the user. In this example, it is api-user.

4. Enter the Password and Confirm Password.

5. Select the following:

a. Administrator Type: Dynamic

b. Admin Role: Panorama administrator

c. Password Profile: None

6. Click OK.

Adding Templates
To add templates:

1. Under Panorama, select Templates.

2. Click Add.

3. In the Template screen, enter the Name of the template. In this example, it is

Stellar_template.

4. Select a Default VSYS.

5. Click OK.

6. Next under Templates, click Add Stack.

7. In the Template Stack screen, enter the Name of the template stack. In this example, it

is Stellar_Stack.

8. Add the Palo Alto firewall. In this example, it is PA-VM.

9. Add the template. In this example, it is Stellar_template.

10. Click OK.

Adding Device Groups
To add device groups:

1. Under Panorama, select Device Groups.

2. Click Add.

3. In the Device Group screen, enter the Name of the device group. In this example, it is

Stellar_Device_Group.

4. Check the Palo Alto firewall. In this example, the PA-VM firewall was added to

Stellar_Device_Group.

5. Add the template stack. In this example, it is Stellar_Stack.

6. Click OK.

Adding Address Groups
To add address groups:

1. Under Objects, select Address Groups.

2. Click Add.

3. In the Address Group screen, enter the Name of the source address group. In this

example, it is Stellar_Src.

 Do not select Shared.

4. Select a Type, for example, Static.

5. Select an IP address.

6. Click OK.

7. In the Address Group screen, enter the Name of the destination address group. In this

example, it is Stellar_Dst.

 Do not select Shared.

8. Select a Type, for example, Static.

9. Select an IP address.

10. Click OK.

11. View the address groups under the Device Group as follows:

Adding Policies
To add policies:

1. Under Panorama, select Policies > Security > Pre Rules.

2. Check that you have your Device Group selected. In this example, it is

Stellar_Device_Group. Click Add.

You will be adding two policies to refer to the source and destination address groups. In
this example, they are Stellar_Src and Stellar_Dst.

First, configure Stellar_Src.

3. In the Security Policy Rule screen, under the General tab, enter the Name of the

policy. In this example, it is Stellar_Security_Policy_Deny_Src_Group.

4. Under the Source tab, select Any and then add the source address group. In this

example, it is Stellar_Src.

5. Under the Destination tab, select Any.

6. Under the Application tab, select Any.

7. Under the Service/URL Category tab, select Any.

8. Under the Actions tab:

a. For the Action, select Deny.

b. For the Log Setting, select Log at Session End.

9. Under the Target tab, for the Device Group, select the firewall. In this example, the

Device Group is Stellar_Device_Group and the firewall is PA-VM.

10. Under the Usage tab, view the information.

11. Click OK.

12. Next, configure the policy to refer to the destination address group. In this example, it is

Stellar_Dst.

13. In the Security Policy Rule screen, under the General tab, enter the Name of the

policy. In this example, it is Stellar_Security_Policy_Deny_Dst_Group.

14. Under the Source tab, select Any and then select Any.

15. Under the Destination tab, add the destination address group. In this example, it is

Stellar_Dst.

16. Under the Application tab, select Any.

17. Under the Service/URL Category tab, select Any.

18. Under the Actions tab:

a. For the Action, select Deny.

b. For the Log Setting, select Log at Session End.

19. Under the Target tab, for the Device Group, select the firewall. In this example, the

Device Group is Stellar_Device_Group and the firewall is PA-VM.

20. Under the Usage tab, view the information.

21. Click OK.

Adding the Connector in Stellar Cyber
With the firewall rules in place, you can add the Palo Alto Networks Panorama connector in
Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Palo Alto Networks Panorama from the Type dropdown.

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

the firewall, for example, an admin level user name.

12. Enter the Password for that user name.

 The password should not include non-ASCII special characters.

13. Enter the Device IP Address.

14. (Optional) Enter the Device Port. The default is 443.

15. Enter the Software Version. This is the Panorama API version, such as 10.1, 10.2,

11.0, or 11.1.

 If your software version is 11.1.3, the Panorama API version is 11.1.

16. Enter the Device Group you noted above in Adding Device Groups.

17. Enter the Source IP Group you created in Adding Address Groups (for example,

Stellar_Src).

18. Enter the Destination IP Group you created in Adding Address Groups (for example,

Stellar_Dst).

19. Click Next. The final confirmation tab appears.

20. Click Submit.

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

