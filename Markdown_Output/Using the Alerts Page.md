Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using the Alerts Page

 Learn more at Stellar Cyber Academy.

The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.

J02 Introduction to Features in the User Interface (02h:24m)  

Alerts in the UI (10m:00s)

Explore the Alerts view, learning how to filter, sort, and manage Alerts within the
Stellar Cyber Platform. Understand how machine learning drives alert generation and
prioritization, and how to use these alerts to create custom Cases.

Alert Management (33m:00s)

Explore available views for managing and investigating alerts, including the Alerts
Table, Kill Chain, and Threat Hunting views within the Stellar Cyber Platform. Learn to
leverage MITRE ATT&CK data, threat intelligence, and toolbar filters to enhance alert
triage and investigation workflows. Follow along with a demonstration on interacting
with alerts across different views, applying search tool queries, and conducting threat-
hunting activities efficiently. Discover how to tune alert settings and use custom
filtering options for focused analysis across the data lake.

J03 Investigations and Workflows (05h:48m)  

Workflow Tools in the Stellar Cyber UI (35m:00s)

Explore workflow tools within the Stellar Cyber UI, including case management,
knowledge sharing, task assignment, and alert triage. Discover ways to enhance
collaboration, automate notifications, and integrate the UI tools into efficient SOC
workflows.

Building Workflows in Stellar Cyber - Foundations (45m:00s)

Discover foundational strategies for building workflows in the Stellar Cyber Platform,
focusing on tools that support knowledge transfer, case management, and task
tracking. Learn how to structure workflows to streamline operations within your SOC.

Alert Triage and Investigation Fundamentals (32m:00s)

Master the basics of alert triage, including prioritizing alerts by severity and relevance.
See how the Stellar Cyber UI can assist in managing high-priority alerts and grouping
related events for streamlined analysis.

Alert Handling (90m:00s)

Follow practical examples of investigating command anomalies, DNS tunneling
activity, and privilege escalation alerts. Learn techniques to analyze these high-risk
behaviors, understand their impact on network security, and see how Stellar Cyber
workflow and investigation tools help identify, manage, and mitigate advanced
threats.

The first time you access a link on the portal during a session, you must log in to access
content.

Select Detections | Alerts to navigate to the Alerts page. This page allows you to view
observed alerts organized by the XDR Kill Chain and analyzed with machine learning. From
here, you can also access alert details and create custom alert types. Stellar Cyber generates
alerts by using machine-learning algorithms to search for specific security-related events. You
can get to the Alerts page by:

Selecting the Detections | Alerts menu option

Clicking a stage in the XDR Kill Chain loop



See Machine Learning and Analytics Overview for an introduction to Stellar
Cyber's machine-learning technology and links to individual alert descriptions
organized by index and XDR Kill Chain stage.

See All Alert Types by Name for details on the available alert types and the
actions you should take when one is triggered.

Stellar Cyber also provides an interactive tool  that lets you look up alert types
by data source, alert name, event type, or source index.

The Alerts page lists the available alert types according to the filters set in both the Filters panel
and the filter controls at the top of the page.

You can always see which display filters are applied to the Alerts page by examining the
checked boxes in the Filters panel at the left of the display.

Alerts Page Components
As shown in the figure below, the Alerts page consists of the following main components:

Alerts and Status panels – Provides at-a-glance status graphs for Critical vs. Total and
Open vs. Total alerts within the filters set in both the Filters panel and the Content
Search box at the top of the page. Open alerts are those with a status of either New or
In Progress.

Filters panel – Provides display filters for the Alerts page using XDR Kill Chain stages
and tactics, Source, Tags, and Status, among others. Filters applied here
automatically affect the counts shown in the Alerts and Status panels. Depending on
how you arrived at the Alerts page, some of these filters will often be automatically set
(for example, if you arrived by clicking an XDR Kill Chain stage in the Home
Dashboard).

