✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Using InSyncs
InSyncs synchronizes ServiceNow and Stellar Cyber to streamline case management and
enhance communication between the two systems.
Using InSyncs, you can:
Open and close a Stellar Cyber case in ServiceNow.
Update a case in Stellar Cyber, which updates a ticket in ServiceNow.
Request information from ServiceNow and update the Activity Log in Stellar Cyber.
Retrieve data from ServiceNow data tables to update cases in Stellar Cyber.
Post data from Stellar Cyber cases to update ServiceNow data tables.
Delete a Stellar Cyber case, which deletes a case in ServiceNow.
To ensure the data is synchronized, Stellar Cyber listens for updates from ServiceNow and
updates the Stellar Cyber cases or alerts every five minutes when changes occur. Updates from
Stellar Cyber to ServiceNow are performed live and are applied immediately.
For more information, see the following:
Using the InSyncs Table
Configuring InSyncs
Automatically and Manually Synchronizing
Viewing InSyncs in Alerts
Viewing InSyncs in Cases
Using the InSyncs Table
To configure and view integration syncs, select System | INTEGRATIONS | InSyncs.
The InSyncs Overview table is displayed in the InSyncs tab.

The InSyncs Overview table has the following columns:
Name—name of the integration sync (or InSync)
Tenant Name—name of the tenant. All Tenants means that the integration sync can be
used across tenants.
Status—status of the integration sync:
Success (green)
Error (red)
Inactive (gray)
Messages—messages about the Status
Type—type of integration sync, such as ServiceNow
Pause/Sync—toggle of the integration sync
Actions—actions available for an integration sync, such as Edit this row, Delete this
row, or Test.
Using Search
Use the Search box to search for information about an InSync.
Using Filters
Click the Filters icon ( ) to use defined filters.
To use defined filters:
For Name, select the name of an integration sync using the check boxes or Select All.
The number of integration syncs of each name is displayed on the right.

For Tenant Name, select All Tenants or enter the name of a tenant in the Search box.
For Status, select the status using the check boxes or Select All. The number of
integration syncs of each status is displayed on the right.
For Messages, select the message using the check boxes or Select All. The number of
integration syncs of each message is displayed on the right.
For Type, select the type using the check boxes or Select All. The number of
integration syncs of each type is displayed on the right.
For Pause/Sync, select either Pause or Sync using the check boxes or Select All. The
number of integration syncs of each toggle is displayed on the right.
You can click Add new filter to deselect a filter in the dropdown menu.

You can also type in the Add new filter box to search for a filter.
To exit, click the Filter icon again. The configured filters are displayed at the top of the table.
To clear an individual filter, click the icon to the right of the filter ( ).
To clear all filters, click Clear All.
Using Columns
Click the Columns icon ( ) to add or remove columns in the table using check boxes.
To exit, click the Columns icon again.
Pausing InSyncs
To pause an integration sync, click the toggle in the Pause/Sync column from Sync to Pause.
Starting InSyncs
To start an integration sync, click the toggle in the Pause/Sync column from Pause to Sync.
Editing InSyncs
To edit an existing integration sync, click the Edit icon ( ) on a row in the table. The Edit
ServiceNow InSync dialog displays.

To create an integration sync, see Configuring InSyncs.
Deleting InSyncs
To delete an integration sync, click the Trash icon ( ) in the Actions column for a row in the
table.
Testing InSyncs
To test the integration sync, click Test. A message displays.
 Test only validates credentials, whereas Status reflects the import and export of data
