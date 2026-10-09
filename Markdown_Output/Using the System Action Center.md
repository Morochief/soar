✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Using the System Action Center
Learn more at Stellar Cyber Academy.
The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.
M02 Administration Essentials for Tenants, Users, and System (03h:46m)  
System Action Center (24m:00s)
Learn to configure the System Action Center for monitoring and notifications, and watch
a demonstration of its capabilities in action. Create rules for events such as case
assignments and offline sensors, and explore configuration options for managing alerts
across deployments to enhance system monitoring within the Stellar Cyber Platform.
The first time you access a link on the portal during a session, you must log in to access
content.
You use System | System Action Center to create and manage rules that specify when system
notifications are triggered and where they are sent. Triggered notifications always appear in the
Notification Center, available under the in the main toolbar. You can also configure
notifications with both email and Slack actions to send messages to specified recipients,
including both those defined in the System | Recipients page and those you specify manually on
demand.
System notifications help you keep tabs on important system events in the following categories:
Case Management – Get notifications when cases are assigned, closed, escalated,
created, updated, or have a score that meets or exceeds a specified threshold.
Connector Monitoring – Get notifications when specified connectors haven't sent data
over a given time interval so you can address issues in real time.
Device Sensor Monitoring – Get notifications for different device sensor health issues
(for example, no data or heartbeats).

License Enforcement – Find out proactively when your license limits are approaching
an undesirable state or have been exceeded.
License Usage – Get notifications when asset usage or ingestion usage exceeds
specified thresholds or when asset counts decrease by a configurable percentage.
Log Source Monitoring – Get notifications when log sources stop sending data.
Platform Health – Get notifications when Stellar Cyber Platform health issues affect
data ingestion, storage, cluster performance, or UI availability.
 Platform Health alerts are only available as part of an Early Access Program and
may not appear in your version of the Stellar Cyber Platform. Contact your account
manager to inquire about taking part in an Early Access Program.
Playbook Monitoring – Get notifications when an ATH Playbook experiences a change
in status (for example, failure or recovery).
Scheduled Report Monitoring – Get notifications when a scheduled report fails.
Sensor Token – Get notified when a token used to authorize sensors is about to expire.
Server Sensor Monitoring – Get notifications when server sensors experience a
change in status, stop sending data, or stop sending heartbeats.
TIP Feed Monitoring – Get notifications when a TIP feed stops sending data or does
not respond to polling.
User Modifications – Get notifications for a wide variety of events related to user
accounts and RBAC policies.
 Refer to Best Practices for the System Action Center for guidance on ways you can use
the System Action Center effectively in your organization.
See the following sections for details on working with the System Action Center:
Required Privileges
Working with the System Action Center Page
Creating New System Notification Rules
Using the System Action Center
Required Privileges
The System Action Center is only available to accounts with both Root scope and the System |
System Action Center privilege assigned to their profile in System | ORGANIZATION
MANAGEMENT | Role-Based Access Control. By default, this includes only the Super Admin
role. The necessary privileges in the Role-Based Access Control page are shown below:

Working with the System Action Center Page
The System Action Center lists each of the defined system action rules in a standard Stellar
Cyber table, as shown below.
Available System Action Rules
The table below summarizes the available System Action Rules. Further details on each rule
type are provided later in the topic.
Defa
| Category | Name | Description |     |
| -------- | ---- | ----------- | --- |
ult
Case Case assigned Notify user a case has been assigned to them. Disa
| Management |     |     | bled |
| ---------- | --- | --- | ---- |
Case Case closed Notify user that a case has been closed. Disa
| Management |     |     | bled |
| ---------- | --- | --- | ---- |
Case Case escalated Notify user that a case has been escalated. Disa
| Management |     |     | bled |
| ---------- | --- | --- | ---- |
Case Case meets Notify users a case has met a desired notification threshold. Disa
| Management | threshold |     | bled |
| ---------- | --------- | --- | ---- |
Case Case updated Notify user that a case has been updated to 'In Progress' status. Enab
| Management |     |     | led |
| ---------- | --- | --- | --- |
Case New case created Notify users of a new case has been created. Disa
| Management |     |     | bled |
| ---------- | --- | --- | ---- |
Connector No data from Get notified when any connector doesn't send data within a set amount of time. Enab
| Monitoring | connector(s) |     | led |
| ---------- | ------------ | --- | --- |
Connector Connector status Get notified when the health status of any connector changes from healthy to Enab
| Monitoring | change | unhealthy. | led |
| ---------- | ------ | ---------- | --- |
Device Sensor Device sensor Get notified when any Device sensor sends a supported feedback message (for Disa
Monitoring feedback example, when a sensor has been upgraded). bled
Device Sensor Device sensor Get notified when any device sensor ingestion changes unexpectedly. Disa
| Monitoring | ingestion change |     | bled |
| ---------- | ---------------- | --- | ---- |

Defa
| Category | Name | Description |     |
| -------- | ---- | ----------- | --- |
ult
Device Sensor Device sensor Get notified when the health status of any device sensor changes to unhealthy. Disa
| Monitoring | status change |     | bled |
| ---------- | ------------- | --- | ---- |
Device Sensor Get notified when a new sensor fails to register with the Stellar Cyber platform.
New sensor
Monitoring
registration failed

