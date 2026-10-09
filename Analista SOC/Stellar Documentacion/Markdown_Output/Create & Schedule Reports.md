Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Create & Schedule Reports

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lesson.

J03 Investigations and Workflows (05h:48m)  

Workflow Tools in the Stellar Cyber UI (35m:00s)

Explore workflow tools within the Stellar Cyber UI, including case management,
knowledge sharing, task assignment, and alert triage. Discover ways to enhance
collaboration, automate notifications, and integrate the UI tools into efficient SOC
workflows.

P09 Creating Dashboards and Reports in Stellar Cyber (30m:00s)  

PART 1: Mastering Dashboards and Reports in Stellar Cyber (06m:00s)

Learn how dashboards in the Stellar Cyber Platform provide real-time insights by
aggregating data from multiple sources. Understand how visual elements like heat maps
support threat detection, while reports deliver structured insights for compliance and
operational summaries.

PART 2: Using Dashboards and Reports for Threat Detection and Remediation

(07m:30s)

Discover how dashboards centralize security data for faster incident triage and threat
response. Explore prebuilt dashboards for compliance and vulnerabilities, and see how
exporting reports communicates findings to stakeholders.

PART 3: DEMO: Creating and Scheduling Custom Reports and Dashboards in Stellar

Cyber (12m:45s)

Watch a demonstration of creating custom reports and dashboards. See how to edit
queries using the Query Builder, create data visualizations, and export reports as CSV
or PDF files.

The first time you access a link on the portal during a session, you must log in to access
content.

A major part of the Stellar Cyber Platform is the ability to generate reports that you can view in
the UI and schedule for recurring generation and delivery to specified recipients. Stellar Cyber
lets you schedule reports based on PDF reports and exported dashboards. Use the instructions
in this article to understand how to view, clone, schedule, delete, send, and download reports.

PDF Reports

Accessibility to PDF Reports

Generate a PDF Report

Create a Scheduled PDF Report

Generate and View a Scheduled PDF Report

Generate and Edit a Scheduled PDF Report

Delete a Scheduled PDF Report

Generate and Send a Scheduled Report

View Report History

Download a Scheduled PDF Report

Exported Dashboards

Generate and View an Exported Dashboard

Clone and Edit an Exported Dashboard

Schedule a Report Based on an Exported Dashboard

View Report History

Download an Exported Dashboard

Notes on Predefined Exported Dashboards

Cover Themes

Create and Apply Cover Themes

PDF Reports
On the Reports (Beta) tab at Reporting | Reports, there are two predefined, or "pre-canned",
PDF reports: Case Report and Executive Summary.

The Case Report contains a table of contents followed by three sections:

Executive Summary – This shows the case volume for the current period and three
previous periods, making any trend in case load over this time immediately apparent. It
also displays the number of created cases vs. the number of resolved cases, which lets
you see how your team is handling its case load.

Case Funnel – This shows how much data Stellar Cyber ingested and how many
individual alerts it discovered and correlated into cases, how many cases it filtered, and
then, from 5.3.0, how many cases it determined to be true positives.

More information about the Case Funnel

The Case Funnel includes data beyond what appears on the Cases page and is
generated from report-specific queries of stored data, some of which isn't surfaced
elsewhere in the UI. For example, when alert filters are applied, the total number of
alerts created before filtering (Alerts Created) does not appear in the UI because
they've already been filtered out.

The funnel shows how activity narrows from ingested data to validated case
outcomes across the selected report period. Each stage represents a different level
of reduction:

Ingestion Volume – The total volume of data ingested during the report
period.

Alerts Created – The number of alerts generated from that ingested data
during the same period.

Cases Created – The number of cases created by correlating related alerts
during the report period before case filtering is applied.

Filtered Cases – The number of created cases that remain after case
filtering is applied.

True Positives – The number of cases in the report period that you or
someone on your team determined to represent real security findings rather
than benign or non-actionable activity.

Some values in the Case Funnel do not have a direct one-to-one display elsewhere
in the UI. In particular, the Cases page shows current case lists, queues, and case
statistics, but it does not expose the full Case Funnel or all of its intermediate counts
as standalone widgets.