between ServiceNow and Stellar Cyber. Even when the integration sync is in Error status,
the credential test can be successful.
Exporting CSV
Click Export CSV to export the table as a spreadsheet file.
You can export Selected Columns or All Columns. The spreadsheet is downloaded to your
Downloads folder.
Selecting View
Click Select View to preserve a table layout. See Saved View Configurations for details.
Configuring InSyncs
You can create up to three InSyncs. During the configuration, you will authenticate the user with
ServiceNow, select the type of integration sync (alerts, cases, or both), and provide the name of
a ServiceNow alert database table, case database table, or both.
You need a User role that has access to the system dictionary to read field attributes for InSyncs
configuration. If you know the name of the ServiceNow table, you need a User role that has
access to the table (for reading, creating, and deleting the records in that table). To create a non-
admin user and assign roles to it, refer to Creating an App, Tables, and a Default User Role and
Creating a Non-Admin User and Assigning a Role.
 Make sure that the rules created in ServiceNow will not interfere with the creation of records
in the table. If a ServiceNow rule requires certain fields to be populated, and if those fields
are not available on Stellar Cyber, the record may not be created.
To create an integration sync:
1. Click Create.

The asterisk (*) indicates a required field.
2. Enter a unique name for the integration sync in the InSync Name field.
3. (Optional) You can toggle Sync after creation to disabled. It is enabled by default.
4. Click Next.
The asterisk (*) indicates a required field.
5. The authentication type is Basic, which is already selected.
6. Enter the URL to which to synchronize, for example, https://myaccount.service-
now.com.
7. Enter the Username.
8. Enter the Password.
9. (Optional) You can toggle Sync after creation to disabled. It is enabled by default.
10. Click Next.
11. Select the type of configuration using the buttons for Cases, Alerts, or Both.
Depending on your selection, the configuration options are:
For Cases:
a. (Optional) Select Filters by categories, score, tenant. You can select filters
by Assignee, Severity (Critical, High, Medium, or Low), or Status (Escalated,
New, In Progress, Resolved, or Canceled). You can also Select All. The
default is all the case filters.
b. Select Tenant. You can filter by specific tenants, tenant groups, or all tenants.

To select all tenants, select All Tenants. If you select All Tenants,
you cannot select specific tenant groups or tenants (because they are
already included in all).
To select specific tenant groups, select them from the Tenant Groups
list. You can select one or more tenant groups.
To select specific tenants, select them from the Tenants list. You can
select one or more tenants.
The resulting list can include a mix of tenant groups and tenants. If
there is any overlap between tenant groups and tenants, the
duplicates are filtered out. Tenant Groups are prefixed with Group.
c. Select a Score range from 0 to 100 using the slider.
d. Enter the name of a Case database table in ServiceNow from which to collect
data, then click Confirm to verify the database table. A message displays if the
database table cannot be found or if fields in the database table cannot be
found. To obtain table names, see Obtaining ServiceNow Table Names.
The asterisk (*) indicates a required field.
 If the ServiceNow database table is created from an extensible table, only
the fields created from the current table, not the parent table, can be used
for field mapping.
e. For Field Mapping, match the fields on Stellar Cyber and ServiceNow to
synchronize them. If the fields do not match, they will not be synchronized.
Stellar Cyber sends their status to ServiceNow. If the ServiceNow status is
changed or updated to a status that matches in Stellar Cyber (case-sensitive),
it updates.
The Stellar Cyber fields are on the left side of the Field Mapping table, the
arrows in the center of the table indicate the direction of the field mapping, and
the ServiceNow fields are on the right side of the table.
In this example, the Stellar Cyber Case Name field is mapped to Name in
ServiceNow with bidirectional synchronization (Case Name to Name and

Name to Case Name) and the Tenant Name is mapped to Description with
unidirectional synchronization.
 Unmapped means that the selected field maps to Null.
