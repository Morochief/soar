✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Managing Tenants
Learn more at Stellar Cyber Academy.
The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.
M02 Administration Essentials for Tenants, Users, and System (03h:46m)  
Multi-Tenant Concepts and Configuration (38m:00s)
Explore multi-tenant architecture within the Stellar Cyber Platform, including how data
segregation, machine learning customization, and operational views support managed
security service providers (MSSPs) managing multiple organizations or business units.
Learn how tenant-specific Interflow data is stored and processed within the data lake,
and how threat intelligence and machine learning models can be scoped and tuned at
the tenant level. Follow a step-by-step demonstration on creating and configuring
tenants, assigning access levels, and setting up a tenant admin user with two-factor
authentication. Discover how tenant boundaries enforce data isolation while allowing
centralized visibility across your environment within the Stellar Cyber Platform.
The first time you access a link on the portal during a session, you must log in to access
content.
The Stellar Cyber multi-tenant feature allows all the features and capabilities of Stellar Cyber,
including machine learning, to be applied to any number of independent networks.
See the Tenants overview page for general information about tenants.
Tenants Table
When you select the System | ORGANIZATION MANAGEMENT | Tenants option, Stellar Cyber
displays a table of the existing tenants similar to the example below.

The columns are:
Name – The name of the tenant.
ID – The unique ID number for the tenant. This number is often required for sensor and
software setup functions to precisely identify the tenant.
Contact Name – The name of the person responsible, as entered.
Contact Phone – The phone number of the person responsible, as entered.
Address – The address of the tenant, as entered.
Last Ingestion Volume (GB) – The amount of data ingested on behalf of the tenant as
of the previous day. This value is updated every midnight, local system time.
Number of Users – The number of tenant users.
Number of Sensors – The number of sensors installed for the tenant.
Date Created – The timestamp of when the tenant was created.
Action – The actions you can take.
The actions you can take are:
Click Create to create a new tenant.
The Add Tenant dialog box (described below) appears.
Click to edit the corresponding tenant.
The Edit Existing Tenant dialog box appears.
Click to delete the corresponding tenant.
For details on this, see:
Removing Tenants (v4.3.5+)
See the Tables page for more information on working with tables.
Adding or Editing Tenants
All fields other than the tenant name are stored in the record without further processing. Their
values can be defined by the system owner's policy.
1. When you either add a new tenant or edit an existing tenant, a panel similar to the
following appears:

Here you can enter or update the following:
Tenant Name – A unique name that identifies the tenant. This field is required.
It supports a maximum of 256 UTF-8 characters, both in the Tenants page
and in the API.
 Note: Tenant name fields were expanded from 50 characters to 256 in
the 6.3.0 release. Make sure you continue to use tenant names with a
maximum of 50 characters for any managed sensors running releases
prior to 6.3.0 to ensure compatibility.
Contact Name – The name of the party responsible for the tenant.
Contact Email – The email address of the party responsible for the tenant.
Contact Phone – The phone number of the party responsible for the tenant.
Address – The address of the party responsible for the tenant.
Enable Custom DHCP Lease Period – Toggle this on to specify a custom
DHCP lease period for this tenant. Stellar Cyber uses this period to release IP
addresses from the asset IDs, preventing the accumulation of multiple asset
IDs for a single asset (due to changing IP addresses). If you don't enable this,
the tenant uses the default DHCP lease period, which is 72 hours.
Ingestion Target – Use this field to create a target ingestion limit for this
tenant. The value you specify here is for your reference only and is not
enforced.
2. After modifying the above fields, select Next to proceed.
The Authentication Method panel enables you to configure tenant-specific overrides
to the global authentication strategy.
Choose the Authentication Method for the tenant:
Choose Default for the tenant to use the same settings as the global
authentication (set in System | ORGANIZATION MANAGEMENT | Settings). If
you choose this option, no further configuration steps are required other than

optionally enabling two-factor authentication (2FA) and setting a per-tenant
session idle timeout.
You might choose Local authentication if the server is globally using Single
Sign-On (SSO), but you want a specific tenant to use the Local authentication
from the Stellar Cyber server. If you choose this option, no further configuration
steps are required other than optionally enabling 2FA and setting a per-tenant
session idle timeout.
Choose SSO (SAML) if you want the tenant to use a different SSO from the
global configuration, or the global configuration is Local but that tenant wishes
to use SSO. To configure tenant-specific SSO (Authentication Only), you must
first set up the Identity Provider (IdP) that will provide SSO authentication for
Stellar Cyber users. For a list of IdPs that Stellar Cyber supports, see
Configuring Users, Roles and Authentication.