This feature is only available as part of an Early Access Program and may not
appear in your version of the Stellar Cyber Platform. Contact your account
manager to inquire about taking part in an Early Access Program.
Device Sensor No data from Get notified when any device sensor doesn't send data within a set amount of time. Disa
| Monitoring | device sensor(s) |     | bled |
| ---------- | ---------------- | --- | ---- |
Device Sensor No heartbeat from Get notified when any device sensor doesn't send heartbeat within a set amount of Disa
| Monitoring | device sensor(s) | time. | bled |
| ---------- | ---------------- | ----- | ---- |
License License in Get notified when the license state drops to warning violation or out-of-compliance. Enab
| Enforcement | undesirable state |     | led |
| ----------- | ----------------- | --- | --- |
License License limit Get notified when the license limit is exceeded on a given day. Enab
| Enforcement | exceeded |     | led |
| ----------- | -------- | --- | --- |
License Usage Asset count Get notified when licensing asset counts (V2 Devices, V2 Users, V2 Total) decrease Enab
dropped by a configurable percentage threshold between evaluation intervals. led
License Usage Asset threshold Get notified when assets exceed a limit on a given day. Enab
|     | exceeded |     | led |
| --- | -------- | --- | --- |
License Usage Ingestion Get notified when ingestion exceeds a limit on a given day. Disa
|     | threshold |     | bled |
| --- | --------- | --- | ---- |
exceeded
| Log Source | No data from all |     | Disa |
| ---------- | ---------------- | --- | ---- |
Get notified when no log sources send data within a set amount of time.
| Monitoring | log sources |     | bled |
| ---------- | ----------- | --- | ---- |
Log Source No data from log Get notified when specified log sources do not send data within a set amount of time. Disa
| Monitoring | source(s)       |     | bled |
| ---------- | --------------- | --- | ---- |
| Playbook   | Playbook status |     | Disa |
Get notified whenever the status of an ATH Playbook changes (for example, failure or
| Monitoring | change | recovery). | bled |
| ---------- | ------ | ---------- | ---- |
Scheduled Scheduled report Get notified whenever a scheduled report fails to execute successfully. Disa
| Report | failed |     | bled |
| ------ | ------ | --- | ---- |
Monitoring
Sensor Token Token is about to Get notified three days before a token used to authorize sensor installations will Enab
|     | expire | expire. | led |
| --- | ------ | ------- | --- |
Server Sensor No data from Get notified when any server sensor doesn't send data within a set amount of time. Disa
| Monitoring | server sensor(s) |     | bled |
| ---------- | ---------------- | --- | ---- |
Server Sensor No heartbeat from Get notified when any server sensor doesn't send heartbeat within a set amount of Disa
| Monitoring | server sensor(s) | time. | bled |
| ---------- | ---------------- | ----- | ---- |

Defa
| Category | Name | Description |     |
| -------- | ---- | ----------- | --- |
ult
Server Sensor Server sensor Get notified when the health status of any server sensor changes to unhealthy. Disa
| Monitoring | status change |     | bled |
| ---------- | ------------- | --- | ---- |
| TIP Feed   | No data from  |     | Disa |
Get notified when a TIP feed has not polled for new IoCs within the expected
| Monitoring | TIP feed          | timeframe. | bled |
| ---------- | ----------------- | ---------- | ---- |
| TIP Feed   | TIP feed received |            | Disa |
Get notified when a TIP feed encounters an error during polling.
| Monitoring | error |     | bled |
| ---------- | ----- | --- | ---- |
User Account lockout Get notified whenever any user's account is locked due to login failures. Disa
| Modifications | triggered |     | bled |
| ------------- | --------- | --- | ---- |
User Account password Get notified whenever any password policy is changed. Disa
| Modifications | change |     | bled |
| ------------- | ------ | --- | ---- |
User New RBAC profile Get notified whenever a new RBAC profile is created. Disa
| Modifications | created |     | bled |
| ------------- | ------- | --- | ---- |
User New user created Get notified when a new user is created. Disa
| Modifications |     |     | bled |
| ------------- | --- | --- | ---- |
User RBAC profile Get notified whenever an RBAC profile is deleted. Disa
| Modifications | deleted |     | bled |
| ------------- | ------- | --- | ---- |
User User RBAC Get notified whenever a user's privilege profile is escalated. Disa
| Modifications | privilege |     | bled |
| ------------- | --------- | --- | ---- |
escalation
User User deleted Get notified when a user is deleted from the platform. Disa
| Modifications |     |     | bled |
| ------------- | --- | --- | ---- |
User User has disabled Get notified whenever a user disabled 2FA. Disa
| Modifications | 2FA |     | bled |
| ------------- | --- | --- | ---- |
System Action Center Fields
The System Action Center lists the defined notification rules with the following information:
Name – The name assigned to the rule when it was created.
Category – Rules are available in the categories listed in the table in the previous
section (Case Management, Connector Monitoring, Log Source Monitoring, and so on).
Type – Each category of rule has multiple rule types available.
Tenant – The tenant to whom the notification rule belongs.
Description – Either the standard description of the rule provided by Stellar Cyber, or
the description provided when the rule was created.
Creator – The user account that created the rule.
Status – Rules can be either Enabled or Disabled using the toggle in this column.
 Changes to a rule's status require a few minutes to take effect. During this time, for
example, you may still receive notifications for a rule you have disabled.

 As described in About Built-In Rules, the built-in License Enforcement rules cannot
be disabled.
Edit  and Delete  icons.
 As described in About Built-In Rules, the built-in rules cannot be deleted.
Clone – When you check a rule's box, a new Clone button appears that lets you make
a copy of the selected rule for editing. This is useful when you want to create a new rule
that is very similar to an existing rule.
 When you clone a Case Management rule, Stellar Cyber automatically disables
the Send to case assignee option to help prevent duplicate emails.
In addition, the System Action Center supports standard Stellar Cyber table functionality:
Sort on column headers.
Click the "hamburger" menu available in a column header to pin, autosize, or reset
columns.
Use the collapsible Filters tab to control what's displayed in the table.
Use the collapsible Columns tab to add/remove columns from the table.
Export the table in CSV format.
About Built-In Rules
The System Action Center lists both built-in rules and user-configured rules:
The built-in rules are as follows:
Rule Category Built-In Rules
License Enforcement License in undesirable state
License limit exceeded
License Usage Asset count dropped
Asset threshold exceeded
Ingestion threshold exceeded
Built-in rules cannot be deleted. Because of this, they will not have a delete  icon at
the far right of their entry in the table, as is shown below for the first several rules.
Built-in rules can be edited (for example, if you want to add an email address for
notifications for the rule).
The built-in License Monitoring rules can be disabled using the toggle in the Status
column.
The built-in License Enforcement rules (License in undesirable state and License
limit exceeded) cannot be disabled.
User-configured rules can be edited, deleted, and enabled/disabled. They always have
the delete  icon at the far right of their entry in the table.