In the Field Mapping table, you can select the ServiceNow fields from the
dropdown menus, which have different options depending on the ServiceNow
database table.
With field mapping, a field type of string can only map to a string field.
Likewise, a URL field can only map to a URL. Date and time must follow a
specific format. For details, see Supported Field Types.
For Alerts:
a. (Optional) Select Filters by categories, score, tenant. You can select filters
by Source (Built-in or Custom) or Status (Closed, Ignored, In Progress, or
New). You can also Select All. The default is all the alert filters.
b. Select Tenant. You can filter by specific tenants, tenant groups, or all tenants.
To select all tenants, select All Tenants. If you select All Tenants,
you cannot select specific tenant groups or tenants (because they are
already included in all).
To select specific tenant groups, select them from the Tenant Groups
list. You can select one or more tenant groups.
To select specific tenants, select them from the Tenants list. You can
select one or more tenants.
The resulting list can include a mix of tenant groups and tenants. If
there is any overlap between tenant groups and tenants, the
duplicates are filtered out. Tenant Groups are prefixed with Group.
c. Select a Score range from 0 to 100 using the slider.
d. Enter the name of an Alert database table in ServiceNow from which to
collect data, then click Confirm to verify the database table. A message

displays if the database table cannot be found or if fields in the database table
cannot be found. To obtain table names, see Obtaining ServiceNow Table
Names.
The asterisk (*) indicates a required field.
 If the ServiceNow database table is created from an extensible table, only
the fields created from the current table, not the parent table, can be used
for field mapping.
e. For Field Mapping, match the fields on Stellar Cyber and ServiceNow to
synchronize them. If the fields do not match, they will not be synchronized.
Stellar Cyber sends their status to ServiceNow. If the ServiceNow status is
changed or updated to a status that matches in Stellar Cyber (case-sensitive),
it updates.
The Stellar Cyber fields are on the left side of the Field Mapping table, the
arrows in the center of the table indicate the direction of the field mapping, and
the ServiceNow fields are on the right side of the table.
In this example, the Stellar Cyber Alert Name field is mapped to alert name in
ServiceNow with unidirectional synchronization and the Assignee is mapped to
Updated by with bidirectional synchronization (Assignee to Updated by and
Updated by to Assignee).
 Unmapped means that the selected field maps to Null.
In the Field Mapping table, you can select the ServiceNow fields from the
dropdown menus, which have different options depending on the ServiceNow
database table.
With field mapping, a field type of string can only map to a string field.
Likewise, a URL field can only map to a URL. Date and time must follow a
specific format. For details, see Supported Field Types.
For Both:
a. Click the Cases tab to configure the same fields as for Cases above.

b. Click the Alerts tab to configure the same fields as for Alerts above.
12. (Optional) You can toggle Sync after creation to disabled. It is enabled by default.
13. Click Submit. Once an InSync is created, you can view it in Alerts.
Creating an App, Tables, and a Default User Role
You can create a default user role, which you will need to assign to a non-admin user, when you
create an app.
To create an app, the alert and cases database tables, and a default user role:
1. In the App Engine Studio, click Create app.
2. Enter a name for the app and click Continue.
3. An admin role name and a user role name are automatically created. You can change
the name of the user role name and click Continue.
4. Wait for the app to be created, then click Go to app dashboard.
5. Create two database tables, one for alerts and one for cases. To get started, click Add
in the Data section.

6. Click Create a blank table and click Continue.
7. Click Create new table and click Continue.
8. Give the table a name, such as Cases, and click Continue.
9. Add permissions to your table. Select All for both the admin role and the user role, then
click Continue.
10. Wait for the table to be added, then click Edit table.

11. Add the columns to the table that are listed in Supported Field Types. (There are
different supported field types for cases and for alerts.) To get started, click Add field.
12. Enter the Column label and Column name, select a Type, and click Add.
13. The column is added. Click Add field to continue adding columns to the table.
14. You can go to the App Home to see the created table.
15. To create another table, such as Alerts, click Add.
16. Repeat the previous steps to create the other table and add the columns to it. When
finished, there are two tables, one for Cases and one for Alerts.
17. Click the Security tab. (To access this tab, you must be an admin user.) The Default
user role needs to be assigned to a user. Go to the procedure for Creating a Non-Admin
User and Assigning a Role.
Creating a Non-Admin User and Assigning a Role