Alerts table – Provides a sortable table listing the alert types available according to the
current filters set in both the Filters panel and the Content Search box at the top of the
page. By default, only triggered alerts are shown. However, you can change this to view
all alert types by toggling the Show alert types without hits option in Alert Options in the
Filters panel. You can sort the table by columns such as Critical, High Fidelity, or Total to
see which alerts have been triggered. When you are ready to dive deeper, use the View
button to see the Alert Detail page for the corresponding alert.

The table includes a Create button that takes you to the standard workflow for creating
a new alert type. You can create new alert types that are available for use in Automated
Threat Hunting (ATH) playbooks.

The visible alerts are restricted to those accessible to the currently active tenant. Refer
to "Which Custom Alert Types Can I See?," below, for information on which customer
alert types are visible to you, depending on how you are logged in. The columns for
Tenants and Tenant Group are displayed only for Partner users and Root users.

InSyncs – If there are any integration syncs, they are displayed at the top of the Alerts
page.

Understanding the Alerts and Status Cards

The Alerts and Status cards appear immediately above the Alerts table as illustrated below:

Alerts Card – Use this card to assess the number of Critical versus Total alerts for the
selected Time Interval and filters.

The bar graph shows the number of critical alerts and the percentage of the
total number of alerts that match the selected filters. Critical alerts are those
with an Alert Score of 75 or greater.

The Critical indicator shows you the trend in critical alert generation,
comparing the net increase or drop in critical alerts to the previous Time
Interval of the same size.

The Total indicator shows you the trend in total alerts, comparing the net
increase or drop in total alerts generated to the previous Time Interval of the
same size.

Status Card – Shows the number of Open alerts versus Total alerts for the selected
Time Interval and filters. Open alerts are shown both as a count and a percentage of
the total. You can also see trend information for both Open and Totalalerts over the
selected time interval below the graph.

The Open indicator shows you the trend in alert closure, comparing the net
increase or drop in open alerts to the previous Time Interval of the same size.

The Total indicator shows you the trend in total alerts, comparing the net
increase or drop in total alerts generated to the previous Time Interval of the
same size.

 Open alerts are those with a status of either Open or In progress.

Using Filters in the Filters Panel

The Filters panel provides a collapsible set of display filters that can be applied to the Alerts
page. Click the Filters button at the top left of the display to toggle the Filters panel open and
closed.

The counters in the Alerts and Status cards and the alert types listed in the Alerts table are all
subject to the display filters set in the Filters panel. For example, suppose you clicked the
XDR Kill Chain | Initial Attempts entry in Filters panel:

The Alerts table updates to reflect just those alert types available at the Initial
Attempts XDR Kill Chain stage.

The Alerts and Status cards update to reflect just those alerts triggered at the Initial
Attempts XDR Kill Chain stage.

Showing Alert Types Without Hits

The Filters panel also includes an Alert Options | Show Alert types without hits option.
Enable this option and sort the table by Stage or Tactic to see the alert types available at a
particular XDR Kill Chain stage or using a particular tactic (or, alternatively, set a filter for the
stage/tactic in the Filters panel).

About the XDR Kill Chain Counters in the Filters Panel

The XDR Kill Chain entries in the Filters panel also show you Critical/Total alert counters
subject to the global filters at the top of the display. For example, in the figure below, you can see
that there are no critical alerts out of the total alerts at the Exploration stage in the selected Time
Interval:

Automatically Configured Filters

Depending on how you arrived at the Alerts page, some of the display filters may already be set
for you. For example, if you drilled to Alerts by clicking an XDR Kill Chain stage in the home
dashboard, the corresponding stage is already selected as a filter. You can set the following
types of filters in the Filters panel:

Tags – You can set display filters on both predefined and custom tags.

Alert Options – You toggle on and off the display of alert types without hits.

Alert Score – You can limit the display to just those alerts within a specified range of
scores. Click Alert Score and use the slider to specify the range.

Queries – You can use a configured query as a display filter.

