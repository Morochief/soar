✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Microsoft Entra ID SSO
You can configure Stellar Cyber to use Microsoft Entra ID SSO (formerly Azure Active Directory
SSO) for Authentication or Authentication and Authorization using the procedure in this
topic. The configuration includes application creation, user and group assignments, SAML setup,
optional authorization, optional multi-factor authentication (MFA), and Stellar Cyber settings.
You must collect the following information as you progress through the procedure:
User Principal Names (email addresses for users that will log into Stellar Cyber with
SSO)
Claim/Attribute Information (Applicable for Authorization only)
Identifier (Entity ID)
Login URL
Reply URL (the Stellar Cyber callback URL to which Microsoft Entra ID sends its SAML
authentication response)
Certificate
The Microsoft Entra ID configuration steps are based on version 2.4.
Perform the following steps in the order shown below:
1. Create a Stellar Cyber Application for SSO in Microsoft Entra ID
2. Add Users/Groups to the Stellar Cyber SSO Application
3. Configure SAML-based Single Sign-On (SSO)
4. Configure Authorization (Optional)
5. Configure Multi-Factor Authentication Support (Optional)
6. Configure Authentication in Stellar Cyber
Create a Stellar Cyber Application for SSO in Microsoft
Entra ID
Sign in to the Microsoft Entra Admin Center, access Enterprise Applications, and add a new
application that uses Microsoft Entra ID for authentication.

1. Sign in to the Microsoft Entra Admin Center  with an account that has the Cloud
Application Administrator or Application Administrator role.
2. In the left-hand menu, select Identity | Applications | Enterprise applications.
3. At the top of the page, select New application.
4. In the Browse Microsoft Entra Gallery, select Create your own application.
5. Enter a name for the application (for example, Stellar Cyber SSO), select Integrate
any other application you don't find in the gallery (Non-gallery), and then Create.
Microsoft Entra ID creates the application and displays the Overview page. With your application
created, you can now add users and configure SAML.
Add Users/Groups to the Stellar Cyber SSO Application
Assign the users and groups that you want Microsoft Entra ID to authenticate to the application.
You will need to add these for the following purposes:
For Authentication Only SSO configurations: You will use these to create user
accounts in Stellar Cyber.
For Authentication and Authorization SSO configurations: You will use these to
assign values to claim attributes (not applicable for per-tenant SSO).
1. In the Getting Started section of the Stellar Cyber SSO application Overview, select
Assign users and groups.
You can also access this from Manage | Users and groups in the side menu.
2. Select Add user/group in the action menu at the top of the page.
3. In the Add Assignment panel, select None Selected under Users.

4. Select the users or groups that you want to assign, tap or select Select and then
Assign to finalize the assignments.
 For each assigned user, select its name and note the User principal name (email
address). Ensure that it exactly matches the corresponding Stellar Cyber user
email address. Usernames and email addresses in both Microsoft Entra ID and
Stellar Cyber are case sensitive.
5. You must make note of each user's User Principal Name for these reasons:
For Authentication Only SSO configurations: You will use these to create
user accounts in Stellar Cyber.
For Authentication and Authorization SSO configurations: For this type of
configuration, users are automatically added to Stellar Cyber. You will use the
User Principal Names, though to assign values to claim attributes (not
applicable for Tenant-specific SSO; Authorization configurations apply only to
Global SSO).
For users, select Display Name and copy the User Principal Name.
For groups, select Display Name and then select the Members link in the left
side of the navigation panel. This displays a list of members (users) in that
group. You can now select each user Name and copy the User Principal
Name.
Now that you have added users to the application, you can configure the SSO SAML section.
Configure SAML-based Single Sign-On (SSO)
Configure basic SAML settings, download the signing certificate, and copy URLs to use when
configuring SSO settings in the Stellar Cyber UI.
1. In the Getting Started section of the Stellar Cyber SSO application Overview, select Get
started for 2. Set up single sign-on.
 You can also access this from Manage | Single sign-on in the side menu.