Creating New System Notification Rules
You create a new system notification rule by clicking the Create button at the top of the System
Action Center, selecting the category and type of rule you want to create from the menu that
appears, and following the wizard's prompts. Alternatively, if you want to use an existing rule as a
template for a new one, you can check the box for the source rule in the list and click the Clone
button to create an editable copy.
Click the headings below for specific instructions on the type of rule you want to create:
About System Notification Actions
When you create a new system notification rule using the instructions in the sections below, you
always have the option of configuring actions for the rule. The System Action Center supports
the following action types:
Email – Email actions send emails to specified recipients, including both those defined
in the System | Recipients page and those you type into the wizard manually.
Slack – Slack actions send Slack messages to specified channels or recipients using
the URL for an incoming webhook that you create in the Slack API . You can select a
Slack recipient defined in the System | Recipients page or type in the URL for the
incoming webhook manually.
Email and Slack messages both include a summary of the event(s) that triggered the notification
and a link back to the Stellar Cyber platform to a location that makes sense based on the type of
notification that was generated. You can configure a rule with any combination of email and Slack
messages, including multiple destinations.
 In addition to performing any custom actions you configure, triggered notifications also
always appear in the Notification Center, available under the icon in the main toolbar.
 The contents of email and Slack messages are not yet configurable.
Consolidated or Individual Notifications
By default, the System Action Center sends consolidated notifications, grouping all triggered
instances for a given rule in the same time interval into a single message. This gives you a useful
summary of all events matching a given rule without overwhelming your inbox or Slack feed. For
example, here's a consolidated email showing multiple matching events from a No data from
connector(s) rule:
In some situations, however, you may want a rule to send individual notifications for each
individual event. This can be useful in situations where you want to use an automated system to

perform individual actions based on individual System Action Center events (for example,
sending System Action Center emails to a designated Support inbox used by a tool such as
Jira Service Management to generate separate tickets automatically).
In these cases, you can configure your rules to send individual notifications for each event. You
do this by checking the Send individual... box for a Notification in the Actions step. Here's how
that appears for an email notification. A similar option appears for Slack notifications:
A rule configured with the Send individual option... enabled sends separate notifications for
each separate event matching the rule's conditions. For example, here's one of the individual
emails sent by the same rule from our first example when it's been reconfigured with Send
individual... enabled.
Creating a Case Management Notification Rule
Case Management rules notify you when specified case-related events take place. You can
create rules that notify you when the following events related to cases take place:
Case assigned
Case closed
Case escalated
Case meets threshold
Case updated
New case created
The mechanics for creating a case management notification rule are mostly the same regardless
of the specific type of rule you are creating. The differences are summarized in the procedure
below:
1. Click the Create button at the top of the System Action Center and select Case
Management from the dropdown that appears.
2. Select the type of Case Management notification rule you want to create.

The Create Notification wizard starts with the Category set to Case Management and
the Type set to the rule type you selected.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected. Click
anywhere in the Tenant field to display a pick list including all tenants available on the
system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.
7. Use the Advanced step to specify details related to the type of case management rule
you selected. The options are different for each rule type and are summarized in the
table below:
Case
Managem
Description Configuration Options
ent Rule
Type
Case Generates a notification when a
assigned case's Assigned to field in the
Case Details page changes.
Case Generates a notification when a
closed case's Status is changed to Check the Send to case assignee box to send an email notification
Resolved in the in the Case to the case's assignee. This email is sent in addition to any other
Details page. email or Slack actions you specify in the Actions step.
Case Generates a notification when a
escalated case's Status is changed to
Escalatedin the in the Case
Details page.

Case
Managem
Description Configuration Options
ent Rule
Type
Case Generates a notification when a Use the Score Threshold option to specify the case score at which
meets case's score meets a threshold this notification is generated.
threshold you specify.
Case Generates a notification any Check the Send to case assignee box to send an email notification
updated time an update is made to a to the case's assignee. This email is sent in addition to any other
case. email or Slack actions you specify in the Actions step.
New case Generates a notification when a Use the Score Threshold option to set a minimum score threshold at
created new case is created. which new case notifications generate notifications. This lets you tune
the noise level for the rule; a higher minimum threshold generates
fewer notifications.
8. Click Next when you are ready to continue.
9. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification Type: Email
section:
Check the Send individual email for each notification option if you
would like to send separate emails for each triggered instance of the
rule. If you do not check this option, the System Action Center sends
a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list containing
all email recipients configured in the System | Recipients page. If you
want to send an email to someone who is not already configured in
the Recipients page, you can also type addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can click

the Add Configuration button and add a second Email notification
with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each notification
option if you would like to send separate Slack messages for each
triggered instance of the rule. If you do not check this option, the
System Action Center sends a consolidated Slack message listing all
matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that will
receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the Slack
API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and Slack
messages, including multiple destinations.
10. Click Next and review the settings for your notification rule. Use the Back button to go
back and correct anything that's not quite right. When you are satisfied, click Submit to
add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Links in Case Notification Emails

Notification emails sent from the System Action Center for Case Management events include a
link to the case in the user interface. Refer to Using the System Action Center for important
configuration instructions to ensure that these links work correctly.
Preventing Duplicate Case Notification Emails
If you configure multiple Case assigned rules, you can prevent duplicate emails by make sure
that only one of them has the Send to case assignee option enabled. Stellar Cyber helps you
with this by disabling the option in cloned Case Management rules.
Creating a Connector Monitoring Notification Rule
Connector Monitoring rules help you keep tabs on the status of your connectors. You can
create the following types of Connector Monitoring rules:
Connector status change – Get notified when the status of a connector changes
from healthy to one of the unhealthy states (Error, Warning, or Unavailable). New
notifications are sent every five minutes for this rule type.
No data from connector(s) – Get notified when specified connectors have not sent
traffic over the time interval you configure.
Use the following procedure to create a Connector Monitoring rule:
1. Click the Create button at the top of the System Action Center and select Connector
Monitoring from the dropdown that appears.
2. Select the type of Connector Monitoring rule you want to create.
The Create Notification wizard starts with the Category set to Connector
Monitoring and the Type set to the rule type you selected.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.

7. Check the Include All Connector Types field if you would like to apply this rule to
both all current and future connector types.
 When this box is checked, new connector types are automatically added to the
notification rule as they are added to the Stellar Cyber platform. If this option is
not enabled, you will need to add new connector types to the rule as they become
available in the platform for the rule to trigger on them.
8. Use the Connector Type(s) field to specify the types of connectors for this rule.
 Note that this field is not active if you checked Include All Connector Types.