This section helps you understand how Stellar Cyber turned ingested telemetry into
alerts, correlated alerts into cases, reduced low-value case volume through filtering,
and surfaced meaningful security findings. You can use it to estimate investigation
workload, identify where noise is reduced, and focus attention on the cases that
matter most.

Top 10 Cases by Severity – This shows the most critical issues the team faced in the
current period reported.

The Executive Summary contains a table of contents followed by sections for Deployment
Summary, Cases, Alerts, Assets, and Visibility. Each section has one or more subsections that

provide a high-level summary of the incidents Stellar Cyber discovered, assets it detected, and
amount of data it received.

A few notes about the Executive Summary content:

In Deployment Summary: Visibility

The reported number of deployed sensors might not always match the actual
number because the Executive Summary includes only sensors that are
actively running on the network during the time that the report covers, not the
total number of sensors that are in the Stellar Cyber database.

Device Sensors Deployed – For SaaS deployments, this count includes
Modular Sensors only. For on-premises deployments, it includes Modular
Sensors, Security Sensors, and Network Sensors. (Note: Security Sensors
and Network Sensors are types of Device Sensors available for deployment
on-premises until the 5.1.1 release.)

In Visibility (second chart) – The data volume for Sensors includes data from all
available sensors: Linux, Windows, and Modular. In addition, for on-premises
installations deployed before 5.1.1, the data volume also includes data from Security
Sensors and Network Sensors.

When you generate either of these reports, Stellar Cyber produces a PDF. It's formatted in
landscape orientation for viewing on monitors. If printed, the reports are designed for A4 paper
sizes (21.0 x 29.7 cm, or 8.27 x 11.69 in).

The logo that appears on the report is the same as the Organization Logo set in System |
ORGANIZATION MANAGEMENT | Settings.

Accessibility to PDF Reports

To view PDF reports in the Reports (BETA) tab and scheduled PDF reports in the Manage
table, your user profile must have Add a Report enabled. By default, Add a Report is enabled in
these predefined profiles: Super Admin, Platform Admin, and Security Admin. However, it's
disabled in the predefined User profile. If you're logged in to the Stellar Cyber UI with the User
profile, you cannot access any actions for reports, even Preview.

Because it's not possible to edit the User profile, create a new profile based on it, enable Add a
Report in this profile, and apply the new profile to user accounts that you want to be able to view
reports.

1. Select System | ORGANIZATION MANAGEMENT | Role-Based Access Control |

User | Create New Profile from this Template, give the new profile a name, select a
behavior for setting privileges to new features, and Save it.

2. Scroll to the Respond section, enable Add a Report, and then scroll to the bottom and

Save Changes.

3. Select System | ORGANIZATION MANAGEMENT | Users, select the Edit icon for a
user account, change the User Privilege from User to your newly created user profile,
and then Submit the change.

The user with this profile can now view PDF reports.

Generate a PDF Report

To generate a Case Report or Executive Summary, select its name. Stellar Cyber immediately
generates a new PDF report for data gathered the previous day.

Create a Scheduled PDF Report

To clone the selected report, change time zones, schedule it to cover a specified period of time,
and either run it immediately or at a recurring interval, select Schedule and configure the
settings displayed.

Report Details

Content

Report Name: Enter a unique name for the scheduled report.

Tenant: Depending on the scope of your user account (Root, Partner, Tenant), you
can select All Tenants, one or more tenant groups, or one or more individual tenant
names. If you select All Tenants, you can enable Per-Tenant Report to generate
individual reports for each tenant or disable it to generate one consolidated report for
all tenants. If you choose one or more tenant groups or multiple individual tenants,
the Per-Tenant Report becomes enabled automatically and cannot be disabled. This
means that Stellar Cyber generates discrete reports for each tenant rather than one
large, consolidated report for all of them.

 If you choose a Tenant Group with a custom logo assigned in the Tenant Groups

page, that logo replaces the Stellar Cyber logo in both Case and Executive
Summary reports. The same is true for reports generated for individual tenants
within a Tenant Group with a custom logo assigned.

Report Timezone: Choose a time zone to define the local time where the activity
occurred that you want to include in the report.

Scheduling

Type: Select either Run now to generate a report immediately after completing the
configuration and selecting Submit or Schedule for future to generate a recurring
report based on your configuration.

