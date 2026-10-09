Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using Chart Builder

This topic describes how to access a table of all previously created charts and tables used in
Dashboards or Reports. It also describes how to edit or delete existing charts using the Chart
Builder, as well as how to create new charts for later use.

Access the Chart Builder as follows:

From the System | Saved Objects | Charts menu, create or edit from the displayed list of
existing charts.

From within Dashboards, you can create and modify charts in that dashboard.

Query Behavior Notes
The following points clarify how queries behave when used in charts created with the Chart
Builder, including important scoping and filtering rules that may affect your results.

Query scope: The scope of a query determines which tenants can use it. Whether it's
possible to create a query for All Tenants depends on the scope of the object being
queried, such as charts, correlations, and Automated Threat-Hunting (ATH) rules. In
short, the scope of a queried object cannot be more restrictive than the scope of the
query itself. For example, if you create an ATH rule for All Tenants, then the query for
this ATH rule can either be All Tenants or just a single tenant, such as "Tenant A" for
example. However, if you create an ATH rule for Tenant A, then the query cannot be for
All Tenants because the other tenants won’t have this ATH rule and won’t be able to
query it. In this case, the query can only be for Tenant A.

Filter behavior for IP address fields: Beginning in version 6.0.0, the Chart Builder
restricts filter operators for IP address fields (such as srcip and dstip) to only those
that are semantically valid. Specifically, only the operators is, field exists, and
field does not exist are supported. Operators like starts with, ends with, and
contains are no longer available for these fields, as they are incompatible with IP data
types. Dashboards using unsupported operators must be updated to ensure correct
filtering behavior.

Working with the Charts List

When you launch charts from the System | Saved Objects | Charts menu, a list of existing
charts is displayed. From here, you can manage charts, and create new ones, either from
scratch or by cloning an existing chart. These are displayed in a table that can be sorted,
searched and exported in the same way as other tables in Stellar Cyber.

Use the charts list to manage the charts available for display in dashboards throughout the
Stellar Cyber product. Note the following:

Dashboards created by System cannot be modified or deleted. Instead, clone the chart
and modify the copy.

The In Use field lets you see which dashboards are affected by changes you make to
the chart.

Before you are permitted to delete a chart, you must remove it from any associated
dashboards. Hover your mouse over the In Use field to identify dashboards using that
chart. Navigate to Dashboards | CREATION | Dashboards to open the Dashboards
Hub, where you can locate and open the affected dashboards to modify them.

When cloning a chart, make sure that the source chart does not include any special
characters in its name. Chart Builder prevents you from creating new charts with
disallowed special characters but does not prevent cloning of existing charts with
disallowed special characters. Letters, underscores, spaces, dashes, numbers and
periods are permitted.

The charts list, like many tables in Stellar Cyber, supports export, sorting, edit, and delete
operations. You can filter which charts to display based on chart attributes. Expand a row, select
an attribute, and then select a filter based on whether you want to view charts that include the
attribute (Filter For) or if you want to view charts that exclude it (Filter Out).

Creating and Editing Charts
When you select create or edit from the System | Saved Objects | Charts page or from
Dashboards | Custom | <custom_dashboard_name>, the chart builder tool opens.

Launched from Charts page

Launched from a

dashboard

From either launch point you can use the following features to create or modify a chart:

Counter – Use this to add a dynamic count.

Area chart – Use this to visualize change over time.

Bar chart – Use this to compare several categories.

Pie chart – Use this to see the distribution of items compared to the total.

Heatmap – Use this to see a geographic distribution.

Table – Use this to add a simple table of data.

About the "Filter by event status" Option

Regardless of the type of chart you are creating, the Chart Builder's last step lets you configure
the Filter by event status option. This feature specifies whether data in this chart is subject to
the global Status filter available in the main toolbar:

Enabled (default) – Chart data can be filtered using the global Status filter in the main
toolbar.

Disabled – Chart data is displayed regardless of the current setting of the global Status
filter in the main toolbar.

The figure below summarizes how this option works:

Adding a Count

To add a count:

1. Select New counter.

The Chart Builder dialog box appears with Counter selected.

2. Select Next to view settings for the chart name, tenant whose data the chart displays,

and the indices from which the chart retrieves data.

3. Enter a Chart Name, choose a Tenant, choose one or more Indices, and then select