You need a User role that has access to the system dictionary to read field attributes for InSyncs
configuration. If you know the name of the ServiceNow table, you need a User role that has
access to the table (for reading, creating, and deleting the records in that table).
To create a non-admin user and assign roles to it:
1. In ServiceNow, click the All tab, and search for Users under User Administration.
2. Click New.
3. Enter the information for the new user and click Submit.
4. Locate the user you created.
5. Select the user to edit it, then select the Roles tab and click Edit.
6. Search in the Collection for the personalize_dictionary. Also search for a previously
created role, which will start with x_ and have the previously created role as part of the
role name (a sys_id). Click the right arrow (>) to move a role from the Collection to the
Roles List.

7. Click Save. The roles are added.
8. You can also add additional roles, but these two roles are required.
 To set a password for the user at this time, you can click Set password.
Obtaining ServiceNow Table Names
If you know the name of the ServiceNow table, you need a User role that has access to the table
(for reading, creating, and deleting the records in that table). If you do not know the name of the
ServiceNow table, you need an Admin role to obtain it.
In the following procedure, the menu item for System Definition | Tables is only displayed for a
User Role of Admin in ServiceNow.
For example, to change your role to Admin if your role was App Engine Studio Creator,
navigate to Change User Role. click Admin, and then click Change User Role.
To obtain table names in ServiceNow:
1. In the main ServiceNow browser window, navigate to the All menu, click System
Definition, and then click Tables.
2. In the Tables list, click the table Label.
3. Note the table Name.

Supported Field Types

Note the following:
It is recommended you configure URL fields with URL type and other string fields
with String (Full UTF-8) type.
The date and time format must be %Y-%m-%d %H:%M:%S. See Changing the
System Time Format for details.
The following table describes the supported field types for cases.
|     | Stellar |     | Direct |
| --- | ------- | --- | ------ |
Field Name Stellar Cyber Field Type ServiceNow Field Types Supported
|           | Cyber Field  |        | ion                                        |
| --------- | ------------ | ------ | ------------------------------------------ |
| Case Name | name         | string | Both String, String (Full UTF-8)           |
| Who       | details.who  | list   | Out String, String (Full UTF-8)            |
| What      | details.what | list   | Out String, String (Full UTF-8)            |
| When      | details.when |        | Out String, String (Full UTF-8), Date/Time |
int
| Where    | details.where | list   | Out String, String (Full UTF-8)  |
| -------- | ------------- | ------ | -------------------------------- |
| Severity | severity      | string | Out String, String (Full UTF-8)  |
| Status   | status        | string | Both String, String (Full UTF-8) |
| Assignee | assignee_na   | string | Both String, String (Full UTF-8) |
me
Score score float Out String, String (Full UTF-8), Decimal, Floating Point
Number, Integer, Long
Stellar Case case_url string Out URL, String, String (Full UTF-8)
URL
| Case ID          | ticket_id    | string  | Out String, String (Full UTF-8) |
| ---------------- | ------------ | ------- | ------------------------------- |
| Tenant ID        | cust_id      | string  | Out String, String (Full UTF-8) |
| Close All Alerts | update_alert | boolean | Both                            |
Boolean
s
(set to true to close all alerts)
Tenant Name tenant_name string Out String, String (Full UTF-8)
| Comments |     | list | Both |
| -------- | --- | ---- | ---- |
stellar_com
Journal
ments
| Activities |     | list | Out |
| ---------- | --- | ---- | --- |
activities
Journal

