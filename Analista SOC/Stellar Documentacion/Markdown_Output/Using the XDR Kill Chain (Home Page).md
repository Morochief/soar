✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Using the XDR Kill Chain (Home Page)
Learn more at Stellar Cyber Academy.
The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.
J02 Introduction to Features in the User Interface (02h:24m)  
Alerts in the UI (07m:00s)
Explore the Alerts view, learning how to filter, sort, and manage Alerts within the Stellar
Cyber Platform. Understand how machine learning drives alert generation and
prioritization, and how to use these alerts to create custom Cases.
Alert Management (33m:00s)
Explore available views for managing and investigating alerts, including the Alerts Table,
Kill Chain, and Threat Hunting views within the Stellar Cyber Platform. Learn to leverage
MITRE ATT&CK data, threat intelligence, and toolbar filters to enhance alert triage and
investigation workflows. Follow along with a demonstration on interacting with alerts
across different views, applying search tool queries, and conducting threat-hunting
activities efficiently. Discover how to tune alert settings and use custom filtering options
for focused analysis across the data lake.
J03 Investigations and Workflows (05h:48m)  
Built-In Investigation Views (25m:00s)
Get familiar with built-in investigation views within the Stellar Cyber Platform, such as
case views, alerts, and kill chain views. Learn how to prioritize and sort cases and alerts
for effective triage, using these views to drive incident response.
The first time you access a link on the portal during a session, you must log in to access
content.
The XDR Kill Chain dashboard is the default home page for Stellar Cyber. It provides a central
location for assessing overall risk and threats found within the environment. Drilldowns to

ongoing cases, risky assets, and tactics help you keep the environment and its systems secure
by zeroing in on what requires immediate attention.
The illustration below introduces you to the XDR Kill Chain dashboard's major components.
Following the illustration, you can review detailed information on each of the main components.
XDR Kill Chain Loop – Provides critical/total alert counts at each of the XDR Kill Chain
stages; select a stage to drill to the Alert Types page for the corresponding stage.
Critical alerts are those with an Alert Score of 75 or greater.
Status Panel – Provides at-a-glance status graphs for case status, cases, alerts, users,
and assets, including trend information.
Top Cases Panel – Lists collapsible capsule summaries of the top cases by score;
select a case to drill to its Case Detail view.
Top Risky Assets Panel – Lists collapsible capsule summaries of the top risky assets by
score with multiple drilldowns for further analysis.
Tactics Panel – Provides a bar graph quantifying the alerts observed by Stellar Cyber
according to their corresponding tactics. You can filter by critical or non-critical tactics
and drill to a view of the Alert Types page filtered by the corresponding tactic.
Common Controls – Provides the standard menu bar, as well as search, query, and
filter controls that appear throughout Stellar Cyber.
Getting Back to the XDR Kill Chain Dashboard
The Stellar Cyber XDR Kill Chain dashboard appears immediately after you log in and is the
system's default home page:
If you have not changed your home page by selecting the Set as homepage menu item
from the upper, right-most icon, you can get back to the XDR Kill Chain dashboard by
selecting the Stellar Cyber logo at the upper left of the display or by selecting the
Dashboards | PREDEFINED | XDR Kill Chain menu item.
If you have changed your home page by selecting the Set as homepage menu item,
you can get back to the XDR Kill Chain dashboard by selecting the Dashboards |
PREDEFINED | XDR Kill Chain menu item.

You can assign a different page to display when you select the Stellar Cyber logo
(Home). When you navigate away from the XDR Kill Chain page (which is the default
for Home), for example, to the Alerts page, you can select the Set as homepage menu
item to make that page your new Home page. You can toggle it back by select the
Unset as homepage menu item.
XDR Kill Chain
The centerpiece of the XDR Kill Chain dashboard is the XDR Kill Chain loop. The XDR Kill Chain
identifies five separate stages on the attack landscape, each with its own associated tactics and
techniques. Tactics and techniques include both those based on the MITRE |
 ATT&CK framework , as well as native XDR versions developed by Stellar Cyber. You can