Time Range: Choose Previous day, Previous week, or Previous month. Stellar
Cyber includes data from the first minute to the last minute of the time period
specified relative to the time the report is run.

If you select Run now, you can also choose Custom and set a specific time range
for the report by selecting start and end dates and times in the built-in calendar. The
calendar allows up to three months of historical data and includes a time selector for
setting hours and minutes. These settings define an absolute time range that Stellar
Cyber stores with the report instance. A report generated later from this stored

instance uses the same absolute timestamps to reproduce identical data.

Frequency (available when Schedule for future is selected): Choose how often you
want to generate the report: daily, weekly, or monthly.

Select Day: If you chose weekly, chose one of the seven days in a week.

Select Date: If you chose monthly, choose First Day, Middle of Month, Last Day,
Nth Day of the Month, or Nth Weekday of the Month.

Notes about the two "Nth Day" options:

Nth Day of Month: Specify a calendar day (for example, the 30th). If a
month has fewer days than the value entered (for example, February), the
report runs on the last day of that month.

Nth Weekday of the Month: Specify a weekday and an ordinal value (for
example, the third Thursday). If a month does not include the chosen ordinal
(for example, the fifth Friday), Stellar Cyber generates the report on the
closest available occurrence (the fourth Friday in this example).

Run at: Choose the time of day to run the report. The list contains times at 15-minute
intervals throughout the day.

Timezone: Choose a time zone for the Run at setting to determine when reports are
scheduled to run. Note the difference between Report Timezone, which determines
the data that goes in a report, and Timezone, which determines when the report is
generated. For example, if you're at an office in California and want to generate
reports for a network in Japan, you'd set the Report Timezone for Japan to include
activity when it occurred in its local time zone, and you'd set Timezone for California
to generate the report when you want it in your local time zone.

Output

Language:
default, Stellar Cyber uses the language setting in your user profile.

 Choose the language in which you want the report written. By



 The Cover Theme setting is available as part of an Early Access

Program (EAP) and might not appear in your version of the Stellar Cyber
Platform. Contact your account manager to inquire about taking part in the Early
Access Program to use cover themes.

Cover Theme: Choose a saved theme from the drop-down list to apply a custom
cover page to the report. For more information, see the Cover Themes section below.

Share

Recipients: Choose one or more previously defined recipients to receive the report.
(Define recipients at System | Recipients.)

Reports for All Tenants: When you are logged in as a root user and select
All Tenants, you have the option to enable Per-Tenant Report. If you
enable it, select recipients to whom Stellar Cyber will send tenant-specific
reports. If you don't enable this option, select the root-level recipients
designated as All Tenants to whom Stellar Cyber will send a consolidated
report about all tenants.

Reports for multiple tenant groups or multiple tenants: When you are
logged in as a root user and select multiple tenant groups or multiple
tenants, or if you're logged in as a partner and select multiple tenants in
your tenant group, select recipients for tenant-specific reports.

Stellar Cyber associates every partner with a single tenant group and every
tenant user with a single tenant. Stellar Cyber only sends reports with data
for a specific tenant to recipients associated with its tenant group or with the
tenant itself. For example if there are three tenants and you select all
available recipients, Stellar Cyber generates three reports, one for each
tenant, and sends them only to recipients associated with the tenant for
which a report has data. In other words, if you select recipients for various
tenants, they don't get all the generated reports; each recipient gets just the
report for his or her own tenant. If you configure a report for a tenant but
don't choose a recipient associated with it, Stellar Cyber notifies you by
displaying an error message so you can revise the configuration.

Reports for a single tenant: When you are logged in as a root user and
select a single tenant, select report recipients that are associated with the
selected tenant.

When you are logged in as a partner and select a single tenant, select the
recipients associated with that tenant to whom you want Stellar Cyber to
send reports.

When you are logged in as a tenant user, select the recipients associated
with your tenant to whom you want Stellar Cyber to send reports.

Generate and View a Scheduled PDF Report

To generate and view a scheduled report, select the View scheduled report icon in Actions
column in the Manage table. Because Stellar Cyber doesn't store previously generated reports,

when you select this icon, it generates a new report and displays that. To see its settings after
viewing the newly generated report, select Schedule.