Source – You can set display filters that include or exclude both the Built-in alert types
(those provided with Stellar Cyber) and any Custom alert types available to your
tenancy.

Status – You can set display filters that include or exclude alerts based on their status
(All Open, Any, New, In Progress, Ignored, or Closed).

XDR Kill Chain – You can set display filters on each XDR Kill Chain stage, as well as
their individual associated tactics. Within a stage, tactics are organized from least to
most severe.

You can also use the Add new filter field to add a new filter to the Filters panel. Click in the Add
new filter field to see the list of available filters.

Working with the Alerts Table

The Alerts table lists the alerts available within the filters set in the Filters panel and the Content
Search box at the top of the page. Depending on how you set the Show alert types without
hits toggle, you can view only triggered alerts (the default) or all alerts (Show alert types
without hits enabled).

You can use this table to understand the alert types available at different XDR Kill Chain stages
and using different tactics, as well as to see the triggered alerts. You work with the Alerts table in
the same way you do any Stellar Cyber table. Keep in mind the following techniques that are
particularly useful when working with the Alerts table:

Leave the Show alert types without hits option disabled to focus on triggered alerts.

Sort the table using the Critical, Fidelity, or Severity columns to bring triggered alerts
to the top of the table for investigation.

Enable the Show alert types without hits option and sort the table by Stage or Tactic
to see the alert types available at a particular XDR Kill Chain stage or using a particular
tactic (or, alternatively, set a filter for the stage/tactic in the Alert Types panel).

Each alert type in the table includes a View button that you can use to drill to a detail
display of all the alerts triggered for that type.

The Monitored Tenants and Monitored Tenant Groups columns help you understand
which tenants have access to specific custom alert types.

Click the Columns button at the left of the table to change the columns included in the
table.

The Playbooks column lets you see how many ATH Playbooks a given alert type has
been assigned to. You can click the entry in this column to drill to a filtered view of the
Automation page showing just those playbooks to which the corresponding alert type
has been assigned.

Custom alert types are listed with standard Edit and Delete icons. Keep in mind that
you can only delete a custom alert type if it's not assigned to any playbooks. The
Playbooks column gives you an easy way to determine if it is. If you still want to delete
the custom alert type, you must either remove it from any assigned playbooks or delete
its assigned playbooks entirely.

Using InSyncs

If there are any integration syncs, they are displayed at the top of the Alerts page. The status of
the InSyncs are displayed, as well as a button you can click to go back to the InSyncs page.

In each ServiceNow icon, the name of the InSync is listed. There is a count of the number of
alerts that have been synced using this InSync and a timestamp of the last synchronization.

The status is indicated in the circle around the NOW icon:

A green circle indicates a Synced status.

A gray circle indicates a Paused status.

A red circle indicates an Error status.

For details, see Using InSyncs.

Common Search and Filter Techniques

Stellar Cyber provides a variety of tools that help you find the data you need. Use the following
summary of common search scenarios to help you perform your own searches, either globally, or
in specific tables. The examples below are in the Alert Detail view, which you can display by
clicking the View button for an alert in the Alerts table.

Filtering and Searching Interflow Data

You can apply quick filters to control which Interflow key-pairs are displayed and perform
searches. You can apply quick filters to display only detections, only TI (Threat

only Non-Enriched fields,
only Enriched fields,
Intelligence) enrichments,
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

Searching for Alerts Without Correlated Cases

You can use the following search in the Lucene Search bar in either the Alerts or Threat Hunting
page to see alerts that have not been correlated to cases in the current time window:

(NOT ( (_exists_:(xdr_event.name OR event_name) AND _exists_:orig_index) OR

(stellar.ath.type:raw AND stellar.ath.to_incident:true))) OR xdr_event.name:

(ade_outbytes_anomaly OR ade_outbytes_anomaly_flip)

Creating a New Alert Type