hover your mouse over any XDR Kill Chain stage to see a popup listing the tactics tracked at the
corresponding stage.
Each of the stages reports counts for critical and total alerts within the selected filters and
provides a drilldown to the Alert Types display, filtered for the corresponding stage.
The XDR Kill Chain includes the following stages, each identified by its own distinctive color and
icon. These colors and icons are used consistently throughout the user interface to reinforce
stage identification.
| XDR Kill  Icon | Summary | Associated | Associate Classic Attacks |     |
| -------------- | ------- | ---------- | ------------------------- | --- |
| Chain          |         | MITRE |    | d                         |     |
| Stage          |         | ATT&CK     | XDR Tacti                 |     |
|                |         | Tactics    | cs                        |     |
Port scanning
| Initial  | Attackers are trying to access your network. |             |          |                |
| -------- | -------------------------------------------- | ----------- | -------- | -------------- |
|          |                                              | Resource    | XDR SBA  | External brute |
| Attempts |                                              |             |          | force login    |
|          |                                              | Development |         | attempts       |
|          |                                              |             | External | Phishing       |
Probes of
|     |     | External | XDR NBA |     |
| --- | --- | -------- | ------- | --- |
known
|     |     | Credential |     | security holes |
| --- | --- | ---------- | --- | -------------- |
External

Access
XDR UBA
Reconnaissance

|     |     | Initial Access |    |     |
| --- | --- | -------------- | --- | --- |

Persiste Attackers are trying to maintain access to your Persistence  XDR EBA External
trojans
nt systems in spite of defensive techniques.
Execution  External Account
Foothold manipulation
XDR Malw
Defense
are
Evasion 
XDR Intel
Command and
Control 
Explorati Attackers are inspecting your network, learning Collection  Internal Internal port
scans
on about your environment before taking further action. XDR NBA
Discovery  External
SQL dumpfile
s
Suspicious
SMB copies
Propagat Attackers are trying to obtain additional privileges Internal
Internal Internal
spyware
ion and access and control additional systems on your
Credential XDR UBA Internal
network. trojans
Access 
Internal
Internal brute
force
Privilege XDR Malw
Escalation  are
Lateral
Movement 
Exfiltrati Attackers are trying to steal data, potentially Exfiltration  Syn floods
on dumping it in a way that avoids detection, and/or Ransomware
& Impact vandalizing your systems and data. Impact  File action
anomalies
This Kill Chain loop provides an immediate barometer of the quantity and severity of the events
observed by Stellar Cyber within the current filter settings. Each stage of the Kill Chain loop is
shown with counts for critical and total alerts within the current filters:
The number on the left reports the number of critical alerts within the current filters.
These alerts have been scored by machine learning services with a Alert Score of 75 or
greater and are most likely to need immediate attention.
The number on the right reports the total number of alerts detected within the current
filters.
 The dashboard only shows data matching the current filters set using the controls at the top
of the display (time, event score, sensor, and so on).
Drilling to Alerts from the XDR Kill Chain Loop
You can select any of the stages in the XDR Kill Chain loop to drill to the Alerts page with a
display filter automatically applied so that just the alert types at the selected stage are displayed,
as illustrated in the figure below.

Pausing the XDR Kill Chain Loop
You can pause the animation of the XDR Kill Chain loop from upper, right-most menu, as shown
below:
Status Panel
The Status panel appears immediately above the XDR Kill Chain and displays separate, color-
coded cards illustrating counts and trends for Case Status, Cases, Alerts, Users, and Assets.
The bar graphs and counters in the Status Panel cards all function in roughly the same
way. Consider the Cases status card shown below:
Case Status – Use this panel to gauge your progress on addressing cases that match
the selected filters:
The bar graph shows the number of Closed cases (those with a Status of
either Resolved or Cancelled set in the Case Detail page) compared to the
total number of cases that match the selected filters.
The Closed indicator shows you the trend in case closure, comparing the net
increase or drop in closed cases to the previous time window of the same size.
Closed cases are those with a status of either Resolved or Cancelled in the
Case Detail page.
The Total indicator shows you the trend in total cases, comparing the net
increase or drop in total case closures to the previous time interval of the same

