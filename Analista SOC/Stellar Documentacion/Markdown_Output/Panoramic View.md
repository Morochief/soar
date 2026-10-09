Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Panoramic View

Stellar Cyber provides a host-centric way to view alert activity for specific hosts, including display
of a 360 Panoramic view using either of the following methods:

Access Dashboards | Panoramic, select the blue three-dot icon in the upper right
corner of a specific tile, and then choose 360 View Panoramic from the pop-up menu
that appears.
From the context menu for specific data such as in Event Details, select 360 View
Panoramic.

 The data on this screen is subject to the filter terms set by the tools at the top of the screen.

See the Filter page for more information on working with filters.

Dashboards | Panoramic
When you access Panoramic views from the Dashboards menu, you have the option of
examining hosts based on whether they are internal (Suspect Assets) or external (Suspect
External Hosts). These tabs display a scrollable grid of cards, each of which shows the
information for a single host.

As shown in the figure below, each host is listed with the following information and context-
sensitive drill-downs. Use the drill-down menu to further analyze a specific host, including drilling
into a 360 panoramic view (described below).

Risk score. The number in the circle indicates risk. The highest risk is 100 and the least
is zero.

IP address or hostname of the asset.

Context menu access
asset:

 for drill-downs to the following additional Stellar Cyber for the

Asset Detail View – Opens the Assets | Asset Analytics | Asset Details tab
for the selected friendly name, hostname, or IP address as the filter.

360 Panoramic View – Opens the Dashboards | Panoramic view with the
selected friendly name, hostname, or IP address as the filter.

VT VirusTotal Lookup – Performs a lookup on virustotal.com  for the
selected friendly name, hostname, or IP address.

  Add as Including Filter – Creates a filter to display only those events
containing the value in the field.

 Add as Excluding Filter – Filters out those events containing the value in
the field.

 Copy to Clipboard – Copies the field value to the clipboard so it can be
pasted elsewhere.

Copy as Query – Copies a pre-built Lucene query that searches for related
activity involving the IP address of the asset across multiple fields. Use this
query in tools like Threat Hunting or Search to investigate communications
where the IP appears as source, destination, or host.

XDR Kill Chain summary. Alert counts are shown for each XDR Kill Chain stage,
identified using their consistent stage icons and colors. You can click any stage entry to
drill to the Detections | Alerts page, filtered for the corresponding asset and Kill Chain
stage.

A one-line summary for the most severe alert associated with the asset. You can click
the  button to drill to the Event Display for the alert, including the supporting Interflow
data.

360 Panoramic View
The 360 Panoramic View is an extensive summary of an individual host, including a common
Header section and then separate Attack Diagram and Timeline tabs. An example of this
display is shown in the following image.

The view contains the following sections:

Header – The top section holds a summary of the identity of the host. Not all fields will
have values depending on the vantage points of the sensor(s) are able to collect data
and also what reference information is available. The first number is the calculated risk

which is the prime indicator of the display. You can use the
IP and Host drilldowns available in the Suspect Assets summary list.

 menu to access the same

Attack Diagram – This appears to the right of the Kill Chain Time Sequence. It
provides a connection chart that lists all (or as many as possible) hosts that are
interacting with the currently selected host. The colored dots on the connection lines
represent the detectors that identified the information.

 Hovering the mouse cursor over the IP addresses in the Attack Diagram provides

additional information on the associated host.

Timeline – Each stage of the XDR Kill Chain has its own time-series graph of alerts that
involve this host. Each alert type is assigned its own color and mentioned in the legend.

Table – The bottom of the display provides a table of all the events in the data
set for the host.

See the Tables page for more information on working with tables.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

