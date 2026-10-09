✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Microsoft Entra ID (formerly Azure
Active Directory) Connectors
This connector allows Stellar Cyber to collect data from external sources and add the records to
the data lake and, optionally, to issue response actions.
Microsoft Entra ID (formerly Azure Active Directory) integration with Stellar Cyber provides
advanced identity and access management capabilities, enabling organizations to manage user
access and security policies across their network, and providing enhanced security controls and
compliance features.
The user information from Microsoft Entra ID (formerly Azure AD) enriches event Interflow
records and provides user profile details for User Behavior Analytics. You can also disable (and
re-enable) users for applicable events, confirm a compromised user, dismiss the risk of a user,
remove a user from a group, and revoke sign-in sessions.
If you have more than one Microsoft Entra ID, you must create one connector for each of them.
 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.
Connector Overview: Microsoft Entra ID
Capabilities
Collect: Yes
Respond: Yes
Native Alerts Mapped: Yes
Runs on: DP
Interval: Configurable
Collected Data

Content Type Index Locating Records
Windows Events
Audit Log Collection msg_class
:
Sign-in Logs Collection
azure_ad
Risk Detection Collection
_audit
Risky User Collection
azure_ad
User Profile _signin
Service Principal Sign-in Logs Collection azure_ad
_risk_de
tection
azure_ad
_risky_u
ser
user_pro
file
azure_ad
_service
_princip
al_sign_
in
msg_origi
n.source:
azure_ad
msg_origi
n.vendor:
azure_ad
msg_origi
n.category
:
iam
Domain
https://graph.microsoft.com/
Response Actions
Action Required Fields
Disable User
userPrincipalName
 The Disable User action requires
User.EnableDisableAccount.All and
User.ReadWrite.All permissions.
Confirm Compromised The conditions for creating the Confirm
Compromised and Dismiss Risk actions are as
follows:

Action Required Fields
msg_class of Content Type User ID on Which
to Perform Action
azure_ad_audit initiatedBy.use
r.id
azure_ad_signin userId
Dismiss Risk
azure_ad_risk_detection userId
azure_ad_risky_user azure_ad.id
user_profile user_profile.id
 The Confirm Compromised and Dismiss Risk
actions use the riskyUsers API, which requires
an Microsoft Entra ID P2 license and
IdentityRiskyUser.ReadWrite.All permissions.
Revoke Existing Sign-In Sessions
userPrincipalName
 The Revoke Existing Sign-In Sessions action
requires User.RevokeSessions.All permission.
user_id and group_id
Remove User from Group
 The Remove User from Group action requires
GroupMember.ReadWrite.All permission.
user_id and group_id
Add User to Group
 The Add User to Group action requires
GroupMember.ReadWrite.All permission.
There are two other ways to disable the Microsoft Entra ID user:
Navigate to Automation | Action History and choose the User Actions tab. See Create a
Disable User Action.
Navigate to Assets | User Behavior Analytics and choose the Users tab. See Disable a User
Action.
Third Party Native Alert Integration Details
This connector can ingest several log types, but only Risk Detection logs are relevant to alert mapping.
Select the Risk Detection Collection content type.
Deduplication is by tenantid, riskEventType, riskLevel, userDisplayName, and ipAddress.
For details, see Integration of Third Party Native Alerts.
For full alert integration of Microsoft Entra ID, the following license is required:
Microsoft Entra ID P2 (some non-premium detections do not require P2)
 The integration does not include alerts of "riskEventType": "generic".