|     | Stellar |     | Direct |
| --- | ------- | --- | ------ |
Field Name Stellar Cyber Field Type ServiceNow Field Types Supported
|              | Cyber Field |        | ion |
| ------------ | ----------- | ------ | --- |
| Last Updated | last_comme  | string | Out |
String, String (Full UTF-8)
Comment
nt
The following table describes the supported field types for alerts.
Stellar Cyber Directi
Field Name Stellar Cyber Field ServiceNow Field Types Supported
Field Type on
Alert Name xdr_event.display_na string Out String, String (Full UTF-8)
me
Alert Description xdr_event.description string Out String, String (Full UTF-8)
Stage xdr_event.xdr_killchai string Out String, String (Full UTF-8)
n_stage
Tactic xdr_event.tactic.name string Out String, String (Full UTF-8)
Technique xdr_event.technique.n string Out String, String (Full UTF-8)
ame
Score event_score float Out String, String (Full UTF-8), Decimal, Floating Point
Number, Integer, Long
Fidelity fidelity float Out String, String (Full UTF-8), Decimal, Floating Point
Number, Integer, Long
Severity severity int Out Integer, String, String (Full UTF-8)
Threat Intel threat_score int Out Integer, String, String (Full UTF-8)
| Data Period | data_period  | int    | Out String, String (Full UTF-8) |
| ----------- | ------------ | ------ | ------------------------------- |
| Status      | event_status | string | String, String (Full UTF-8)     |
Both
| Assignee | assignee | string | Both String, String (Full UTF-8) |
| -------- | -------- | ------ | -------------------------------- |
Alert URL alert_url string Out URL, String, String (Full UTF-8)
| Tenant ID | tenantid  | string | Out String, String (Full UTF-8) |
| --------- | --------- | ------ | ------------------------------- |
| Case ID   | ticket_id | string | Out                             |
String, String (Full UTF-8)
Tenant Name tenant_name string Out String, String (Full UTF-8)
| Comments |     | list | Both |
| -------- | --- | ---- | ---- |
stellar_comments
Journal
| Activities | activities | list | Out |
| ---------- | ---------- | ---- | --- |
Journal
| Last Updated | last_comment | string | Out |
| ------------ | ------------ | ------ | --- |
String, String (Full UTF-8)
Comment
Changing the Date and Time Formats
The date and time must be in the format: %Y-%m-%d %H:%M:%S. To change the date and time
 and
formats, refer to the ServiceNow documentation to Personalize the system date format
Personalize the system time format .

Automatically and Manually Synchronizing
Synchronizing an alert or a case from Stellar Cyber to ServiceNow is fully automated. It is based
on the configuration detailed in Configuring InSyncs. As an example, during configuration you
select the tenant that you want to synchronize, then, if there is a new alert or a new case
belonging to that tenant, it will be synchronized with ServiceNow automatically.
An alert or a case may not be synchronized if it does not satisfy the requirements specified in the
configuration. That is, there may be one alert or one case that does not belong to any of the
existing configurations.
You can manually synchronize an alert or a case if it cannot be synchronized automatically. The
single alert or case can be pushed manually to the existing ServiceNow integrations using a
Sync to ServiceNow button. This button provides a way to manually synchronize an alert or a
case from Stellar Cyber to create a ServiceNow ticket with a single button push. This action will
ensure the alert or case is immediately pushed to ServiceNow and linked appropriately.
 T he manual push is not for pushing changes in order to synchronize immediately. It is for an
alert or a case that cannot be synchronized to any InSync configuration automatically.
Once an alert or a case is manually or automatically synchronized with ServiceNow, any
future changes to it will be automatically synchronized.
In addition, the manual synchronization does not consider any filtering selected in the InSync
configurations.
All eligible InSync configurations will synchronize the alert or case after a manual push. Eligibility
refers to the tenant scope, meaning the scope of the configuration itself, such as All Tenants.
See the following:
Manually Pushing an Alert
Manually Pushing a Case
Viewing InSyncs in Alerts
Click Alerts to go to the Alerts page. At the top of the page, there is a status indicator for the
integration syncs as well as a button you can click to go back to the InSyncs page.
In each indicator, the name of the InSync is listed. There is a count of the number of alerts that
have been synced using this InSync and a timestamp of the last synchronization.

