✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Okta SSO
You can configure Stellar Cyber to use Okta SSO for Authentication or Authentication and
Authorization:
1. Add Stellar Cyber as a New Application in Okta
2. Add Attributes for Assigned Users
3. Assign Okta Users to Authenticate
4. Activate Multifactor Authentication (MFA)
5. Configure SSO Authentication in Stellar Cyber
Add Stellar Cyber as a New Application in Okta
To add Stellar Cyber as a new application in Okta:
1. Log in to Okta and select Applications | Applications.
The Applications page appears.
2. Select Create App Integration.
The Create a new app integration wizard appears.
3. On the Sign-in method page, select SAML 2.0 and then select Next.

4. On the General Settings tab on the Create SAML Integration page, enter an App
name, optionally upload a logo, and then select Next.
5. On the SAML Settings tab, enter the following values for the Single sign on URL and
the Audience URI (SP Entity ID).
A global SSO configuration for a SaaS deployment:
Single sign on URL:
https://your.stellar.cyber.address/saml/login/callback/o
rg_id/<org-id>
Audience URI (SP Entity ID):
https://your.stellar.cyber.address
A tenant-specific SSO configuration for a SaaS deployment:
Single sign on URL:
https://your.stellar.cyber.address/saml/login/callback/o
rg_id/<org-id>/cust_id/<tenant-id>
Audience URI (SP Entity ID):
https://your.stellar.cyber.address
The Single sign on URL in the Okta UI is the URL to which Okta sends its
SAML authentication response. Different identity providers use different names
for this URL as shown in the following table:
Term for the Assertion Consumer Service
Identity Provider
(ACS) URL
Active Directory Federation Relying party SAML 2.0 SSO service URL
Services
Microsoft Entra ID Reply URL
Okta Single sign on URL
OneLogin Assertion Consumer (ACS) URL
Rippling Assertion Consumer Service URL
6. If you are configuring SSO for the whole server, you can enter the following
Name/Value pairs. You will use these as attributes later. This configuration does not
apply to a tenant-specific SSO configuration.

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
|                         | )                            | O   |
| ----------------------- | ---------------------------- | --- |
| s appuser.stellar_scope | r Required for Authorization | N   |
| t                       | o                            |     |
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
|     | e   |     |
| --- | --- | --- |
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
s appuser.stellar_privilege
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
s appuser.stellar_tenant I
(Optional) Specify an individual tenant ID, not name. The ID is available on
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
s appuser.stellar_tenant_group I
(Optional) Specify a tenant group ID, not name. This is typically available
t D
for use by MSSP users with the Partner role. The Tenant Group ID is
e n
displayed on the Tenant Groups page.
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

Values in these fields are case sensitive and syntax matters. Use the
exact indicated syntax and verify there aren't any typos.
If you have created a custom privilege with spaces or dashes, use an
underscore instead. Example: A custom privilege of STML-Super Admin
must be entered as STML_Super_Admin.

7. Select Next.
8. Enter your feedback on the Feedback page and then select Finish.
The new app is immediately created and activated.
9. On the Sign On tab of the application you just created, expand More details.
10. Copy the Sign on URL and download the signing certificate (X.509 certificate).
These are the Entry Point and certificate that you will use to configure Stellar Cyber.
You must next add the same four attributes that you set for the application to the user profile that
will be applied to those who use the application.
Add Attributes for Assigned Users
These attributes let you manage authorization for Stellar Cyber users (not applicable for per-
tenant SSO).
To add attributes for users:
1. Select Directory | Profile Editor.
The Profile Editor page appears with the Users tab active by default.
2. Select the profile for the application you created and then Add Attribute.
The Add Attribute dialog box appears.
3. Leave the Data type as string, enter a Display name and one of the Variable names
you previously created.
The Display name will be shown ifn the UI instead of the variable name and can be
whatever you decide to name it (for, example, "Scope" for the stellar_scope variable).
On the other hand, the variable must be entered exactly as you defined it for the
application. The following are the four variable names:
appuser.stellar_scope
appuser.stellar_privilege
appuser.stellar_tenant
appuser.stellar_tenant_group

4. Leave the other settings at their default values and select Save and Add Another until
you've added all four.
5. After the last one, select Save .
6. Save the configuration.
The new attributes appear at the bottom of the profile editor.
You must now assign the users whom Okta will authenticate to the application.
Assign Okta Users to Authenticate
Assign users to the application in Okta, and if you are configuring Authentication only, create a
corresponding list of users to add to Stellar Cyber. Users are automatically added to Stellar
Cyber when you configure SSO to perform both Authentication and Authorization.
 Only users who already have accounts in the Okta system can be assigned to the
application.
1. Select Applications | Applications, select the name of the application you created,
and then select the Assignments tab.
2. In the Assign dropdown list, choose Assign to People.
The assignment dialog box appears, listing user accounts in Okta.
3. Select Assign for a user that you want Okta to authenticate for access to Stellar Cyber.
Okta displays the selected user's username and the Display names of the four variables
you defined for the user profile that corresponds to this application.
4. Enter the scope, which can be root, tenant, or partner.
5. Enter the privilege, which can be super_admin, platform_admin, security_admin, or
user.
You can also enter a custom privilege you defined in Stellar Cyber, under Admin | Role-
Based Access Control.
6. Enter the exact tenant ID as defined in Stellar Cyber.
7. Enter the exact tenant group ID as defined in Stellar Cyber.

If you set the scope as root and leave the tenant field empty, the root user will have
access to all tenants.
8. When the scope is partner, enter the exact name or ID of a tenant group as defined in
Stellar Cyber.
9. To assign other users to the application, Save and Go Back.
10. Repeat the assignment for all users whom you want Okta to authenticate when they
access Stellar Cyber.
11. When finished, select Done.
If you are using two-factor authentication, you must enable a multi-factor authentication option.
Otherwise, you can proceed to configuring SSO in Stellar Cyber.
Activate Multifactor Authentication (MFA)
You can optionally enable MFA for your users. The steps here allow you to specify which client
you prefer for authentication. It uses the Google Authenticator app.
 Configuration of multi-factor authentication in Okta is independent of whether you enable
2FA in Stellar Cyber. It is possible for you require your users to authenticate with MFA in Okta
and again with 2FA in Stellar Cyber
1. Select Security | Authenticators | Add authenticator.
2. Select Add for Google Authenticator.
Okta automatically adds Google authenticator to the Catch-all Rule, which is applied by
default to all applications. The rule requires any two factor types for users to
authenticate themselves, such as a password and a code from Google Authenticator.

You can now configure SSO authentication in Stellar Cyber.
Configure SSO Authentication in Stellar Cyber
With all your details collected, you are now ready to configure SSO Authentication in Stellar
Cyber. The steps below are generally applicable for use for global configuration or per-tenant
configuration.
Prepare for Users
For Authentication Only SSO: First, manually add all users on the Stellar Cyber
Platform. After this manual entry, users can log in with SSO.
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

Identity Provider Term for Metadata URL
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