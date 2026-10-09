Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Check Point Firewall Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting.

Check Point integration with Stellar Cyber provides real-time visibility into network security
events and enables automated incident response workflows to contain and mitigate threats.

You can configure firewall actions or manually trigger the Block IP firewall action from the event
display.

Connector Overview: Check Point Firewall

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

User Name, Password, Device IP Address, Source IP Group, Destination IP Group, and Policy
Package Name

Adding a Check Point Firewall Connector
To add a Check Point firewall connector:

1. Configure a Check Point Firewall connector
2. Verify Check Point Firewall API access
3. Add the connector in Stellar Cyber
4. Test the connector

Configuring a Check Point Firewall Connector
To configure Stellar Cyber's Check Point Firewall connector actions requires that you have:

Verified your Check Point Firewall has API access enabled

Obtained the following data from your Check Point Firewall Configuration:

User name and password

 The password should not include non-ASCII special characters.

Device IP address

(Optional) Device port

Source IP group

Destination IP group

(Optional) Domain

Policy package name

Verifying Check Point Firewall API Access
Use the following procedures to configure network groups that will be used by the Stellar Cyber
Data Processor when it takes a firewall action. You also need to enable the management API
server.

Adding a New Host

To add a new host (for example, StellarCyber_Unused_Address):

1. Log in as an administrative user to your Check Point Security Management Server

with Check Point's SmartConsole application.

2. From the SmartConsole, open the Object Explorer.

3. Choose New | Host.

4. In New Host, enter an IP address that is not normally used in the network.

5. Click OK.

Adding Network Groups

To configure two network groups containing the new host (for example, StellarCyber_SrcGrp and
StellarCyber_DstGrp):

1. From the SmartConsole, open the Object Explorer.

2. Choose New | Network Group.

3. In New Network Group, enter a name for the first group, such as

StellarCyber_SrcGrp.

4. For each Host you want to monitor in this group, click the [+] sign and select it from the

displayed list of network objects.

5. Click OK.

6. Choose New | Network Group again.

7. In New Network Group, enter a name for the second group, such as

StellarCyber_DstGrp.

8. For each Host you want to monitor in this group, click the [+] sign and select it from the

displayed list of network objects.

9. Click OK.

Adding Policy Rules

To configure policy rules:

1. Navigate to SECURITY POLICIES | Access Control | Policy.

2. Add new policy rules on the top. Also add the management services, such as SSH and

HTTPS, to be accepted.

3. Choose Publish session.

4. Then choose Install policy.

Enabling the Management API Server

1. Navigate to MANAGE & SETTINGS | Blades.

2. Under Management API, choose Advanced Settings.

3. In the Advanced Settings window:

Under Startup Settings, ensure that Automatic start is selected

Under Access Settings, click either All IP addresses that can be used for
GUI clients or All IP addresses.

4. Click OK.

5. To apply the changes, publish and restart the Management API server with api

restart.

6. Click OK.

7. Log in to the Check Point firewall via SSH and type api restart.

Adding the Connector in Stellar Cyber
To add a new Check Point firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Check Point from the Type dropdown.

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

11. Enter the User Name to log in to the firewall.

12. Enter the Password to log in to the firewall.

13. Enter the Device IP Address of the Check Point firewall instance.

14. (Optional) Enter the Device Port, for example 443.

15. Enter the Source IP Group to which to add the IP address.

16. Enter the Destination IP Group to which to add the IP address.

17. (Optional) Enter the Domain.

18. Enter the Policy Package Name.

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