The status is indicated in the circle around the NOW icon:
A green circle indicates a Synced status.
A gray circle indicates a Paused status.
A red circle indicates an Error status.
Viewing the Alert Type Table
At the bottom of the Alerts page, click View on a specific alert type in the table to go deeper into
the alert. For example, click View on the row for the alert type Emerging Threat.
Scroll to the bottom of the Alerts table. The table has an InSyncs column showing the alerts that
have been synced. When you hover over a NOW icon in the InSyncs column, an indicator is
displayed with the status, Ticket ID, and Last Synced date and time for each alert.
Viewing Alert Details
In the Actions column of the table, click i to display alert details. In the Alert Details page, when
you hover over the NOW icon, an indicator is displayed with the status, Ticket ID, and Last
Synced date and time.
If you want to copy the ticket ID, click the JSON tab and search for insyncs and locate the
source_id field.
The JSON also contains the ServiceNow link (source_link).

Manually Pushing an Alert
The manual Sync to ServiceNow button is visible in the Actions tab when an alert cannot be
synchronized to any InSync configuration automatically.
After clicking the Sync to ServiceNow button and if the manual synchronization is successful,
the button is hidden and the ServiceNow icon displays on the top of the Alert Details page.
 Either a Sync to ServiceNow button or a ServiceNow icon displays on the Alert Details
page, but not both at the same time.
Adding a New Case from Alerts
From the Alerts page, you can add a new case. The new case will be created and synchronized
automatically with ServiceNow.
Select a row in the Alert Details table, click Add to Case, and select New Case.
Viewing InSyncs in Cases
This section describes how InSyncs are integrated into the Cases displays. Start by clicking
Cases to go to the Cases page. Then, refer to the sections below for information on the
integrations provided for InSyncs.
InSyncs in the Case Queues Panel
At the top of the Case Queues panel, there is an InSyncs button that you can click to navigate to
the InSyncs page.
InSyncs Column in the Cases Table

The Cases table has an InSyncs column showing the cases that have been linked (if the
InSyncs column doesn't appear, you may need to add it using the column selector). When you
hover over an icon in the InSyncs column, the status, Ticket ID, and Last Synced date and time
for the InSync are displayed.
Click a Case Name in the Cases table to go to the Case Details page.
Manually Pushing a Case from Case Details
In the Case Details page, the manual Sync to ServiceNow button is visible when an alert
cannot be synchronized to any InSync configuration automatically.
After clicking the Sync to ServiceNow button and if the manual synchronization is successful,
the button is hidden and the ServiceNow icon displays in the same area of the Case Details
page.
 Either a Sync to ServiceNow button or a ServiceNow icon displays on the Case Details
page, but not both at the same time.
Viewing InSyncs in Case Details
You can scroll to the bottom of the Case Details page to see the Associated Alerts table with a
separate row for each alert associated with the case. The table has an InSyncs column showing
the alert that has been synced. When you hover over a NOW icon in the InSyncs column, the
status, Ticket ID, and Last Synced date and time are displayed.

Note that the alerts that are correlated to cases are those that can also be synchronized to
ServiceNow.
 Cases are created for all alerts except those from the Sensor Monitoring index. See Alerts
Correlated to Cases.
Viewing Case Activity
Scroll to the right on the Case Details page. Click the icon ( ) for Case Activity. The Case
Activity is displayed.
Viewing the ServiceNow Record
Click the Ticket ID link in the status indicator on the Case Details page to open the ServiceNow
record.
If you added a new case, it is added to the ServiceNow table. You may have to refresh the
window.
Updating the Case Name Example
As an example, you can change the name of a case in Stellar Cyber and see it changed in
ServiceNow:

1. Click on the name of a case in the Case Details page, then type a new case name in
Stellar Cyber.
2. The case name in ServiceNow is updated. You may have to refresh the window.
Viewing Cases in ServiceNow
In ServiceNow, you can preview cases. This provides a view of the data from Stellar Cyber in
ServiceNow.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  