size.
Cases – Use this panel to assess the number of cases that match the selected filters.
The bar graph, Critical and Total indicators all function in roughly the same ways as
the Cases Status panel, except for critical and total case creation.
Alerts – Use this panel to assess the number of critical alerts detected in the selected
time interval. The bar graph, Critical and Total indicators all function in roughly the
same ways as the Case Status panel, except for critical and total alert creation.
Users – Use this panel to assess the number of risky users detected in the selected
time interval. The bar graph, Risky and Total indicators all function in roughly the same
ways as the Case Status panel, except for total and risky user detection.
Assets – Use this panel to assess the number of risky assets detected in the selected
time interval. The bar graph, Risky and Total indicators all function in roughly the same
ways as the Case Status panel, except for risky and total asset detection.
Top Cases Panel
The Top Cases panel lists the most severe Cases for the selected tenant in the selected Time
Interval according to their score. The panel is located at the left of the XDR Kill Chain
dashboard, directly under the Case Status and Cases panels, handily arranging these related
tools together.
 The Top Cases panel only displays open cases, regardless of the setting of the Status filter
at the left of the display. Because of this, any cases you have set to Resolved or Cancelled
do not appear in the Top Cases panel.
A case is a set of multiple correlated alerts and entities constituting a potential unified security
attack, ranked by a dynamically updated score indicating the severity of the attack. Stellar Cyber
uses its machine-learning capabilities to generate cases automatically, grouping related alerts
into a unified case for improved attack resolution.
Cases appear initially in the Top Cases panel as collapsed summary entries, but can be
cascaded open using the ˅ button at their right, as shown below. You can also expand all of the
entries in the list using the Expand all button at the top of the panel.
Cases are reported in the Top Cases panel with the following information:
Name – Stellar Cyber automatically assigns a name to each Case it reports. You can
either accept the default name or supply your own in the Case Detail view.
Tenant – The tenant with which this Case is associated.
Ticket ID – The system-assigned ticket number for the Case.

Status – The status associated with this Case. Can be either New, Escalated, In
Progress, Resolved, or Cancelled. You can change the status in the Case Detail view,
giving you a handy way to track your team's Case response over time.
Case Score – The severity of the Case, as determined by Stellar Cyber. The score
updates in real time as events and entities are added to or removed from the Case.
Scores are color-coded to indicate their severity.
Alerts – A count of the alerts associated with the Case.
 The maximum of associated alerts is 5,000.
Severity– The priority of the Case. Cases start out with a Medium priority, but can be
changed in the Case Detail view to Low, High, or Critical.
Assignee – The assignee for the Case, if any. You can assign resources to Cases in
the Case Detail view.
Modified At – The last time the Case was modified by a user, either by changing any of
its properties (for example, changing its status or name), or by adding/removing any
event associated with the Case.
Creator – The user account that created the Case. Cases created by Stellar Cyber are
listed with a creator of System.
Created – The time at which the Case was created by Stellar Cyber.
Drilling to the Case Detail Page
To view the Case Detail view for the corresponding Case, select the Case name in the Top
Cases panel.
Top Risky Assets Panel
The Top Risky Assets panel lists assets in the selected Time Interval in descending order of Risk
Score. The panel is located at the right of the XDR Kill Chain dashboard, directly under the
Assets status panel, handily arranging these related tools together.
Assets appear initially in the Top Assets panel as collapsed summary entries, but can be
cascaded open using the ˅ button at their right, as shown below. You can also expand all of the
entries in the list using the Expand all button at the top of the panel.
Assets are reported in the Top Assets panel with the highest-risk entries at the top. As shown in
the figure below, each asset is listed with the following information and context-sensitive
drilldowns:

Risk score. The number in the circle indicates risk. The highest risk is 100 and the least
is zero.
IP address or hostname of the asset.
Context menu access for drilldowns to the following additional Stellar Cyber for the
asset:
Asset Detail View – Opens the Assets | Asset Analytics | Asset Details tab
for the selected friendly name, hostname, or IP address as the filter.
360 Panoramic View – Opens the Dashboards | Panoramic view with the
selected friendly name, hostname, or IP address as the filter.
VT VirusTotal Lookup – Performs a lookup on virustotal.com  for the
selected friendly name, hostname, or IP address.
 Add as Including Filter – Creates a filter to display only those events
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
identified using their consistent stage icons and colors. Select any stage entry to drill to
the Alert Types page, filtered for the corresponding asset and Kill Chain stage.
A one-line summary for the most severe alert associated with the asset. Select the
More Info icon to drill to the Event Display for the alert, including the supporting
Interflow data.
Tactics Graph
The Tactics graph at the bottom of the XDR Kill Chain dashboard quantifies alerts by their
associated XDR Kill Chain tactic within the selected filters.