In addition to the alert types provided by Stellar Cyber, you can create your own custom alert
types. Once you've created a custom alert type, you can add it to an automated threat hunting
playbook.

1. Navigate to the Detections | Alerts page and select Create.

The Create an Alert Type dialog box appears.

2. Supply the following information in the Create an Alert Type dialog box:

Alert Type (Required) – Supply a unique, alphanumeric name for the custom
alert type. This name identifies the alert type across the system and
communicates the nature or focus of the alerts it generates.

Tenants (Required) – Either set to All Tenants or select the tenant groups and
tenants that will have access to this custom alert type. For information on how
your tenancy determines which alert types are visible to you, refer to Which
Custom Alert Types Can I See and Act Upon?.

Kill Chain Stage – Choose the applicable XDR Kill Chain stage to which the
custom alert type corresponds. This stage helps classify alerts according to a
structured threat progression model, supporting better threat detection and
response strategies.

Tactic – Choose the tactic associated with this alert type. Tactics represent the
goal or objective behind an attacker’s behavior, such as credential access or
lateral movement. Available options depend on the selected Kill Chain Stage.

Technique – Choose the technique used to carry out the chosen tactic.
Techniques define how attackers achieve their goals and provide additional
specificity for detection. The list of techniques is filtered based on the chosen
Kill Chain Stage and Tactic.

 If you set a value for any one of the fields—Kill Chain Stage, Tactic, or

Technique—you must set all three. The system enforces valid
combinations.

Tags – Apply tags to help categorize, filter, and search for this alert type. Tags
can represent threat categories, response actions, or affected environments.
Tags become mandatory if Kill Chain Stage, Tactic, and Technique are not
defined.

Alert Type Description – Optionally supply an alphanumeric description for
the custom alert type. This field defines the overall purpose or behavior of the
alert type and applies to all alert instances that belong to it. The text appears
prominently near the top of the Alert Type dashboard when viewing grouped
alerts, and it also populates the xdr_event.description field in each alert
instance—but only when the Alert Instance Description field is left empty.

The description is static and does not support dynamic variables. It's intended
to help users quickly understand the function of the alert type at a glance. The
maximum length is 200 characters, including spaces.

Alert Instance Description – Optionally define a dynamic description that is
rendered uniquely for each alert instance. This field supports merge fields—
placeholders wrapped in double curly braces ( {{ }} )—that are replaced with
actual values drawn from the JSON data in an alert record at runtime. When
populated, this field overrides the Alert Type Description and is written to the
xdr_event.description field in the alert record. The dynamically rendered
description appears both in the Alert Details side panel and in the alert
instance table on the Alert Details page.

This field enables you to embed contextual information specific to each event,
such as the affected tenant, user, IP address, or host. For example, entering
Malware alert triggered in {{tenant_name}}. could produce Malware
alert triggered in Acme Corp. when rendered. The maximum length is
200 characters, including spaces.

Common Merge Fields for Alert Instance Descriptions

You can use any available JSON field from the alert record as a merge field.
Below are common examples:

Merge Field

Description

{{srcip}}

{{dstip}}

Source IP address triggering the alert

Destination IP address

{{srcip_username}} Hostname of the source IP address

{{event_name}}

Name of the triggering event

{{severity}}

Alert severity level

{{report_id|int}}

Report ID (Note: Add the int filter to render the ID number as an integer.)*

* You can use the int filter to render numeric field values as integers; for example, report ID

60735526. Otherwise, by default, they're rendered as floating point numbers such as report ID

60735526.0, which would be an incorrect report ID number. To know if a field type is an integer or

