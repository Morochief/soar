Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Integrating with an IdP

You can configure your IdP to provide authentication and, optionally, authorization via SSO to
Stellar Cyber. The authorization defines the scope and privilege assigned to each user. General
steps to configure authorization (the exact steps vary based on your IdP):

1. Log in to your IdP.

2. Configure the SAML Assertion URL (different IdP vendors use different terms for this

URL):
https://your.Stellar Cyber.address/saml/login/callback



A Global selection of Authentication and Authorization applies to all
users (root, partner, and tenant), so the option to change authentication
method for a specific tenant is not applicable when the Global method is
set to Authentication and Authorization. You cannot log in to Tenant
SSO when Global SSO is set to Authentication and Authorization. If
you want to use SSO but also allow local users and tenant override, you
must set the Global authentication method either to Local or to use the
IdP with Authentication Only.

When you configure SSO on a per-tenant basis, you MUST modify the
Single Sign-on URL (and Audience URL, if applicable) to use a customer
ID, otherwise the callback applies to the entire Stellar CyberPlatform not
just the tenant. The ID you use is for a single tenant. Most IdPs support
the following syntax:

https://your.Stellar
Cyber.address/sso/saml/metdata/cust_id/<tenant id>
(This syntax is required for Azure AD B2C SSO configuration)
 Example: https://10.33.2.5/sso/saml/metdata/cust_id
/59125044

https://your.Stellar
Cyber.address/saml/login/callback?cust_id=<tenant
id>

 Example: https://10.33.2.5/saml/login/callback?
cust_id=59125044

When you configure SSO on a per-tenant basis, you must modify the
SSO URL (and Audience URL, if applicable) to use a customer ID. The
ID you use is for a single tenant. Most IdPs support the following syntax:

SaaS tenant –
 https://your.stellar.cyber.address/saml/login/callb
ack/org_id/<organization-id>/cust_id/<tenant-id>

Example

https://1.1.1.1/saml/login/callback/org_id/51408620
/cust_id/59125044

On-premises tenant –
 https://your.stellar.cyber.address/saml/login/callb
ack/cust_id/<tenant-id>

Example

https://1.1.1.1/saml/login/callback/cust_id/5912504
4

3. Edit the user and add the applicable attributes and assign the appropriate value:

Custom Attribute

Values

Global SSO

stellar_scope

root

Required for Authorization

partner

tenant

stellar_privilege

super_admin

Required for Authorization

platform_admin

T

e

n

a

n

t-

s

p

e

c

if

i

c

S

S

O

N

ot

a

p

pl

ic

a

security_admin

user

bl

e

stellar_tenant

ID number for

(Optional) Specify an individual tenant ID, not name. The ID is

configured tenant

available on the Tenants List page.

stellar_tenant_group

ID number for any

configured tenant

group

(Optional) Specify a tenant group ID, not name. This is

typically applicable for use by MSSP users with the Partner

role. The Tenant Group ID is available on the Tenant Groups

page.



Values in these fields are case sensitive and syntax matters. Use the
exact indicated syntax and verify that you have made no typos

If you have created a custom privilege with spaces or dashes, use an
underscore instead. Example: A custom privilege of STML-Security
Admin must be entered as STML_Security_Admin.

4. Save your changes.

For specifics on adding attributes to a user see the SSO topic for your IdP:

Okta user profiles and attributes 

OneLogin custom user fields 

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

