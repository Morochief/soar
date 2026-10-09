Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cisco Meraki Firewall Connectors

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display. With a Cisco Meraki
firewall connector configured, you can create a Stellar Cyber rule to automatically or manually
block on that firewall.

Connector Overview: Cisco Meraki Firewall

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP

Interval: N/A

Collected Data

N/A

Domain

https://api.meraki.com/api/v1

Response Actions

Action

Block IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL, API Key, Organization Name, and Network or Template Name

Adding a Cisco Meraki Firewall Connector
To add a Cisco Meraki firewall connector:

1. Enable API access
2. Add the connector in Stellar Cyber
3. Test the connector

Enabling API Access
Other than having your firewall rules enabled, you will need to obtain the following three things
from your Cisco Meraki account:

Base URL

API Key

Organization Name

Network Name

Obtaining Organization Name, Network Name, and API Key

To obtain the organization name, network name, and API key:

1. Access the Cisco Meraki Dashboard   as a user with administrative privileges.

2. Select your Organization from the navigation menu on the left side of the dashboard.

Then select Organization>Settings, below that.

3. When the right pane refreshes to display the Settings, make note of Organization

Name located at the top of the pane.

4. Next, scroll down the page to API Access and ensure the corresponding checkbox is

enabled.

5. From the top right of the page, click your user name and then select My Profile.

6. When your account details display, scroll to the API Access block and click, the button

to Generate a new API key.

7. Make note of that key as you will not be able to view it later, then check the note box

and click Done.

8. Now, use the navigation pane to display your organization's networks. You will need
either the Name or Template Name of each network for which you want to create a
connector:

If the network is NOT bound to any template, use the Network Name when
you add the connector in Stellar Cyber.

If the network IS bound to a template, use the Template Name when you add
the connector in Stellar Cyber.

As described below, using the correct type of name for your configuration ensures that
Block IP and Revert actions work correctly.

If you want to use more than one network, you can create multiple connector instances
with one for each network or template name.

After you obtain this information, you can proceed to configuring the connector in Stellar Cyber.
Based on the examples above, you should now have:

API Key: 5b2efd9fee131d2b9810caf5423f1c17a61751be

Organization Name: Test Lab

Network Name: Stellar-Meraki-MX64

Obtaining Base URL

The default Base URL is https://api.meraki.com/api/v1, which is for most regions, such as US
and Europe.

For organizations hosted in other countries, enter the following:

For Canada, https://api.meraki.ca/api/v1

For China, use https://api.meraki.cn/api/v1

For India, use https://api.meraki.in/api/v1

For US Government, use https://api.gov-meraki.com/api/v1

Refer to the Cisco Meraki documentation for the Cisco Meraki Dashboard API  or the Base
URI .

Adding the Connector in Stellar Cyber
To add a new Meraki firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Cisco Meraki Firewall from the Type dropdown.

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

11. Enter the Base URL for your region that you noted above in Enabling API Access.

12. Enter the API Key to access the firewall that you noted above in Enabling API Access.

13. Enter the Organization Name you noted above.

14. Enter the Network Name or Template Name you noted above.

 You can specify either a network name or a template name. Keep in mind that if the
network is bound to a template, you must use the template name in order for the
Block IP and Revert actions to work correctly. The Test button still works correctly
if you use the network name for a network that is bound to a template, but the
actions only work correctly if you use the template name. This is summarized in the
table below.

Meraki

Firewall Na

me

Configuratio

n

Added in

Stellar

Cyber

Using...

Supported Operations

Network

Network

Test button, Block IP, and Revert actions all work correctly.

Name, no

Name

template

Network

Template

Test button, Block IP, and Revert actions all work correctly.

Name, bound

Name

to template

Network

Network

Test button works but Block IP does not work correctly. Fails with error message similar

Name, bound

Name

to the following: "{"errors":["Cannot override L3 firewall rules on a

Meraki

Firewall Na

me

Configuratio

n

Added in

Stellar

Cyber

Using...

Supported Operations

to template

network bound to a template - the firewall rules are inherited from the

template"]}."

15. Click Next. The final confirmation tab appears.

16. Click Submit.

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

