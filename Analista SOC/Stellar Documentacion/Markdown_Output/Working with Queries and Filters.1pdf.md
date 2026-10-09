Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Working with Queries and Filters

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

J04 Open XDR Investigation Tools (04h:47m)  

Create and Save Queries with the Query Tool (28m:00s)

Learn to create and save custom queries using the Query Tool, then watch a
demonstration applying these techniques across the Stellar Cyber Platform. Explore
how to build query strings, select relevant fields, and save configurations for efficient
recall, enabling consistent search results across dashboards, ATH playbooks, and
Case Management without recreating searches from scratch.

P03 Using Query Builder and Alert Filters (45m:00s)  

PART 1: Introduction to Query Builder and Alert Filters (08m:15s)

Learn how to use the query builder to create custom queries that refine data searches
across logs, alerts, and events in the Stellar Cyber Platform. See how logical
operators, field types, and nested conditions help pinpoint relevant security data.
Understand how alert filters suppress unnecessary alerts, improving your focus on
critical events.

PART 2: Navigating Query Builder in the UI (07m:15s)

Discover where to access the Query and Filter Manager in the Stellar Cyber Platform
UI. Learn how to build correlation queries to identify attack patterns and visualize
events. See how to create custom charts, threat-hunting views, and filters directly
within different platform areas, such as Investigate and Visualize.

PART 3: Building Effective Queries with Query Builder (11m:15s)

Follow a demonstration of creating complex queries for automated threat hunting and
dashboards. Learn how to nest conditions, use lookup groups, and apply operators
like "greater than" and "within" to refine results. See examples of data exfiltration
detection, SQL dumpfile monitoring, and script anomaly queries.

PART 4: Field Types, Logical Operators, and Lookup Lists (07m:45s)

Understand field types like Boolean, date, IP, and string, and how they impact query
creation. Learn to use logical operators such as "contains," "is in lookup," and "field
exists" for precise filtering. See how lookup groups simplify queries by referencing
predefined lists of values, such as known malicious IP addresses or domains.

PART 5: Alert Filters (07m:15s)

Learn how alert filters help suppress false positives while retaining raw data for
machine learning. See an example of filtering impossible travel alerts by subnet and
event type. Understand the importance of testing queries in the query builder before
applying them as alert filters to avoid missing important alerts.

The first time you access a link on the portal during a session, you must log in to access
content.

You can create queries with specific parameters and conditions to search through large volumes
of data from across your network, filtering and retrieving relevant information from sources such
as logs, network traffic, and security events. You can then include the results in various areas of
the platform such as automation rules, visualization tools, and reports. Additionally, you can build
a library of queries to meet your exact needs, whether you're searching for particular IP
addresses, user activities, or suspicious trends or patterns of network behavior.

Alert filtering helps you manage large numbers of alerts that the Stellar Cyber Platform
generates. Depending on the size of your network, there might be hundreds or even thousands
of alerts generated daily. Therefore, it’s important to filter out those that can be ignored so you
can focus on and respond to the more serious alerts.

 When you filter out specific types of alerts, Stellar Cyber still continues to generate them,
but it then discards them so they don’t populate the system and don’t appear in the UI.
There might be situations where filtered alerts would have provided more context to a case,
so consider when to continue displaying alerts that don’t require analysts’ attention but do
provide a fuller view of the activity occurring and when to filter them so analysts aren’t
inundated with too many low-priority alerts.

Similar to how you can use alert filters to suppress the creation of alerts, you can use case filters

 to suppress the creation of cases. In this way, you can reduce the number of cases to

focus better on the ones that warrant greater attention.

The Query and Filter Manager (System | Saved Objects | Queries and Filters)
centralized hub for managing search queries, alert filters, and case filters. It consists of a query
and filter builder, a queries table, an alert filters table, and a case filters table. The builder lets
you create and test queries while the tables let you easily view, modify, and delete them in one
place. With these capabilities combined, the Query and Filter Manager streamlines how you
interact with queries and filters, whether they were created in the Query and Filter Manager or on
feature pages throughout the Stellar Cyber user interface (UI).

 is a

The query and filter builder is a robust tool that not only lets you construct complex searches and
exclusion filters—as the query builders and filter builders on individual feature pages also do—
but it also includes Run and Save As functions. The Run option lets you test queries before
applying them, ensuring you get expected results without leaving the page. The Save As
function lets you make copies of queries and filters and adjust settings, working on up to ten
variations in tabbed dialog boxes simultaneously. For details about creating queries, alert filters,
and case filters, see Queries and Filters.

Stellar Cyber automatically updates the tables with the queries and filters that you create using
the builder in the manager and the builders that appear on various pages throughout the Stellar
Cyber UI. It's these feature pages themselves where you apply queries to retrieve the data you
want and apply alert and case filters to exclude the alerts and cases you don't want:

Threat Hunting | Correlation Search | New Query  in the Configure section

Automation | Automation | Create to add a new playbook or  ("Edit this row" icon) to
edit an existing playbook | New Query

Reporting | Reports | <report_name> and then select  New query in the Apply
Query drop-down list

System | Saved Objects | Charts | Create to add a new chart or  ("Edit this row"
icon) to edit an existing chart | New Query on the Query step in the chart builder

Dashboards | PREDEFINED | XDR Kill Chain | Filters | Queries | New Query 

Detections | Alerts | View for an Alert Type |  ("More info" icon) for an alert event |
Actions | Add Alert Customization

Cases | Settings (

 in upper right) | Case Filters | + Create or Edit

The tables in the Query and Filter Manager share common behaviors with all tables in Stellar
Cyber, such as column management, sorting, editing, and deleting.

The Query and Filter Manager groups queries and filters together because both use similar logic
in their construction. By combining the builder and tables, the Query and Filter Manager provides
a single location where you can create, edit, and delete queries, alert filters, and case filters,
streamlining their creation and management.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

