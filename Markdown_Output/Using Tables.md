Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using Tables

Tables appear on many different pages in many different contexts, from tables of users to tables
of events. This page describes how to work with tables in Stellar Cyber.

Common Controls
Several controls appear on most tables, allowing you to control the table itself:

Use Search to use Lucene syntax  to search within all pages of table (not just the
currently displayed page).

Click Export CSV to download the table as a CSV file, suitable for import to a
spreadsheet application. You can choose to export the table with the displayed columns
only, or all columns, even if not displayed.

 You can export up to 100,000 rows of a table displaying Interflow data (for example,
the table available in the Alerts page). For all other tables (for example, the System |
DATA SOURCE MANAGEMENT | Sensors | Sensors table), there is no export limit.

Use Select View or Saved Views and save time by preserving your table layout—
columns, filters, and sorting—for quick reuse across sessions and pages.

 and
Click the column name to sort the table on that column. The
which column is being sorted on, as well as the direction of the sort.

 buttons tell you

Tables listing alerts include an Add to Case button that lets you either create a new
case based on the selected alerts or add them to an existing case.

Tables often include a vertical Columns and/or Filters button at the left of the table:

Use the Columns button to toggle the Column Selector panel open and
closed. The Column Selector panel lets you choose which columns to include
in the table. Most Stellar Cyber tables include this button.

Use the Filters button to toggle the Filters panel open and closed. The Filters
panel lets you apply display filters to a table, focusing your work on just those
entries that interest you. The Associated Alerts table in the Detection tab of
the Case Detail display is a good example of this button.

Hover over a column heading until the cursor changes to a pointed hand. Then, click
and drag to rearrange columns in the table.

Right-click a cell to see additional actions you can perform, from copying the contents of
the cell to the clipboard to using the cell data as an include or exclude filter. The exact
actions depend on the table and cell data type; see the example below:

 Not all cells provide this functionality. If the cursor changes to a pointing hand, you

can click for additional actions.

Depending on the type of data displayed, you may have access to more complex
options for drilling elsewhere in Stellar Cyber, as described in Performing Field
Actions and illustrated below.

Click the refresh button

 to refresh the table.

Column Controls
Stellar Cyber tables include a handy set of column controls in each column header. When you
hover your cursor over a column heading, the cursor turns into a pointing hand and a
"hamburger" menu

 appears , giving you access to the column controls summarized below:

Pin Column Left

Pin Column Right

Autosize this Column

Autosize all Columns

Reset Columns

In addition, depending on the table and column type, there may also be a Filter tab that lets you
set specific filters on the column data. For example, in the figure below, we have added the Write
Time column to the Documents table in the Threat Hunting page. As shown, we can perform
the following steps to limit the table's display to a specified window of Write Times:

1. Click in the header of the Write Time column.

2. Click on the Filter tab in the context menu that appears.

3. Use the From and To fields to specify a window of write times to display.

Actions
Several controls allow you to perform actions on the items in the table:

Click Create to add an item. The item added depends on the table; the Create button
only appears on tables where you can add items. For example, it appears on the User,
Tenant, and Automated Threat Hunting Playbookstables, because you can add all of
those items. It does not appear on any events tables, because you cannot add events.

Click

 to edit an item.

Click

 to delete an item.

Click  to see more information about an event in the events table.

Bulk Actions
Event tables allow you to perform bulk actions on multiple events at once. To modify multiple
events, click the checkboxes next to the events you want to modify. The bulk actions become
available, as illustrated below.

Depending on the table and data displayed, you can:

Add to a case
Add a comment
Change event status
Change event tags
Change the assignee

Add a Comment

To add comments to the selected events:

1. Click Add a Comment.

The ADD A COMMENT dialog box appears.

2. Enter your comment.

3. Click Submit.

The comment is immediately added to the selected events.

To remove a comment, simply apply a blank comment.

Change Event Status

To change the status of the selected events:

1. Choose Event Status in the bulk actions dropdown.

2. Choose the new status.

3. Click Apply.

The new status is immediately applied to the selected events.

The default event status filter is All Open. So if you change the status of events to Closed or
Ignored, they disappear from view.

Change Event Tags

To change the tags of the selected events:

1. Choose Event Tags in the bulk actions dropdown.

2. Choose the tag from the dropdown.

3. Click Apply.

The tag is immediately applied to the selected events.

You can also Delete or Clear All tags.

Change the Assignee

To change the assignee on the selected events:

1. Choose Assignee in the bulk actions dropdown.

2. Choose the new assignee.

3. Click Apply.

The new assignee immediately replaces the old assignee.