By default, all connector types are selected. You can remove a specific connector
type by clicking the x in its entry in the field. You can also click anywhere in the field
to display a pick list (shown below) that lets you check the boxes for the connector
types you want to include in the rule. The pick list also includes a Select All option
that lets you add all connector types back to the list if you have removed some.
9. The entries in the Connector Type(s) field are broad types of connectors and not
specific connectors themselves. You use the Excluded Connector(s) field to
exclude specific connectors from the types selected in the Connector Type(s) field
from the inactivity rule. The Excluded Connector(s) pick list shows you just the
specific connectors belonging to the Types that are part of the rule you are creating.
For example, in the figure below, we have only selected the Active Directory
connector type. As you can see, the Excluded Connector(s) pick list shows us all of
the specific Active Directory connectors defined on the system. You can use the pick
list to check the boxes of any specific connectors you want to exclude from inactivity
notifications in this rule.
10. You can use the Excluded Tenant(s) dropdown to exclude specified tenants from
notifications for this rule.
This option only appears when All Tenants is selected in the first step of the rule's
configuration. It gives you a handy way to omit a few tenants whom you don't want to
notify with a particular rule.

11. For a No data from connector(s) rule, you can use the Interval fields to specify the
time window for the rule. You may be concerned if some connectors have not sent
data in a manner of minutes, while others may not give you cause for concern over a
period of days. The Interval controls let you specify both the units (Minutes, Hours,
or Days) and the size of the time window. For example, we have specified an interval
of 12 hours in the figure below:
12. Click Next when you are ready to continue.
13. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.

The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
14. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a Device Sensor Monitoring Rule
Device Sensor Monitoring rules help you monitor the health of your device sensors, notifying
you when they are either offline or haven't sent data within a specified amount of time.

 Device Sensor Monitoring rules only work for device sensors. They are not supported for
Server Sensors (agents).
You can create the following types of Device Sensor Monitoring rules:
Device sensor feedback –This rule is triggered when the feedback from a Device
Sensor indicates that it has been upgraded. Stellar Cyber checks every five minutes
for changes in upgrade feedback.
Device sensor ingestion change – This rule is triggered when a Device Sensor's
daily ingestion deviates more than a specified percentage from its average daily
ingestion over the last seven days. Stellar Cyber compares these values once per
day at 03:00 AM UTC.
Device sensor status change – This rule is triggered when a Device Sensor's
status is either yellow or red, as defined below. A new notification is generated every
five minutes the sensor remains in one of these states. You can investigate further in
the Sensor list.
Yellow – At least one warning condition is affecting the sensor.
Click here to see the possible warning conditions:
Sensor disk usage exceeds 90%
Sensor CPU usage exceeds 99%
Sensor feedback contains a config mismatch error message
Sensor has not updated its status in at least five minutes
Sensor feedback shows a failure to apply a profile with the
Tenable Nessus feature enabled to a sensor running version
4.3.3 or lower (Tenable Nessus support was introduced in 4.3.4)
Sensor feedback contains at least one warning message
Red – At least one danger condition is affecting the sensor.
Click there to see the possible danger conditions:
Sensor has an invalid Engine ID (engid)
Sensor has a conflicting Engine ID (engid)
Sensor configuration is out of sync (either the ver_sent does
not match received ver_ack or one of the two messages is
missing)
Sensor memory usage exceeds 95%
Sensor feedback contains a config failure message
Sensor feedback shows at least one failure during the
application of a new sensor profile.
New sensor registration failed – This rule is triggered when a new device sensor
fails to register and cannot send data to the platform. Check your device connectivity
and sensor configuration.

 This feature is is only available as part of an Early Access Program and may not
appear in your version of the Stellar Cyber Platform. Contact your account
manager to inquire about taking part in an Early Access Program.
No data from device sensor(s) – This rule is triggered when a sensor has not sent
a record with traffic within a specified interval.
No heartbeat from device sensor(s) – This rule is triggered when Stellar Cyber has
not received a heartbeat message from a sensor within a specified interval.
 Notice that the No data and No heartbeat rules monitor for different types of inactivity.
When a No data from device sensor(s) notification is generated, Stellar Cyber may still
have contact with the affected sensor but is not receiving records with traffic. In the case of
the No heartbeat from device sensor(s) notification, Stellar Cyber is not receiving
heartbeats from affected sensors and has not had contact within the specified monitoring
interval.
For all rule types, you can also specify a Mute Interval that specifies a window within which a
repeated instance of the same notification will not be generated.
. Use the following procedure to create a Device Sensor Monitoring rule:
1. Click the Create button at the top of the System Action Center and select Device
Sensor Monitoring from the dropdown that appears.
2. Select the type of rule you want to create. See the start of this section for a
description of the rule types.
The Create Notification wizard starts with the Category set to Device Sensor
Monitoring and the Type set to the selected rule type.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant) field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.

6. Click Next.
7. Set Advanced options for the rule, as described below:
All rules include the Excluded Sensors option, with a dropdown that lets
you exclude specified sensors from monitoring. The list includes all sensors
available to the tenant selected in the first step of the wizard.
Rules with All Tenants selected in the first step include the Excluded
Tenants option, with a dropdown that lets you exclude sensors assigned to
a specified tenant from monitoring. This gives you a handy way to assign a
rule to all but a few excluded tenants.
Some of the rules include additional options, as summarized in the table
below:
Device Sensor Defau
Advanced
Monitoring Rule Description lt
Options
Type Value
Device sensor Ingestion Specify the percentage differential in daily ingestion (up or down) from 20%
ingestion chang Change the average of the previous seven days at which this rule is triggered.
e Percent
No data from No Data Specify the amount of time that can pass without a device sensor 1 hour
device Threshold sending a record with traffic before this rule is triggered.
sensor(s)
Use these options to temporarily silence notifications from the rule for a 1 hour
specified amount of time. Once the rule is triggered, no new
notifications will be generated from the same rule until the Mute
Threshold has passed.
Mute
 Stellar Cyber still monitors the rule for signs of activity from the
Threshold
sensor until the mute threshold passes and restarts the
monitoring interval if they are detected. A new alert is only
generated when the Mute Threshold is passed if no activity has
been seen during the monitoring interval.
No heartbeat No Specify the amount of time that can pass without a device sensor 4
from device Heartbeat sending a heartbeat before this rule is triggered. hours
sensor(s) Threshold

Device Sensor Defau
Advanced
Monitoring Rule Description lt
Options
Type Value
Mute Use these options to temporarily silence notifications from the rule for a 24
Threshold specified amount of time. Once the rule is triggered, no new hours
notifications will be generated from the same rule until the Mute
Threshold has passed.
 Stellar Cyber still monitors the rule for heartbeats from the sensor
