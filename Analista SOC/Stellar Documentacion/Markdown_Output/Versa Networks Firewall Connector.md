Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Versa Networks Firewall
Connectors



This is a Beta feature in this release.

You can connect Stellar Cyber to firewalls so that you can quickly and easily implement firewall
rules on those firewalls from within Stellar Cyber, while you are threat hunting. You can configure
firewall actions or manually trigger a firewall action from the event display.

Connector Overview: Versa Networks Firewall

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP

Interval: N/A

Collected Data

N/A

Domain

<Base URL> and <Versa Director URL>

where <Base URL> and <Versa Director URL> are variables from the configuration of this
connector

Response Actions

Action

Block IP/Unblock IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Versa Base URL, Versa Username, Versa Password, Versa Client ID, Versa Director URL, Versa
Tenant Name, Versa Organization Name, Versa Template Name, Versa Device UUID, Versa
Appliance Name, Versa Source IP Group, and Versa Destination IP Group

Adding a Versa Networks Firewall Connector
To add a Versa Networks firewall connector:

1. Obtain Versa Networks firewall credentials
2. Add the connector in Stellar Cyber
3. Test the connector

Obtaining Versa Networks Firewall Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Versa
Networks firewall credentials:

Versa Base URL—URL for Versa Concerto, which is the same URL used to access the
Versa Concerto user interface.

Versa Username and Versa Password—Username and password for Versa Concerto.

Versa Client ID—Client ID for Versa Concerto.

Versa Director URL—URL for Versa Director, which is the same URL used to access
the Versa Director user interface, for example, https://www.example.com:9183.

Versa Tenant Name—Versa Concerto tenant name in which the IP address will be
blocked.

Versa Organization Name—Versa Director organization name that will be used to
create/update/get an address group to block an IP address. You can locate it in the
Versa Director user interface under Administration > Organizations.

Versa Template Name—Template for Versa Director. You can locate it in the
Configuration > Templates page of the Versa Director user interface.

Versa Device UUID—ID of the firewall device. See the procedure in Locating the Device
UUID.

Versa Appliance Name—Firewall appliance name. You can locate it in the Versa
Director user interface under Configuration > Devices.

Versa Source IP Group and Versa Destination IP Group—Address groups used to help
block or unblock IP addresses. You can locate them in the Versa Director user interface
under Configuration > Templates > <click on corresponding template name> Objects
and Connectors > Objects > Address Groups.

Locating the Device UUID

To locate the device UUID:

1. Log in to Versa Concerto.

2. Select Deploy and then select Inspect.

3. Copy the Payload for publish.

Adding the Connector in Stellar Cyber
To add a new Versa Networks firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Versa Networks Firewall from the Type dropdown.

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

11. Enter the Versa Base URL you noted above in Obtaining Versa Networks Firewall

Credentials.

12. Enter the Versa Username you noted above.

13. Enter the Versa Password you noted above.

14. Enter the Versa Client ID you noted above.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Enter the Versa Director URL you noted above.

17. Enter the Versa Tenant Name you noted above.

18. Enter the Versa Organization Name you noted above.

19. Enter the Versa Template Name you noted above.

20. Enter the Versa Device UUID you noted above.

21. Enter the Versa Appliance Name you noted above.

22. Enter the Versa Source IP Group you noted above.

23. Enter the Versa Destination IP Group you noted above.

24. Click Next. The final confirmation tab appears.

25. Click Submit.

The new firewall connector is immediately active.

Testing the Connector

 The Test button for the Versa Networks Firewall connector verifies login and Versa Source
IP Group/Versa Destination IP Group information. The Test button does not verify other
fields, for example, Versa Tenant Name, Versa Device UUID, or Versa Appliance Name.
However, if those fields are invalid, actions such as Block IP will fail.

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

