Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring XDR Connector

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development. XDR Connector is available for Limited
Availability.

  You must have Root scope to use this feature.

XDR Connect is a webhook  ingestion method that makes it easy to integrate external data
sources. It provides a scalable and standardized framework for rapid connector development and
consistent data ingestion. Use XDR Connect to seamlessly integrate third party data sources into
Stellar Cyber.

An XDR connector is a webhook-based custom connector. You configure the connector in the
user interface, normalize the data, then POST events using the custom-generated webhook
URL.

The XDR connector can be used to integrate a new data source particularly when:

the data is in JSON format

the third party vendor product can send the JSON data directly to a webhook URL

the ingestion does not need custom normalization or enrichment

 The data ingested through the XDR connector does not support customized normalization
and enrichment, so the ingested data does not support third party alert integration, ML-
based detections, or built-in analytics. You can use Automated Threat Hunting (ATH) rules
for additional detections and custom alerts.

If the data requires full normalization, enrichment, third party alert integration, or must be
retrieved through a vendor API rather than pushed via a webhook, you can use a custom script
to post the data in JSON format or you can request a new native API connector from Stellar
Cyber.

To participate in the Early Access Program, contact your account manager. To request an API
connector from Stellar Cyber, you can submit a ticket or contact your Customer Support

representative.

See the following:

Recommended Prerequisite
Creating an XDR Connector
Testing Data Ingestion
Editing a Connector
What is Supported

Recommended Prerequisite
It is recommended that you use Role-Based Access Control (RBAC) to configure a new role,
such as XDR Ingestion Only. This new role is restricted to only have the XDR Connector
Ingestion capability, which is the Webhook (HTTP) POST capability.

Administrators (Super Admin or Platform Admin) can set up an ingestion-only API key to restrict
the amount of capabilities associated with that key.

 API keys are identity-based, not connector-based.

For RBAC, navigate to System | ORGANIZATION MANAGEMENT | Role-Based Access
Control. See Configuring Role-Based Access Control.

For API keys, click your account name on the menu bar and select Profile. In the User Profile
window, click the API Keys tab. See Editing Your User Profile.

Creating an XDR Connector
To create an XDR Connector:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select XDR Connector.

4. The configuration wizard opens. There are three main configuration steps: Index Type,

Namespace, and Connection & Normalization.

5. The first step for Index Type is already selected. Incoming data will be stored in the

selected index. Select an Index type from the dropdown menu based on your data, such
as AWS Events, Scans, Traffic, or Windows Events. The default is Syslog.

Indexes organize data to speed up searches. The following indexes are available:

Index

Details

Syslog (default)

Syslog and Events

AWS Events

AWS CloudTrail

IDPS/Malware

IDS, Suricata, firewall threats from sensors or log forwarders, Maltrace SDS/Sandbox

Sandbox Events

Linux Events

Audit data from Linux agents, Google Workspace, and others

Scans

Traffic

Vulnerability scanner results

Network Traffic, flow traffic from sensors, CloudTrail traffic, firewall traffic logs from sensor log

forwarders, DHCP server logs from sensors

Index

Details

Windows Events

User data from Active Directory, Microsoft Entra ID (formerly Azure Active Directory), and Office

365, and Windows logs from Windows agents, Windows System Security logs, and Windows

events from third party SIEMs

6. Click Next. The Namespace step is now selected.

7. Enter a name for the vendor namespace. Namespace holds ingested data from

common sources, in JSON format, for a source vendor. Namespace is a structured way
to categorize and organize ingested data based on the originating vendor and product.
It has a standardized naming convention, prefixed with ns_.

If there is an existing namespace, it will appear in the dropdown menu as you type.

 A namespace is not unique. It can be shared with multiple connectors. The best
practice is to keep data sources, such as from one vendor, in one namespace.
Examples are Microsoft and Palo Alto.

8. Click Next. The configuration wizard opens to the Configure Connection & Data