Generate and Edit a Scheduled PDF Report

To edit a scheduled report, select the Edit scheduled report icon in the Actions column in the
Manage table. Stellar Cyber generates a new report and displays it and its schedule settings.
You can edit any of the settings of reports that you or someone with the same administrative
scope (root, partner, or tenant) as you. A user with a higher scope can edit most settings in a
report created by a user with a lower scope except the tenants that the report is about.
Therefore, a root-level user cannot change the tenants of a report created by a partner or tenant,
and a partner cannot change the tenant in a report created by a tenant.

Delete a Scheduled PDF Report

To delete a scheduled report, select the Delete report icon in the Actions column in the Manage
table. This icon doesn't appear for scheduled reports created by users with a lower administrative
scope than yours. As a result, a root-level user cannot delete a report created by a partner or
tenant, and a partner cannot delete a report created by a tenant.

Generate and Send a Scheduled Report

To send a scheduled report to specified recipients outside of its usually scheduled runtime, select
the Send report icon in the Actions column in the Manage table. Stellar Cyber prompts you to
confirm running the report outside its scheduled runtime. Confirm your decision to run the report
and send it to the recipients.

View Report History

To view the history of previously generated reports, select the Show Report History icon in the
Actions column on either the Reports (BETA) tab or the Exported Dashboards tab. The
Report History panel appears, showing a list of all past report instances for the selected report,
including those generated manually and those created by schedule.

Each record in the list includes information such as the Execution Time, Tenant, Report Time
Range, Status, Trigger Type (Scheduled or Manual), Duration, and any error message
recorded during generation. Use this information to verify when a report ran, confirm its
completion status, or diagnose a failed generation.

From the Report History panel, you can select Send Report Now to generate and resend a
specific instance of the report using the same configuration and time range as when it originally
ran. It regenerates the selected report using the same absolute start and end times stored when
the original report was created, ensuring the output matches the data from that earlier run.

 Reports generated before upgrading to version 6.3.0s might not reproduce identical data
when sent again because earlier versions did not store absolute time ranges. Reports
generated after upgrading always use the stored timestamps to produce consistent results.

You can export the list in the Report History panel in CSV format if you want to retain a record
of report executions for auditing or troubleshooting.

Download a Scheduled PDF Report

To generate and download a scheduled report, select the View schedule report or Edit
scheduled report icon in the Actions column in the Manage table. When Stellar Cyber displays
the generated report, select the Download icon in the upper right corner of the page and save it
to your local system.

Exported Dashboards
On the Dashboards | CREATION | Dashboards page, you can view, clone, and modify existing
dashboards and create new ones. All the dashboards from that page also appear on the
Exported Dashboards tab at Reporting | Reports. Exported dashboards can be used as the
basis for a type of report called “exported dashboards” to differentiate them from PDF-formatted
reports (Case Report and Executive Summary).

The Exported Dashboards tab shows dashboards organized into various categories: General,
PCI Compliance, CIS Compliance, HIPAA Compliance, License Usage, and Custom. In
contrast to predefined dashboards, dashboards that you create or clone are stored in the
Custom tab. Stellar Cyber generates license usage reports based on the information from
System | ORGANIZATION MANAGEMENT | Licensing tabs of the same name. You don't
create these in Dashboards | CREATION | Dashboards but can use the same tools to clone,
edit, and schedule them.

Generate and View an Exported Dashboard

On the Exported Dashboards tab at Reporting | Reports, select the name of an exported
dashboard. Stellar Cyber immediately generates data to populate the tables, charts, and widgets
in the selected dashboard and displays it.

When you view it, Stellar Cyber provides options to Schedule, Clone Report, and Download. If
it's a custom exported dashboard, you also have the option to edit it at Dashboards |
CREATION | Dashboards.

Clone and Edit an Exported Dashboard

When you clone an exported dashboard, you can use it as the basis for a custom dashboard.

To clone an exported dashboard on Reporting | Reports | Exported Dashboards, select the
dashboard and select Clone Report. Complete the Clone Report settings: enter a name, choose
a tenant, enter a description, and enable or disable Clone all charts.

 The charts used in predefined asset reports such as CIS Control 1 - Inventory of

