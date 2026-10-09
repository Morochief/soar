Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring OneLogin SSO

 From Stellar Cyber v5.4.0, do not use the default Stellar Cyber integration application in

OneLogin. Instead follow the steps below to create a new application.

If you already use OneLogin to manage access to other products in your organization, you can
also configure it as the Identity Provider (IdP) for users accessing the Stellar Cyber Platform.
Integrating Stellar Cyber with OneLogin lets you extend centralized user access control to Stellar
Cyber through Single-Sign On (SSO) and SAML (Security Assertion Markup Language).

 For information about authentication and authorization through SSO, see Integrating with

an IdP.

Adding Stellar Cyber as a New Application in OneLogin
The setup of OneLogin to act as the IdP for Stellar Cyber users involves the addition of Stellar
Cyber user accounts, creation of a Stellar Cyber application, and then the assignment of the
application to the users.

Add Stellar Cyber User Accounts to OneLogin

You can import a set of users in bulk in a CSV file or add them individually. The following
instructions are for adding an individual user whom you want to OneLogin to authenticate when
the user attempts to log in to Stellar Cyber.

1. Log in to the OneLogin UI as a OneLogin administrator.

2. Select System | ORGANIZATION MANAGEMENT | Users | New User.

The New User configuration page appears.

3. Enter values for the First name, Last name, and Email, and then Save User.

4. When using a OneLogin SSO for both user authentication and authorization, select
More Actions | Change Password, enter a default password, select Force user to
update, and then Update.

When users first log in with the default password, they will be prompted to change it.

5. Select Save User to save the user configuration.

6. Repeat to add additional users.

Create a New Stellar Cyber Application in OneLogin

To add Stellar Cyber as a new application in OneLogin:

1. Select Administration | Applications | Applications | Add App.

The Find Applications page appears.

2. Search for SAML Test Connector (IdP) and choose it in the applications list.

The SAML Test Connector (IdP) application appears.

3. Change the name of the application (for example, “Stellar Cyber SSO”), optionally set
rectangular and square icons and add a description, and then Save the application to
create a new one.

 Artwork for Stellar Cyber logos is available for download in the media kit .

After you Save the application with a new name, more options appear in the left menu.

4. Select Configuration and enter the following SAML (Security Assertion Markup

Language) settings:

Audience: Also referred to as EntityID, this identifies the SP (Service Provider) for
which SAML assertions are intended. For SSO (Single Sign-On) authentication of
Stellar Cyber users, enter the IP address or FQDN of the Stellar Cyber Platform where
users log in; that is, https://your.stellar.cyber.address. Note that it must be
preceded by https://

For example, if the Stellar Cyber UI login is at 10.1.1.20, enter https://10.1.1.20

Recipient: This specifies the endpoint URL that processes SAML assertions. Enter the
same Stellar Cyber IP address or FQDN as you did for Audience.

For example, enter https://10.1.1.20

ACS (Consumer) URL Validator: Also referred to as ACS URL Pattern, this validates
the ACS (Assertion Consumer Service) URL to which OneLogin sends SAML responses
and requires a regular expression pattern, using a backslash to escape the dots. The
Stellar Cyber URL varies depending on whether it's for global SSO on the Stellar Cyber
Platform or if it's for tenant SSO.

Global SSO example:
https://10\.1\.1\.20/saml/login/callback/org_id/<org-id>

Tenant
SSO example: https://10\.1\.1\.20/saml/login/callback/org_id/<org-
id>/cust_id\/<tenant-id>

ACS (Consumer) URL: This defines the SP endpoint (Stellar Cyber) that receives and
processes SAML assertions.

Examples

Global SSO example:
https://10\.1\.1\.20/saml/login/callback/org_id/51408620

Tenant
SSO example: https://10\.1\.1\.20/saml/login/callback/org_id/51408620/c
ust_id/59125044

The ACS (Consumer) URL in the OneLogin UI is the URL to which OneLogin sends its
SAML authentication response. Different identity providers use different names for this
URL as shown in the following table:

Identity Provider

Term for the Assertion Consumer Service (ACS) URL

Active Directory Federation

Relying party SAML 2.0 SSO service URL

Services

Microsoft Entra ID

Reply URL

Okta

OneLogin

Rippling

Single sign on URL

Assertion Consumer (ACS) URL

Assertion Consumer Service URL

5. Save the configuration.

6. Select Parameters, leave the default setting Configured by admin selected, and

select the Add ( + ) icon.

7. In the New Field dialog box that appears, enter the following attributes and then Save

the configuration:

Field name: stellar_scope

Include in SAML assertion: (select)

8. After you save the configuration and the dialog box changes from “New Field” to “Edit
Field stellar_scope”, leave the Value at its default setting of - No default - , and Save
again.

9. Repeat the previous three steps to define the scope, role, and privilege for three other

Stellar Cyber user types:

stellar_privilege

stellar_tenant

stellar_tenant_group

 The first two attributes (stellar_cyber and stellar_privilege) are required for
all users. The last two (stellar_tenant and stellar_tenant_group) are only
required for users in a multi-tenant deployment.

10. Save the parameters.

11. Select SSO, leave the other settings as they are, set SAML Signature Algorithm as

SHA-256, and then Save the SSO settings.

12. Copy details to use in the Stellar Cyber SSO (SAML) configuration later.

If you configure Stellar Cyber to use the OneLogin metadata URL, copy the Issuer
URL.

When manually configuring Stellar Cyber to work with OneLogin, you will need the
SAML 2.0 Endpoint (URL) displayed here and the X.509 certificate that you can see
by selecting View Details for X.509 Certificate. Copy and paste them in a text editor
now or return here to copy and paste them into the Stellar Cyber SSO (SAML) manual
configuration later.

Assign the Application to the User

Assign the Stellar Cyber application to a user and set the user’s scope, role, and privileges.

1. Select Administration | Users | Users and then select one of the user accounts you

previously added.

2. In the settings for this user, select Applications.

3. On the Applications tab, select the Add ( + ) icon.

The Assign new login to <username> dialog box appears.

4. Choose the Stellar Cyber application you just created—for example, Stellar Cyber SSO

—and then select Continue.

5. Select Allow the user to sign in, enter values for the attributes you previously defined
—for example, stellar_privilege = super_admin and stellar_scope = root—and then
Save your changes.

By default, a root admin has access to “All Tenants”. You don’t need to set “All Tenants”
as a value in the stellar_tenant field. For a partner, enter a tenant group, which
provides access to all tenants in the group. For a user, specify a single tenant.

 For information about user scope and privilege, see Integrating with an IdP.

6. Save User.

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

Set up SSO

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

Identity Provider

Term for Metadata URL

Active Directory Federation Services

Federation Metadata URL

Microsoft Entra ID

App Federation Metadata URL

Okta

OneLogin

Rippling

If you select Manual Config:

Metadata URL

Issuer URL

Metadata URL

Issuer URL: If this setting is present, enter the Stellar Cyber URL.

Entry Point: Paste the entry point URL you copied from the IdP.

You must include http:// or https:// before the URLs. Different vendors use
different names:

Identity Provider

Term for Entry Point URL

Active Directory Federation Services

SAML Endpoint

Microsoft Entra ID

Login URL or SAML-P Sign-on Endpoint

Okta

OneLogin

Rippling

Sign on URL

SAML 2.0 Endpoint (HTTP)

SAML 2.0 Endpoint (HTTP)

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