Next.

The Chart Name field supports alphanumeric characters, spaces, underscores,
dashes, periods, parentheses, colons, and ampersands. You can also use 2-byte
characters such as Japanese, Chinese, or Korean. Some languages, such as Hindi
or Thai, are partially supported. If you encounter issues, use only the supported
characters listed above.

4. Choose a saved Query or create a new query and then select Next.

The query is optional.

 To remove a selected query, set the query value to None. Deleting it completely

removes it.

5. Choose the Metric you want the chart to use—Average, Count, Max, Min, or Sum—

and then select Next.

6. Use the Filter by event status option to specify whether data in the chart is subject

to the global Status filter available in the main toolbar:

Enabled (default) – Chart data is filtered using the global Status filter in the
main toolbar.

Disabled – Chart data is displayed regardless of the current setting of the
global Status filter in the main toolbar.

7. Select Submit.

Adding an Area Chart

To add an area chart:

1. Select New area chart.

The Chart Builder dialog box appears with Area Chart selected.

2. Select Next to view settings for the chart name, tenant whose data the chart displays,

and the indices from which the chart retrieves data.

3. Enter a Chart Name, choose a Tenant, choose one or more Indices, and then select

Next.

The Chart Name field supports alphanumeric characters, spaces, underscores,
dashes, periods, parentheses, colons, and ampersands. You can also use 2-byte
characters such as Japanese, Chinese, or Korean. Some languages, such as Hindi
or Thai, are partially supported. If you encounter issues, use only the supported
characters listed above.

4. Choose a saved Query or create a new query and then select Next.

The query is optional.

 To remove a selected query, set the query value to None. Deleting it completely

removes it.

5. Choose the Field by which to group data, an Interval Time, an Interval Unit (from
Millisecond to Year), and the Metric you want the chart to use—Average, Count,
Max, Min, Sum, or Unique Count.

6. If you choose any Metric other than Count, also choose a Metric Field.

7. Select Next and then enter a Y-Axis Label for the area chart; for example, Events.

8. Use the Filter by event status option to specify whether data in the chart is subject

to the global Status filter available in the main toolbar:

Enabled (default) – Chart data is filtered using the global Status filter in the
main toolbar.

Disabled – Chart data is displayed regardless of the current setting of the
global Status filter in the main toolbar.

9. Select Submit.

Adding a Bar Chart

To add a bar chart:

1. Select New bar chart.

The Chart Builder dialog box appears with Bar Chart selected.

2. Select Next to view settings for the chart name, tenant whose data the chart displays,

and the indices from which the chart retrieves data.

3. Enter a Chart Name, choose a Tenant, choose one or more Indices, and then select

Next.

The Chart Name field supports alphanumeric characters, spaces, underscores,
dashes, periods, parentheses, colons, and ampersands. You can also use 2-byte
characters such as Japanese, Chinese, or Korean. Some languages, such as Hindi
or Thai, are partially supported. If you encounter issues, use only the supported
characters listed above.

4. Choose a saved Query or create a new query and then select Next.

The query is optional.

 To remove a selected query, set the query value to None. Deleting it completely

removes it.

5. Define the parameters of the data that you want the bar chart to display:

Aggregation: Choose the form of data aggregation that you want the chart to use.

Choose Term to group data by the text in the fields. This is useful when your
data is text, such as tenant names.

Choose Range to group data by ranges. This is useful when your data is
numeric, such as severity.

Choose Filter to define one or more filters for the data groups.

Then, configure the necessary settings, which differ based on your choice of
aggregation.

6. Select Next and then define the orientation and x- and y-axis labels of the bar chart.

By default, the bars in the chart are displayed vertically. Choose Horizontal
to display the bars horizontally.

Enter optional labels for the X and Y axes.

7. Use the Filter by event status option to specify whether data in the chart is subject

to the global Status filter available in the main toolbar:

Enabled (default) – Chart data is filtered using the global Status filter in the
main toolbar.

Disabled – Chart data is displayed regardless of the current setting of the
global Status filter in the main toolbar.

8. Select Submit.

Adding a Pie Chart

To add a pie chart:

1. Select New pie chart.

The Chart Builder dialog box appears with Pie Chart selected.

2. Select Next to view settings for the chart name, tenant whose data the chart displays,