Hardware Assets Summary and CIS Control 1 - Inventory of Hardware Assets Details
rely on a definition that is present with their associated dashboard. For that reason, the
option to clone all charts when you clone a dashboard has been disabled for these reports.

Stellar Cyber saves the dashboard at Dashboards| CUSTOM and displays the new dashboard
with settings to Edit, Clone, Export, and Delete it.

There are also options to edit the time settings (Time Type, Time Interval, and Auto Refresh) in
the upper right of the page and set data filters in the upper left of the page.

The data in a dashboard is subject to the filters and queries defined on the page. The exception
to this are the Operational Dashboard and Analyst View, which are intentionally unaffected by the
Status (event_status) filter.

 The scope of a query determines which tenants can use it. Whether it's possible to create a
query for All Tenants depends on the scope of the object being queried, such as charts,
correlations, and Automated Threat-Hunting (ATH) rules. In short, the scope of a queried
object cannot be more restrictive than the scope of the query itself. For example, if you create
an ATH rule for All Tenants, then the query for this ATH rule can either be All Tenants or just
a single tenant, such as "Tenant A" for example. However, if you create an ATH rule for
Tenant A, then the query cannot be for All Tenants because the other tenants won’t have this
ATH rule and won’t be able to query it. In this case, the query can only be for Tenant A.

When select Edit, you have options to change the layout of the content in the dashboard, add
and delete widgets, and use the Chart Builder to modify widgets.

When done with your edits, Save them.

If you want to make more edits to a dashboard later, select the dashboard at Dashboards|
CUSTOM.

Schedule a Report Based on an Exported Dashboard

Select a dashboard name, select Schedule, and configure the settings displayed in the Report
Details panel.

Report Details

Content

Report Name: Enter a unique name for the scheduled report.

Tenant: Depending on the scope of your user account (Root, Partner, Tenant), you
can select All Tenants or an individual tenant name. If you select All Tenants, Stellar

Cyber generates one consolidated report for all tenants. If you choose an individual
tenant, Stellar Cyber generates for just that tenant.

Apply Query: To refine the data included in the report, apply a saved query. If you
don't have a saved query, you can create a new query and then apply it.

Report Timezone: Choose a time zone to define the local time where the activity
occurred that you want to include in the report.

Scheduling

Type: Select either Run now to generate a report immediately after completing the
configuration and selecting Submit or Schedule for future to generate a recurring
report based on your configuration.

 Stellar Cyber does not save reports whose type is Run now.

Time Range: Choose last 15 minutes, last 30 minutes, last 1 hour, last 5 hours,
last 12 hours, last 24 hours, this past week, this past month, Previous day,
Previous week, or Previous month. Stellar Cyber includes data from the first
minute to the last minute of the time period specified relative to the time the report is
run.

If you selected Run now, you can also choose Custom and use the calendar to
select exact start and end dates and times. The calendar permits choosing up to
three months of historical data. These absolute timestamps are stored with the report
and used if the report is sent or generated again later to ensure the same dataset is

reproduced.

Frequency (when Schedule for future is selected): Choose how often you want to
generate the report: daily, weekly, or monthly.

Select Day: If you chose weekly, chose one of the seven days in a week.

Select Date: If you chose monthly, choose First Day, Middle of Month, Last Day,
Nth Day of Month, or Nth Weekday of the Month.

Notes about the two "Nth Day" options:

Nth Day of Month: Specify a calendar day (for example, the 30th). If a
month has fewer days than the value entered (for example, February), the
report runs on the last day of that month.

Nth Weekday of the Month: Specify a weekday and an ordinal value (for
example, the third Thursday). If a month does not include the chosen ordinal
(for example, the fifth Friday), Stellar Cyber generates the report on the
closest available occurrence (the fourth Friday in this example).

Run at (when Schedule for future is selected): Choose the time of day to run the
report. The list contains times at 15-minute intervals throughout the day.

Timezone (when Schedule for future is selected): Choose a time zone for the Run
at setting to determine when reports are scheduled to run. Note the difference
between Report Timezone, which determines the data that goes in a report, and

Timezone, which determines when the report is generated. For example, if you're at
an office in California and want to generate reports for a network in Japan, you'd set
the Report Timezone for Japan to include activity when it occurred in its local time
zone, and you'd set Timezone for California to generate the report when you want it
in your local time zone.