Required Credentials and Configurations
Application (client) ID, Directory (tenant) ID, Secret Key (password), and Microsoft Entra
ID Subscription Plan
Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Windows Events index,
use the query: msg_class: azure_ad_risk_detection AND NOT riskEventType: generic
Adding the Microsoft Entra ID Connector
To add the Microsoft Entra ID connector:
1. Register an application
2. Configure the application
3. Add the connector in Stellar Cyber
4. Test the connector
5. Verify ingestion
Registering an Application
Follow the instructions below to register an application and configure Microsoft Entra ID portal.
During the process, make note of the following values for use when you create the connector
later:
Application (client) ID
Directory (tenant) ID
Secret Key (password)
1. With an administrative account, log in to the portal you use for Microsoft Entra ID
administration of the Microsoft subscription (tenant) in which you want to register the
Stellar Cyber application. (Example portals are: https://go.microsoft.com,
portal.azure.com, and https://admin.microsoft.com/adminportal). If your account gives
you access to more than one tenant, select your account icon and then the Microsoft
Entra ID tenant that you want.
The Dashboard appears.
2. Select Microsoft Entra ID from the left navigation pane.
3. In the navigation pane, select App registrations. A pane for adding and managing App
registrations is displayed.
4. Click New registration. A pane is opened for your new parameters.

5. Enter a Name.
6. Choose a supported account type. Accounts in this organizational directory only is
typical.
7. The Redirect URI setting is not required.
8. Click Register. The registration is created and a summary of it is displayed.
9. Copy the following details to a file:
Display Name
Application (client) ID
Directory (tenant) ID
You are now ready to configure the application.
Configuring the Application
1. To set the access to the application, under App registrations in the navigation pane
under Manage, select Manifest.
a. In the Microsoft Graph App Manifest (New), locate the field for
isFallbackPublicClient and set it to true.
b. Click Save.
2. To create your secret key, in the navigation pane under Manage, select Certificates
& secrets.
a. Click New client secret. The Add a client secret pane is displayed.
b. Enter a Description.
c. Choose an expiration.

d. Click Add. The secret key is created and is now displayed in the Client
secrets list.
e. Copy the Value. This is the Password you will use to add the connector in
Stellar Cyber.
3. To set the permissions for your application, in the navigation pane under Manage,
select API Permissions. The API permissions pane appears.
a. Click Add a permission. The Request API permissions pane appears.
b. Click Microsoft Graph. The pane updates to offer Delegated permissions or
Application permissions.
c. Click Application permissions.
The pane updates to display options for setting permissions.
d. Set the following permissions for the logs you want to collect.

Logs API Permission License Required
Audit AuditLog.Read.All Microsoft Entra ID Free
Sign in AuditLog.Read.All Microsoft Entra ID P1 or P2
Directory.Read.All
Risk detection security reports IdentityRiskEvent.Read.All Microsoft Entra ID P1 or P2
Risky user security reports IdentityRiskyUser.Read.All Microsoft Entra ID P2
User profile User.Read.All None
Service principal sign-in AuditLog.Read.All Microsoft Entra ID P1 or P2
Directory.Read.All
e. Click Add permissions. The API permissions page redisplays with your
added permissions.
f. If you are the super admin, grant the permissions. Select the checkmark to
Grant admin consent for <account name>.
Otherwise, wait for the super admin to grant them.
 Make sure that the permissions are granted. If you add the connector
before permissions are granted, the process fails.
When the permissions are granted successfully, there will be a green
checkmark in the Status column.
4. If your connector will be used for respond actions, the API must also be configured with
application permissions. From the API Permissions pane, click Add a permission
again.
a. In the Request API permissions pane, click Microsoft Graph.
b. Click Application permissions.
c. For the Disable User response action, enable
User.EnableDisableAccount.All and User.ReadWrite.All.
For the Confirm Compromised and Dismiss Risk response actions, enable
IdentityRiskyUser.ReadWrite.All.

For the Revoke Existing Sign-In Sessions action, enable
User.RevokeSessions.All.
For the Remove User from Group action, enable
GroupMember.ReadWrite.All.
For the Add User to Group action, enable GroupMember.ReadWrite.All.
d. Click Add permissions. The API permissions page re-displays with your
added permissions.
 The permissions can take up to two hours to propagate to historical data. We suggest you
add the permissions at least two hours prior to adding the connector in Stellar Cyber, as
Stellar Cyber will try to pull historical logs when first configured.
Adding the Connector in Stellar Cyber
With the application registered, permissions granted, and the access information handy, you can
add the Microsoft Entra ID connector in Stellar Cyber:
1. Log in to Stellar Cyber.
2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.
3. Click Create and select Connector.
The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.
4. Choose SaaS from the Category dropdown.
5. Choose Microsoft Entra ID (formerly Azure Active Directory) from the Type
dropdown.
The asterisk (*) indicates a required field.

6. For Function, enable the Collect checkbox. If you would like to issue response actions,
also enable Respond.
7. Enter a Name.
 Notes:
This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.
8. Choose a Tenant Name. The Interflow records created by this connector include this
tenant name.
9. Choose the device on which to run the connector.
10. (Optional) When the Function is Collect, you can apply Log Filters. For information,
see Managing Log Filters.
11. Click Next. The Configuration tab appears.
The asterisk (*) indicates a required field.
12. Enter the Application ID you noted above.
13. Enter the Directory ID you noted above.
14. Enter the Password you noted above.
15. Select the applicable Microsoft Entra ID Subscription Plan from the menu:
Enterprise Plan
GCC Government Plan
GCC High Government Plan
DoD Government Plan
To learn about Microsoft Entra ID government plans, refer to the following Microsoft
documentation: https://learn.microsoft.com/en-us/azure/security/fundamentals/feature-
availability .
 The Government Plans do not support the Sign-in Logs content type.
16. Choose the Interval (min). This is how often the logs are collected.
17. Choose the logs you want to collect. These must match the permissions you set in
Microsoft Entra ID. None are collected by default, so you must select at least one log.
Note the following:

| Log | Required License | Required Permissions |     |
| --- | ---------------- | -------------------- | --- |
Alert Integration
| Audit Log | Microsoft Entra ID Free | AuditLog.Read.All | No  |
| --------- | ----------------------- | ----------------- | --- |
Sign-in Logs Microsoft Entra ID P1 or P2 AuditLog.Read.All No
Directory.Read.All
Risk Detection Microsoft Entra ID P1 or P2 Identity.RiskEvent.Read.All Mapped to Stellar Cyber
Alerts
Risky User Microsoft Entra ID P2 Identity.RiskyUser.Read.All Mapped to Stellar Cyber
Alerts
| User Profile | N/A | User.Read.All | No  |
| ------------ | --- | ------------- | --- |
Service Principal Microsoft Entra ID P1 or P2 AuditLog.Read.All No
| Sign-in Logs |     | Directory.Read.All |     |
| ------------ | --- | ------------------ | --- |

When the new connector is first active, it will collect logs for the content types as
follows:
| Log          |     | Log Collection for First Data Pull |     |
| ------------ | --- | ---------------------------------- | --- |
| Audit Log    |     | 1 hour                             |     |
| Sign-in Logs |     | 1 hour                             |     |
Risk Detection
15 days
| Risky User |     | 15 days |     |
| ---------- | --- | ------- | --- |
User Profile
from the beginning
Service Principal Sign-in Logs
1 hour
18. (Optional) Stellar Cyber allows you to customize the scope of the request the collector
should request for the selected log type. For example, specifying 60 minutes specifies
that when the collector requests data, the request should delay completion until a full 60
minutes of data has been collected. To override the default delays, check the box at the
top of the page for Advanced Settings. Any of the logs you selected now display a
configurable delay field.
19. Click Next. The final confirmation tab appears.

20. Click Submit.
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
is exceeded. query.
If this occurs unexpectedly or too often, work with
your API provider to investigate the server limits,
user licensing, or quotas.
For a full list of codes, refer to HTTP response status codes .
Verifying Ingestion
To verify ingestion:
1. Select Threat Hunting.
The Interflow Search tab appears.
2. Change the Indices to Windows Events.
The table immediately updates to show ingested Interflow records.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  