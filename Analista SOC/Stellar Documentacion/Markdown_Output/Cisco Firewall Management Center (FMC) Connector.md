Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cisco Firewall Management Center
(FMC) Connectors

This connector allows you to Block an IP using an API call to the Cisco FMC (formerly
Firepower Management Center) firewall you configure below.

Connector Overview: Cisco FMC

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: N/A

Collected Data

N/A

Domain

https://<Device IP Address>

where <Device IP Address> is a variable from the configuration of this connector

Response Actions

Action

Block IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

User Name and Password for API access

Device IP Address: This is the Cisco FMC IP address

Source IP Group, Destination IP Group (are required for the API but can be empty)

A Cisco FMC policy to block an IP address, a source IP group rule, and a destination IP group
rule

Cisco FMC must be enabled for API access

Adding a Cisco FMC Connector
To add a Cisco FMC connector:

1. Configure Cisco FMC and obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector

Configuring Cisco FMC and Obtaining Credentials

1. Follow guidance on the FMC website to enable API functionality  for the firewall.

2. Make note of the host IP address for your Cisco FMC instance. This is used as the

Device IP Address during configuration.

3. Create a user for use with the API:

a. Log into the Cisco FMC console as an administrative user.

 Do not use an administrator user for your connector configuration.

b. Display the Settings menu and select the option for Users.

c. From the Users screen, click Create User.

d. In the dialog that displays, configure a user for use with Stellar Cyber that has

at least the Network Admin role.

 Do not create the user with administrative privileges.

e. Make note of the User Name and Password that you create.

 The password should not include non-ASCII special characters.

f. Click Save.

4. Create a Source IP Network Group for use with Stellar Cyber.

a. Navigate to the Objects tab on the Network page. Click Add Network and

select Add Group from the dropdown.

b. In the dialog that displays, enter a name for the group, to be associated with

Stellar Cyber.

c. Select Allow Overrides.

 It is not necessary to add networks to the group.

d. Click Save.

e. Click Yes.

5. Repeat the previous steps to create a Destination IP Network Group.

6. Configure a policy to block the IP address.

a. Navigate to Policies | Access Control.

b. Click New Policy.

c. In the dialog that displays, enter a name for the policy. Make sure Block all

traffic is selected.

d. For the Targeted Devices, select a device from the Available Devices and

click Add to policy.

e. Click Save.

7. Add a rule to block the source IP group.

a. Enter a rule name and select Enabled.

b. Select Block from the Action dropdown.

c. For the Source Networks, select the Source IP Network Group for use with

Stellar Cyber from the Available Networks and click Add to Source
Networks.

d. For the Destination Networks, select any from the Available Networks and

click Add to Destination.

e. Click Save.

8. Add a rule to block the destination IP group.

a. Enter a rule name and select Enabled.

b. Select Block from the Action dropdown.

c. For the Source Networks, select any from the Available Networks and click

Add to Source Networks.

d. For the Destination Networks, select the Destination IP Network Group for

use with Stellar Cyber from the Available Networks and click Add to
Destination.

e. Click Save.

f. You can view the policy and the rules as follows:

9. You should have the following information ready to configure your connector:

User Name and Password

Device IP Address

Source IP Group

Destination IP Group

Cisco FMC must be enabled for API access

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Cisco FMC  connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Cisco FMC from the Type dropdown.

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

11. Using the data you collected in the previous section, complete the following fields:

User Name

Password

Device IP Address

Source IP Group

Destination IP Group

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