2. Select the SAML option, select Edit in the 1. Basic SAML Configuration section, fill in
the required fields, and then Save the configuration.
If you are configuring SSO for the entire Stellar Cyber system:
Identifier (Entity ID): Enter the Stellar Cyber URL. For example:
https://192.168.24.110.
Reply URL: Use the Stellar Cyber URL, appended with
/saml/login/callback/org_id/<org-id>. The format is
https://<your.stellar.cyber.address>/saml/login/callback/org_id
/<org-id>, where <org-id> is the Organization ID on the license page. For
example:
https://192.168.24.110/saml/login/callback/org_id/0c5b67d2e9e54
398be1e4d1cff1edc3

Logout URL: This setting is here for future functionality but is not currently
supported.
The Reply URL in the Microsoft Entra ID UI is the URL to which Microsoft Entra ID
sends its SAML authentication response. Different identity providers use different
names for this URL as shown in the following table:
If you are configuring SSO for a tenant:
Identifier (Entity ID): Enter the Stellar Cyber URL.
Reply URL: Use the Stellar Cyber Platform URL, appended with
/saml/login/callback/org_id/<org id>/cust_id/<tenant-id>. The
format is
https://<your.stellar.cyber.address>/saml/login/callback/org_id
/<org-id>/cust_id/<tenant-id>, where <org-id> is the Organization ID
on the license page. For example:
https://192.168.24.110/saml/login/callback/org_id/0c5b67d2e9e54
398be1e4d1cff1edc3d/cust_id/59125044
Logout URL: This setting is here for future functionality but is not currently
supported.
The Reply URL in the Microsoft Entra ID UI is the URL to which Microsoft Entra ID
sends its SAML authentication response. Different identity providers use different
names for this URL as shown in the following table:
Identity Provider Term for the Assertion Consumer Service (ACS) URL
Active Directory Federation Relying party SAML 2.0 SSO service URL
Services
Microsoft Entra ID Reply URL
Okta Single sign on URL
OneLogin Assertion Consumer (ACS) URL
Rippling Assertion Consumer Service URL
Configure Authorization (Optional)
Authorization allows you to assign Stellar Cyber scopes, privileges, and tenant options within
Microsoft Entra ID, rather than within Stellar Cyber. If you want to configure Authorization in
addition to Authentication, you must add Microsoft Entra ID attributes / claims (scopes) for use in
Stellar Cyber This procedure adds the required fields to the Microsoft Entra ID users you
associated with the application.


You must configure the basic identity, above, before you perform the steps in this section. If
you are configuring Authentication only, or per-tenant SSO authentication, skip this
section.
Add Stellar Cyber Fields to User Accounts
1. In the Set up Single Sign-On with SAML section of the Stellar Cyber SSO application
configuration, select Edit in the 2 Attributes & Claims section.
2. Select Add new claim, enter the following claim settings, leave the others as they are,
and then Save the configuration.
Name: Enter stellar_scope.
Source: Attribute
Source Attribute: Choose a relevant user attribute (for example,
user.extenstionattribute1).
 You define attributes in this step; values are added in a later step.
3. Repeat the previous step to add the following attributes: stellar_privilege,
stellar_tenant, and stellar_tenant_group
 Take care when entering the required attributes and values. Typos in either mean
that users are not authenticated and cannot log in. Typos in the optional attributes
and values mean that users are not assigned to the appropriate tenant or tenant
group (but are authenticated).

