Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Adding a Table to Group Source IP Addresses
by Event Fidelity

This example illustrates how to add a table that groups source IP addresses by fidelity to your
custom dashboard.

 For detailed explanations of the settings in this example, see Custom Dashboard

Components.

1. Select Dashboards | CUSTOM and select the dashboard you want to edit.

The dashboard appears.

2. Select Open in Visualizer and then select Edit.

The display switches to the editing canvas.

3. Select New table.

The Chart Builder dialog box appears with the Chart Type section on display and
Table selected.

4. Select Next to enter the General section and enter the following settings:

Chart Name: Source IP Addresses by Fidelity

Tenant: All Tenants

Indices: Alerts

Table Type: Groupings

5. Select Next to advance to the Query section, leave Query as None, and select Next

again.

The Groupings section appears.

6. Select + Add Grouping twice to create a total of three groupings.

The groupings are processed sequentially, and you can rearrange them to change the
configuration.

7. Expand the Column 1 grouping and enter the following:

Column Label: Fidelity

Aggregation: Range; Field: fidelity

8. Select + Range three times and enter the following for the name, start, and end of each

range:

First range: less than 30, ≥ 0, < 30

Second range: 30 to 70, ≥ 30, < 70

Third range: greater than 70, ≥ 70, < 100

9. Expand the Column 2 grouping and enter the following:

Column Label: Source IP Address

Aggregation: Term; Field: srcip

Metric: Count

Order: Descending

Size: 5

10. Expand the Column 3 grouping and enter the following:

Column Label: Number

Aggregation: Metric; Metric: Count

11. Select Next to save your configuration and advance to the Options section.

12. Leave Rows per Page at 20 and Filter by event status enabled, and then select

Submit.

Stellar Cyber adds the table and displays it on the editing canvas.

13. Select Save.

The dashboard appears with your new table.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