Tactics are listed in XDR Kill Chain order, from left to right along the x-axis of the graph.
Bar graph entries for each tactic are displayed in their corresponding XDR Kill Chain
stage color.
Drill to the Alert Types page by selecting any bar graph entry for a tactic and selecting
the Drilldown pop-up that appears. In response, the Alert Types page appears, already
filtered by the selected tactic and time interval.
Hover your mouse over the Legend entries to include  or exclude  critical or non-
critical alerts from the graph. Critical alerts are those with an Alert Score of 75 or
greater.
 Once you've applied an include/exclude filter, you can see its current settings at the
top of the display. As shown below, you can also clear the filter to return the display
to its unfiltered state.
Common Menus and Controls
This section summarizes the common menus and controls that appear on Stellar Cyber pages:
Main Menu
The user interface has icons on the left side of the screen. Selectk the icon to expand the
icons into text menus to navigate to any function in Stellar Cyber.
All the menus are described in the Overview of New User Interface.
Select the logo to get back to the current Home page.
Dashboards: Access both predefined and custom dashboards, as well as create and
manage new dashboards and charts.

Cases: Manage cases– sets of multiple correlated alerts – reported by Stellar Cyber.
Detections: Display a list of alerts observed by Stellar Cyber, organized by the
XDR Kill Chain and analyzed with machine learning and view Detection Management.
Threat Intelligence: Access both IoCs and threat intelligence feeds.
Threat Hunting: Use selected views to perform threat hunting.
Assets: View asset analytics and user behavior analytics.
Automation: Define your own alert types through automation and initiate and manage
actions such as user, firewall, or device actions taken in response to events.
Reporting: Create and schedule reports.
System: Access to administrative tools.
Filter Controls
Stellar Cyber's display filters are available both in the toolbar and as a collapsible panel at the
left of most displays:
Toolbar filters are at the top of pages that display query results, which is most pages in
Stellar Cyber. For example:
The Filters panel is available at the left of most displays by toggling it open with the
button in the toolbar:
When you set a filter, the displayed data is immediately updated. In addition, if you set a filter
from the Filters panel, the filter button updates to show the number of filters applied once the
panel is toggled closed. For example – .
 The filter settings are persistent within a session. If you go to another page the search
results remain the same. For example, if you are on the Kill Chain page and go to the
Threat Hunting page, the same records are displayed.
Each of the controls take effect immediately, except for a Time Type of absolute.
See the About Filters page for a complete description of these controls.

 The filter settings are persistent for the current session. So they are maintained when you
go to a new page.
 You can configure a preset filter for all of your views on your User Profile.
Search Tool
The search tool performs a simple search on the set of records displayed. Although easy to use,
it is capable of complex search operations. For more information see the About Search page.
Saved Query / Query Builder
Use the Query Builder to construct both simple and complex queries that search the Stellar
Cyber database.
You can also save and retrieve queries.
See About Queries for a complete description on how to use queries.
 The current query setting is persistent for the current session and is maintained when you
go to a new page.
Current User
The Current User dropdown shows an icon for the currently logged-in user in the upper, right-
most corner of the user interface. It provides access to the following functions:
Set as homepage – Lets you get back to the XDR Kill Chain Dashboard.
Pause Animation – Lets you pause the animation of the XDR Kill Chain graphic.
Profile – Lets you edit your user settings.
Feature preview – Lets you switch between the legacy user interface and the new user
interface
Light theme – Lets you switch between the light theme and the dark theme
Logout – Ends the current session and returns you to the Login page.
Selected Tenant
All records in the Stellar Cyber system are assigned to a tenant. In addition to the filter controls,
search and query results can be narrowed to reflect only those records of a specific tenant.
Alternatively, all tenants can be included.

 Stellar Cyber users assigned to a tenant but who are not admin users cannot change the
