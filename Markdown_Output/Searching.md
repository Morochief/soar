Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Searching

The search tool is often the first tool used when searching the Stellar Cyber data lake for specific
information. Although it performs the same function as the Queries tool it is more convenient for
quick operations. Its state is not saved across sessions or changes.

 The search tool is one of the set of controls covered in the Filter page. This page provides

more details on its function.

The search tool appears on the upper left corner of any page where it applies. Its operation is
that of a text box where any text may be entered once it is selected.

In the search box, you can enter any text, such as the name of a connector or a key field.

 When a search is active, a Clear all button appears. Clicking this button removes the filter

and set the tool to an empty string. See the examples below.

As with the other filter tools, the effect of the search terms are combined with all others to
produce the search results which is the set of all records being displayed on the screen. This
means that any search term entered is only going to match records that match all the other
filters.

 The search tool uses the Lucene query syntax used in Kibana, a popular graph database

system. See the Documentation  for more information.

Simple Search

The easiest use of the search tool is to simply type a string of characters. The string is compared
to all data in the record.

Because this type of search has to scan all record fields it may result in a long execution time for
the search. Using a tagged search as described in the next section may be a better choice.

 The search is not case sensitive.

Start Small
Searching a large amount of data can tie up the system for a significant length of time, especially
text searches. Start with a short time interval, see what you get, then expand the interval and
refine the search.

Use Quotes for Phrases and Special Characters
If you're searching with a phrase or special characters, enclose the search terms in quotes. For
example, a search for windows sensors lists everything with either windows or sensors. A
search for "windows sensors" returns only records with the specific phrase windows sensors.

Wildcards
In search strings the * can be used to match any string of characters and the ? can be used to
match any one character. So the string

Russia

and

Rus*

and

Ru??ia

will all match Russia.

Including Reserved Characters in a Search
The search tool uses standard rules for including reserved characters in your search and
requires you to escape them with a leading backslash. This applies to any of the following
characters that are reserved for use as operators in a query:

+ - = && || > < ! ( ) { } [ ] ^ " ~ * ? : \ /

For example, if you want to search for a file and path such as C:\myfile.txt, you must escape
both the colon and the backslash in the path with a leading backslash, as follows:

Using Regular Expressions in a Search
You can use regular expressions (regex) in searches. For example, the following syntax
searches for any username that ends with $:

username: / .*$ /

The regular expression is .*$ and must be enclosed in / /.

 For documentation about using regular expressions in Elasticsearch, see Elasticsearch

Guide (v8.17) .

Ranges
Some fields are not treated as strings for search purposes. Specifically, dates and IP addresses
are numeric values which cannot be matched with wildcard characters. These fields can be used
with a range syntax of the form [x TO y]. This is most useful when matching IP addresses
within a subnet. For example:

srcip:[192.168.1.0 TO 192.168.1.255]

will match all source IP address in the 192.168.1.0/24 sub-net.

Tagged Search

A tagged search calls out specific keys within the records being searched. In this case only the
dstip (destination IP address) field is being considered in the search, resulting in considerably
less processing time.

There are a large number of keys that may be relevant to a specific search. See the Interflow
overview page for more information about Interflow keys.

 The red underline in the image above is a result of the spell-check feature of the browser.

This may be disregarded if it appears.

Complex Search

For more precise searches, the search tool can also accept logical operations such as AND, OR,
and NOT. The full search term is entered as

srcip:10.0.11.6 AND command:apt-get

By combining terms the results may be refined to a smaller set of records.

 If a complex search is repetitively entered, it may save time to create a saved query instead.

See the Queries page for more information.

Common Search and Filter Techniques

Stellar Cyber provides a variety of tools that help you find the data you need. Use the following
summary of common search scenarios to help you perform your own searches, either globally, or
in specific tables:

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

