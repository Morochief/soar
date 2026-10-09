✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Azure NSG Connectors
You can connect Stellar Cyber to the Azure Network Security Group (NSG) firewall so that you
can quickly and easily implement firewall rules from within Stellar Cyber, while you are threat
hunting. You can configure firewall actions or manually trigger a firewall action from the event
display.
Connector Overview: Azure NSG
Capabilities
Collect: No
Respond: Yes
Native Alerts Mapped: No
Runs on: DP
Interval: N/A
Collected Data
N/A
Domain
<Auth URL> and <Base URL>
where <Auth URL> and <Base URL> are variables from the configuration of this connector
Response Actions
Action Required Fields
Block IP/Unblock IP srcip or dstip
Third Party Native Alert Integration Details
N/A
Required Credentials and Configurations

Auth URL, Base URL, Tenant ID, Client ID, Client Secret, Subscription ID, Resource Group
Name, and Network Security Group Name
Adding an Azure NSG Connector
To add an Azure NSG firewall connector:
1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
Obtaining Azure NSG Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Azure NSG
firewall credentials:
Auth URL—The authentication URL for API access. The default is
https://login.microsoftonline.com.
Base URL—The base URL for API access. The default is
https://management.azure.com.
Tenant ID—The tenant from which to request permission, also known as the Directory
ID.
Client ID—The client ID, also known as the Application ID that the app registration
portal assigned when the app was registered.
Client Secret—The password that you generated for your app in the app registration
portal, also known as the API Access Key.
Subscription ID—The credentials that uniquely identify the Microsoft Azure subscription.
Resource Group Name—The name of the resource group that contains the network
security group. The resource group must exist.
Network Security Group Name—The name of the network security group. The NSG
must exist in the resource group.
Prerequisites
Create a network security group under a resource group. Follow the guidance in the Microsoft
documentation to:
Create an Azure resource group 
Create an Azure network security group 
Registering an Application
Follow the guidance in the Microsoft documentation to register an application .
1. With an administrative account, sign in to the Microsoft Entra admin center.
2. In the navigation pane, select App registrations. A pane for adding and managing App
registrations is displayed.

3. Click New registration. A pane is opened for your new parameters.
4. Enter a display Name for your application.
5. Choose a supported account type. Accounts in this organizational directory only is
typical.
6. The Redirect URI setting is not required.
7. Click Register. The initial app registration is completed and a summary of it is
displayed.
8. Copy the following details to a file:
Display Name
Application (client) ID, which is the Client ID you will use to add the
connector in Stellar Cyber
Directory (tenant) ID, which is the Tenant ID you will use to add the
connector in Stellar Cyber
 There is no need to grant API permissions for the app.
9. To add a client secret to the application, select Certificates & secrets and New client
secret.

10. Add a Description and select an expiry.
11. Click Add. The client secret is displayed in the Client secrets list.
12. Copy the Value. This is the Client Secret you will use to add the connector in Stellar
Cyber.
Assigning a Role to the NSG
To assign the Network Contributor role to the registered app in the Network Security Group:
1. Navigate to Network security groups and locate your existing NSG.
2. Click Access control (IAM).
3. Click Add and select Add role assignment.
4. In the Add role assignment page, click the Role tab.
5. Enter Network and select Network Contributor.
6. Click Next.
7. In the Members tab, click Select members.
8. In the Select members page, select the previously registered app and click Select. It
appears in the Add role assignment page.

9. Click Review + assign.
10. To verify, click Access control (IAM).
11. Click View.
12. Click the Role assignments tab.
13. You can use the search box to locate the member and view the assigned role.
Locating the Subscription ID
To locate the Subscription ID:
1. Navigate to Subscriptions.
2. View the Subscription name and Subscription ID.
Adding the Connector in Stellar Cyber
To add a new Azure NSG firewall connector in Stellar Cyber:
1. Log in to Stellar Cyber.
2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.
The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.
4. Choose Firewall from the Category dropdown.
5. Choose Azure NSG (Network Security Group) from the Type dropdown.
The asterisk (*) indicates a required field.
6. For this connector, the supported Function is Respond, which is enabled already.
7. Enter a Name.
 Notes:
This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.
8. Choose a Tenant Name. The Interflow records created by this connector include this
tenant name.
9. Choose the device on which to run the connector.
10. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.
11. Enter the Auth URL you noted above in Obtaining Azure NSG Credentials.
12. Enter the Base URL you noted above.
13. Enter the Tenant ID you noted above.
14. Enter the Client ID you noted above.
15. Enter the Client Secret you noted above.
16. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL
certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.
17. Enter the Subscription ID you noted above.
18. Enter the Resource Group Name you noted above.
19. Enter the Network Security Group Name you noted above.
20. Select a Region from the drop-down.
21. Click Next. The final confirmation tab appears.
22. Click Submit.
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
using the X button. If the test fails, you can select the  button from the same row to review and
correct issues.
 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.
Repeat the test as needed.
Display sample messages...
Success ! Failure with summary of issue:
Show More example detail:
If the test fails, the common HTTP status error codes are as follows:
HTTP E HTTP Stan
rror dard Error Explanation Recommendation
Code Name
400 Bad This error occurs when there is an error in the
Did you configure the connector correctly?
Request connector configuration.
401 Unauthorize
This error occurs when an authentication credential is Did you enter your credentials correctly?
d
invalid or when a user does not have sufficient
Are your credentials expired?
privileges to access a specific API.
Are your credentials entitled or licensed for that
specific resource?
403 Forbidden This error occurs when the permission or scope is not
Did you enter your credentials correctly?
correct in a valid credential.
Do you have the required role or permissions for
that credential?
404 Not Found This error occurs when a URL path does not resolve Did you enter your API URL correctly?
to an entity.
429 Too Many
This error occurs when the API server receives too The server or user license/quota will eventually
Requests
much traffic or if a user’s license or entitlement quota recover. The connector will periodically retry the

HTTP E HTTP Stan
| rror dard Error | Explanation | Recommendation |
| --------------- | ----------- | -------------- |
Code Name
|     | is exceeded. | query. |
| --- | ------------ | ------ |
If this occurs unexpectedly or too often, work with
your API provider to investigate the server limits,
user licensing, or quotas.
For a full list of codes, refer to HTTP response status codes .
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        