Normalization page. This page has steps, which are listed on the left-hand side. Use
them to configure the webhook connector settings.

9. In Generate Connector Link, click Generate and copy connector Link. The system
will generate a unique webhook path/link. This is the endpoint where you will post data
from third party systems to go into Stellar Cyber.

A successful message is displayed. Also, the Method and Path populates.

 Authentication uses your existing API token, which is stored in the API Keys tab of

your User Profile. See Managing Users.

10. In General, name your connector. Provide a clear and descriptive name to easily
identify the connector by name. Use up to 50 alphanumeric characters, (letters,
underscores, dashes, and numbers). The Connector Name must be unique (across all
connectors, not just XDR connectors).

11. In the Tenant Name, select the tenant to ingest data into. If you manage multiple

tenants, select one tenant for this connector.

12. In Normalization Setup, click Upload to upload sample data from your source in a

single JSON file.

The sample data sets up normalization. It helps with format validation and previewing
data ingestion. In addition to uploading, you can also paste sample data into the window
and edit the data.

 Use the Preview button in Normalized Data Preview to check the JSON syntax

and validate the sample data.

13. In Normalization Parameters, provide the vendor and source information and the

optional timestamp normalization.

a. Specify the Vendor name and data Source to enrich metadata and improve

event categorization. Use up to 50 alphanumeric characters. The vendor is the
name of the vendor associated with the data source, such as event or log data.
Examples of vendors are: Microsoft_Sentinel, PaloAlto_Prism, and Office365.

b. (Optional) Specify the Timestamp Path. Use this field to configure how

timestamps are extracted and parsed from the incoming data. The timestamp
path is a dot-notation path to the timestamp field in your JSON data, for
example, event_created_at.



If you specify an optional timestamp, the event timestamp is extracted and

set using the Timestamp Path and Timestamp Format fields.

If you do not specify an optional timestamp, the time event of ingestion is

used as the event's timestamp.

c. (Optional) Select the Timestamp Format used in your data from the drop-

down. The options are:

UNIX_EPOCH—Unix epoch seconds (10 digits), converted to
milliseconds

UNIX_MILLIS—Unix epoch milliseconds (13 digits), already in correct
format

ISO8601_EXTENDED—ISO 8601 extended format: %Y-%m-
%dT%H:%M:%S%z

ISO8601_BASIC—ISO 8601 basic format: %Y%m%dT%H%M%S%z

RFC3339—RFC 3339 format: %Y-%m-%dT%H:%M:%S%.%L%z

RFC2822—RFC 2822 format: %a, %d %b %Y %H:%M:%S %z

POSTGRESQL—PostgreSQL format: %Y-%m-%d %H:%M:%S.%N

MYSQL—MySQL format: %Y-%m-%d %H:%M:%S

WINDOWS_FILETIME—Windows FILETIME: 100-nanosecond
intervals since 1601-01-01

SYSLOG—Syslog format (no year): %b %d %H:%M:%S

SYSLOG_YEAR—Syslog format with year: %Y %b %d %H:%M:%S

APACHE_COMMON—Apache common log
format: %d/%b/%Y:%H:%M:%S %z

14. In Normalized Data Preview, you can review the data sample. You can visualize the
results and verify the normalized data before submitting. Click the Preview button to
validate the data sample. If successful, there is a Preview Success message.

However, the following example shows an error message. See Validation Error
Messages for all possible error messages and warnings. You will need to correct any
errors before the Submit button is enabled.

15. Click Submit. In the Connector Overview, a successful message is displayed. You can
use the XDR Connector you just configured to test data ingestion. See Testing Data
Ingestion.

Validation Error Messages

The following error messages are possible during validation of the data sample.

Category of Error Message

Name of Error Message

Error Message Details

Field Count Limit Errors

Field limit exceeded

"Field limit exceeded:

{total_fields} fields

(current: {current_count},

new: {len(new_fields)},

limit:

{self.max_fields_limit}). New

fields: {',

'.join(new_fields[:5])}{'...'

if len(new_fields) > 5 else

''}"