Output

Asset Tag: Filters the records included in the report based on the asset tags
assigned to assets in your network. Assets are servers, routers, and host systems in
the private network monitored by Stellar Cyber, and asset tags are values assigned
to these assets to help categorize or identify them. The following options are
available:

--: Ignores asset tags when determining which records to include in the
report. Records for assets with and without asset tags are both included.

Any: Includes only records for assets that have an asset tag, regardless of
the tag type. Records for assets without an asset tag are not included.

None: Includes only records for assets that do not have an asset tag.
Records for assets with an asset tag are not included.

<asset tag name>: Includes only records for assets associated with the
asset tag you choose from a list of previously defined tags. You can choose
only one asset tag per report.

Language:
default, Stellar Cyber uses the language setting in your user profile.

 Choose the language in which you want the report written. By

PDF Table Size: Set the maximum number of rows you want tables in the report to
include. The available options are 25, 50, 100, 500, and 1000. When no value is
chosen, Stellar Cyber applies Default (from chart config), which uses the row count
of each table in the chart configuration defined in Dashboard Builder. If the chart
configuration does not specify a row count, the table defaults to 25 rows. Instead of
using Default (from chart config), you can choose one of the values in the drop-
down list. This setting applies uniformly to all table widgets that appear in the report,
including system tables such as Audit Logs and Asset tables. Clearing a previously
chosen value returns to the default behavior.

 Some email systems truncate or refuse to send messages with excessive

records included. If you find that emailed reports are not being sent, try reducing
the Table Size below 1000 records.

Export as CSV: To include a CSV file with the scheduled report, turn on the Export
as CSV toggle. (It’s disabled by default for new scheduled reports.)

 The drop-down list of CSV record maximums only appears to participants in the

Early Access Program.

When you enable this toggle, a drop-down list appears with the following options:
100, 500, 1000, 5000, 10000, and All Records. The default selection is 1000. When