|     | V   | T   |
| --- | --- | --- |
C
|     | a   | e   |
| --- | --- | --- |
u
|     | l   | n   |
| --- | --- | --- |
st
|     | u   | a   |
| --- | --- | --- |
o
|     | e   | n   |
| --- | --- | --- |
m
|     | s   | t-  |
| --- | --- | --- |
A
|     | (   | s   |
| --- | --- | --- |
tt
|                      | s          | p   |
| -------------------- | ---------- | --- |
| ri Source Attribute* | Global SSO |     |
|                      | e          | e   |
b
|     | t   | c   |
| --- | --- | --- |
u
|     | l   | if  |
| --- | --- | --- |
te
|     | a   | i   |
| --- | --- | --- |
N
|     | t   | c   |
| --- | --- | --- |
a
|     | e   | S   |
| --- | --- | --- |
m
|     | r   | S   |
| --- | --- | --- |
e
|                            | )   | O   |
| -------------------------- | --- | --- |
| s user.extensionattribute1 | r   | N   |
Required for Authorization
| t   | o   |     |
| --- | --- | --- |
ot
| e   | o   |     |
| --- | --- | --- |
a
| l   | t   | p   |
| --- | --- | --- |
l
|     | p   | pl  |
| --- | --- | --- |
| a   |     | ic  |
a
| r   |     | a   |
| --- | --- | --- |
r
_
|     | t   | bl  |
| --- | --- | --- |
| s   |     | e   |
n
c
e
o
r
p
t
e
e
n
a
n
t
s user.extensionattribute2
s Required for Authorization
t
u
e
p
l
e
l
r
a
_
r
a
_
d
p
m
r
i
i
n

v p
i l
l a
e t
g f
e o
r
m
_
a
d
m
i
n
s
e
c
u
r
i
t
y
_
a
d
m
i
n
u
s
e
r
s user.extensionattribute3 I (Optional) Specify an individual tenant ID, not name. The ID is available on
t D
the Tenants List page.
e n
l u
l m
a b
r e
_ r
t fo
e r
n c
a o
nf

n ig
t u
r
e
d
te
n
a
nt
s user.extensionattribute4 I (Optional) Specify a tenant group ID, not name. This is typically available for
t D
use by MSSP users with the Partner role. The Tenant Group ID is displayed
e n
on the Tenant Groups page.
l u
l m
a b
r e
_ r
t fo
e r
n a
a n
n y
t c
_ o
g nf
r ig
o u
u r
p e
d
te
n
a
nt
g
r
o
u
p
Any available user.extensionattributeX (where X is 1-15) may be used.

Values in these fields are case sensitive and syntax matters. Use the exact
indicated syntax and verify that you have made no typos. If you have created a
custom privilege with spaces or dashes, use an underscore instead. Example: A

