Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Managing Traffic Filters: Applications

 You must have Root scope to use this feature.

You can create traffic filters that sensor profiles use to filter applications before they're sent to the Stellar Cyber
platform (also referred to as the Data Processor). You can apply filters to Linux server sensors and modular sensors
to drop network traffic that matches your criteria. An application filter applies only to data intended for the Traffic index
and has no impact on other traffic data (such as syslogs) or Windows server sensors. Filtered applications also still
appear in Threat Hunting detection records for flood and scan detections. After you create these application filter
definitions, you can group them for more efficient use when configuring your sensors for metadata filtering.

 The table in this pane operates the same as all other tables in Stellar Cyber. You can sort, add, edit, and delete,

and export the displayed list.

To create or edit an Application filter:

1. Navigate to System | DATA SOURCE MANAGEMENT | Data Filters | Traffic Filters.

A panel for managing the traffic-based Application filters appears.

2. Select Create to add a filter (the Add Custom Application screen appears) or select the Edit icon to edit a

row.

3. Enter the Application Name.

This is the name of the filter that appears when you assign it in a sensor profile.

4. Choose the Tenant Name.

You can choose a specific tenant or All Tenants.

5. Define the filter using a combination of Protocol, Source IP address, and Destination IP address.

These fields are available as follows:

When Matched on Protocol is set to HTTP or HTTPS, you use the Attribute, Operation, and
Pattern fields to define your filter.

The Matched on Source and Matched on Destination options are not available when Matched
on Protocol is set to HTTP or HTTPS.

When Matched on Protocol is set to UDP or TCP, you can use either one or both of the Matched
on Source and Matched on Destination options to specify the address to match for the filter.

6. If you set Matched on Protocol to either HTTPS or HTTP, set up a pattern match as follows:

a. For HTTPS, choose whether to match a pattern in a Common name or a Server name. You can

match a pattern in any part or parts of a common name (CN) such as www.yourdomain.ai.

For HTTP, choose whether to match a pattern in a URI or a Server name. HTTPS traffic requires
certificate validation, and because certificates contain a CN, it's possible to filter by CN. In contrast,
HTTP traffic is not encrypted, allowing for detailed URI filtering that includes all parts of a domain
name plus URI components such as path, query, and fragment (for example,
http://www.yourdomain.com/path/to/resource?id=123&name=test#section1).

For both HTTPS and HTTP, you can filter by matching server name patterns. These can be a
partial or full server name (for example, w or www). Although it’s not a strict rule, the server name is
often the subdomain at the far left of a CN or domain name.

b. Specify whether the string to match Begins with, Ends with, or Contains the specified pattern.

c. Use the Pattern field to specify the string to match.

CN examples for HTTPS:

"Begins with www.yourdomain" matches www.yourdomain.com and
www.yourdomain.ai, but not secure.yourdomain.ai.

"Ends with yourdomain.ai" matches www.yourdomain.ai and web.yourdomain.ai but
not www.yourdomain.com.

"Contains yourdomain" matches www.yourdomain.com and web.yourdomain.ai but not
www.mydomain.ai.

URI examples for HTTP:

"Begins with www.yourdomain.ai/api/" matches www.yourdomain.ai/api/status
but not www.yourdomain.ai/v1/api/.

"Begins with /api/" matches URIs with a path that begins with /api/v1/users and
/api/status but not with /v1/api/users.

"Ends with #section" matches all URIs that end with the fragment #section but not
those that end with anything else.

"Contains ?user=" matches all URIs with the query ?user= but not any URIs without it.

Server name examples for HTTPS and HTTP:

"Begins with w" matches server names that start with w such as www and web but not sww.

"Ends with w" matches server names that end with w such as www and sww but not web.

"Contains w" matches server names with a w in any position (www, web, sws) but not server
names that don't contain a w such as secure.

 If two traffic filters are configured with the same pattern but use different operators (Begins

with, Ends with, or Contains), Stellar Cyber prioritizes the operators as follows, from highest
to lowest – Begins with, Ends with, Contains.
For example, if you create separate filters for a pattern that ends with mydomain.com and a
pattern that contains mydomain.com, any network traffic with this string present will match the
ends with filter because that filter has higher priority.

7. If you set Matched on Protocol to either UDP or TCP, use either one or both of the Matched on Source

and Matched on Destination options to specify the address to match for the filter.

A Matched on Source filter matches based on the source IP address of the packet. Enter the
Source IP/Mask in CIDR format.

A Matched on Destination filter matches based on the destination IP address and/or port of the
packet. Use the Define by specific IP and/or Define by specific Port fields to define the filter.

If you use one of the Matched on Source/Destination fields, but not the other, the other is presumed to be
set to Any. For example, if you set Matched on Source to 192.168.1.25/24 and leave Matched on
Destination unspecified, all traffic from 192.168.12.25/24 is matched.

8. Select Submit.

The filter is immediately available, but is not active until you include it in a sensor profile.

 Although the new filter is active as soon as it is bound to a sensor profile, it can take between 3-9

minutes before Stellar Cyber shows matching data under the new application name configured for the
filter in aella-adr-* (for example, My_Traffic_Filter) instead of an internal name (for example, HTTPS-
20000).

Applying Traffic Filters

You can add the filter to a modular sensor profile under Feature Customization | Network Traffic |
Application Metadata | Exclude certain applications.

You can add the filter to a standard sensor profile under Feature Customization | Network | Application
Metadata | Exclude certain applications.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

