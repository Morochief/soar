Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Role-Based Access Control

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M02 Administration Essentials for Tenants, Users, and System (03h:46m)  

User Management with Role-Based Action Control (20m:00s)

Discover how to manage user privileges using role-based access control (RBAC) within
the Stellar Cyber Platform. Follow a demonstration on configuring privilege profiles —
including Super Admin, Platform Admin, and Security Admin — and learn how to assign
roles and scopes to control access levels across tenants. Explore how RBAC
configurations help meet organizational security needs while ensuring compliance with
access control policies.

The first time you access a link on the portal during a session, you must log in to access
content.

You can use role-based access control (RBAC) to manage access to Stellar Cyber by assigning
scopes and privileges to users. Use scope to manage access to tenants. Use privilege to
manage access to functions. You assign scope and privilege when adding or editing users.

Use the options in the System | ORGANIZATION MANAGEMENT | Role-Based Access
Control page to perform the following tasks:

Create or edit privilege profiles
Delete privilege profiles
Use Your IdP to Manage RBAC

Creating or Editing a Profile
Scopes are managed and maintained by Stellar Cyber; you cannot create or change scopes.

Privileges are managed through profiles, which you can create and change. Stellar Cyber
provides four default privilege profile templates (which are marked Default in the View Other

Profiles | Select a Profile Type panel):

Super Admin – Provides full access to the system.

Platform Admin – Provides full access, except for RBAC and selected system settings
(external storage and standby management, for example).

Security Admin – Lets you view, edit, and add sensors, recipients, connectors, reports,
dashboards, queries, and others but not delete them. View-only access to most system
pages.

User – Provides view-only access to most system options, including queries.

You can click any of the listed profile types to see its associated privileges. Privileges listed with
a ü in the display are enabled as part of the corresponding profile while those with an x are
disabled. Privileges are nested under the top-level entries in the Profile Configuration page
according to their relative position within the main areas of product functionality.

You can use these default profiles as-is and assign them to users, or you can create new, custom
profiles based on these templates. You cannot edit the default profiles.

Whether you create a new profile or edit an existing one, you have the same options for defining
privileges.

User Management and RBAC

In general, you can only delete users with a lower-level permission than your own account. This
means:

Super Admin users can delete users with any permissions except the default Super
Admin account and their own account.

Platform Admin users can delete Security Admin users and regular Users.

The exception to this rule is Security Admin users. Security Admin users only have View
permissions for users by default. They do not have add, edit, or delete user privileges.

Creating a New Profile

When you create new profiles, they show up in the Select a Profile Type panel with the four
default templates (and any other custom profiles). However, they do not have the Default
indicator. There is no limit to the number of new profiles you can create.

To create a profile:

1. Select System | ORGANIZATION MANAGEMENT | Role-Based Access Control, and

then select View Other Profiles.

The Select a Profile Type panel appears.

2. Select a profile.

You can select any profile—one of the defaults or a previously created custom profile.
The selected profile then appears.

3. Select Create New Profile from this Template.

The Create a Profile screen appears.

4. Enter the name of the new profile.

5. Select one of the Behavior for new features in future releases options.

These options define how this profile manages the privileges for features added to
Stellar Cyber in the future. The options are:

Inherit from Template – When new Stellar Cyber features are released, the
privilege profile templates are updated to include privileges for the new
features. Choose Inherit from Template if you want your custom template to
inherit those updated privileges as-is.

 A custom profile always inherits from one of the 4 default templates. If you
create a new profile from an existing custom profile, the new one inherits
from the same template as the existing one.

Read Only – Choose Read Only if you want your custom template to add new
features with read-only access privileges.

None – Choose None if you want your custom template to add new features
without allowing access to them.

6. Select Save.

The new profile appears with the new name you defined and editable privileges.

7. Define privileges.

8. Save Changes.

Your changes take effect immediately, but you remain in the new profile to make more
changes.

You can now assign this profile to users on the System | ORGANIZATION MANAGEMENT |
Users page. It appears as an option in the User Privilege drop-down list.

 For very conservative RBAC, create a new profile and choose No Access and assign that
