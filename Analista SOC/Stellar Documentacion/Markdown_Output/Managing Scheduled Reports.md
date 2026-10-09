Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Managing Scheduled Reports

Stellar Cyber can automatically run scheduled reports and email them to configured recipients.
Any number of scheduled reports can be active in the system and can be viewed in the Manage
table at Reporting | Reports. The table appears in the lower half of the page below the Reports
(Beta) and Exported Dashboards tabs.

 The Manage table behaves like all other Stellar Cyber tables. You can change the displayed
columns, sort by columns, and export the displayed list, for example. This table also includes
an Actions column, which—depending on the report or exported dashboard configuration
and your user account scope and privileges—is where you can view, edit, delete, and send
reports and exported dashboards.

The Manage tables include the following columns:

 The term "Report" in the table column names applies to both PDF reports and exported

dashboards functioning as reports.

Report Name – The name of a report

Report Type – This field is automatically populated for reports from one of the
predefined report tabs. For Custom reports, this field is the same value as the Report
Name and cannot be modified.

Created At – The timestamp when a report was created

Created By – The name of the Stellar Cyber user who created a report

Report Time Interval – The interval of time for which a report is scheduled

Frequency – How often a report is run

PDF Type – The type of PDF

Day of Month – For a report that's scheduled to run on a monthly basis, this indicates
when it's run: First Day, Middle of Month, or Last Day.

Day of Week – For a report that's scheduled to run on a weekly basis, this indicates
which day of the week it's run

Failed Reason – If Stellar Cyber was unable to run a report, a reason appears is here;
for example, "FailOutstanding"

Last Modified At – The timestamp when a report was last modified

Last Sent Time – The most recent time that a report was run and sent to recipients

Report Timezone – The time zone defining the local time where the activity occurred
that you want to include in the report.

Schedule Time – The time of day to run and send a report

Last Generation Step – If Stellar Cyber is unable to generate and send a report, this
states the last step in the process when the failure occurred.

Possible "Last Generation Steps"

Set up Error Listeners: Configure listeners to monitor any response errors that
occur when the UI page sends HTTP requests to the UI server.

Go To Login Page: Simulate a user navigating to the login page and attempting to
log in using a specified account and password.

Set Report on Page: Define the configuration parameters for a specific report prior
to its generation.

Redirect to Report Page: Generate the report and then redirect the user to the
report page.

Report Loading: Wait for the report generation process to complete.

Report Load Complete: Confirm that the report has been successfully generated.

Get Report Source: Retrieve the PDF content of the report from the page.

Get CSV Text: Obtain the CSV file of the report from the page.

Send Report to Server: Transmit the report to the email server.

Per Tenant Flag – Whether discrete reports are generated for individual tenants

Possible Values

N/A: When a scheduled report is based on exported dashboards, there is no option
to generate reports for each tenant.

True or False: When a scheduled PDF report is for All Tenants, this indicates if
separate reports are generated for each tenant (True) or not (False). When a report
is for multiple tenants or a tenant group, per-tenant reports are always enabled.

( - ): When a report is for a single tenant, a dash indicates that the per-tenant report
setting is irrelevant (and is ignored).

Schedule Timezone – The time zone defining when to run and send a report. Note the
difference between Report Timezone, which determines the data that goes in a report,
and Schedule Timezone, which determines when the report is generated. For
example, if you're at an office in California and want to generate reports for a network in
Japan, you'd set the Report Timezone for Japan to include activity when it occurred in
its local time zone, and you'd set Schedule Timezone for California to generate the
report when you want it in your local time zone.

Schedule Type – This indicates if a report is Scheduled or Run Now

Send CSV – Indicates whether a CSV file is configured to be sent

Sent Status—The result of the report run

Shared With – Icons with initials of report recipients. Hover your cursor over them to
see the full recipient name.

Status Message – The delivery status of one or more reports, depending on the
number of tenants in the report configuration and type of delivery (one consolidated
report or multiple discrete reports for all tenants). Select the

Tenant/Tenant Group – The tenant for which the report was run

Theme – Identifies the cover theme applied to a report, if one is configured.

You can initiate the following tasks in the Actions column:

Select the View scheduled report icon to generate a report and display it in your
browser. The report contains data for the current time range defined in its schedule,
such as the most recent seven-day period from the moment you select View
scheduled report.

Select the Edit scheduled report icon
settings in the Report Details dialog box that appears.

 to generate a scheduled report and edit

Select Delete report

 to delete the scheduled report.

 This only deletes the scheduled report, not the original PDF report or exported

dashboard on which it was based.

Select Show report history to view previous executions of a report and optionally
resend a specific instance. For detailed instructions, see View Report History in Create
& Schedule Reports

Select Send Report Now to generate and email a scheduled report to the specified
recipients. The report uses the relative time range defined in its schedule, calculated
from the moment you select this action. For example, a report configured for the last
seven days includes data from the most recent seven-day period ending at the time you
run it.

 Both View scheduled report and Send Report Now generate a report using the

current time range, while Send Report Now in the Report History panel
reproduces the data from the time the original report was created.

You can also Export a list of scheduled reports in CSV format.

Troubleshooting Emailed Reports
The following tips can help you troubleshoot issues with emailed reports:

Some email systems may truncate or refuse to send messages with excessive records
included. If you find that emailed reports are not sending, try reducing the table size
configured in a scheduled report below 1000 records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

