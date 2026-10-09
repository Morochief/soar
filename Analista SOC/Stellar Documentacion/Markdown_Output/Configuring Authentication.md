Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Authentication

Stellar Cyber supports Local or SSO (Single Sign-On) authentication. With local authentication,
you log in directly to the Stellar Cyber Platform, and your user credentials are managed locally
within the platform. With SSO authentication, you log in through an external IdP (Identity
Provider), which authenticates you and relays the login to Stellar Cyber. For either authentication
model, you specify whether two-factor authentication (2FA) is Off, Optional, or Mandatory. Use
the procedures in this section to define your Stellar Cyber global authentication strategy.

Configuring Local Authentication

Configuring SSO Authentication

Note the following:

You can separately customize the authentication strategy for individual tenants in
System | ORGANIZATION MANAGEMENT | Tenants.

You can specify 2FA for specific tenants in System | ORGANIZATION MANAGEMENT
| Tenants, and for specific users in their User Profile.

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

Configuring Local Authentication
If you select Local authentication, you can still opt to configure two-factor authentication (2FA),
which allows you to set whether 2FA is required at all, or optionally specify 2FA as being required
at the user/tenant level.

 You can override the global authentication settings on a per-tenant basis. Refer to Managing

Tenants Tenant-level authentication settings affect how tenant-level users authenticate
themselves, but they don't affect partner authentication. Regardless of the authentication
settings of tenants in their tenant group, partners use the same authentication method as
root-level users.

1. Log in to the Stellar Cyber user interface (UI) as a root user with super admin privileges

and select System | ORGANIZATION MANAGEMENT | Settings.

2. In the Authentication Settings section, choose Local for Authentication Method.

3. Choose a 2FA method.

Off: If you choose this option, Stellar Cyber user accounts are not offered a
2FA option.

Mandatory: If you choose this option, all users for every tenant are required to
use 2FA when logging in to Stellar Cyber.

Optional: If you choose this option:

The 2FA option can be customized for individual tenants under
System | ORGANIZATION MANAGEMENT | Tenants.

Individual users can choose to enable 2FA under their User Profile,
accessed from the top menu of the Stellar Cyber UI.

You can enforce 2FA for specific users under System |
ORGANIZATION MANAGEMENT | Users when adding or editing a
user



The overall Global Settings for 2FA affect authentication for partners and
tenant users. For example, if 2FA is Mandatory, all users must use 2FA.

Enabling 2FA here is independent of what you have configured on your
SSO service. Enabling it here causes a separate 2FA prompt to be
displayed upon logging in to Stellar Cyber.

The 2FA page from Stellar Cyber refers to use of Google Authenticator,
but other authenticator applications also work.

Configuring SSO Authentication
SSO authentication logs you in to Stellar Cyber automatically, using the IdP provider you
configured. The first time you log in, your SSO login appears. After you log in to your SSO
service, the SSO automatically logs you in to Stellar Cyber the next time you access the page
(assuming you are logged in to the SSO service). To log out of Stellar Cyber, log out of your
SSO.

 You can override the global authentication settings on a per-tenant basis. Refer to Managing

Tenants Tenant-level authentication settings affect how tenant-level users authenticate
themselves, but they don't affect partner authentication. Regardless of the authentication
settings of tenants in their tenant group, partners use the same authentication method as
root-level users.

Configure your IDP

Stellar Cyber supports several IdPs using SAML 2.0. Stellar Cyber supports use of an IdP for
Authentication as well as Authentication and Authorization.

ADFS

Azure AD B2C

Google

Microsoft Entra ID (formerly Azure Active Directory)

NetIQ

Okta

OneLogin

Rippling

Use either the general procedure for integrating Stellar Cyber with your IdP or one of the
following detailed procedures before you configure Stellar Cyber SSO authentication.

General IdP Integration

Azure AD B2C SSO Integration

Microsoft Entra ID SSO Integration

Okta SSO Integration

OneLogin SSO Integration

Rippling SSO Integration

Enable Users

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

Enabling SSO Globally

A general procedure to configure SSO authentication in Stellar Cyber is provided here:

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

Stellar Cyber logs all users out (including you) and restarts. When it restarts, it begins using
SSO.

 If Stellar Cyber loses connectivity with your IdP, users cannot log in. However, the root

admin user must always authenticate locally, so can log in from https://your.Stellar

Cyber.address/login.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

