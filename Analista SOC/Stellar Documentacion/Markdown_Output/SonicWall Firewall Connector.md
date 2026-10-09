Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring SonicWall Firewall Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. For either action you
must already have your firewall connected.

Connector Overview: SonicWall Firewall

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

User Name, Password, Device IP Address, Source IP Group, Destination IP Group, and External
Zone

Adding a SonicWall Firewall Connector
To add a new SonicWall firewall connector:

1. Configure SonicWall:

For version 7.0 of Sonic OS
For previous versions of Sonic OS

2. Enable and test the connector in Stellar Cyber:

a. Add the connector in Stellar Cyber
b. Test the connector
c. Verify ingestion

Configuring SonicWall

Configuration in SonicWall v7.0

To enable integration using the v7.0 version of SonicWall:

1. Log in to your SonicWall firewall.

2. Navigate to the Device tab from the top of the console.

3. From the left side navigation, select Firewall > Settings > Administration.

4. On the pane that displays, select the tab for Audit / SonicOS API.

5. In the section for SONICOS API, toggle the following options as indicated:

SonicOS API: ON

CHAP authentication: ON

RFC-2617 HTTP Basic Access authentication: ON

Session security using RFC-7616 Digest authentication: OFF

6. Click Accept.

7. Ensure the following are also configured on the server:

a. Navigate to Device > Local Users & Groups > Local Groups > Edit User

Group.

b. Ensure that the group for the user you will be configuring has the following

setting enabled.

c. In the event of multiple administrators, when there is preemption by another

admin, the user should drop to non-config mode. You can configure this option
in the following location: Device > Administration > Login / Multiple
Administrators:

 Only one session can run using the provided credentials. If a user logs

into the console through the browser, it impacts the connector. So if a user
logs into the console, they should drop to non-config mode.

Creating SonicWall Address Object Groups

 The address groups must contain only IPv4 addresses.

1. Log in to your SonicWall firewall.

2. Navigate to the Object tab on the top of the console.

3. From the left side navigation, select Match Objects > Addresses.

4. In the pane that displays, ensure the Address Object sub-tab is displayed, then click

Add.

5. In the Address Object Settings dialog, enter the following:

a. Name: 0.0.0.0_LAN

b. Zone Assignment: LAN

c. Type: Host

d. IP Address: 0.0.0.0

6. Click Save.

7. Click Add again to repeat this and add a WAN configuration:

a. Name: 0.0.0.0_WAN

b. Zone Assignment: WAN

c. Type: Host

d. IP Address: 0.0.0.0

8. Click Save.

9. Click the sub-tab for Address Groups and select the Add button.

10. In the Add Address Groups dialog, do the following:

a. Set the Name to Stellar_src_group.

b. Locate and select the 0.0.0.0_WAN you just configured from the Not In Group

list and click the right arrow to add it to the In Group list.

11. Click Save.

12. Click Add again. The Add Address Object Group screen appears.

13. Enter the following:

a. Set the Name to Stellar_dst_group.

b. Locate and select the 0.0.0.0_LAN you just configured from the Not In Group

list and click the right arrow to add it to the In Group list.

14. Click Save.

Creating SonicWall Access Rules

To create SonicWall access rules:

1. Log in to your SonicWall firewall.

2. Navigate to the Policy tab on the top of the console.

3. From the left side navigation, select Rules and Policies > Access Rules. The existing

rules are displayed in a new pane on the right.

4. From the bottom of the new pane, click the Add button.

5. In the Adding Rule dialog, configure the rule as follows:

Name : Stellar_dst_rule

Action : Deny

SOURCE:

Zone / Interface: LAN

Address: Any

Port/Services: Any

DESTINATION:

Zone / Interface: WAN

Address: Stellar_dst_group

Port/Services: Any

6. Click Add.

7. Click Add again to configure a rule for the source group.

8. Enter the following:

Name : Stellar_src_rule

Action :  Deny

SOURCE:

Zone / Interface: WAN

Address: Any

Port/Services: Any

DESTINATION:

Zone / Interface: LAN

Address: Stellar_src_group

Port/Services: Any

9. Click Add.

10. Confirm the rules are entered by searching for Stellar in the search dialog in the

Access Rules pane.

Configuration in Sonicwall v6.x:

To enable integration using previous releases of SonicOS:

1. Log in to your SonicWall firewall.

2. Click Manage. The management dashboard appears.

3. Under System Settings, click Appliance | Base Settings.

The firewall settings page appears.

4. Scroll down to SonicOS API.

5. Click Enable SonicOS API.

6. Enable RFC-7616, CHAP, and RFC-2617.

7. Click Accept.

The API is now enabled.

Creating SonicWall Address Object Groups

 The address groups must contain only IPv4 addresses.

To create SonicWall address object groups:

1. Log in to your SonicWall firewall.

2. Click Manage. The management dashboard appears.

3. Under Policies, click Objects | Address Objects.

The existing address objects appear.

4. Click Add. The Add Address Object screen appears.

5. Enter the following:

a. Name: 0.0.0.0_LAN

b. Zone Assignment: LAN

c. Type: Host

d. IP Address: 0.0.0.0

6. Click OK.

7. Click Add again. The Add Address Object screen appears.

8. Enter the following:

a. Name: 0.0.0.0_WAN

b. Zone Assignment: WAN

c. Type: Host

d. IP Address: 0.0.0.0

9. Click OK.

10. Click Address Groups.

11. Click Add. The Add Address Object Group screen appears.

12. Enter the following:

a. Name: Stellar_src_group

b. In Group: 0.0.0.0_WAN

13. Click OK.

14. Click Add again. The Add Address Object Group screen appears.

15. Enter the following:

a. Name: Stellar_dst_group

b. In Group: 0.0.0.0_LAN

16. Click OK.

Creating SonicWall Access Rules

To create SonicWall access rules:

1. Log in to your SonicWall firewall.

2. Click Manage. The management dashboard appears.

3. Under Policies, click Rules | Access Rules.

The existing rules appear.

4. Click Add. The Add Rule screen appears.

5. Enter the following:

a. Policy Name: Stellar_dst_rule

b. Action: Deny

c. From: LAN

d. To: WAN

e. Source Port: Any

f. Service: Any

g. Source: Any

h. Destination: Stellar_dst_group

6. Click Add.

7. Click Add again. The Add Rule screen appears.

8. Enter the following:

a. Policy Name: Stellar_src_rule
b. Action: Deny
c. From: WAN
d. To: LAN
e. Source Port: Any
f. Service: Any
g. Source: Stellar_src_group
h. Destination: Any

9. Click Add.

Adding the Connector in Stellar Cyber
To add the SonicWall Firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose SonicWall Firewall from the Type dropdown.

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

 The password should not include non-ASCII special characters.

13. Enter the Device IP Address.

14. (Optional) Enter the Device Port. The default is 443.

15. Enter the Source IP Group that you created earlier. Our example uses

Stellar_src_group.

16. Enter the Destination IP Group that you created earlier. Our example uses

Stellar_dst_group.

17. Enter the External Zone. This example uses WAN.

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

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Search for msg_origin.source: sonicfw.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