not, check if the field is tagged with a hashtag ( # ) in Details view of the Interflow record for an alert

instance. If it is, include the int filter here to render it correctly as an integer.

Add Custom Key Fields – You can add key fields to the custom alert type to
make them more prominent and readily accessible during alert analysis. Any
field in the JSON tab of an alert can be promoted to the Key Fields tab.

Select the plus sign (

) next to Add Custom Key Fields and then select the

right angle bracket (

) to expand a Custom Field.

The asterisk (*) indicates a required field.

a. Enter the Key. This is a field in the JSON data; for example, hostip.

b. (Optional) Enter a Label. This is what appears in the user interface;

for example, Host IP.

c. (Optional) Enter a Description. This is what appears in the user

interface when you hover over the key field; for example, The host
IP address.

In the following example alert type, a custom field was created:

3. Select Submit to add the custom alert type to the list.

Show All Alert Types to See Your New Alert Type

 Your custom alert type will only appear in the list right away if the Show alert types without
hits option is enabled under Filters | Alert Options, as illustrated below. Because you just
created the alert type, it likely won't have any hits yet.

Adding the Custom Alert Type to a Playbook

Once you've created a custom alert type you can add it to an Automated Threat Hunting
playbook. You can either do this directly from the Automation | Automation page, or you can
drill to a pre-filled template for a new playbook using the custom alert type as follows:

1. Create the custom alert type using the procedure in the previous section.

2. Ensure that the Alert options | Show alert types without hits option in the Filters

panel is enabled and locate your new custom alert type in the Alerts table.

 You can make it easier to find custom alert types by setting the Source filter in the

Alert Types panel to Custom as in the figure below.

3. We just created the custom alert type named AutoEx. Now we can click its three-dot

 and use the + Add Playbook option to launch the standard ATH Playbook

menu
workflow with the template pre-filled to use our custom alert type.

When you start a playbook using this technique, the template is automatically pre-filled with the
Actions section populated based on the alert type settings:

Type is set to Create Alert

Alert Type is set to the selected alert type.

Kill Chain Stage, Tactic, Technique, Tags, and Description are all pre-filled based on
the custom alert type settings.

Editing Custom Alert Types

You can edit a custom alert type using its standard Edit button at the right of its entry in the Alerts
table. Keep in mind, however, that once a custom alert type is assigned to a playbook, you
cannot delete its assigned Tenants or Tenant Groups.

Which Custom Alert Types Can I See and Act Upon?

The policy of Stellar Cyber is to restrict access to different objects based on ownership and
tenancy. In general, you can only see and act upon custom alert types that were created by or
assigned to a tenant or tenant group to which you are logged in as. Start by checking your
Tenancy at the upper right of the display. For example, the user below is logged in with the STML
tenant.

You can always see alert types set to All Tenants. From there, your tenancy determines which
custom alert types you can see and act upon, as follows:

If you are logged in with a tenant and the tenant owns the alert type.

If you are logged in with a tenant and the tenant list for the alert type includes the
tenant.

If you are logged in with a tenant and the alert type is assigned to a tenant group that
includes that tenant.

If you are logged in with a tenant group and the alert type is assigned to that group.

If you are logged in with a tenant group and a tenant in the tenant group owns the alert
type.

If you are logged in with a tenant group and a tenant in the alert type’s tenant list is in
the tenant group.

About Deduplication for Custom Alerts

To reduce noise and focus attention, Stellar Cyber automatically deduplicates multiple instances
of the same custom alert if they fire within a small window of time (five minutes, by default).
Stellar Cyber performs this deduplication by discarding fields that are always different between
separate alerts, calculating a hash, and monitoring future events for matches.

 You can override the default settings for deduplication of alerts created as part of an ATH

Playbook and specify your own time window. Refer to Create Alert Action .

Click here to see which fields are not considered for the purposes of custom alert

deduplication:

Certain fields are always different between two Interflow records, even if those records
represent multiple iterations of the same alert. Because of this, they are discarded before the
hash used to identify duplicate alerts is calculated. For that reason, the following fields are not
considered when calculating the hash used for deduplication:

Exact matches between:

stellar_index_id

stellar_uuid

timestamp

timestamp_utc

write_time

xdr_event

index

id

type

Fields containing the following substrings:

stellar

time

date

index

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