Table Navigation
Tables in Stellar Cyber include standard controls to move between multiple pages of data. As
illustrated in the figure below, you can use the following tools to speed your way through multiple
pages of data:

See the total number of table entries across all pages.

Change the number of entries per page.

Scroll forward or backward a single page of data.

Using Table Filters and the Search Bar
You can also set filters directly from table cells. Once set, they appear in the Filters panel. This
section provides some tips on using the global search bar, table filters, and the filters panel to
find what you're looking for:

Filtering and Searching Interflow Data

You can apply quick filters to control which Interflow key-pairs are displayed and perform
searches. You can apply quick filters to display only detections, only TI (Threat

Intelligence) enrichments,
only Non-Enriched fields,
only Enriched fields,
or any combination of these filters. When you don't apply a filter, you see all the key-value pairs
for an event.

When you apply the Detection filter, Stellar Cyber displays only the key-value pairs with field
names that begin with xdr_event.

When you apply the TI Enrichments filter, Stellar Cyber displays the following fields if the event
has been enriched with this information:

srcip_reputation

dstip_reputation

srcip_reputation_source

dstip_reputation_source

srcip_geo and all its subproperties

srcip_geo.city

srcip_geo.countryCode

srcip_geo.countryName

srcip_geo.latitude

srcip_geo.longitude

srcip_geo.region

dstip_geo.region and all its subproperties

dstip_geo.city

dstip_geo.countryCode

dstip_geo.countryName

dstip_geo.latitude

dstip_geo.longitude

dstip_geo.region

 If the above fields for an event have not been enriched with information, Stellar Cyber does

not display them.

When you apply the Enriched filter, Stellar Cyber displays only fields that Stellar Cyber added to
the record after ingestion. This filter is broader than TI enrichments because it includes all
platform-added enrichment fields, not only threat intelligence and geolocation fields.

When you apply the Non-Enriched filter, Stellar Cyber displays only fields that came from the
original detection or log record before Stellar Cyber enrichment. This filter is useful when you
want to review the source facts separately from the context added by Stellar Cyber.

For example, if you're acting as an MSSP analyst and are preparing an alert summary for a
customer, you can use Non-Enriched to focus on the original detection facts, then use Enriched
to review the added platform context separately. To learn more about configured enrichments,
see Configuring Data Enrichment .

When you apply multiple filters, Stellar Cyber displays key-value pairs that match any selected
filter.

Search for any term that appears in a field key, name, or value and use commas to separate
multiple terms. Stellar Cyber displays all results that match any of the search terms you enter. If
you're applying a filter at the time of a search, then Stellar Cyber limits its search to just the
filtered data. If no filter is applied, then it searches through all unfiltered data.

Searching for a Specific Interflow Key and Value

You can search for Interflow keys with specific values in a table in several ways:

Expand an entry in the table to view key-value pairs and use the Filter For button for
one of the key-value pairs to search for matching records. Once you add a term as a
filter in this way, it automatically appears in the Filter Panel at the left of the display, too.
For example, in the figure below, we're searching for Tactics matching the displayed
value.

Add the Interflow key directly in the Filter Panel. If the attribute you want to search for is
not already listed in the panel, you can use the Add new filter functionality to add it.
Then, supply the value in the field. For example:

Searching for a Value Without a Key

If you know the value you want to search for but aren't certain of the Interflow key (for example, a
number), your best route is the Content Search box at the top of all Stellar Cyber pages. Take
advantage of the full Lucene syntax  to search for partial matches, fuzzy matches, and so on.

Excluding Values from a Table

Sometimes, it can be useful to narrow a search by temporarily excluding all records with a
certain Interflow key value. This is the perfect time to use the Filter Out button in a table cell. For
example, in the figure below, we're excluding all records matching the selected Host IP address:

Removing Some Filter Criteria

You can remove individual filter criteria from the current search by deselecting the check box in
the filter panel. For example:

Removing All Filter Criteria

You can remove all filter criteria by clicking the Clear all button at the top of the filter panel. For
example:

Searching for a Specific Alert Type

You can search the Alerts table for all alerts of a specific type using either the Content Search
box or a table filter in the Alert Type column:

Use the Content Search box to search the Alerts table for all alerts of a specific type by
including the name of the Alert Type you want to search for in quotation marks. For
example, to search for the Emerging Threat alert type, you would enter the following in
the search bar:

Use a table filter in the Alert Type column as follows:

1. Click the "hamburger" menu in the Alert Type column header.

2. Navigate to the Filter tab in the context menu that appears.

3. Start typing the name of the alert type for which you want to search in the text

box.

4. When the matching alert type appears, click its box to apply the filter.

