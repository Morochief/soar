Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Managing Settings

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M02 Administration Essentials for Tenants, Users, and System (03h:46m)  

Custom-Branded Logos for Platform UI and Reports (18m:00s)

Explore how to configure and apply custom-branded logos within the Stellar Cyber
Platform UI and tenant reports. Follow the steps to upload partner and customer-specific
logos, and watch a demonstration of how branding settings take effect across platform
interfaces and generated reports.

The first time you access a link on the portal during a session, you must log in to access
content.

 You must have the Super Admin role with Root scope assigned to your account to use this

feature.

Use the System | ORGANIZATION MANAGEMENT | Settings page to manage global settings
for Stellar Cyber. You can make changes in each section independently; each section has its
own Submit button. You can also make changes per tenant. Tenant configurations take
precedence over the global configuration.

Use this page to understand how to:

Change authentication settings
Change global settings
Change tech support settings
Change object-level ACL settings

About Timeouts for Administrative Sessions

Stellar Cyber automatically logs you out of a session after the session idle timeout expires, which
is 60 minutes by default. In the Authentication Settings section, you can set it between 3 and
1440 minutes. It's customizable for each tenant. (For information about setting a custom session
idle timeout for a tenant, see Managing Tenants .)

Authentication Settings
This section allows you to configure Local or SSO authentication. With local authentication, you
log in directly to Stellar Cyber and user credentials are managed locally by Stellar Cyber. SSO
authentication logs you in to Stellar Cyber automatically, using the IdP provider you configured.
The first time you log in, your SSO login appears. After you log in to your SSO service, the SSO
automatically logs you in to Stellar Cyber the next time you access the page (assuming you are
logged in to the SSO service). To log out of Stellar Cyber, log out of your SSO.

Session Idle Timeout: Stellar Cyber automatically logs you out of a session after the session
idle timeout expires, which is 60 minutes by default. You can set it between 3 and 1440 minutes.
It's customizable for each tenant. (For information about setting a custom session idle timeout for
a tenant, see Managing Tenants .)

For detailed procedures to configure Local and SSO authentication, including overrides for
tenants, refer to the following topics:

Configuring Authentication

Logging In



A Global selection of Authentication and Authorization applies to all users (root, partner,
and tenant), so the option to change authentication method for a specific tenant is not
applicable when the Global method is set to Authentication and Authorization. You
cannot log in to Tenant SSO when Global SSO is set to Authentication and
Authorization. If you want to use SSO but also allow local users and tenant override, you
must set the Global authentication method either to Local or to use the IdP with
Authentication Only.

Global Settings

This section provides the following controls:

System Timezone – Set your timezone relative to UTC and to your most common
operational timezone. Stellar Cyber adds the timezone in the alert descriptions of the
Login Time Anomaly.

Organization Logo / Organization Logo (Light theme)

Use these options to upload a logo to use in the UI (top left corner), on the login page,
and on reports. You can upload separate logos for use in both the dark and light
themes.

 See the top of this page for recommended lessons about this section at

Stellar Cyber Academy.

When you select Submit, the logo is immediately visible in the UI.

Select Delete to replace the uploaded logo with the default Stellar Cyber logo.

The Organization Logo replaces a Tenant Logo uploaded when adding or
editing a Tenant Group.

To completely rebrand Stellar Cyber (removing "Powered by Stellar Cyber",

adding your custom login screen, and customizing the
technical support.

 menu, contact

Login Message – Supply an optional text message to display to users in a popup
window upon login to Stellar Cyber. If you leave this field empty, Stellar Cyber does not
display a login message. Note that this is a global message that appears to all tenants
on each login.

Enable AI Investigator – Toggles the AI Investigator feature on or off for your
organization. When the feature is off, all related user interface controls are hidden.
When the feature is on, users have access to AI-powered threat investigation.

Enable AI Case Analysis & Summary – Toggles the availability of AI-generated case
analysis and summaries for all tenants.

 Even if you previously used AI-assisted case analysis in the Early Access

Program, after upgrading to 6.4.0s you must toggle on Enable AI Case Analysis &
Summary to continue using it in 6.4.0s.

Select Submit to save these settings and immediately make them active.

Tech Support Settings
You can have your sensors collect logs to help troubleshoot sensor performance. The logs
contain detailed information that is not exposed on the user interface.

At the top you can see the current size of the tech support logs. You can configure:

Collect Logs From Sensor – Enabled by default. Clear this to stop collecting logs from
your sensors.

Support Portal URL – Point the Support Portal entry in the
location instead of Stellar Cyber's support portal.

 menu to a custom

Collect Usability Data for Product Analytics – This setting allows Stellar Cyber to
perform usage analytics, such as access to documentation pages. The setting is on by
default, but can be disabled for your environment, if needed.

Select Submit to save these settings and immediately make them active.

Object ACL (Access Control List) Settings

. These settings
Configure global defaults for Object-Level Sharing and Access Control
determine whether new and existing user-defined objects—such as dashboards—are accessible
to all users by default (Default Allow) or only to their owners (Default Deny). Changing these
settings lets you control content visibility and modification policies across the Stellar Cyber
Platform. For details about both global and dashboard-specific configurations, see Configuring
Object-Level Sharing and Access Control.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