until the mute threshold passes and restarts the monitoring
interval if they are detected. A new alert is only generated when
the Mute Threshold is passed if no heartbeats have been seen
during the monitoring interval.
The image below shows the Advanced step for a No data from device sensor(s)
rule:
8. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list

containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.

9. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a License Enforcement Notification Rule
License Enforcement rules notify you about issues regarding your licenses. You can create the
following types of License Enforcement rules:
License in undesirable state – This rule is triggered when your license enters the
warning, violation, or out-of-compliance state. Refer to .Understanding License
Compliance for details on each of these license states.
License limit exceeded – This rule is triggered when your license is exceeded on a
given day, but remains below the 110% of usage that would put it in a warning state.
 The system includes built-in License in undesirable state and License limit exceeded
rules that can be neither disabled nor deleted. You can edit those rules to change who is
notified by them or, alternatively, you can create additional License Enforcement rules
using the procedure below to notify different sets of people with different emails.
. Use the following procedure to create a License Enforcement rule:
1. Click the Create button at the top of the System Action Center and select License
Enforcement from the dropdown that appears.
2. Select either License in undesirable state or License limit exceeded, depending
on the type of rule you want to create. See the start of this section for a description of
the two rule types.
The Create Notification wizard starts with the Category set to License Enforcement
and the Type set to the selected rule type.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.

6. Click Next.
7. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:

Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
8. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a License Usage Notification Rule
License Usage rules notify you about issues regarding your licenses. You can create the
following types of License Usage rules:
Asset count dropped – This rule is triggered when the counts of your V2 Devices,
V2 Users, or V2 Total assets decrease by a configurable percentage threshold

between evaluation intervals. This rule polls every 15 minutes for asset counts to
check for significant drops. When the drop exceeds the specified percentage
threshold, the rule generates a notification.
 Although Stellar Cyber evaluates this condition every 15 minutes, it sends this
notification a maximum of once per day for the same condition.
 "V2 assets" are also referred to as entity-based assets.
Asset threshold exceeded – This rule is triggered when your license's asset
threshold is exceeded on a given day.
Ingestion threshold exceeded – This rule is triggered when your license's volume-
based threshold is exceeded on a given day.
 The system includes built-in Asset count dropped, Asset threshold exceeded, and
Ingestion threshold exceeded rules that cannot be deleted. You can disable these rules
or edit them to change who is notified by them. Alternatively, you can create additional
License Usage rules using the procedure below to notify different sets of people with
different emails.
. Use the following procedure to create a License Usage rule:
1. Click the Create button at the top of the System Action Center and select License
Usage from the dropdown that appears.
2. Select the type of rule you want to create. See the start of this section for a
description of the rule types.
The Create Notification wizard starts with the Category set to License Usage and
the Type set to the selected rule type.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.

6. Click Next.
7. Are you configuring an Asset Drop or Asset/Ingestion Threshold Exceeded rule?
Asset Drop Rules:
a. Select the Asset Type(s) to monitor. You can select V2 Devices,
V2 Users, or V2 Total assets.
 "V2 assets" are also referred to as entity-based assets.
b. Specify the Drop Threshold percentage. This rule checks asset
counts every 15 minutes to see if the selected type has dropped by
more than the percentage specified here, generating a notification
if it has.
 Although Stellar Cyber evaluates this condition every 15
minutes, it sends this notification a maximum of once per day
for the same condition.
c. Use the Monitored Tenants field to select the tenants whose
assets will be monitored by this rule. Click anywhere in the
Monitored Tenant(s) field to display a pick list including all tenants
available on the system where you can select specific tenants to
which this rule applies.
Asset/Ingestion Threshold Exceeded Rules:
a. Select the Tenant to which the rule applies. By default, All Tenants
are selected. Click anywhere in the Tenant field to display a pick
list including all tenants available on the system where you can
select the tenant to which this rule applies.
b. Use the Threshold field to specify by how much the asset or
ingestion threshold must be exceeded in order for this rule to be
triggered:
Asset threshold exceeded – The threshold specifies the
number of assets above the allowed threshold at which

this notification is triggered.
Ingestion threshold exceeded – The threshold specifies
the number of GB above the allowed threshold at which
this notification is triggered.
8. Click Next.
9. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:

Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
10. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a Log Source Monitoring Notification Rule
Log Source Monitoring rules help you keep tabs on the status of your log sources. You can
create the following types of Log Source Monitoring rules:
No data from all log source(s) – Get notified when no log sources send data over
the time interval you configure.

No data from log source(s) – Get notified when specified log sources have not sent
data over the time interval you configure.
 Log Source Monitoring rules only monitor log sources that have sent data within the last