and the indices from which the chart retrieves data.

3. Enter a Chart Name, choose a Tenant, choose one or more Indices, and then select

Next.

The Chart Name field supports alphanumeric characters, spaces, underscores,
dashes, periods, parentheses, colons, and ampersands. You can also use 2-byte
characters such as Japanese, Chinese, or Korean. Some languages, such as Hindi
or Thai, are partially supported. If you encounter issues, use only the supported
characters listed above.

4. Choose a saved Query or create a new query and then select Next.

The query is optional.

 To remove a selected query, set the query value to None. Deleting it completely

removes it.

5. Define the parameters of the data that you want the pie chart to display and then

select Next:

Aggregation: Choose the form of data aggregation that you want the chart to use.

Choose Term to group data by the text in the fields. This is useful when your
data is text, such as tenant names.

Choose Range to group data by ranges. This is useful when your data is
numeric, such as severity.

Choose Filter to define one or more filters for the data groups.

Then, configure the necessary settings, which differ based on your choice of
aggregation.

6. Use the Filter by event status option to specify whether data in the chart is subject

to the global Status filter available in the main toolbar:

Enabled (default) – Chart data is filtered using the global Status filter in the
main toolbar.

Disabled – Chart data is displayed regardless of the current setting of the
global Status filter in the main toolbar.

7. Select Submit.

Adding a Heatmap

To add a heatmap:

1. Select New heatmap.

The Chart Builder dialog box appears with Heatmap selected.

2. Select Next to view settings for the chart name, tenant whose data the chart displays,

and the indices from which the chart retrieves data.

3. Enter a Chart Name, choose a Tenant, choose one or more Indices, and then select

Next.

The Chart Name field supports alphanumeric characters, spaces, underscores,
dashes, periods, parentheses, colons, and ampersands. You can also use 2-byte
characters such as Japanese, Chinese, or Korean. Some languages, such as Hindi
or Thai, are partially supported. If you encounter issues, use only the supported
characters listed above.

4. Choose a saved Query or create a new query and then select Next.

The query is optional.

 To remove a selected query, set the query value to None. Deleting it completely

removes it.

5. Choose the Field type by which you want to group the data in the pie chart:

dstip_geo_point – Visualizes data using geographic locations derived from
destination IP addresses that match the query in the previous steps and
plots points for them on a heatmap. This helps identify where outbound
traffic is targeting.

hostip_geo_point – Visualizes data using geographic locations derived
from internal host IP addresses and plots points for them on a heatmap.
This can help map internal systems, though private IPs may not always yield
meaningful geo-locations.

location_geo_point – Visualizes data using geographic locations derived
from enriched or user-defined location fields and plots points for them on a
heatmap. This offers flexibility when using connector-enriched or metadata-
based geographic data.

remote_ip_geo_point – Visualizes data using geographic locations derived
from remote system or user IP addresses and plots points for them on a
heatmap. This is useful for visualizing connections from remote users, such
as VPNs or cloud access.

srcip_geo_point – Visualizes data using geographic locations derived from
source IP addresses that match the query in the previous steps and plots
points for them on a heatmap. This helps track where connections originate.

6. Choose the type of Metric to use for the Field. You can choose from

Average, Count, Max, Min, or Sum.

7. If you choose any Metric other than Count, also choose a Metric Field.

8. Select Next and then name and set your thresholds.

The thresholds specify at what value the heatmap changes the color codes of
geopoints shown in the display. This way, geopoints with a higher count are
displayed, for example, in red.

9. Use the Filter by event status option to specify whether data in the chart is subject

to the global Status filter available in the main toolbar:

Enabled (default) – Chart data is filtered using the global Status filter in the
main toolbar.

Disabled – Chart data is displayed regardless of the current setting of the
global Status filter in the main toolbar.

10. Select Submit.

For more on heatmaps and converting them from previous releases, refer to the related
Dashboard component topic.

Adding a Table

To add a table:

1. Select New table.

The Chart Builder dialog box appears with Table selected.

This section of the chart builder is titled Chart Type.

2. Select Next to view settings for the chart name, tenant whose data the chart displays,

and the indices from which the chart retrieves data.

This section of the chart builder is titled General.

3. Enter a Chart Name, choose a Tenant, and then choose one or more Indices.