tenant setting.
Select the Tenant drop-down list at the top right of the user interface to change the selected
tenant.
See the About Tenants page for more information on Stellar Cyber tenants.
 The Select Tenants setting is persistent within the current session and is maintained when
you go to a new page.
Utility Icons
The icons at the upper right of the user interface provide access to general utilities.
Select the question mark icon to open the Help menu, which provides access to
knowledge base topics, API documentation, the Resource Center, and other learning
and support tools. For details, see .Help Menu and Resource Center .
Select the alarm bell icon to open Notifications to show you the number of unread
system notifications. Select the icon to launch the Notification Center. Users with
appropriate access can specify rules that govern how system notifications are
generated in the System Action Center.
Select the tasks icon to open Tasks to keep track of the progress, success, or
failure of ongoing Stellar Cyber activities (bulk actions to Cases, asset edits, cold data
queries, tenant creations, data purges, tenant removals, and so on). You can only see
tasks related to activities you yourself have initiated or those from other users who are
within your user scope (for example, a Super Admin with Root scope can see tasks
from all users).
Here's how you display the Task List, complete with some successful bulk actions:

Depending on the type of task displayed and its current state, different options are
available for managing tasks, including the ability to clear, and in some cases, cancel,
ongoing tasks.
 You can also view the Task List as its own page using the System | Task
Management option.
Help Menu and Resource Center
The Help menu gives you direct access to documentation, training, and support resources. From
the Help menu, you can open the Resource Center, which brings together walkthroughs,
documentation, training, community discussions, support options, and Stellar Cyber news in a
single location.
Help Menu
Select the question mark icon in the top-right menu bar to open the Help menu. From here, you
can access context-sensitive Knowledge Base topics, the Knowledge Base home page, API
references, Resource Center, and the Stellar Cyber software version that's currently running.
Knowledge Base > current page name – Opens the specific knowledge base topic for
the active page, providing context-sensitive help.
Knowledge Base Home – Opens the home page of the Stellar Cyber Knowledge
Base.
API Docs – Opens a direct link to Swagger-based API documentation. Developers can
use this interactive UI to understand all available endpoints, view request/response
models, and execute live API calls for testing and validation.
Product Roadmap – Discontinued.
Resource Center – Opens the Resource Center (see below for details).
System Information – Displays the version of the currently running Stellar Cyber
software.
Resource Center

The Resource Center is a central hub for learning, documentation, and community access. From
here, you can launch product walkthroughs for new and updated features by selecting What's
New? (Feature Walkthroughs)), open Stellar Cyber release notes and documentation, access
the Stellar Cyber Academy, join community discussions, and connect with the Support Portal. At
the bottom of the Resource Center, you can stay current with the latest Stellar Cyber News.
It includes the following items:
What’s New? (Feature Walkthroughs) – Launches product walkthroughs that
introduce new or updated features. The walkthroughs appear as interactive overlays on
top of the user interface, highlighting selectable elements and providing clear, step-by-
step guidance.
 After upgrading to a new Stellar Cyber software version, a banner appears at the
top of the UI from which you can access walkthroughs. If you dismiss the banner, it
does not reappear automatically. However, you can still access the walkthroughs
later from the What’s New? (Feature Walkthroughs) link in the Resource Center.
Release Notes – Opens a list of the latest sets of Stellar Cyber release notes from
which you can choose which ones to read.
Stellar Cyber Knowledge Base – Opens the Stellar Cyber documentation home page
(the same topic as the Knowledge Base Home link in the Help menu).
Stellar Cyber Academy – Opens the Stellar Cyber Academy login page or home page,
depending on your login state.
Community – Opens the Stellar Cyber Community page in the Customer Success
portal.
Support Portal – Opens the Stellar Cyber Customer Success Sign In page or your
account landing page, depending on your login state. From the landing page you can
view or create support tickets and access additional Customer Success resources such
as announcements, documentation, community discussions, and training links.
At the top of the Resource Center is a search tool that lets you search the content in the
Resource Center.
At the bottom of the Resource Center are two additional options: Home and News. Selecting
Home returns to the Resource Center with all the links described above. Selecting News opens
a list of recent Stellar Cyber news articles such as blog posts, podcasts, webcasts, and so on.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  