A Global selection of Authentication and Authorization
applies to all users (root, partner, and tenant), so the option to
change authentication method for a specific tenant is not
applicable when the Global method is set to Authentication
and Authorization. You cannot log in to Tenant SSO when
Global SSO is set to Authentication and Authorization. If you
want to use SSO but also allow local users and tenant override,
you must set the Global authentication method either to Local
or to use the IdP with Authentication Only.
Although you can customize SSO configuration on a per-tenant
basis, the Authorization capability is only supported at the
global level. Overrides you make at the tenant level are for
Authentication only, so the toggle for Authentication and
Authorization is not offered in the tenant editor.
The authentication method for partners is the same as that for
root users. Any authentication overrides for tenant-level users in
a tenant group have no effect on the authentication method for
the partners who manage the group.
If you choose SSO (SAML) as the authentication method for the tenant,
configure your IdP to include the customer ID in the tenant callback. The ID
you use is for a single tenant. Most IdPs support the following syntax:
SaaS tenant –
https://your.stellar.cyber.address/saml/login/callback/
org_id/<org-id>/cust_id/<tenant-id>
Example
https://1.1.1.1/saml/login/callback/org_id/51408620/cust
_id/59125044

On-premises tenant –
 https://your.stellar.cyber.address/saml/login/callback/
cust_id/<tenant-id>
Example
https://1.1.1.1/saml/login/callback/cust_id/59125044
3. If you select SSO (SAML), then select Metadata URL or Manual Config:
If you select Metadata URL:
Issuer URL: Leave this empty. The IdP provides the Issuer URL as part of the
metadata it returns.
Metadata URL: Paste the URL you copied from the IdP. The URL must begin
with either https:// or http://. Different vendors use different names for the
Metadata URL:
| Identity Provider                    | Term for Metadata URL       |     |
| ------------------------------------ | --------------------------- | --- |
| Active Directory Federation Services | Federation Metadata URL     |     |
| Microsoft Entra ID                   | App Federation Metadata URL |     |
| Okta                                 | Metadata URL                |     |
| OneLogin                             | Issuer URL                  |     |
| Rippling                             | Metadata URL                |     |
If you select Manual Config:
Issuer URL: Paste the issuer URL that you previously copied from the IdP
when configuring it.
Entry Point: Paste the entry point URL you previously copied from the IdP.
You must include http:// or https:// before the URLs. Different vendors use
different names:
Term for Issuer
| Identity Provider |     | Term for Entry Point URL |
| ----------------- | --- | ------------------------ |
URL
| Active Directory Federation | Federation Service | SAML Endpoint |
| --------------------------- | ------------------ | ------------- |
| Services                    | Identifier         |               |
Microsoft Entra ID Identifier (Entity ID) Login URL or SAML-P Sign-on
Endpoint
| Okta     | Issuer                | Sign on URL              |
| -------- | --------------------- | ------------------------ |
| OneLogin | Issuer URL            | SAML 2.0 Endpoint (HTTP) |
| Rippling | Issuer or SAML Issuer | SAML 2.0 Endpoint (HTTP) |
URL
IDP Certificate: Upload the certificate file you previously downloaded from the
IdP.
4. If you select SSO (SAML), then also select Allow Clock Skew to allow for system time
differences between Stellar Cyber and the IdP. Authentication messages have an

expiration. If the system times on Stellar Cyber and your IdP are not synchronized, the
messages might expire before they even get to Stellar Cyber. The result is that users
cannot log in, because they cannot authenticate.
5. Choose a Two-Factor Authentication option that matches your IdP configuration:
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
6. Set a custom session idle timeout for the users of the tenant or accept the default
timeout.
The minimum is 3 minutes, the maximum is 1440 minutes (24 hours), and the default is
60 minutes.
7. Select Next and then Submit your configuration to save the tenant.
After creating a new tenant, Stellar Cyber requires time to prepare it for efficient data
ingestion. During this period, which can sometimes take up to two hours, you can check
its status either in the tenant table, where a “Not ready for ingestion” message appears,
or in the task list at the top right of the UI, where a “Tenant Ingestion Readiness” task
progresses from “pending” to “in progress” to “complete.” When the tenant is ready, the
message is removed from the table and the task status changes to “complete.” At that
point, assign sensors to the tenant and configure connectors and parsers to begin
ingesting data.
Tenant Groups

You can add tenants to groups on the Tenant Groups page. See Tenant Groups for more
information.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  