profile to your users. While you can use a default profile template, that template will inherit a
level of access to the new features. By creating a new profile and choosing No Access, you
can review the new features and determine which access privileges, if any, to give users.

Editing a Profile

You can edit a profile at any time. To edit a profile:

1. Select System | ORGANIZATION MANAGEMENT | Role-Based Access Control and

then select View Other Profiles.

The Select a Profile Type panel appears.

2. Select a custom profile (you cannot edit the four default profile templates).

The selected profile appears.

3. Define privileges.

4. Save Changes.

Your changes take effect immediately, but you remain in the new profile to make more
changes.

Defining Privileges

You can define access privileges globally and at the feature group, feature, and function levels.
To define privileges, simply toggle privileges on or off.

 If you see üand ü instead of toggles, you are looking at one of the four default templates,

which you cannot edit. Create or view another profile.

Select Reset, at the bottom of the page, to reset all privileges to the last save.

Feature Group-Level Privileges

You can enable or disable an entire group of features. If you disable this, pages for features in
this group do not appear in Stellar Cyber for users with this user profile.

When you disable a feature group, all features and features in this group are also disabled.

 To quickly enable all privileges for a group, toggle the group to disabled and then back to

enabled. When you toggle it to enabled, all privileges underneath are also enabled.

For example, if you disable Help, the "?" icon doesn't appear in the menu bar. If you disable
Knowledge Base or Release Notes, the Knowledge Base or Release Notes drop-down menus
don't appear.

Feature-Level Privileges

You can enable or disable individual features. If you disable a feature, the link to the page for it
does not appear in the menu for users with this user profile. For example, you can disable
Alerts, which turns off the Detections | Alerts page.

The Root Only note indicates that a feature is only available for users with the Root scope, in
addition to this privilege. Users must have both Root scope and this privilege.

 To quickly enable all privileges under a page, toggle the page to disabled and back. When

you toggle it to enabled, all privileges underneath are also enabled.

Function-Level Privileges

You can enable or disable functions under a feature. If you disable a function, that function
appears but is disactivated in the Stellar Cyber UI for users with this user profile.

For example, if you disable Delete Alert Types, the option to delete alert types appears on the
Alerts page but is grayed out.

 To grant view-only privileges, disable all functions under a page, but leave the page enabled.

The user can view the page (because it is enabled), but cannot perform any functions.

Privileges Example

For this example let's look at some of the privileges for the System | Administration menu.

At the top, the Administration group of features is enabled for this profile. Users with this profile
assigned will see the features in this group in the Stellar Cyber UI.

Under that grouping, features for Licensing and User Management are enabled. Users will see
links to pages for these features in the navigation menu.

The Licensing feature also requires Root scope. Users will only see this feature if they have
Root scope as well as this profile.

Deleting a Privilege Profile
To delete a privilege profile:

1. Select System | ORGANIZATION MANAGEMENT | Role-Based Access Control and

then select View Other Profiles.

The Select a Profile Typepanel appears.

2. Select a custom profile (you cannot delete the four default profile templates).

The profile appears.

3. Select Delete.

The profile is immediately deleted.

You cannot delete a profile if it's assigned to users. To quickly see the users a profile is assigned
to and change it:

1. Select System | ORGANIZATION MANAGEMENT | Users.

2. Select the Privilege column to sort the table on privilege and then look for users with

the privilege profile.

3. Select  to edit the user.

4. Assign a different privilege profile in the User Privilege drop-down list.

5. Submit.

Using Your IdP to Manage RBAC
If you use an IdP to provide SSO to Stellar Cyber, you can also use the IdP to manage RBAC:

1. Configure authorization on your IdP.

2. Configure SSO as the Authentication Method on the System | ORGANIZATION

MANAGEMENT | Settings page, if you haven't done so already.

3. Choose Authentication and Authorization in the Use IDP for setting in the SSO

configuration.

4. Submit.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