Batch field limit exceeded

"Batch would exceed field

limit: {current_count}

existing + {len(new_fields)}

Category of Error Message

Name of Error Message

Error Message Details

new = {current_count +

len(new_fields)} (limit:

{self.max_fields_limit})"

Field Type Conflict Errors

Type conflict within batch

"Type conflict within batch

for field '{field_name}':

{all_fields[field_name]} vs

{field_type}"

Individual field type conflict

"Type conflict for field

'{field_name}': expected

{existing_type}, got

{new_type}"

Incompatible field types

"Incompatible type for field

'{field_name}': expected

{existing_type}, got

{new_type}"

Field Name Validation Errors

Invalid characters in field name

"Invalid characters in field

Field name too long

name '{field_name}'. Only

alphanumeric, underscore,

dot, @ and hyphen are

allowed."

"Field name too long:

'{field_name[:50]}...'

({len(field_name)} chars, max

255)"

Field name dot placement:

"Field name cannot start or

end with dot: '{field_name}'"

The following warnings are possible during validation of the data sample.

Category of Warning

Name of Warning

Warning Details

Type Coercion Warnings

Type coercion warning

"Type coercion for field

'{field_name}': {new_type} ->

{existing_type}"

Field Value Warnings

String value too large

"String value at '{path}'

exceeds keyword limit

({len(value.encode('utf-8'))}

bytes > 32766)"

Category of Warning

Name of Warning

Warning Details

Large array warning

"Large array at '{path}':

{len(value)} elements"

Testing Data Ingestion
To test data ingestion, post data to the saved webhook URL. For example, you can use
Postman, or any other tool that generates HTTP requests, to forward the data to the endpoint.

XDR Webhook Hostname

For the XDR webhook hostname, in general you use the standard domain for your instance in
front of the webhook path. For example, if your domain is stellarcyber.ai, an example of the entire
URL is:

https://stellarcyber.ai/webhook/xxxxxxxxxxxx

But if you use a Data Analyzer (DA), provide the DA name and port 8889. You can use any DA.
For example, if you have a receiver called da1.example.com, the full URL with the hostname
and path will include the receiver URL and port, for example:

https://da1.example.com:8889/webhook/xxxxxxxxxxxx

Example of Testing Data Ingestion

To test data ingestion (this example uses Postman):

1. Paste the webhook URL into the POST and set the Body to JSON with the request you

are sending. This is how a third party system pushes events to Stellar Cyber.

2. For Authentication, go to Headers and Authorization. The header format is Bearer

token. Paste your existing API token.

3. Click Send.

4. In the Connector Overview, locate your configured connector. The Type will be

XDR Connect.

5. Once data is received, click View Events to see the new events.

6. Drill down in the Event Details by selecting More Info. It is located in the Actions

column of the connector table.

7. Click the JSON tab. You can verify the parsed fields, and ensure that data normalization

is working correctly.

8. Click the Details tab to see the normalized fields.

Editing a Connector
To edit an existing connector:

1. In the Connector Overview, locate your configured connector. The Type will be

XDR Connect.

2. Click the edit icon (

) on the row for your configured connector. It is located in the

Actions column of the connector table.

3. You can edit the fields in the Configure Connection & Data Normalization page.

What is Supported
This section details what is supported by XDR Connect in this release.

Protocols

HTTPS

HTTP Methods

POST

API Requests

A single API request is supported.

Authentication Method

A header-based authentication method is supported. A users' API token is used as a
Bearer token for the ingestion.

Privileges

An API token with ingestion privilege.

API Token Expiration

90 days (recommendation)

Content Types

A single content type for each webhook is supported.

Deployed On

Data Processor (DP)

Tenants

A single tenant is supported.

RBAC

To create the configuration, the Root user (Super Admin) is supported.

Normalization

Level 1 (L1) normalization is supported (which means there will not be any alerts or
detections).

Data Formats

Only well-formed JSON data is supported.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

