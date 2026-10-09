Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

User Behavior Analytics

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

J02 Introduction to Features in the User Interface (02h:24m)  

User Behavior and Asset Analytics (45m:00s)

Explore the User Behavior and Asset Analytics tools in the Stellar Cyber Platform to add
context to your security investigations. Learn to assess user activity and analyze assets
for behavioral anomalies using machine learning-driven insights from the data lake.
Follow a demonstration on monitoring user activity and asset interactions, and discover
how to investigate unusual behavior patterns using toolbar filters and the search tool.
Leverage Interflow data and threat intelligence to support threat detection and enhance
your security operations workflow.

The first time you access a link on the portal during a session, you must log in to access
content.

The Assets I User Behavior Analytics page displays security-related information on individual
users via its sensors and connectors. Stellar Cyber user behavior analytics (UBA) is based on
machine learning to analyze traffic and produce security status and event information. Details for
how data is selected in the individual tabs and charts are described below.

 The data displayed by the components described below is subject to the Filter settings at

the top of the screen.

Tabs
Select one of the tabs to see the following sections:

Overview – A summary of user analytics.

Users – Data on specific users. This also provides access to User Details for individual
users.

Real ID – A display of users with their various identities.

The Overview page lets you perform actions on the dashboard.

Dashboard Actions

You can perform the following actions on this dashboard:

Edit

Clone

Export

See the Dashboard Actions page for details on each action.

Overview
The overview dashboard provides a visual perspective of top users for aspects that may be of
interest for further analysis.

 The data in these charts differ from the Users table (described below) in that these are
specific queries, while the user list is all observed users in the selected time period.

The charts are based on the following queries, subject to the Filter settings at the top of the
screen.

The Top Active Users by Source Host chart queries the Traffic and Windows indices
for srcip_username.

The Top Active Users by Destination Host chart queries the Traffic and Windows
indices for dstip_username.

The Top Users with Alert chart queries the Alert index for srcip_username or
dstip_username.

The Top 10 Users by Risk chart queries the Stellar Cyber mongodb for the top 10
users that have largest risk score values.

Users
The Users dashboard lists the users that have been found through IdP connectors, such as
Active Directory, Microsoft Entra ID (formerly Azure AD), Okta, and Duo Security, as well as via
events seen by a Windows Server Sensor. In addition, users are also discovered through GSuite
and Office365.

 The data in this table differs from the Overview (described above) in that these are all
observed users with a last seen timestamp occurring within the filtered time period.

The columns are:

Name – The name of the user as seen on the host. You can select the name to view the
User Details page described in the following section.

Activity – The activity status of the user (Active, Inactive, Idle).

Risk Score – The risk associated with the user.

The calculated user risk score is an overall assessment of how likely the user is going
to be involved in a security breach. The user risk score:

is calculated every 10 minutes
includes open security events from the last 24 hours (if you close an event, it is
removed from the next calculation)
considers the privilege level of users
weights the presence of many different alert types more highly than large
numbers of the same alert

Timestamp – The time of the last event seen .

Last Profile Changed – The time the user record was last updated.

Logon Time – If available, the time the user last logged in.

SID – The system ID detected for the user.

Data Sources – The different data sources from which information about this user was
obtained (for example, windows_agent, active_directory, and so on).

 User data is found through Identity Provider connectors, such as Active Directory,
Microsoft Entra ID (formerly Azure AD), Okta, and Duo Security, as well as via
events seen by a Windows Server Sensor. In addition, users are also discovered
through GSuite and Office365.

Last Logoff Time – If available, the time the user last logged off the system.

Logon Count – The number of times a user has logged in.

Expires – The date and time that the user's authorization expires.

Last Bad Password Time – If it occurred, the last time that a login with this user name
was attempted with a bad password.

Bad Password Count – The number of times this user name was attempted with a bad
password.

Tenant Name – The name of the tenant associated with this user.

Sensor – The sensor that detected the activity.

Action – A button labeled "Details" that, when selected, brings up the User Detail
display.

Disable a User Action

1. Select the icon to the right of a user in the table

.

2. Choose a Connector from the drop-down list.

You can select either Active Directory or Microsoft Entra ID connectors.

3. Set a Duration of either Forever or Limited.

If you choose Limited, then enter Days, Hours, and Minutes.

4. Choose a user name from the UserPrincipalName drop-down list or type the name of

the user to disable him or her.

5. Select Submit.

The request to disable the user is sent.

Bulk Actions

You can perform bulk actions on a group of users. Select the check boxes next to the users you
want to modify. You can:

Add a tag
Add a location
Change privilege level
Add a description

Adding a Tag

To tag a group of users:

1. Select the check boxes next to the users to which you want to add a tag.

2. Choose tag in the bulk actions drop-down list above the table.

3. Choose the tag to apply.

You can also enter a new tag. The tag replaces an existing tag.

4. Select Apply.

The tag is immediately applied.

To remove a tag, simply apply a blank tag.

Adding a Location

To add a location to a group of users:

1. Select the check boxes next to the users to which you want to add a location.

2. Choose location in the bulk actions dropdown.

3. Choose the location to apply.

You can also enter a new location. The location replaces an existing location.

4. Select Apply.

The location is immediately applied.

To remove a location, simply apply a blank location.

Changing Privilege Level

The default privilege level is Medium. A higher privilege level increases the risk score. For
example, if two users have the same events, the user with a higher privilege level will have a
higher risk score. To change the privilege level of a group of users:

1. Select the check boxes next to the users whose privilege level you want to change.

2. Choose privilege level in the bulk actions dropdown.

3. Choose the privilege level to apply.

4. Select Apply.

The privilege level is immediately applied.

Adding a Description

To add a description to a group of users:

1. Select the check boxes next to the users to which you want to add a description.

2. Choose description in the bulk actions dropdown.

3. Enter the description.

4. Select Apply.

The description is immediately applied.

To remove the description, simply apply a blank description.

User Details

Select a user's name on the Assets | User Behavior Analytics page to see the User Details
screen.

You can see the details Stellar Cyber has collected about the user, including what's been
ingested from connected sources.

You can:

 Add as Including Filter
 Add as Excluding Filter
 Copy to Clipboard
See the user's activities

 Adding as an Including Filter

To see only those events with this user:

1. Click  next to the Name field.

The Actions list appears.

2. Click .

The filter is immediately applied and the events table is updated.

 Adding as an Excluding Filter

To see only those events without this user:

1. Click  next to the Name field.

The Actions list appears.

2. Click .

The filter is immediately applied and the events table is updated.

 Copying to Clipboard

To copy the user's name to your clipboard:

1. Click  next to the Name field.

The Actions list appears.

2. Click  Copy to Clipboard.

Seeing the User's Activities

To see the user's activities, scroll to the bottom of the page. The section at the bottom provides
additional details on the user's activities, summarized in both tiles and a multi-tabbed table. The
tiles display the number of events in the corresponding category. You can select the tabs or tiles
to see a table of the events.

Alerts

Related Assets

Commands

Authentications

Login Failures

Files

Real ID
The Real ID dashboard shows a table of users with all of their various identities. The identities
are imported from Active Directory and correlated with a single SID. That SID is used to link all
user identities.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