you select a specific number, the CSV file contains up to that many rows per table.
When you select All Records, the CSV file contains up to the system-configured
maximum number of rows (20000 by default). If the export exceeds this limit, a
notification indicates how many records were exported (for example, "Only the first
20,000 records will be exported"). If you need a different limit, contact your Stellar
Cyber representative.

 As with the PDF Table Size setting, large CSV exports can cause emailed

reports to exceed limits imposed by some email systems. If reports are not being
delivered, reduce the maximum number of exported records in CSV files.

PDF Type: Choose Default, Print Optimized (Deprecated), Preserve Layout
(Deprecated), or Enhanced Print Optimized (Deprecated).

 The Default PDF type and deprecation of the other three types only appear to

participants in the Early Access Program.

From 6.6.0, dashboard reports use a PDF type called Default, which renders the
dashboard as it appears in the Dashboard Builder. The previous PDF type options—
Print Optimized, Preserve Layout, and Enhanced Print Optimized—are marked
as “Deprecated”. Existing scheduled reports that use these deprecated types
continue to use them unless you change them.

When you choose Print Optimized (Deprecated), Stellar Cyber generates a PDF
with report data neatly presented on 8.5 x 11" pages to look good when printed.

When you choose Preserve Layout (Deprecated), Stellar Cyber generates a PDF
that presents the data in the same layout used in the UI without regard to a standard
paper size for printing.

Zoom Level

When you choose Preserve Layout (Deprecated) as the PDF Type, an additional
Zoom Level setting appears. Use this to adjust the resolution width of the
dashboard export to improve the readability and layout of the content. Each zoom
level sets a virtual screen width for the rendering engine, which affects how much
content fits horizontally on each page of the exported PDF:

Level 1 (3840 px) – Maximum width. Use when dashboards contain wide
tables, numerous columns, or dense visualizations that otherwise appear
truncated or compressed at lower resolutions. Suitable for viewing on
large screens or for reports shared digitally.

Level 2 (2560 px) – High width. A balance between detail and layout.
Ideal for dashboards with moderate content density where maximum
width is not necessary but clarity is still important.

Level 3 (1920 px) – Medium width. Suitable for standard dashboards that
fit well in common HD screen resolutions. Use this level when layout and
readability are acceptable at moderate widths.

Level 4 (1440 px) – Default and narrowest width. Use when content is
minimal or when the exported report will be viewed on smaller screens.
This level may result in truncation or overlapping if dashboards are highly
detailed.

Selecting an appropriate zoom level helps avoid layout issues such as overlapping
chart labels, truncated table cells, or misaligned visual elements in the exported
PDF. If the content appears cut off or compressed in the output, try increasing the
zoom level to a wider setting.

When you choose Enhanced Print Optimized (Deprecated), Stellar Cyber
generates a print-ready PDF with improved chart clarity and cleaner table formatting,
splitting wide tables across pages to ensure the display of all columns.

Cover Theme: When you select Default or Enhanced Print Optimized
(Deprecated) as the PDF Type, an additional Cover Theme setting appears.
Choose a saved theme from the drop-down list to apply a custom cover page to the
report. For more information, see the Cover Themes section below.

Chart Colors: When you select Default as the PDF Type, choose a color palette for
the charts in the PDF. The drop-down list displays color preview badges next to each
palette name so that you can identify the palette before choosing it.

 The Default PDF type and deprecation of the other three types only appear to

participants in the Early Access Program.

Share

Recipients: Choose one or more previously defined recipients to receive the report.
(Define recipients at System | Recipients.)

Previewing a Scheduled Report

 The report preview only appears to participants in the Early Access Program.

When you open a scheduled dashboard report, Stellar Cyber loads a preview of the
dashboard automatically. A loading spinner appears while Stellar Cyber fetches the report
data. Once loading is complete, the preview renders the full dashboard with all widgets.

If you edit and save the report settings, the preview updates to reflect the changes.

PDF Rendering Notes

The following rendering behaviors apply to PDF output generated from dashboards:

Line charts – When a line chart has many data points with long axis labels, Stellar
Cyber rotates the X-axis labels 45 degrees to prevent overlap. Charts with fewer data
points or shorter labels display horizontal labels.

Heatmaps – Heatmap widgets render correctly in PDF output regardless of how
many color thresholds are configured.

Backwards Compatibility

Existing scheduled reports created in previous releases continue to function without changes.
Legacy PDF types (Print Optimized, Preserve Layout, and Enhanced Print Optimized) remain
available, and previously configured table size settings are preserved.

View Report History

You can also view report history for reports based on exported dashboards. Select the Show
Report History icon in the Actions column on the Exported Dashboards tab. The list of
historical entries and available actions are the same as for PDF reports. For details, see View
Report History in the PDF Reports section above.

Download an Exported Dashboard

To download an exported dashboard on Reporting | Reports | Exported Dashboards, select
the name of the dashboard and then select the Download icon in the upper right of the page.

Stellar Cyber opens a PDF version of the exported dashboard in a new browser tab.

 You might need to enable your browser to allow pop-ups and multiple-file downloads from

the Stellar Cyber UI.

To download the PDF, select the Download icon in the upper right of the page and save it to
your management system. When done, close the browser tab and return to the Stellar Cyber UI.

Notes on Predefined Exported Dashboards

In general, the contents of predefined exported dashboards are self-explanatory. This section
provides some additional notes to help you understand what you're seeing:

The byte counts in Ingestion Dashboard (in the General category) represent the
amount of data sent by connectors and sensors to the Stellar Cyber Platform. After data
arrives at the Stellar Cyber Platform from these sources, it undergoes additional
enrichment and compression before it's stored on disk. Because of this, the byte counts
shown in the Ingestion Dashboard don't match those in System | ORGANIZATION
MANAGEMENT | Licensing | Volume Usage or the exported dashboards in the License
Usage category, which represent the actual data stored on disk, post-enrichment and
compression. To summarize:

Ingestion Dashboard – Reports byte counts based on data sent by
connectors and sensors to the Stellar Cyber Platform prior to enrichment and
compression.

License Usage exported dashboards – Report byte counts based on actual
data stored on disk. These are the counts used for licensing purposes.

Some exported dashboards, including Alerts (in the General category), include
sections breaking out alerts into Critical, Major, Minor, and Notice severities. Each of
these severities corresponds to a different bucket of Alert Scores, as follows:

Alert Severity

in Stellar

Best Practices for Monitoring and Investigation

Cyber

Critical

Alerts of high severity and fidelity that must be investigated immediately

Major

Alerts that are likely to be true positives or that could have significant security consequences and

should be given priority to investigate

Minor

Alerts of lesser severity and/or fidelity that should be investigated if time permits; or otherwise be

investigated together with correlated alerts in cases

A

l

e

rt

S

c

o

r

e

Al

er

t

S

c

or

e

≥

7

5

Al

er

t

S

c

or

e

≥

5

0

a

n

d

<

7

5

Al

er

t

S

c

Alert Severity

in Stellar

Best Practices for Monitoring and Investigation

Cyber

Notice

Alerts of weak abnormal signals that are likely false positives or of less security concern, and may

be investigated together with related alerts and events, such as alerts in the same cases and

relevant events identified in threat hunting

A

l

e

rt

S

c

o

r

e

or

e

≥

2

5

a

n

d

<

5

0

Al

er

t

S

c

or

e

<

2

5

Similarly, exported dashboards might break out alerts according to their fidelity (High
Fidelity or Other Fidelity). These fidelity levels correspond to fidelity scores as follows:

Fidelity Level in Stellar Cyber

High Fidelity

Other Fidelity

Cover Themes

Fidelity Score

Fidelity Score ≥ 75

Fidelity Score < 75

 Cover themes, for customizing report covers, are available as part of an Early

Access Program (EAP) and might not appear in your version of the Stellar Cyber
Platform. Contact your account manager to inquire about taking part in the Early
Access Program and enabling cover themes.

Cover themes let you customize the cover page of PDF reports (Case Report and
Executive Summary) and reports generated from exported dashboards. With cover
themes, you can define the background image and color palette, include optional footer
text, and choose whether the company logo is displayed on the cover of your reports.
Using cover themes ensures consistent branding, provides space for confidentiality
notices or contact information, and produces professional, visually engaging reports.
Multi-tenant environments can maintain separate themes per tenant, making reports
adaptable for both internal use and client-facing communication.

Create and Apply Cover Themes

To use cover themes, you must first create them in the Report Settings panel and then
apply them when scheduling reports. The following steps describe how to create a
theme with your desired images, colors, and footer text, and how to apply that theme to
a report so it appears on the PDF cover page.

1. Navigate to Reporting | Reports and select the Report Settings icon in the

upper right corner on either the Reports (BETA) tab or Exported dashboards
tab.

The settings panel appears, showing the Themes tab with all existing cover
themes. From here you can create, edit, or delete themes. Each entry shows
the configured background, colors, and footer settings, with icons to edit or
delete them.

 Although one of the options is labeled + Create/Update Theme, it's only
used for creating themes. To edit an existing theme, use the Edit theme
icon in the Actions column.

2. Select + Create Cover Theme (or + Create/Update Theme) to open the

theme editor and configure a new theme.

General Settings

Name: Enter a unique name for the theme. This name appears in the
Cover Theme drop-down list when scheduling reports.

Background Image: Upload a JPG or PNG file (maximum size 5 MB)
for the cover background.

Show Logo: Enable this option to display the system logo defined in
System | ORGANIZATION MANAGEMENT | Settings.

Color Settings

Define hexadecimal values for the primary and secondary font colors,
icon color, footer title color, and border color. The border color is also
used for elements inside the report.

Footer Settings

Show Footer Text: Enable the footer text option to include additional
information at the bottom of the cover page, such as confidentiality
notices or contact details. You can add up to two lines of text:

Footer First Line: Primary footer text line.

Footer Second Line: Optional secondary footer text line.

3. When finished, select Save.

The theme now appears in the Themes list and is available to apply when
scheduling reports.

4. Select one of the reports on either the Reports (BETA) tab or Exported

dashboards tab.

This immediately generates a report.

5. Select Schedule above the displayed report.

The Report Details panel opens.

6. In the Output section, choose a saved theme from the Cover Theme drop-

down list.

The chosen theme defines the appearance of the PDF cover page.

 For reports based on exported dashboards, ensure the PDF Type is set

as Enhanced Print Optimized. The Cover Theme option does not appear
for other PDF types.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