The Chart Name field supports alphanumeric characters, spaces, underscores,
dashes, periods, parentheses, colons, and ampersands. You can also use 2-byte
characters such as Japanese, Chinese, or Korean. Some languages, such as Hindi
or Thai, are partially supported. If you encounter issues, use only the supported
characters listed above.

4. Choose the Table Type—either Per record or Groupings—and then select Next.

Per record: This table type displays individual Interflow records exactly as they
appear in the dataset, without any aggregation. Use this option when you want
detailed, event-level visibility, such as examining specific alerts, logs, or user actions
in raw form.

Groupings: This table type summarizes data by aggregating records based on
selected fields. It is best suited for identifying patterns or trends, such as total event
counts per IP address or average session duration per user, enabling higher-level
analysis.

The Table Type determines how many sections are in the chart builder.

When the table displays data per record, there are four sections: Chart
Type, General, Query, and Options.

When the table displays data in groupings, there is an additional section for
a total of five: Chart Type, General, Query, Groupings, and Options.

After you select Next, the chart builder advances to the Query section.

5. Choose a saved Query or create a new query and then select Next.

The query is optional.

 To remove a selected query, set the query value to None. Deleting it completely

removes it.

The next section of the chart builder depends on the table type you selected in the
General section. If the table type is Per record, the next section is Options (skip the
next step). If the table type is Groupings, the next section is Groupings and then
Options after that.

6. If you chose Groupings as the table type, configure a grouping for Column 1 in the

Groupings tab.

Each column in a Groupings table defines how to group and summarize data from
Interflow records. You can add multiple columns, and the groupings will be processed
sequentially from left to right.

Below is a detailed explanation of each Aggregation type and the dynamic options
that appear for each.

Term: Use this to group records based on exact values of a field. A possible
use case might be to show the top ten destination IP addresses by event
count.

Field: Choose a text-based field such as srcip, event.name, or
tenant_name.

Metric: Select a summary operation: Average, Count (the default),
Max, Min, or Sum.

Metric Field: If you choose any Metric other than Count, also
choose a Metric Field.

Order: Choose Ascending or Descending to control the sort
order of group results.

Size: Specify how many top groups to show.

Range: Use this to group numeric values into named ranges. For example,
you might categorize severity into low (0-30), medium (31-70), and high (71-
100).

Field: Choose a numeric field such as severity, fidelity, or
totalbytes.

+ Range: Select to add one or more custom ranges.

Custom name for a range (optional): Enter a label for the range;
for example, Low, Medium, and High.

≥: Enter an inclusive lower bound to start the range.

<: Enter an upper bound to end the range.

Filter: Use this to group data into logical buckets defined by filters. Use
either + Filter or + Query String Filter. For detailed information about
configuring filters, see Queries and Filters.

Metric: Use this to compute a single value over all matching records. It does
not group records but simply returns a summary value. You might use this,
for example, to display the average fidelity across all Interflow records.

Metric: Chose Average, Count, Max, Min, or Sum.

Field: If the Metric is not Count, choose a numeric field to
summarize the data; for example, totalbytes, duration, or
fidelity.

Date histogram: Use this to group records into fixed time intervals. For
example, you might group events by day to show trends over time.

Field: Choose a time-based field, such as event.timestamp.

Interval Time: Enter a numeric value.

Interval Unit: Select the time unit: Millisecond, Second, Minute,
Hour, Day, Week, Month, or Year.

You can add another column to the table with another grouping of data by selecting
+ Add Grouping and repeating the previous instructions to configure Column 2.

When you select Next, the next section is Options.

7. If you chose Per record as the table type in the General section of the chart builder,

configure the following in the Options section:

Select + Column to add one or more columns to the table.

Choose the field name for the data to display in each column and enter a
title for each column.

Enter the field to Sort By and choose the Rows per Page to define how
many rows to display for each page.

If you chose Groupings as the table type in the General section of the chart builder,
choose how many Rows per Page to display.

8. Use the Filter by event status option to specify whether data in the chart is subject

to the global Status filter available in the main toolbar:

Enabled (default) – Chart data is filtered using the global Status filter in the
main toolbar.

Disabled – Chart data is displayed regardless of the current setting of the
global Status filter in the main toolbar.

9. Select Submit.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

