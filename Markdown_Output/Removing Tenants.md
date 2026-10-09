Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Removing Tenants

 Only administrative users with a Root scope and Super Admin or Platform Admin privileges
can delete tenants and clear database indices on System | Data Tenants. All other types of
users can see the page but cannot delete tenants or clear database indices.

When you completely remove a tenant from Stellar Cyber, all of the objects configured for it are
automatically removed such as charts, reports, dashboards, connectors, custom log parsers,
sensors, and admin users. As a safety measure, because the delete function is not reversible, a
list of objects is displayed for review prior to completing the action.

For objects that a tenant is allowed to access but is not the sole user (such as those
assigned to All Tenants), the tenant is removed from the object; the object itself is not
deleted.

When the tenant being removed is the only remaining tenant in a group, that tenant
group is also removed along with the partner user managing the group.

Authentication objects associated with the tenant, such as IdP certificates are also
automatically removed when the tenant and its users are removed.

Stellar Cyber also gives you the option to clear one or more of its database indices. This purges
data in the Records, Assets, Users (that is, “Asset Users”), and Cases. For compliance
purposes, you might need to keep this data for a certain length of time after deleting the tenant. If
so, then leave all the indices unselected.

1. Select System | ORGANIZATION MANAGEMENT | Tenants.

The table of tenants is displayed.

2. Select  on the row for that tenant.

A Deletion Confirmation dialog box appears with a list of objects associated with the
selected tenant. Note that certain objects are listed as a count, such as assets, rather
than by name

3. Review the list and, optionally, visit the management page for the object to reassign it to

another tenant, or All Tenants, or to export it (where applicable).

 The delete is not reversible, so review the objects before you proceed.

Automation | Automation (ATH playbooks)

Reporting | Reports

Respond | Scheduled Reports

System | ORGANIZATION MANAGEMENT | Tenant Groups

System | ORGANIZATION MANAGEMENT | Users

System | DATA SOURCE MANAGEMENT | Data Filters | Log Filters

System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles

System | DATA SOURCE MANAGEMENT | Sensors | Sensors

System | DATA SOURCE MANAGEMENT | Traffic Filters | Custom
Applications

System | DATA SOURCE MANAGEMENT | Datata Filters | Traffic Filters |
Application Groups

System | Saved Objects | Watchlists

System | Saved Objects | Queries and Filters

System | Recipients

System | Saved Objects | Saved Scripts

System | DATA MANAGEMENT | Enrichments

System | INTEGRATIONS | Connectors

System | Saved Objects | Charts

Dashboards | CREATION | Dashboards

4. Below the list of objects in the Deletion Confirmation dialog box, select any database
indices you want to clear—Records, Assets, Users (that is, “Asset Users”), and
Cases.

5. After you are ready to proceed with the delete, select Yes, permanently remove this

tenant.

When you purge data and delete a tenant, Stellar Cyber displays the progress of the
data purge and tenant deletion in a Task List panel. If both tasks succeed, the task list
indicates that the data was cleared and Stellar Cyber automatically removes the tenant
from the System | ORGANIZATION MANAGEMENT | Tenants page. Stellar Cyber
keeps any data not selected for deletion for the remainder of its configured retention
cycle and then eventually deletes it as well.

If one or both of the data purge and tenant deletion tasks are unsuccessful, the task list
indicates that an error occurred. The tenant configuration remains on the Tenants page
as an inaccessible entry with the reason for the failure summarized in the Message
column. If this happens, contact Stellar Cyber Customer Services for assistance.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

