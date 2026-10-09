Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Logging In

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lesson.

M02 Administration Essentials for Tenants, Users, and System (03h:46m)  

User Login Experience with 2FA (04m:12s)

Learn how to navigate the user login process with two-factor authentication (2FA)
enabled. See how to configure authenticator apps, scan QR codes, and manage backup
verification codes for secure access to the Stellar Cyber Platform.

The first time you access a link on the portal during a session, you must log in to access
content.

Stellar Cyber supports local or SSO authentication, as well as override of the global
authentication method for individual tenants. With local authentication, you log in directly to
Stellar Cyber and user credentials are managed locally by Stellar Cyber. For SSO, your Stellar
Cyber server is integrated with an IDP for authentication purposes. For either authentication
model, two factor authentication (2FA) may have been enabled. Use the sections below to
understand how the login behavior may vary with the way your administrator has configured
authentication. For setup steps, refer to Configuring Authentication



A Global selection of Authentication and Authorization applies to all users (root,
partner, and tenant), so the option to change authentication method for a specific
tenant is not applicable when the Global method is set to Authentication and
Authorization. You cannot log in to Tenant SSO when Global SSO is set to
Authentication and Authorization. If you want to use SSO but also allow local
users and tenant override, you must set the Global authentication method either to
Local or to use the IdP with Authentication Only.

For Authentication Only SSO: First, manually add all users on the Stellar Cyber
Platform. After this manual entry, users can log in with SSO.

For Authentication & Authorization SSO: Configure all users through the IdP.

For Local access (bypass) when SSO is enabled: If Stellar Cyber loses
connectivity with your IdP, users configured for SSO cannot log in. As a preventive
bypass method, manually create a new user in the Stellar Cyber Platform with root
scope and with a valid email address that has "+admin" appended to a valid user
name, as follows: <user>+admin@yourorganization.com
(joe+admin@yourorganization.com). The user you create must be able to
receive a password reset email at <user>@yourorganization.com. This email
alias is what Stellar Cyber uses to permit the bypass of an SSO for a local login.
After you create this separate user account, the user can log in two ways:

An SSO user with <user>@yourorganization.com

or

A local user at https://your.stellar.cyber.address/login using
<user>+admin@yourorganization.com

 If SSO is configured, it's recommended to keep an active administrative

account in the Stellar Cyber user management.

When the organization is configured globally to use SSO, and there are no tenant-
specific authentication overrides, Stellar Cyber is automatically loaded without further
authentication. (Unless the tenant/user has NOT already logged into the global SSO. In
that case, a login screen similar to the one below is displayed.) If the IDP setting of the
organization is set to both Authentication and Authorization, any tenant-specific
authorization methods are not applied.

When more than one organization is hosted on a Stellar Cyber server, or the user's
organization is configured globally to use Localauthentication, or when at least one
tenant is configured to use a different method of login than the global setting

1. A login screen prompts for your username or email address.

2. After the user is identified, one of the following occurs:

If the user is Local – A password prompt is displayed if the
organization is configured globally to use Local authentication or is
configured for SSO but that tenant 's configuration has an override to
use Local authentication.

If the user has tenant-specific SSO – That tenant's SSO login
screen is displayed if the organization is configured globally for SSO
but the tenant is configured to use a different SSO, or the
organization is configured globally for Local, but the tenant is using
SSO.

 If Stellar Cyber loses connectivity with your IdP, users configured for SSO cannot log in.

See the note for Local Access above.

Logging in with 2FA Enabled
Two-factor authentication (2FA) is independent of whether Stellar Cyber is configured for local or
SSO authentication. The Authentication settings specify whether 2FA is mandatory, optional, or
off at the global level for all users. This can be configured at the tenant level, as well. If 2FA is
required and enabled, use this example to understand how to log in with 2FA for the first time:

1. On your smartphone or other device, install an authentication application, such as

Google Authenticator.

2. Browse to your Stellar Cyber server and enter your user name and password.

When 2FA is enabled for your account, the following panel appears the first time you log
in:

3. Open the Authenticator app mentioned above.

4. Scan the QR code that Stellar Cyber displays.

The Authenticator application displays a 6-digit authenticator code.

5. Enter that authenticator code in Stellar Cyber and then select Verify.

Stellar Cyber displays backup verification codes. These are one-time codes you can
use if you do not have access to the authentication app.

6. Copy the verification codes because they will not be displayed again.

7. Select Continue.

Stellar Cyber logs you in.

The next time you log in, enter the two-factor verification code when prompted.



After you have done this one time, the Authenticator application associates you
with Stellar Cyber, so you do not need to scan the QR code again.

You can reset the Authenticator application from your User Profile menu if you
want to use a different Authenticator application.

Account Lockouts
For user accounts with Local authentication, Stellar Cyber protects against brute force login
attempts by locking the user account when five failed login attempts have occurred in a five-
minute period. This protection occurs for either password authentication or 2FA authentication
modes. (Lockout of users authenticated through SSO is managed according to the policies
implemented on their corresponding IdP.)

Lockout Rules

When a user is locked out, an error message displays. The first time a user is locked
out, they can try again in 10 minutes. After a second lockout, the duration is 20 minutes.
All future lockout periods for that user are 30 minutes.

The error message is dynamically updated with a countdown timer so the user knows
how much longer the timeout will persist (10 minutes, then 9 minutes, then 8 minutes,
and so on).

After a user with appropriate privileges (such as security, partner or super admin)
unlocks the user account, the lockout duration for that user is reset. Subsequent failed
attempts will start at the 10-minute duration.

Any user, including those with partner and super admin privilege, can be locked out.

Monitor and Reset Lockout Activity

Users with appropriate privileges—security, partner or super admin—can access the
Users page to review lockout status and unlock users whose accounts are currently
locked (System | ORGANIZATION MANAGEMENT | Users).

After a lockout has occurred, a small lock icon appears to the left of a user's table entry
and the Account Lockouts button is enabled. Select the lock icon to view the user's
activity or to unlock the account. You can also select the Account Lockouts button to
display the activity log for a single user, or select one or more users unlock them all at
the same time.

Lockouts and Unlock actions are reported in the Activity Log (System |
 ORGANIZATION MANAGEMENT | Users | Activity Log).

In the unlikely event that all of your administrative accounts are locked out, contact
Stellar Cyber Customer Success for assistance.

Requesting a Reset for Forgotten Passwords
User accounts with Local authentication can request a password reset using the Forgot
Password link on the Password screen. This link appears after using the main login screen to
supply an email address that exists in the Stellar Cyber database and selecting Next.

Limits on Password Reset Requests

Stellar Cyber protects against brute force login attempts by limiting password reset requests from
the Password screen as follows:

You can not reset your password more than three times in a 24-hour period.

You can not request a password reset email more than three times per hour.

Stellar Cyber only lets you request a password reset email if both of these conditions are true.
These limits persist across system upgrades and restarts, ensuring consistent application of the
restrictions.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