custom privilege of STML-Security Admin must be entered as
STML_Security_Admin.
4. When done, exit the Attributes & Claims editor panel.
Assign Values to Stellar Cyber Fields (Graph Explorer Method)
Microsoft Entra ID does not provide a GUI-based mechanism to modify the attribute values. This
procedure uses Microsoft Graph Explorer to edit and validate the attributes. If you wish to
automate the steps, refer to the PowerShell method, below.
1. To set the attribute values, retrieve the list of User Principal Names you saved above.
2. Open Microsoft Graph and log in with your administrator Microsoft Entra IDCredentials
(https://developer.microsoft.com/en-us/graph/graph-explorer ).
3. In the query pane, change the GET action menu to PATCH.
4. Now enter this query URL, replacing the <user principal name> below with a User
Principal Name you saved earlier.
https://graph.microsoft.com/beta/users/<user principal name>
5. Enter the following content as the Request Body, replacing the attribute values with
one of the supported values in the table above:
 Take care when entering the required attributes and values. Typos in either mean
that users are not authenticated and cannot log in. Typos in the optional attributes
and values mean that users are not assigned to the appropriate Stellar Cyber
tenant or tenant group (but are authenticated).
{
"onPremisesExtensionAttributes": {
"extensionAttribute1": "root",
"extensionAttribute2": "security_admin"
}
}
6. Click Run Query to set the values.
7. To verify the values were set correctly, change the query type back to GET.
8. Now enter this query URL, replacing the <user principal name> below with the same
User Principal Name (Microsoft Entra ID login) you just set above.
https://graph.microsoft.com/beta/users/<user principal name>?
$select=onPremisesExtensionAttributes

9. Click Run Query and review the list of extensionAttributes to verify the values were set.
Assign Values to Stellar Cyber Fields (PowerShell Method)
For Authentication Only SSO: First, manually add all users on the Stellar Cyber
Platform. After this manual entry, users can log in with SSO. Use the list of User
Principal Names that you saved.
For Authentication & Authorization SSO: Configure all users through the IdP.
For Local access (bypass) when SSO is enabled: If Stellar Cyber loses connectivity
with your IdP, users configured for SSO cannot log in. As a preventive bypass method,
manually create a new user in the Stellar Cyber Platform with root scope and with a
valid email address that has "+admin" appended to a valid user name, as follows:
<user>+admin@yourorganization.com (joe+admin@yourorganization.com). The
user you create must be able to receive a password reset email at
<user>@yourorganization.com. This email alias is what Stellar Cyber uses to permit
the bypass of an SSO for a local login. After you create this separate user account, the
user can log in two ways:
An SSO user with <user>@yourorganization.com
or
A local user at https://your.stellar.cyber.address/login using
<user>+admin@yourorganization.com
 If SSO is configured, it's recommended to keep an active administrative account in
the Stellar Cyber user management.
As an alternative to the Microsoft Graph Explorer method, you can use PowerShell to set the
attribute values. The commands in this section can also be automated in PowerShell.
1. Open PowerShell from your Windows system as an administrative user.
2. From the PowerShell command line, run the bolded commands and replace $User
value with the login you used above. The last two lines illustrate assigning values to the
stellar_scope and stellar_privilege attributes. If you used all four attributes, add
commands for those and specify the Tenant ID and Tenant Group ID exactly as they are
listed in Stellar Cyber.
 Be sure that you assign the correct value to the correct extension number. In this
example extensionAttribute1 is for stellar_scope, which is being given root;
extensionAttribute2 is for stellar_privilege and is being assigned security_admin.
Review your list of extension attributes carefully before running these commands.

PS C:\WINDOWS\system32> Install-Module AzureAD
Untrusted repository
You are installing the modules from an untrusted repository. If you trust
this repository, change its
InstallationPolicy value by running the Set-PSRepository cmdlet. Are you sure
you want to install the modules from
'PSGallery'?
[Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help
(default is "N"): Y
PS C:\WINDOWS\system32> $AzureAdCred = Get-Credential
Enter your Azure admin user and password
PS C:\WINDOWS\system32> Connect-AzureAD -Credential $AzureAdCred
PS C:\WINDOWS\system32> $User = "dstarr@aella.onmicrosoft.com"
PS C:\WINDOWS\system32> $UserId = (Get-AzureADUser -Searchstring
$User).ObjectId
PS C:\WINDOWS\system32>
PS C:\WINDOWS\system32> Set-AzureADUserExtension -ObjectID $UserId -
ExtensionName extensionAttribute1 -ExtensionValue "root"
PS C:\WINDOWS\system32> Set-AzureADUserExtension -ObjectId $UserId -
ExtensionName extensionAttribute2 -ExtensionValue "security_admin"
PS C:\WINDOWS\system32> exit
Following is an example of this sequence:
Configure Multi-Factor Authentication Support
(Optional)
Microsoft Entra ID and Stellar Cyber support multi-factor authentication (MFA). If you intend to
set up Stellar Cyber access with two-factor authentication (2FA; a subset of MFA), you must
enable a Conditional Policy in Microsoft Entra ID that supports this type of authentication and
assign it to users and groups.
 Configuration of MFA in Microsoft Entra ID is independent of whether you enable 2FA in
Stellar Cyber. It is possible for you require users to authenticate with MFA in Microsoft Entra
ID and again with 2FA in Stellar Cyber

1. In Microsoft Entra Admin Center, select Protection | Security Center | Conditional
Access.
If you don’t see Security Center in the Protection section of the menu, select Show
more.
2. Select + Create new policy and enter a name for the policy, such as Require MFA for
Stellar Cyber.
3. Under Assignments, select the Specific users included link for Users or workload
identities and then select Specific users included.
4. Select the Users and groups that you specified to be members of the Stellar Cyber
Microsoft Entra ID application created above, and then select Select.
5. Under Assignments, select the No cloud apps, actions, or authentication contexts
selected link for Cloud apps or actions.
6. Select Include | Select apps, and then select the None link to open the Select Cloud
apps panel.
7. When the selection pane opens, locate the Stellar Cyber Microsoft Entra ID application
you created above and then select Select.
8. In the Grant section, select 0 controls selected.
9. In the side panel that opens, select Grant access, select Require multi-factor
authentication, and then select Select.
10. At the bottom of the page, change the Enable policy toggle from Report-only to On.
11. Select Create.
The policy is created and the Conditional Access Policy page is redisplayed to
include the new policy.

Collect Microsoft Entra ID Access Details
At this stage, you should have collected all your user information and have set up the Microsoft
Entra ID application for Stellar Cyber SSO access. Your certificate and access details are now
ready to copy/download. Use this procedure to ensure you have all the noted information before
you proceed to the next section.
 If you are configuring Authorization, you must perform that procedure (see previous
section) prior to downloading the certificate in this section.
1. If you have navigated away from the application page, select Home on the portal and
navigate back Identity | Applications | Enterprise applications.
2. Locate and display the application you created above.
3. Select Single sign-on from the left side navigation or select Get started for 2. Set up
single sign on.
4. On the Set up Single Sign-On with SAML page, download or copy (as appropriate)
the items below for use when you set up SSO in Stellar Cyber:
Step 1: Basic SAML Configuration
Identifier (Entity ID) – The Stellar Cyber URL. Microsoft Entra ID uses this to
recognize and establish a trust relationship with Stellar Cyber as a service
provider (SP).
Step 2: Attributes & Claims (Applicable only if you configured Authorization)
User.extensionattributeX values for all the Stellar Cyber claim names you
added
Step 3: SAML Certificates
Certificate (base 64) – You upload this as the IdP certificate in Stellar Cyber.
Step 4: Set up Stellar Cyber SSO
Login URL – This is used for the Entry Point URL field in Stellar Cyber, to link
with Microsoft Entra ID.
In addition to the above details, you should have previously noted all of the User Principal
Names (email addresses) for all users that will use Microsoft Entra ID SSO with Stellar Cyber.
Configure Authentication in Stellar Cyber
With all your details collected, you are now ready to configure SSO Authentication in Stellar
Cyber. The steps below are generally applicable for use for global configuration or per-tenant
configuration.
Prepare for Users
For Authentication Only SSO: First, manually add all users on the Stellar Cyber
Platform. After this manual entry, users can log in with SSO. Use the list of User
Principal Names that you saved.
For Authentication & Authorization SSO: Configure all users through the IdP.

For Local access (bypass) when SSO is enabled: If Stellar Cyber loses connectivity
with your IdP, users configured for SSO cannot log in. As a preventive bypass method,
manually create a new user in the Stellar Cyber Platform with root scope and with a
valid email address that has "+admin" appended to a valid user name, as follows:
<user>+admin@yourorganization.com (joe+admin@yourorganization.com). The
user you create must be able to receive a password reset email at
<user>@yourorganization.com. This email alias is what Stellar Cyber uses to permit
the bypass of an SSO for a local login. After you create this separate user account, the
user can log in two ways:
An SSO user with <user>@yourorganization.com
or
A local user at https://your.stellar.cyber.address/login using
<user>+admin@yourorganization.com
 If SSO is configured, it's recommended to keep an active administrative account in
the Stellar Cyber user management.
Enable SSO
1. Log in to Stellar Cyber and select System | ORGANIZATION MANAGEMENT |
Settings.
2. In the Authentication Settings section, select SSO (SAML) as the Authentication
Method.
3. Select Metadata URL or Manual Config:
If you select Metadata URL:
Issuer URL: If this setting is present, enter the Stellar Cyber URL.
Metadata URL: Paste the URL you copied from the IdP. The URL must begin
with either https:// or http://. Different vendors use different names for the
Metadata URL:
Identity Provider Term for Metadata URL
Active Directory Federation Services Federation Metadata URL
Microsoft Entra ID App Federation Metadata URL
Okta Metadata URL
OneLogin Issuer URL
Rippling Metadata URL
If you select Manual Config:
Issuer URL: If this setting is present, enter the Stellar Cyber URL.
Entry Point: Paste the entry point URL you copied from the IdP.
You must include http:// or https:// before the URLs. Different vendors use
different names:

Identity Provider Term for Entry Point URL
Active Directory Federation Services SAML Endpoint
Microsoft Entra ID Login URL or SAML-P Sign-on Endpoint
Okta Sign on URL
OneLogin SAML 2.0 Endpoint (HTTP)
Rippling SAML 2.0 Endpoint (HTTP)
IDP Certificate: Upload the certificate file you downloaded from the IdP.
4. Select Require Signed Response only if the IdP requires it.
 Verify whether your IdP requires signed SAML responses. Some IdPs, such as
Okta, require them by default. If so, then enable Require Signed Response here
as well.
5. Select Allow Clock Skew to allow for system time differences between Stellar Cyber
and your IdP. Authentication messages have an expiration. If the system times on
Stellar Cyber and your IdP are not synchronized, the messages might expire before
they even get to Stellar Cyber. The result is that users cannot log in, because they
cannot authenticate.
6. Choose your IdP setting: Authentication Only or Authentication and Authorization.
Note the following:

A Global selection of Authentication and Authorization applies to all
users (root, partner, and tenant), so the option to change authentication
method for a specific tenant is not applicable when the Global method is
set to Authentication and Authorization. You cannot log in to Tenant
SSO when Global SSO is set to Authentication and Authorization. If
you want to use SSO but also allow local users and tenant override, you
must set the Global authentication method either to Local or to use the
IdP with Authentication Only.
Although you can customize SSO configuration on a per-tenant basis, the
Authorization capability is only supported at the global level. Overrides
you make at the tenant level are for Authentication only, so the toggle
for Authentication and Authorization is not offered in the tenant editor.
The authentication method for partners is the same as that for root users.
Any authentication overrides for tenant-level users in a tenant group have
no effect on the authentication method for the partners who manage the
group.
Choose Authentication Only for Stellar Cyber to authenticate users from your
IdP, but manage scope and privilege locally. If you choose this, you must
create the user in Stellar Cyber before adding them to your IdP.
Choose Authentication and Authorization for Stellar Cyber to authenticate
users from your IdP, along with their scope and level of privilege. You must

configure authorization on your IdP before enabling this, otherwise users
cannot log in. If you choose this, you do not need to create the user in Stellar
Cyber. Stellar Cyber creates the user and assigns scope and privilege based
on the information passed from the IdP.
 When Global Settings is configured for Authentication & Authorization,
the option to Create new users manually is hidden because new users
must come from the IdP source.
7. Choose a Two-Factor Authentication option that matches your IdP configuration:
Off: If you choose this option, Stellar Cyber user accounts are not offered a
2FA option.
Mandatory: If you choose this option, all users for every tenant are required to
use 2FA when logging in to Stellar Cyber.
Optional: If you choose this option:
The 2FA option can be customized for individual tenants under
System | ORGANIZATION MANAGEMENT | Tenants.
Individual users can choose to enable 2FA under their User Profile in
the Stellar Cyber UI.
You can enforce 2FA for specific users under System |
ORGANIZATION MANAGEMENT | Users when adding or editing a
user

The overall Global Settings for 2FA affect authentication for
partners and tenant users. For example, if 2FA is Mandatory, all
users must use 2FA.
Enabling 2FA here is independent of what you have configured
on your SSO service. Enabling it here causes a separate 2FA
prompt to be displayed upon logging in to Stellar Cyber.
The 2FA page from Stellar Cyber refers to use of Google
Authenticator, but other authenticator applications also work.
8. Review your settings and then Submit them.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  