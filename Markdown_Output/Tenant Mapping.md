Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Tenant Mapping

 Root-level users



Early Access Program: If this feature doesn’t appear in your version of the Stellar Cyber
Platform, contact your account manager to inquire about taking part in the Early Access
Program and enabling its functionality.

Tenant Mapping
 is a feature that lets a single parser route incoming log events to
different Stellar Cyber tenants based on a tenant ID embedded in each event. Without it, a
parser is bound to one tenant and sends all of the logs it processes to that tenant. With Tenant
Mapping, a parser can examine each log event as it arrives, extract a tenant identifier from a
designated field, and direct the event to the appropriate tenant automatically.

This capability is particularly useful in two scenarios:

Managed security service providers (MSSPs) that monitor multiple customer
environments from a single platform. Customer logs from different organizations often
arrive in a single stream, each event tagged with a customer identifier. Tenant Mapping
allows one parser to deliver them to the correct customer tenant without manual
intervention.

Enterprises with multi-tenant deployments where logs originate from different business
units, regions, or subsidiaries, each represented as its own Stellar Cyber tenant. A
central parser configuration can handle the full log stream and distribute events based
on the organizational identifier embedded in each log.

The practical benefit in both cases is consolidation: instead of deploying and maintaining a
separate parser for each tenant, you configure one parser and one tenant map, and Stellar
Cyber assigns each log to the correct tenant automatically. As the number of tenants grows, you
update the tenant map rather than create new parsers.

Tenant Mapping works in conjunction with Parser Studio. When you configure a parser in Parser
Studio and enable Tenant Mapping on the Raw Log step, you designate a field in the incoming
log event that carries the tenant identifier. Stellar Cyber then uses that field—and, if necessary, a

tenant map to translate a vendor tenant ID to a Stellar Cyber tenant ID—to assign each event to
the correct tenant.

 Tenant Mapping and Parser Studio are accessible only to root-level users. For information
about enabling Tenant Mapping in a custom parser configuration, see Parser Studio –
Parsers.

Tenant maps are created and managed on the Tenant Mapping page, which is where you define
the lookup dictionary that the parser uses at runtime. A tenant map must exist before you can
select it in a parser configuration.

How Tenant Mapping Works
When a parser with Tenant Mapping enabled processes an incoming log event, it performs the
following steps:

1. The parser extracts the value at the configured JSON path from the log event.

For example, if the configured field is metadata.tenant_id, the parser reads the value
of that field from the event.

2. Depending on which Tenant Mapping option is configured in the parser, one of the

following happens:

If the parser uses Stellar Tenant ID, the parser extracts the Stellar Cyber tenant ID
value from the log. The parser uses it to assign the event to the matching tenant
directly. No lookup table is needed.

or

If the parser uses Vendor Tenant ID, the parser extracts the vendor tenant ID from a
vendor-assigned identifier in the log. The parser then looks it up in the selected tenant
map. If it finds a matching entry, Stellar Cyber associates the event to the
corresponding Stellar Cyber tenant. If the tenant map can't match the vendor tenant ID
with a Stellar Cyber tenant, Stellar Cyber assigns the log to the same tenant as the
sensor that received it.

 If events are appearing under an unexpected tenant, review your tenant map

entries.

The Tenant Mapping Page
To access Tenant Mapping, navigate to System | ORGANIZATION MANAGEMENT | Tenant
Mapping.

The page displays an Entries table of existing tenant maps. Each row represents one tenant
map and shows the following information:

Column

Name

Description

The name defined for the tenant map when it was created

Description

An optional description describing some aspect of the tenant map such as its purpose

# Entries

The number of vendor tenant ID-to-Stellar Cyber tenant ID mappings that the tenant map contains

Last Modified Time The date and time the tenant map was last updated

Actions

Edit (pencil icon) and Delete (trash icon*) controls for each tenant map

* Before deleting a tenant map, confirm that no parser configurations in Parser Studio are
currently using it. Deleting a tenant map that is referenced by an active parser causes that parser
to lose its tenant assignment capability. Log events that previously matched entries in the deleted
tenant map will instead be assigned to the tenant associated with the sensor that receives them.

The page also provides the following controls:

+ Create Tenant Mapping – Opens the Create Tenant Map dialog box to define a new
tenant map.

Export CSV – Exports the list of tenant maps shown in the table.

Select View – Opens the Saved Views panel to create or apply a customized table
view.

 For information about Export CSV and Select View, see Using Tables.

Create a Tenant Map
Before you begin, confirm the following:

You have the Stellar Cyber tenant IDs for every tenant you want to include in the tenant
map. You can find tenant IDs on the Tenants page (System | ORGANIZATION
MANAGEMENT | Tenants).

You have the vendor tenant IDs that the third-party system uses to identify those
tenants in its log events.

(Optional) If you are uploading a CSV file, you have prepared it with the correct two-
column format: Vendor Tenant ID and Stellar Cyber Tenant ID. You can download the
provided template from the + Create Tenant Mapping dialog box to use as a starting
point.

To create a tenant map:

1. Navigate to System | ORGANIZATION MANAGEMENT | Tenant Mapping and then

select + Create Tenant Mapping.

The Create Tenant Map dialog box appears.

2. Enter a descriptive name in the Tenant Mapping Name field.

Choose a name that makes the tenant map easy to identify when selecting it in a parser
configuration in Parser Studio.

3. (Optional) Enter a description in the Description field.

Consider including additional context, such as the vendor system the tenant map
supports or the set of tenants it covers.

4. Add entries to the tenant map using one or both of the following methods:

Upload a CSV file: Drag your prepared CSV file into the upload area, or select the area
to browse for the file. When the upload succeeds, a confirmation banner displays the
number of entries loaded and the entries appear in the Entries table. Confirm that the
count in the banner matches the number of data rows in your file.

 Use the link to download a provided template, which is a pre-formatted CSV file

with the correct column structure and a sample row that you can replace with your
own data.

Add entries manually: Select + Add Entry. An inline row appears in the Entries table.
Enter the Vendor Tenant ID and the Stellar Cyber Tenant ID in the respective fields.
Repeat for each additional entry.

You can combine both methods: Upload a CSV file to load a batch of entries, and then
use + Add Entry to append individual entries in the same session.

Each vendor tenant ID must be unique within a tenant map. If you add an entry whose
vendor tenant ID already exists in the tenant map and then select Create or Update,
the duplicate entry is silently discarded and the original is retained. The pre-save count
shown in the confirmation banner won't match the post-save entry count if duplicates
are staged. Check the # Entries column after saving to confirm the final count.

5. Review the entries in the Entries table to confirm that the Vendor Tenant IDs and Stellar
Cyber Tenant IDs are correct and that the Stellar Cyber Tenant Name column reflects
the expected tenant names.

The following are some notes about the file upload and processing:

The Stellar Cyber Tenant Name column that appears in the Entries table
after upload is resolved automatically from the Stellar Cyber Tenant ID. It's not
a column in the CSV file and does not need to be provided.

After uploading, confirm that the number of entries shown in the confirmation
banner matches the number of data rows in your CSV file. If the counts do not
match, remove the affected entries and re-upload the file.

Uploading a CSV file to a tenant map that already contains entries replaces all
existing entries with the contents of the uploaded file. The upload does not
append to existing entries. Before uploading, ensure that your CSV file
contains all of the entries you want the tenant map to contain, not just the new
ones you are adding.

6. To remove an entry, select the Delete icon for that row.

7. Select Create.

The new tenant map appears in the Tenant Mapping table on the main page and is
now available for selection when configuring a parser in Parser Studio. (For
information, see Parser Studio.)

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