The filter appears at the top of the table, as in the figure below:

Search Tips

When using table data as a filter, be aware of whether the data includes multiple values.
For example, the figure below shows values of both modular_sensor and
Linux_agent for the data_sources Interflow key. Rather than using the Filter For
button to add this entire term as a search filter, try manually supplying one or the other
in the Filters panel at the left of the display.

If you encounter inconsistent results when using regular expressions in Lucene search,
the underlying cause may be the computational cost of the generated query. Complex
or overly broad regex patterns can produce resource-intensive queries that impact
platform performance and result consistency.

To ensure reliable and efficient execution, define regular expressions as narrowly and
specifically as possible. Avoid overly generic patterns, and constrain the scope of
matching wherever feasible.

If you are searching for a string in a specific field and not receiving results, try including
the field both with and without a .keyword suffix.

For example, to search for a specific value in the event_data.TargetUserName field,
try using a search for the string in both the event_data.TargetUserName and
event_data.TargetUserName.keyword fields. For example:

event_data.TargetUserName: "W2K16N527164H51$" OR

event_data.TargetUserName.keyword: "W2K16N527164H51$"

Other Filters that Affect Data Display (Tenant Selection
& Indices)
As you navigate Stellar Cyber, notice these primary settings that affect data visibility in
conjunction with the other settings you make in both the toolbar and the filters panel.

Tenant Filter

The Tenant selection menu is displayed at the top of the Stellar Cyber interface. While the tenant
selection is not in the filter controls, selecting a tenant filters the results just as any other filter.

You can also select All Tenants to essentially remove that filter. If your role is a tenant admin or
user, your tenant is automatically selected and cannot be changed. This maintains privacy
between tenants.

Indices

The Data Lake stores data in indices. Each index is used for a different purpose depending on
what the source of data is. For example, there is one index for Linux events and another for
Syslog records. When building your filter, remember that:

The search results always display data from a single index.
The filter controls do not include a control for which index is used to produce the
results. This parameter is usually supplied invisibly by the current page.
On the XDR Kill Chain Home Page the Alerts index is used. Other pages might use a
different index depending on their function.
The Threat Hunting page defaults to the Alerts index; a menu is available from this
page for you to change the index to match the threat type you are investigating. Select
one or more indices to complement the filter you set in the toolbar.

The indices are defined here.

Saved View Configurations
The Saved View Configurations feature lets you preserve and reapply customized table layouts
across different sessions and contexts within the Stellar Cyber UI. Rather than reconfiguring
columns, filters, and sorting options each time you revisit a page, you can save your preferred
setup as a view and reload it instantly when needed.

This feature is designed to improve efficiency and usability by supporting consistent,
personalized data views wherever you work with structured table data.

 The Views feature replaces the behavior in releases prior to 6.0.0, where Stellar Cyber

automatically saved your last table layout. Beginning with 6.0.0, you must manually save a
View to preserve any changes to column settings before navigating away from the page.
You can now save multiple Views and reuse them across different tables for consistency.

How to Use Saved Views

When you interact with a table that supports saved views, you can access the feature through
either the Select View or Saved Views button above the table.

To create and use a saved view:

1. Customize the table layout to your needs using built-in controls:

Show or hide specific columns

Reorder and resize columns

Apply sorting, filters, and pagination

2. Click Select View (or Saved Views) to open the Saved Views panel.

3. Select + Create New View, enter a name and a description, and then Save your current

table configuration as a View.

 All Views are saved on a per-user basis.

4. To apply an existing View, open the Saved Views panel and select a View.

The table updates automatically to reflect the applied View configuration.

5. To return the current View to the default table layout, open the Saved Views panel and

click Unselect View to the right of the current View name.

Manage Views

The Saved Views panel lets you organize and maintain your table configurations. The following
are some key features:

Create New View: Save the current table setup under a unique name.

Apply View: Select any saved View to update a table instantly.

Unselect View: Revert to the default layout without removing the saved View
configuration.

Search and Filter: Use the built-in search to locate Views by name or filter Views using
the All, Applicable, or Favorite tabs.

Manage View Metadata: Mark Views as favorites and see details via contextual menus.

Edit, Clone, and Delete Views: Use the Actions menu (three vertical dots) on the right
of a View in the Views list to edit, clone or remove it.

This function provides a centralized, consistent experience for managing how you interact with
data, enhancing both usability and efficiency.

Can't Use Table Buttons?
If you see buttons at the top of a table that are grayed out and unavailable, it's likely that you
need to select one or more items in the table to enable them. Try checking the boxes of a few
items in the table and see if the buttons become available.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