30 days. To ensure consistent inactivity evaluation, retain Analytics Data Engine (ADE)
data for at least 30 days.
Use the following procedure to create a Log Source Monitoring rule:
1. Click the Create button at the top of the System Action Center and select Log
Source Monitoring from the dropdown that appears.
2. Select the type of Log Source Monitoring rule you want to create.
The Create Notification wizard starts with the Category set to Log Source
Monitoring and the Type set to the rule type you selected.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.
7. Set Advanced options for the rule, as described below:
a. Set the rule-specific options described in the table below:
Device Sensor
Advanced
Monitoring Rule Description
Options
Type
No data from all Excluded By default, this rule is configured to trigger when all log sources for
log source(s) Log the specified tenant (or All Tenants) stop sending data. You can use
Source(s) the Excluded Log Source(s) controls to omit specified rules from
the rule's checks.
No data from You can configure a No data from log source(s) rule as either a whitelist using
log source(s) the Included Log Source(s) option or as a blacklist using the Excluded Log
Source(s( option:
Included Alert me ONLY if these specific sources go silent.
Log
Choose the log sources you care about; nothing else is monitored.
Source(s)
This is useful when you have a handful of critical sources (for

Device Sensor
Advanced
Monitoring Rule Description
Options
Type
example, three key firewalls).
The dropdown includes all log sources available to the tenancy
selected in the previous step.
Excluded
Alert me if ANY source goes silent, EXCEPT these.
Log
Monitors all sources globally but suppresses excluded log sources.
Source(s)
The dropdown includes all log sources available to the tenancy
selected in the previous step.
b. Use the Excluded Tenant(s) dropdown to exclude specified tenants from
notifications for this rule.
This option only appears when All Tenants is selected in the first step of the
rule's configuration. It gives you a handy way to omit a few tenants whom
you don't want to notify with a particular rule.
c. Set the No Data and Mute thresholds for the rule:
No Data Specify the amount of time that can pass without log sources sending data before this
Threshold rule is triggered.
Use these options to temporarily silence notifications from the rule for a specified
amount of time. Once the rule is triggered, no new notifications will be generated from
the same rule until the Mute Threshold has passed.
Mute
 Stellar Cyber still monitors the rule for signs of log source activity until the mute
Threshold
threshold passes and restarts the monitoring interval if they are detected. A new
alert is only generated when the Mute Threshold is passed if no activity has been
seen during the monitoring interval.
The image below shows the Advanced step for a No data from all log
source(s) rule:
8. Click Next when you are ready to continue.
9. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.

Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.

Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
10. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a Platform Health Rule
Platform Health rules help you monitor the health of your Stellar Cyber Platform, notifying you
when there are health issues affecting data ingestion, storage, cluster performance, or UI
availability.
 Platform Health alerts are only available as part of an Early Access Program and may not
appear in your version of the Stellar Cyber Platform. Contact your account manager to
inquire about taking part in an Early Access Program.
You can create the following types of Platform Health rules:
Severit
Alert Description Firing Notification Recovery Notification
y
Cluster node is down Get notified when a Critical A cluster node is down – The cluster node has been
cluster node goes platform capacity is temporarily restored and platform capacity
down. reduced and some operations is operating normally.
may be interrupted or slower.
Data cluster health Get notified when the Critical Search and recent data may be Data cluster health has been
degraded data cluster health temporarily unavailable. restored and search and recent

Severit
Alert Description Firing Notification Recovery Notification
y
degrades. data are available.
Data ingestion Get notified when data Critical Data ingestion has dropped to Data ingestion has recovered
decreased ingestion has dropped near zero for at least one hour and events are appearing in the
significantly. – recent events may not appear platform as expected.
in the platform. Verify that your
data sources and sensors are
sending data as expected.
Ingestion delay Get notified when data Warning Data ingestion is delayed Data ingestion delay has
threshold exceeded ingestion delay exceeds beyond the configured returned to within the
the configured threshold – recent events may configured threshold.
threshold. not yet be searchable.
Ingress has high 4xx Get notified when the Warning Platform access is experiencing The 4xx error rate has returned
error rate ingress 4xx error rate a high rate of authentication to within the acceptable
exceeds the threshold. errors. Verify client credentials threshold.
and connectivity, then review
the affected sources in the
System Action Center.
Ingress has high Get notified when Warning The platform is experiencing Ingress latency has returned to
latency ingress latency exceeds high ingress latency and may within the acceptable threshold.
the threshold. be responding slowly.
Message type ingestion Get notified when Warning Ingestion for the specified Ingestion for the specified
decreased ingestion for a specific message type has dropped message type has recovered
message type has significantly — recent events of and events are appearing in the
dropped significantly. this type may not appear in the platform as expected.
platform. Verify that your data
sources are sending data as
expected.
Receiver anomaly Get notified when an Critical An anomaly has been detected The receiver pipeline anomaly
detected anomaly is detected in in the receiver pipeline – data has been resolved and data
the receiver pipeline. ingestion may be delayed or ingestion is operating normally.
incomplete.
Storage nearing Get notified when Warning Storage is nearing capacity – Storage capacity is no longer
capacity storage is nearing its data retention may be affected near its limit and data retention
capacity limit. if unresolved. is not at risk.
UI is unreachable Get notified when the UI Critical The platform console may be The platform console is
becomes unreachable. temporarily unreachable. reachable.

For all rule types, you can also specify a Mute Interval that specifies a window within which a
repeated instance of the same notification will not be generated.
. Use the following procedure to create a Platform Health rule:
1. Click the Create button at the top of the System Action Center and select Platform
Health from the dropdown that appears.
2. Select the type of rule you want to create. See the start of this section for a
description of the rule types.
The Create Notification wizard starts with the Category set to Platform Health and
the Type set to the selected rule type.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant) field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.
7. Set Advanced options for the rule, as described below:
Mute Use these options to temporarily silence notifications from the rule for a specified amount of 24
Threshol time. Once the rule is triggered, no new notifications will be generated from the same rule until hour
d the Mute Threshold has passed. s
8. Use the Suppression step to set up a schedule of times during which notifications
from the rule will not be displayed in the Notification Center or sent to configured
recipients. This can be handy for suppressing notifications from sensors that you
know are normally not seeing any data during specific hours.
The times you configure for the Suppression schedule are specified in browser time.
a. Use the Mute Schedule checkbox to enable or disable suppression for the
rule. When Mute Schedule is checked, you can set up a schedule as
follows:

b. Select a time zone for the schedule from the dropdown. By default, the time
zone is set to your browser's time zone.
c. Use the Start Day/Time and End Day/Time fields to specify a window of
time during which notifications from the rule are not sent.
d. Use the + Row button to add an additional row to the schedule. Each row
creates a new window of time during which notifications from the rule are
not sent.
The figure below shows a sample Suppression schedule configured to
exclude notifications during weekends and late evenings on Monday nights
to Tuesday mornings:
9. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.

Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
10. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.

Creating a Playbook Monitoring Notification Rule
Playbook Status Change rules help you keep tabs on the status of your ATH Playbooks. To
avoid gaps in detection and ingestion, Playbook Monitoring rules alert you when any of the
following status changes occur:
Playbook Status Change Description
Initialization Failed
The playbook did not complete its startup process when it
was created or enabled. Because initialization was
unsuccessful, the playbook cannot run.
This may occur if an error is encountered during setup or if
required system records are not created properly. Until the
underlying issue is resolved, the playbook will remain inactive
and unable to execute.
Consecutive Failures
The playbook has failed multiple times in a row, indicating an
ongoing issue rather than a one-time error.
Repeated failures typically point to configuration problems,
permission issues, integration failures, or logic errors that
need investigation.
High Failure Rate The playbook is failing at a high rate compared to its recent
execution history. By default, this status is triggered when
more than half of the most recent runs have failed.
This signals reduced reliability and suggests that the playbook
may be unstable or inconsistently executing.
Recovered (Informational)
A playbook that was previously failing has successfully
completed its most recent run.
This indicates that the issue affecting earlier executions has
been resolved and the playbook is currently operating as
expected.
Missed Scheduled Run (Error) A scheduled playbook did not execute within its expected time
window. By default, this status is triggered when execution is
more than three minutes late.
This may indicate scheduling delays, system performance
issues, or interruptions that prevented the playbook from
running on time.
Use the following procedure to create a Playbook Monitoring rule:
1. Click the Create button at the top of the System Action Center and select Playbook
Monitoring from the dropdown that appears.
2. The only type of Playbook Monitoring rule is Playbook Status Change. Select that
rule type.

The Create Notification wizard starts with the Category set to Playbook Monitoring
and the Type set to Playbook Status Change.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.
7. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can

click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
8. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a Scheduled Report Monitoring Rule

Scheduled Report Monitoring rules can notify you when a scheduled report has failed, helping
you investigate report generation issues in real time. Scheduled Report Monitoring rules check
for failed reports every five minutes.
. Use the following procedure to create a Scheduled Report Monitoring rule:
1. Click the Create button at the top of the System Action Center and select Scheduled
Report Monitoring | Scheduled report failed from the dropdown that appears.
The Create Notification wizard starts with the Category set to Scheduled Report
Monitoring and the Type set to Scheduled report failed.
2. Supply a name for your notification rule in the Name field.
3. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant) field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
4. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
5. Click Next.
6. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:

Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:

Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
7. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a Sensor Token Rule
Sensor Token rules notify you three days before a token is about to expire. Tokens are used to
authorize sensor installations.
Use the following procedure to create a Sensor Token rule:
1. Click the Create button at the top of the System Action Center and select Sensor
Token from the dropdown that appears.
2. The only rule available in the Sensor Token category is Token is about to expire.
This rule notifies you when a token is three days from expiring.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant) field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.

