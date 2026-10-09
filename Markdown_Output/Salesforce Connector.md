Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Salesforce Connectors

Salesforce connectors allow Stellar Cyber to ingest Salesforce logs and add them to the data
lake. There can be any number of Salesforce connectors active.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Salesforce

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Login History

Setup Audit Trail

User Cache (not configurable in the
user interface)

Index

Syslog

Locating Records

msg_class:

salesforce_LoginHi
story

salesforce_SetupAu
ditTrail

msg_origin.source:

salesforce

msg_origin.vendor:

salesforce

msg_origin.category:

Content Type

Index

Locating Records

saas

Domain

https://<Hostname>:<Port>

where <Hostname> and <Port> are variables from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

For Client ID / Client Secret Auth Method: Token Endpoint URL, Username, Password, Client ID,
Client Secret, and Security Token

For Certificate Auth Method: Token Endpoint URL, Certificate, Consumer Key, and JWT User

Adding a Salesforce Connector

Salesforce Lightning View

To add a Salesforce connector in the Lightning view, follow the instructions in Lightning
View: Building a Connected App and then:

1. Add the connector in Stellar Cyber
2. Test the connector
3. Verify ingestion

Salesforce Classic View

To add a Salesforce connector in the Classic view, follow the instructions in Classic
View: Building a Connected App and then:

1. Add the connector in Stellar Cyber
2. Test the connector
3. Verify ingestion

Lightning View: Building a Connected App

 The following steps are based on the Lightning view of the salesforce.com console, not the
Classic view. See Classic View: Building a Connected App if you are using the Classic
view.

You will need to collect the following salesforce.com information:

User login name and password, and the Security Token for that user

 The password should not include non-ASCII special characters.

Client ID (for OAuth2) or Consumer Key

Client Secret (for OAuth2) or Consumer Secret

