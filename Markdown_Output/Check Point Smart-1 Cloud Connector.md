Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Check Point Smart-1 Cloud
Connectors

You can connect Stellar Cyber to the Check Point Smart-1 Cloud firewall so that you can quickly
and easily implement firewall rules from within Stellar Cyber, while you are threat hunting. You
can configure firewall actions or manually trigger a firewall action from the event display.

This responder supports blocking/unblocking IP addresses across gateways managed by Check
Point Smart-1 Cloud by manipulating host objects and groups referenced in firewall access
policies.

Connector Overview: Check Point Smart-1 Cloud

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: N/A

Collected Data

N/A

Domain

<Base URL>

where <Base URL> is a variable from the configuration of this connector

Response Actions

Action

Block IP/Unblock IP

Required Fields

srcip or dstip

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Base URL, Cloud Management ID, API Key, Source IP Group Name, Destination IP Group
Name, and Policy Package Name

Adding a Check Point Smart-1 Cloud Connector
To add a Check Point Smart-1 Cloud firewall connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector

Obtaining Check Point Smart-1 Cloud Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Check Point
Smart-1 Cloud firewall credentials:

Base URL—The Smart-1 Cloud Management API host URL used for API access. See
Obtaining Base URL.

(Optional) Port—The HTTPS port number for the Check Point Management API. The
default is 443.

Cloud Management ID—The unique identifier for your cloud-hosted security
management instance. See Obtaining Cloud Management ID.

API Key—The authentication credentials. See Generating the API Key.

Source IP Group Name—The name of the existing group used as the source address
group in the access policy rule. See Obtaining Source IP Group Name.

Destination IP Group Name—The name of the existing group used as the destination
address group in the access policy rule. See Obtaining Destination IP Group Name.

Policy Package Name—The name of the policy package that contains the access layer
and access rules referencing the source or destination IP groups. See Obtaining Policy
Package Name.

Prerequisites

Make sure that the source/destination IP group exists in the Check Point Smart-1 Cloud and is
referenced by blocking rules in the access rulebase.

Make sure that the policy package exists, and there are access rules inside the policy package's
access layer that reference the source/destination IP group.

Stellar Cyber will check if the group or policy exists, but will not create one if it is not found.

Obtaining Base URL

Follow the guidance in the Check Point Management & Smart-1 Cloud Administration Guide
under Using the Settings. See To use the Management API settings .

To get started, in the Web SmartConsole navigate to Settings > API & SmartConsole.

In the Management API section, copy the Web request structure.

In the following example:

https://<MAAS-HOST>/<DOMAIN-UID>/web_api

enter the full URL, including https://.

This value is the Base URL used by the connector.

Obtaining Cloud Management ID

To get started, in the Web SmartConsole navigate to Settings > API & SmartConsole.

Copy the value shown in the API URL path after the host and before /web_api.

In the following example:

https://<MAAS-HOST>/<DOMAIN-UID>/web_api

enter only:

<DOMAIN-UID>

This value is the Cloud Management ID used by the connector.

Generating the API Key

Follow the guidance in the Check Point Management & Smart-1 Cloud Administration Guide
under Best Practices. See Step 1 - Generate an API Key .

To get started, in the Web SmartConsole navigate to Settings > API & SmartConsole.

In the Management API section, click Generate.

Obtaining Source IP Group Name

Follow the guidance in the R81 Quantum Security Management Administration Guide under
Creating an Access Control Policy. See the Source and Destination Columns  of the Access
Control Policy Rule Base.

Find the access rule used for blocking source IP addresses. Copy the group object name shown
in the Source column.

Obtaining Destination IP Group Name

Follow the guidance in the R81 Quantum Security Management Administration Guide under
Creating an Access Control Policy. See the Source and Destination Columns  of the Access
Control Policy Rule Base.

Find the access rule used for blocking destination IP addresses. Copy the group object name
shown in the Destination column.

Obtaining Policy Package Name

Follow the guidance in the R81 Quantum Security Management Administration Guide under
Managing Policies. See Working with Policy Packages .

To get started, in the Web SmartConsole navigate to Menu > Manage policies and layers.

Find the policy package that contains the relevant Access Control policy type and access rules,
then copy the policy package name.

Adding the Connector in Stellar Cyber
To add a Check Point Smart-1 Cloud firewall connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Firewall from the Category dropdown.

5. Choose Check Point Smart-1 Cloud from the Type dropdown.

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

11. Enter the Base URL you noted above in Obtaining Check Point Smart-1 Cloud

Credentials.

12. (Optional) Enter the Port. The default is 443.

13. Enter the Cloud Management ID you noted above.

14. Enter the API Key you noted above.

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

 In addition to testing for connectivity, the Test button for the Check Point Smart-1 Cloud
connector tests whether the login succeeds with the provided API Key and Base URL,
whether the Source/Destination IP Group Name exists, whether the Policy Package Name
exists, whether the Policy Package's access layers include rules that use the Source IP
Group Name as the source address and the Destination IP Group Name as the destination
address.

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