6. Click Next.
7. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not

check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
8. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a Server Sensor Monitoring Rule
Server Sensor Monitoring rules help you monitor the health of your Server Sensors, notifying
you when they are either offline or haven't sent data within a specified amount of time.
 Server Sensor Monitoring rules only work for server sensors. They are not supported for
Device Sensors (dedicated sensors).
You can create the following types of Server Sensor Monitoring rules:
No data from server sensor(s) – This rule is triggered when a server sensor has not
sent a record with traffic within a specified interval.
No heartbeat from server sensor(s) – This rule is triggered when Stellar Cyber has
not received a heartbeat message from a server sensor within a specified interval.
 Notice that these rules are monitoring for different types of inactivity. When a No
data from server sensor(s) notification is generated, Stellar Cyber may still have

contact with the affected Server Sensor but is not receiving records with traffic. In
the case of the No heartbeat from server sensor(s) notification, Stellar Cyber is
not receiving heartbeats from affected Server Sensors and has not had contact
within the specified monitoring interval.
For both the No data and No heartbeat rules, you can also specify a Mute
Intervalthat specifies a window within which a repeated instance of the same
notification will not be generated.
Server sensor status change – This rule is triggered when the status of a Server
Sensor is either yellow or red, as defined below. A new notification is generated
every five minutes the sensor remains in one of these states. You can investigate
further in the Sensor list.
Yellow – At least one warning condition is affecting the sensor.
Click here to see the possible warning conditions:
Sensor disk usage exceeds 90%
Sensor CPU usage exceeds 99%
Sensor feedback contains a config mismatch error message
Sensor has not updated its status in at least five minutes
Sensor feedback shows a failure to apply a profile with the
Tenable Nessus feature enabled to a sensor running version
4.3.3 or lower (Tenable Nessus support was introduced in 4.3.4)
Sensor feedback contains at least one warning message
Red – At least one danger condition is affecting the sensor.
Click there to see the possible danger conditions:
Sensor has an invalid Engine ID (engid)
Sensor has a conflicting Engine ID (engid)
Sensor configuration is out of sync (either the ver_sent does
not match received ver_ack or one of the two messages is
missing)
Sensor memory usage exceeds 95%
Sensor feedback contains a config failure message
Sensor feedback shows at least one failure during the
application of a new sensor profile.
 The exception to this is a failure to apply a modular sensor
profile with the Tenable Nessus feature enabled to a sensor
running 4.3.3 or lower. Those failures are reported as
warnings and only display the yellow LED, as described
above.
Use the following procedure to create a Server Sensor Monitoring rule:

1. Click the Create button at the top of the System Action Center and select Server
Sensor Monitoring from the dropdown that appears.
2. Select the type of rule you want to create. See the start of this section for a
description of the rule types.
The Create Notification wizard starts with the Category set to Server Sensor
Monitoring and the Type set to the selected rule type.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant) field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.
7. Set Advanced options for the rule, as described below:
All rules include the Excluded Sensors option, with a dropdown that lets
you exclude specified sensors from monitoring. The list includes all sensors
available to the tenant selected in the first step of the wizard.
Rules with All Tenants selected in the first step include the Excluded
Tenants option, with a dropdown that lets you exclude sensors assigned to
a specified tenant from monitoring. This gives you a handy way to assign a
rule to all but a few excluded tenants.
Some of the rules include additional options, as summarized in the table
below:

D
ef
au
Server Sensor Monitoring Rule Type Advanced Options Description lt
Va
lu
e
No data from server sensor(s) Specify the amount of 1
time that can pass ho
without a server ur
No Data Threshold sensor sending a
record with traffic
before this rule is
triggered.
Mute Threshold Use these options to 1
temporarily silence ho
notifications from the ur
rule for a specified
amount of time. Once
the rule is triggered,
no new notifications
will be generated from
the same rule until the
Mute Threshold has
passed.
 Stellar Cyber still
monitors the rule
for signs of
activity from the
sensor until the
mute threshold
passes and
restarts the
monitoring
interval if they
are detected. A
new alert is only
generated when
the Mute
Threshold is
passed if no
activity has been
seen during the

D
ef
au
Server Sensor Monitoring Rule Type Advanced Options Description lt
Va
lu
e
monitoring
interval.
No heartbeat from server sensor(s) No Heartbeat Threshold Specify the amount of 4
time that can pass ho
without a server urs
sensor sending a
heartbeat before this
rule is triggered.
Mute Threshold Use these options to 24
temporarily silence ho
notifications from the urs
rule for a specified
amount of time. Once
the rule is triggered,
no new notifications
will be generated from
the same rule until the
Mute Threshold has
passed.
 Stellar Cyber still