Redirect URL (for
example: https://login.salesforce.com/services/oauth2/token)

If you need to reset your Security Token, refer to the following
article: https://salesforce.stackexchange.com/questions/321186/how-to-reset-security-token-of-
api-only-user .

To add a Salesforce connector in the Lightning view:

1. Create a connected app
2. Add a profile
3. Add a user
4. Use a Certificate Authentication Method (Optional)

Creating a Connected App

To create a connected app:

1. Navigate to PLATFORM TOOLS | External Client Apps | Settings.

 Type External Client Apps in the Quick Find box if you are having trouble finding

these options.

2. Enable the Allow creation of connected apps option and click the New Connected

App button.

3. Under Basic Information, enter a Connected App Name, an API Name, and a

Contact Email.

4. Under API (Enable OAuth Settings), set the following options:

Check the Enable OAuth Settings box.

Supply the following Callback URL:

https://login.salesforce.com/services/oath2/token

Check the Use digital signatures box.

5. Scroll down to Selected OAuth Scopes. Use the Add and Remove arrows to move

Available and Selected OAuth Scopes. Choose the following:

Access Lightning applications (lightning)

Manager user data via APIs (api)

Perform requests at any time (refresh_token, offline_access).

6. Enable the following checkboxes:

Require Secret for Web Server Flow

Require Secret for Refresh Token

Enable Client Credentials Flow

Here's how things look so far:

7. Scroll down and click Save. Changes can take up to 10 minutes to take effect.

8. Click Continue.

9. Under API (Enable OAuth Settings), for Consumer Key and Secret, click Manage

Consumer Details.

10. Click the Copy buttons to copy and save the Consumer Key and Consumer Secret.

You need these for the Stellar Cyber connector configuration,

11. Under PLATFORM TOOLS, navigate to Apps > Connected Apps > Manage

Connected Apps and click Edit for your app.

12. Under OAuth Policies, for Permitted Users, choose Admin approved users are pre-

authorized.

13. Scroll down and click Save.

Adding a Profile

To add a profile:

1. Under ADMINISTRATION, navigate to Users | Profiles and click New Profile.

2. Select Analytics Cloud Integration User as an Existing Profile to clone from, enter a

new Profile Name, and click Save.

3. In the new profile, under Profile Detail, click Assigned Connected Apps.

4. Click Edit.

5. Under Connected App Access, add the connected app you created in Creating a

Connected App.

6. Click Save.

Adding a User

To add a user:

1. Under ADMINISTRATION, navigate to Users |  Users, click New User, and click Edit.

2. Add general information for the user.

3. For the User License, choose Analytics Cloud Integration User.

4. For Profile, choose the profile you created in Adding a Profile.

5. Click Save.

Using a Certificate Authentication Method (Optional)

Before adding the connector in Stellar Cyber, note that there are two authentication methods.
The first uses Client ID / Client Secret. The second uses a certificate.

For the certificate authentication method, generate the certificate in Salesforce and upload it to
the Stellar Cyber platform.

To generate the certificate in Salesforce, there are two options for the certificate and private key,
self signed or public signed. The private key (.key) is used to sign the JWT claim generated by
your code. The certificate (.crt) is uploaded to Salesforce to validate your signed JWT assertions.

Self-Signed Certificate

For a self signed certificate, create an RSA x509 private key/certification pair, as follows:

openssl req -x509 -sha256 -nodes -days 36500 -newkey rsa:2048 -keyout
salesforce.key -out salesforce.crt

Public-Signed Certificate

For a public-signed certificate, you give the public CA signed certificate and private key to Stellar
Cyber.

For either the self signed or public signed certificate, upload the certificate when you create the
Manage Connected App. In the previous procedure, Adding a Connected App, make sure to
select Use digital signatures under API (Enable OAuth Settings).

When you have the certificate, upload it to the Stellar Cyber platform on the System | Saved
Objects | Certificates page by clicking Upload. Refer to Managing Certificates for details. When
you upload the certificate and private key, click Server Certificate.

Classic View: Building a Connected App
You must build a connected app in Salesforce. You must use v51 (or later) of the API. As you
build this app, you will need to collect the following salesforce.com information:

User login name, password, and the Security Token for that user

 The password should not include non-ASCII special characters.

Client ID (for OAuth2) or Consumer Key

Client Secret (for OAuth2) or Consumer Secret

Redirect URL (for
example, https://login.salesforce.com/services/oauth2/token)

 The following steps are based on the Classic view of the salesforce.com console, not the

Lightning view. See Using the Lightning View if you are using the Lightning view.

Verifying the User Requirements

This section verifies that the app's user permissions are sufficient, and that the user Security
Token can be obtained. These two procedures should be completed before creating the app.

User Role

This user must have a role that includes the permission for View Setup and Configuration, so
that the created app is permitted to access these needed data types:

SetupAuditTrail: discover new connections being configured or established

LoginHistory: Salesforce logins

1. Log in as an administrative user to your salesforce.com account.

2. Select the Setup menu option.

3. Access the Administer > Manage Users > Users option from the left hand navigation

pane.

4. When the user list displays, locate your username, and click the Profile description at

the far right.

5. When the profile details display, locate the block for Administrative Permissions and
ensure the check box for View Setup and Configuration is enabled. If it is not, then
edit the profile and save the changes, or change the profile to one that has this
permission enabled.

Security Token

The remaining user item is the Security Token associated with your user account.
Salesforce.com does not provide a means to display this token, which is generated and emailed
to you when you first created the account and password. If you do not know your token, and do
not have other apps tied to this account, you can reset the Security Token with the following
steps:

1. From the top banner of the salesforce.com home page, open the menu that shows your

user name, then select My Settings.

2. The left hand navigation bar updates for your Settings. Expand the section for

Personal.

3. Select the menu option to Reset My Security Token.

4. Since resetting the token invalidates any app using the previous token, a warning
displays. To confirm that you are prepared for that result, click the Reset Security
Token button. The new token is emailed to the address for the account.

5. Make note of the Security Token for use in the Stellar Cyber connector.

Creating a Connected App

1. Still logged in as the user above, click Setup to display the left hand navigation panel.

2. Select the menu option for s Build > Create > Apps.

3. The app management panel displays. Locate the section for Connected Apps and click

New.

4. Complete the fields in the Basic Information section:

Connected App Name: note this for use in Stellar Cyber

5. Check the box for API (Enable OAuth Settings), then complete the following:

Callback URL: This is used in Stellar Cyber as the Token Endpoint URL
(https://login.salesforce.com/services/oath2/token)

Selected OAuth Scopes: At a minimum, include Provide access to your
data via the Web (in later versions, this is renamed to Manage user data via
Web browsers (web)

Check the boxes for Require Secret for Web Server Flow and for Require
Secret for Refresh Token Flow

6. Your application view should look similar to the one depicted below. Click Save, then

click Continue.

7. The Connect App details screen displays, from where you can now collect the following

information:

Consumer Key (or Client key for OAuth2) This is used in Stellar Cyber as the
Client ID

Consumer Secret (or Client Secret for OAuth2) This is used in Stellar Cyber
as the Client Secret

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Salesforce connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SaaS from the Category dropdown.

5. Choose Salesforce from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name. Enter the Connected App name of the app you created.



Notes:

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

12. Enter the Token Endpoint URL you noted above.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Choose the Auth Method to use Client ID / Client Secret or Certificate.

For Client ID / Client Secret Auth Method:

a. Enter the Username of the user associated with the app you created.

b. Enter the Password for that user.

c. Enter the Client ID. This is the Consumer Key you noted above.

d. Enter the Client Secret. This is the Consumer Secret you noted above.

e. Enter the Security Token.

For Certificate Auth Method:

The asterisk (*) indicates a required field.

a. Choose the Certificate to use from the dropdown list of uploaded certificates.

b. Enter the Consumer Key you noted above.

c. Enter the JWT User.

14. Choose the Interval (min). This is how often the logs are collected.

15. Choose the Content Type you would like to collect. The logs for Login History and

Setup Audit Trail are supported.

 There is also a User Cache content type that is always on. This content type is not

configurable in the user interface.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active.

Testing the Connector

 The Test button for the Salesforce connector tests permissions as well as connectivity, such

as if an administrator account is required.

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

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Login History and Setup Audit Trail, change the Indices to Syslog.

For User Cache only, change the Indices to Sensor Monitoring.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

