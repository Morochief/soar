Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Active Directory Federation
Services SSO

These instructions explain what to configure in Active Directory Federation Services (AD FS) and
in Stellar Cyber so that AD FS can authenticate Stellar Cyber administrative users. It’s assumed
that you’ve already deployed AD FS and are using it to authenticate users on your network. If
not, see Deploy and configure AD FS . It’s also assumed that user accounts for Stellar Cyber
administrative users have already been added to Active Directory and that each account has an
email address and password. AD FS will use these to authenticate users during login.

If you use domain names in the authentication settings for Stellar Cyber (the relying party), use
domain names in the configuration for AD FS (the identity provider). Similarly, if you use IP
addresses in Stellar Cyber, use IP addresses on AD FS.

Active Directory Federation Services
1. Log in to Server Manager and view the Dashboard.

2. Select Tools | AD FS Management.

This opens the AD FS management console.

AD FS Server: Create a Relying Party Trust

1. Select Add Relying Party Trust in the right panel or access the context menu for
Relying Party Trusts in the left panel and select Add Relying Party Trust there.

To access the context menu when using a mouse, right-select Relying Party Trusts in
the left panel. To access it when using a handheld device, long-press (press and hold)
Relying Party Trusts.

The Welcome to the Add Relying Party Trust Wizard appears.

2. Leave Claims aware selected and then Start.

3. In the Select Data Source step, select Enter data about the relying party manually

and then select Next.

4. In the Specify Display Name step, enter a name for the relying party such as Stellar
Cyber AIO CE, optionally enter any notes for future reference, and then select Next.

5. Skip the Configure Certificate step and select Next.

6. Select Enable support for the SAML 2.0 WebSSO protocol and enter the Relying
party SAML 2.0 SSO service URL. The exact URL depends on the type of Stellar
Cyber deployment (on premises or SaaS) and whether the SSO applies to the entire
Stellar Cyber system or to a single tenant.

If you are configuring SSO for the entire Stellar Cyber system:

Relying party SAML 2.0 SSO service URL: Use the Stellar Cyber Platform
URL, appended with /saml/login/callback/org_id/<org-id>. The format
is https://<your.stellar.cyber.address>/saml/login/callback/org_
id/<org-id>, where <org-id> is the Organization ID on the license page.
For example:
https://192.168.24.110/saml/login/callback/org_id/0c5b67d2e9e54
398be1e4d1cff1edc3

If you are configuring SSO for a tenant:

Relying party SAML 2.0 SSO service URL: Use the Stellar Cyber Platform
URL, appended with /saml/login/callback/org_id/<org
id>/cust_id/<tenant-id>. The format

is https://<your.stellar.cyber.address>/saml/login/callback/org_
id/<org-id>/cust_id/<tenant-id>, where <org-id> is the Organization
ID on the license page. For
example:  https://192.168.24.110/saml/login/callback/org_id/0c5b6
7d2e9e54398be1e4d1cff1edc3d/cust_id/59125044

This is the URL where ADFS sends SAML assertions to Stellar Cyber after a successful
authentication. An assertion contains a user’s authentication details and attributes.

The Relying party SAML 2.0 SSO service URL in the ADFS UI is the URL to which
ADFS sends its SAML authentication response. Different identity providers use different
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

7. When done, select Next.

8. For the Configure Identifiers step, enter the Stellar Cyber URLs that will communicate

with Active Directory. For example:

https://your.stellar.cyber.address

9. Skip the Choose Access Control Policy step and select Next.

10. Skip the Ready to Add Trust step and select Next.

11. Leave Configure claims issuance policy for this application selected and Close.

AD FS: Add Rules

Create transform rules to define where Active Directory authenticates users and what attributes it
returns to Stellar Cyber after a successful user authentication.

Rule 1

1. In the Relying Party Trusts page, access the context menu of the relying party trust you

just made and Edit Claim Issuance Policy.

To access the context menu when using a mouse, right-select the relying party trust
name. To access it when using a handheld device, long-press (press and hold) the
relying party trust name.

2. Add Rule to check the email address on an incoming claim against the Name IDs in the

Active Directory attribute store.

3. Leave the claim rule template as Send LDAP Attributes as Claims, and then select

Next.

4. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as NameID.

Attribute store: Active Directory

LDAP Attribute: E-Mail-Addresses

Outgoing Claim Type: E-Mail Address

After AD FS (the identity provider) authenticates a user, this rule instructs it to take the
value of the email attribute in the user’s Active Directory account and transform it into an
E-Mail Address claim in the token it sends to Stellar Cyber (the relying party).

Rule 2

1. Add Rule to transform the incoming claim type of E-Mail Address to an outgoing claim

type of Name ID.

The value (for example, user@yourdomain.com) remains the same; it’s just the claim
type that changes.

2. For the claim rule template choose Transform an Incoming Claim and then select

Next.

3. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as Transform Name ID.

Incoming claim type: E-Mail Address

Outgoing claim type: Name ID

Rule 3

1. Add Rule to set the scope of the Stellar Cyber user as Root.

2. For the claim rule template choose Send Claims Using a Custom Rule, and then

select Next.

3. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as Stellar Scope (Root).

Custom rule: => issue(Type = "stellar_scope", Value = "root");

Rule 4

1. Add Rule to set the scope of the Stellar Cyber user as a tenant.

2. For the claim rule template choose Send Claims Using a Custom Rule and then

select Next.

3. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as Stellar Scope (Tenant).

Custom rule: => issue(Type = "stellar_scope", Value = "tenant");

Rule 5

1. Add Rule to set the scope of the user as a Stellar Cyber partner.

2. For the claim rule template choose Send Claims Using a Custom Rule and then

select Next.

3. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as Stellar Scope (Partner).

Custom rule: => issue(Type = "stellar_scope", Value = "partner");

Rule 6

1. Add Rule to set the administrative privilege of the Stellar Cyber user as Super Admin.

2. For the claim rule template choose Send Claims Using a Custom Rule and then

select Next.

3. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as Stellar Privilege (Super_Admin).

Custom rule: => issue(Type = "stellar_privilege", Value =
"super_admin");

Rule 7

1. Add Rule to set the Stellar Cyber tenant name for the user.

2. For the claim rule template choose Send Claims Using a Custom Rule and then

select Next.

3. Enter the following in Add Transform Claim Rule Wizard and then select Finish:

Claim rule name: Enter a name such as Stellar Tenant (tenant-name).

Custom rule: => issue (Type = "stellar_tenant", Value = "tenant-name");

 Replace tenant-name with the actual name of the tenant.

4. To save the set of rules, select OK.

Stellar Cyber

Configure Stellar Cyber to authenticate users using SSO (SAML) with
Active Directory Federation Services.

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