monitors the rule
for heartbeats
from the sensor
until the mute
threshold
passes and
restarts the
monitoring
interval if they
are detected. A
new alert is only
generated when
the Mute
Threshold is
passed if no
heartbeats have

D
ef
au
Server Sensor Monitoring Rule Type Advanced Options Description lt
Va
lu
e
been seen
during the
monitoring
interval.
The image below shows the Advanced step for a No data from server sensor(s)
rule:
8. Use the Suppression step to set up a schedule of times during which notifications
from the rule will not be displayed in the Notification Center or sent to configured
recipients. This can be handy for suppressing notifications from sensors that you
know are normally not seeing any data during specific hours.
 The times you configure for the Suppression schedule are specified in browser
time.
a. Use the Mute Schedule checkbox to enable or disable suppression for the
rule. When Mute Schedule is checked, you can set up a schedule as
follows:
b. Select a time zone for the schedule from the dropdown. By default, the time
zone is set to your browser's time zone.
c. Use the Start Day/Time and End Day/Time fields to specify a window of
time during which notifications from the rule are not sent.
d. Use the + Row button to add an additional row to the schedule. Each row
creates a new window of time during which notifications from the rule are
not sent.
The figure below shows a sample Suppression schedule configured to exclude
notifications during weekends and late evenings on Monday nights to Tuesday
mornings:

9. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:

Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
10. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a TIP Feed Monitoring Notification Rule
TIP Feed Monitoring rules help you keep tabs on the status of your configured TIP feeds. You
can create the following types of TIP Feed Monitoring rules:
No data from TIP feed – Get notified when a TIP feed does not respond with new
indicators of compromise across a configurable number of recent polls (default 4,
range 1-24).
TIP feed received error – Get notified when a TIP feed receives an error during a
poll (error codes 401, 403, or 500).
Use the following procedure to create a TIP Feed Monitoring rule:

1. Click the Create button at the top of the System Action Center and select TIP Feed
Monitoring from the dropdown that appears.
2. Select the type of TIP Feed Monitoring rule you want to create.
The Create Notification wizard starts with the Category set to TIP Feed Monitoring
and the Type set to the rule type you selected.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Set the options in the Advanced step corresponding to your selected rule type:
Def
aul
TIP Feed Monitoring Rule Type Advanced Options Description t
Val
ue
No data from TIP feed Specify the number of 4
successive polls
without receiving
No Data Polls
updated IOCs at
which this rule will
trigger a notification.
TIP feed received error N/A
No configurable N/A
options. Rule triggers
on error codes 401,
403, or 500.
7. Click Next when you are ready to continue.
8. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.

Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list
containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.

You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.
9. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Creating a User Modifications Rule
User Modification rules help you monitor a wide variety of changes and events related to user
accounts, giving you a powerful audit trail for identity management.
You can create the following types of User Modification rules:
Account lockout triggered – This rule is triggered when a user's account is locked
out due to excessive failed login attempts.
Account password change – This rule is triggered when an account's password
has been changed.
New RBAC profile created – This rule is triggered when a new RBAC profile is
created.
New user created – This rule is triggered when a new user account is created.
RBAC profile deleted – This rule is triggered when an RBAC profile is deleted.
User RBAC privilege escalation – This rule is triggered when the a user's RBAC
profile is changed to one with increased capabilities in the platform (for example, from
User to Platform Admin).
User deleted – This rule is triggered when a user account is deleted.
User has disabled 2FA – This rule is triggered when two-factor authentication is
disabled for a user account.
 For all User Modification rules, new notifications are sent every five minutes.

. Use the following procedure to create a User Modifications rule:
1. Click the Create button at the top of the System Action Center and select User
Modifications from the dropdown that appears.
2. Select the type of rule you want to create. See the start of this section for a
description of the available rule types.
The Create Notification wizard starts with the Category set to User Modifications
and the Type set to the selected rule type.
3. Supply a name for your notification rule in the Name field.
4. Select the Tenant to which the rule applies. By default, All Tenants are selected.
Click anywhere in the Tenant) field to display a pick list including all tenants available
on the system where you can select the tenant to which this rule applies.
5. You can either accept the system-provided Description or supply your own. The
description supplied here appears in the System Action Center's table of rules.
6. Click Next.
7. Use the Actions step to specify how this rule notifies you when it is triggered:
All rules have In Platform enabled so that triggered instances appear in the
Notification Center.
Click the Add Configuration button and choose whether to add an Email or
Slack action, as illustrated below.
Set the following options for an Email action in the Notification
Type: Email section:
Check the Send individual email for each notification option if
you would like to send separate emails for each triggered instance
of the rule. If you do not check this option, the System Action
Center sends a consolidated email listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify who will receive a notification
email when the rule is triggered. Click to display a pick list

containing all email recipients configured in the System |
Recipients page. If you want to send an email to someone who is
not already configured in the Recipients page, you can also type
addresses in manually.
Use the Subject field to specify the subject line of the email. If you
want to use different subject lines for different recipients, you can
click the Add Configuration button and add a second Email
notification with a different subject line and set of addressees.
The figure below shows a configured Email notification:
Set the following options for a Slack action in the Notification Type: Slack
section:
Check the Send individual Slack messages for each
notification option if you would like to send separate Slack
messages for each triggered instance of the rule. If you do not
check this option, the System Action Center sends a consolidated
Slack message listing all matching events.
 Refer to Consolidated or Individual Notifications for details.
Use the Recipients field to specify the Slack channel or user that
will receive a message when the rule is triggered.
You can click to display a pick list containing all Slack recipients
configured in the System | Recipients page. You can also manually
type in the URL for an incoming webhook that you create in the
Slack API .
The figure below shows a configured Slack notification:
Email and Slack messages both include a summary of the event(s) that
triggered the notification and a link back to the Stellar Cyber platform to a
location that makes sense based on the type of notification that was
generated. You can configure a rule with any combination of email and
Slack messages, including multiple destinations.

8. Click Next and review the settings for your notification rule. Use the Back button to
go back and correct anything that's not quite right. When you are satisfied, click
Submit to add your rule to the list.
The rule appears in the System Action Center's list and is automatically Enabled.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  