Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Rippling SSO

You can configure Stellar Cyber to use Rippling single sign-on (SSO) for user authentication. In
Security Assertion Markup Language (SAML) terminology, Stellar Cyber then becomes the
Service Provider (SP) and Rippling becomes the Identity Provider (IdP) for Stellar Cyber admin
user authentication.

Adding Stellar Cyber as a New Application in Rippling
Add Stellar Cyber as a new application in Rippling.

Create Custom Fields and Edit Users

1. Log in to Rippling as a user with super admin or full admin permissions, or as an
administrator with permission to manage a Rippling or third-party application.

2. Select Settings | Data Manager | Employee | Employee Information and then select

the New custom field icon ( + ) at the top of the Field panel.

3. Select Start from scratch and create the following custom fields as explained in Collect

a custom field from new hires when they onboard to Rippling .

 You must be logged in to a Rippling account to view the knowledge base article.

Custom Field Name

Default Value

Values

Required

stellar_scope

root

Yes

root

partner

tenant

Custom Field Name

Default Value

Values

Required

stellar_privilege

Platform Admin

super_admin

Yes

stellar_tenant

stellar_tenant_group

(none)

(none)

platform_admin

security_admin

user

(can be empty)

(can be empty)

Yes

Yes

4. Select the People icon in the left navigation panel to access the list of employees and

select the name of a user account for someone who will be a Stellar Cyber
administrative user.

This opens the user's account settings.

5. Select Custom Fields | Edit and add the custom fields you just created, choosing the

appropriate scope and privilege level for the user.

6. Select Role Information | Edit, and set Will get access to work email as Yes.

7. Save your edits.

8. Repeat the previous steps for all users who need to log in to Stellar Cyber.

Create a Custom Application for Stellar Cyber

1. Select IT Management (icon) | Custom App | Create new Custom app.

2. On the Create new app page, enter the following and then select Continue:

Name: Enter a name such as StellarDPApp.

Select Categories: Security

Upload Logo: (Select an image of the Stellar Cyber logo, which you can download from
the Stellar Cyber Media Kit .)

What type of app would you like to create?: Single Sign-on (SAML)

3. On Select Installer, select I’m the <application_name> admin, I’ll install it and then

select Continue.

Set up SSO for Stellar Cyber through Rippling

1. On the Create new app page, copy or download the following and then select

Continue:

Single Sign-on URL or Target URL: Copy this for later use as the Entry Point if you
manually configure SSO in Stellar Cyber.

Issuer or IdP Entity ID: Enter the Stellar Cyber URL.

X509 Certificate: Download this so you can later upload it to Stellar Cyber if you
manually configure SSO there.

IdP Metadata URL: Copy this for later if you use Metadata URL when configuring
SSO in Stellar Cyber.

2. Enter the following URL so that Rippling can submit SAML assertions (SAML

messages) to Stellar Cyber.

Assertion Consumer Service URL: (Note that the URL varies depending on whether
it's for global SSO on Stellar Cyber or per-tenant SSO.)

Global SSO:
https://your.stellar.cyber.address/saml/login/callback/org_id/<org-id>

Tenant
SSO: https://your.stellar.cyber.address/saml/login/callback/org_id/<or
g-id>/cust_id/<tenant-id>

The Assertion Consumer Service URL in the Rippling UI is the URL to which Rippling
sends its SAML authentication response. Different identity providers use different
names for this URL as shown in the following table:

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

3. Enter the following URL so that Rippling can uniquely identify Stellar Cyber account.

Service Provider Entity ID: https://your.stellar.cyber.address

4. Select Move to Next Step.

5. On SSO App Access Rules, set up a rule to determine who will get SSO access—for
example, Set up rules for which new hires or transitions should have an account
—and then select Create custom policy.

6. Under “Which departments should get access to <application_name>?”, select Only

departments I specify, choose one or more departments, and then select Save
changes.

7. On SSO Provision Time, define when to start applying the SSO app access rules by

selecting As soon as they’ve signed their offer letter or agreement and then
Continue.

8. On SSO for admin, let anyone with a full admin account in Rippling sign in to the

<application_name> admin account by selecting Let Stellar Cyber, Inc. admins sign
in to <application_name> admin account and then selecting Continue.

The next step in the SSO setup is Verify SSO Integration. However, before doing this,
you must first configure SSO authentication with Rippling in Stellar Cyber. Either keep
Rippling open to the Verify SSO Integration page or log back in and return to it after
setting up SSO with Rippling on Stellar Cyber.

Configuring SSO Authentication in Stellar Cyber
With all your details collected, you are now ready to configure SSO Authentication in Stellar
Cyber. The steps below are generally applicable for a global or per-tenant configuration.

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

Testing SSO Integration
To test the setup with your email address, return to the Verify SSO Integration in Rippling and do
the following:

1. On the Verify SSO Integration page, select + Connect via Rippling and confirm that

you were able to connect.

2. Select IT Management | Custom App | Manage Custom Apps and check that the

Status for your Stellar Cyber application is Active.

3. Select HR Management | People, open one of the users, and select Role Information

for this user.

4. Make sure that Will get access to work email is Yes for this user and for all users who

must use Rippling SSO to log in to Stellar Cyber.

5. Select Custom fields and check that stellar_privilege is Platform Admin and

stellar_scope is root (or one of the other values set in the custom fields) for this user
and all users who must use Rippling SSO to log in to Stellar Cyber.

6. For users who need administrative access to Stellar Cyber, select IT Management |
Identity Management | Custom App | Manage Custom Apps | Visit App | (for
<application-name>) | Overview, and in the Employee Access table, select Grant
Access.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

