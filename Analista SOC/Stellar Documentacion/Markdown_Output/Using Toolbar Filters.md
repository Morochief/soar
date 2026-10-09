Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using Toolbar Filters

The primary function of Stellar Cyber is to surface important information from a very large data
set. Use this topic to understand how to use Stellar Cyber's display filters to find information
more quickly and more easily.

 There are additional tools that allow you to create and reuse filters and queries and apply

them to sensors directly. Review related features described in Configuring Global Shared
Resources.

See the following sections for details:

Use Cases for Display Filters

Display Filters in the User Interface

Using Options in the Toolbar

Setting Filters in the Filters Panel

Other Filters that Affect Data Display (Tenant Selection and Indices)

Use Cases for Display Filters
Display filters are useful in any situation where you want to reduce the amount of data appearing
in the user interface and focus on just the information that interests you. For example:

Choose a period of time. The systems starts with a default time period of the last five
hours. The results will show what is going on in the network in real time. However, if
you're investigating a case from a few days ago, set the time filter to display only results
from that time period.
Examine what a given host is doing (or has done). The host in question can be either
internal or external. If you suspect a host might be infected with malware, use the host
or sensor filters to find that host.
Research events related to your cases. Use the assignee filter to see only events
related to cases you own.
Research events related to an open case. Use the case filter to see only events for
that case, or use the events filter to see related events not specific to the case.

Display Filters in the User Interface
The Filters panel is available in a collapsible panel in the upper left of most displays. For
example, on the Detections | Alerts page:

Selecting the Filters button opens a set of choices for filtering the data displayed on the page:

When you set a filter, the displayed data is immediately updated.

 The filter settings are persistent within a session. If you go to another page, the search

results remain the same. For example, if you set a filter on the Kill Chain page and then go
to the Threat Hunting page, the same filtered records are displayed there too.

Using Options in the Toolbar
This section describes the options available in the Stellar Cyber toolbar:

Searching Displayed Data

The Search control provides a powerful way to use Lucene syntax to search for data across all
pages of the currently displayed table.

A basic search is just a string of characters, such as "Intel" or "Google". Other common usages
include country names that appear in the geolocation references for IP addresses, or even IP
addresses themselves. An unqualified string searches all fields in the database. This could be
slow if the data set is very large.

See the Search page for details on constructing searches.

 See the Interflow overview for field names that are useful in searches.

Setting Time Filters in the Toolbar

The Time Type filter is often the first filter you should set. It controls the range of time for
displayed events, and can help greatly narrow the query results. This useful setting gives you a
quick view of what is currently happening in the network. To investigate an event in the past, set
this filter accordingly. To set the time range, choose a Time Type. When you choose a type, the
control immediately to the right of Time Type changes.

 Changes you make in the Time Filter are preserved within your local browser session

storage, not within Stellar Cyber. If you log out of Stellar Cyber and log back in, or if you
switch users, the time setting remains the same as you left it. Storage for different browser
types is independent, so the time setting you make while using one type does not affect the
time setting in another type (such as when you switch between using Chrome and Firefox).

The three available Time Types:

Relative
Daily
Absolute

Relative Time

Relative time sets the time range from the current time of day going backwards. When you
choose relative time, the Time Interval drop-box appears to the right. When you select an
interval less than 24 hours, an Auto Refresh (Min) menu is displayed, allowing you to specify how
frequently you want the data refreshed.

 Relative time is a moving window. As time progresses, new events are added to the results

while older ones drop off.

Daily Time

Daily time isolates individual days. When you choose daily time, the day selection box appears to
the right. Click the arrows to move forward or back by a day at a time. Click the date in the center
to see a calendar pop-up. The time is UTC.

Absolute Time

Absolute time allows you to search within a sequence of days.

To set absolute time:

1. Choose absolute in the Time Type drop-down list.

The Range box appears to the right.

2. Select the From date to set the start day on the calendar pop-up.

You can also set the hour and minute. The Search button starts blinking.

3. Select the To date to set the end day on the calendar pop-up.

You can also set the hour and minute.

4. Select the blinking Search button.

 This is a rare filter that does not take effect immediately. Instead, the control waits, allowing
you to set both dates without having the query execute before you can finish narrowing the
results.

Setting Filters in the Filters Panel
The filters available in the filters panel depend on the table you're currently displaying. This
section provides an overview of some of the most common and useful filters available in the
filters panel:

Alert Score Filter

Use this option to narrow your results to events with a specific score range.

Event Status Filter

Filter on the status of events. By default All Open events are included. The choices include:

No Filter
All Open
New
In Progress
Ignored
Closed

 Keep in mind that the global Status filters available here apply only to security events –

alerts. They do not apply to Cases. You can apply Status filters to Cases, too, but only from
the Cases interface itself.

Sensor Filter

A Stellar Cyber system includes any number of sensors. There are different types but they all
collect data and send it to the data processor via Interflow messages. Each sensor is identified
by a unique name in the system.

You can use the filter to select for all sensors or for a specific sensor. All Sensors is the default.

If you choose a specific sensor, the search results only include data that involves that sensor. If
you choose All Sensors, the filter has no effect on the results.

This filter is useful when investigating the activities that appear in a specific place in the network.
If you choose a Windows or Linux agent sensor, then the results focus on those specific
systems.

See the Architecture Overview page for more information on sensors.

User Name Filter

Filter on a specific Stellar Cyber user.

Event / Asset Tag Filter

Filter on events or assets using a specific tag.

Assignee Filter

Filter on the Stellar Cyber user assigned to investigate.

Additional Scoring Filters

Optionally set specific filters by fidelity, severity, and Threat Intel scores.

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
and Indices)
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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

