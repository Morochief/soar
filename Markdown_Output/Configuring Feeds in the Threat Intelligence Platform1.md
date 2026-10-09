Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Feeds in the Threat Intelligence
Platform

 You must have Root scope to use this feature.

Use the Feeds tab on the Threat Intelligence Platform page to configure and manage threat
intelligence feeds.

To manage IoCs, see Managing IoCs in the Threat Intelligence Platform.

Using the Feeds Tab
The Feeds tab displays the threat intelligence feeds.

The Feeds table has the following columns:

Icon—icon of the feed

Name—name of the feed, such as PhishTank or etpro domain

Type—type of feed:

Built-in feeds are provided by Stellar Cyber

Custom feeds (TAXII and TSV) are added using the Create button and then
providing a collection URL and authentication credentials (see Adding Custom
Feeds)

Premium feeds (Cybersixgill, Anomali ThreatStream, RedSense, Recorded
Future, SOCRadar, CrowdStrike, and ESET) are provided by Stellar Cyber
using credentials that you purchase (see Enabling Premium Feeds)

Status—status of feed:

Success (green)—the feed successfully ran, when it periodically last ran

Error (red)—the feed failed when it last ran or the feed is in Stopped status

Disabled (white)—the feed is Disabled

Status Message—status messages, such as:

Disabled—the feed is disabled

Success—the feed successfully produced IoCs in the latest running cycle (for
Custom and Premium feeds only)

Initializing—the feed is initializing; this status is only displayed on the first run
of the feed

Stopped—the feed has stopped working

Running—the feed is running (for Built-in feeds only)

Failed to connect to feed source—the feed failed to establish a connection to
the data source (for Custom and Premium feeds only) (see Feed Error
Messages for other status messages)

Enabled—toggle of the feed, either Enabled or Disabled

All Built-in, Custom, and Premium feeds can be Enabled and Disabled; when
Enabled, IoCs are fetched and then stored locally; when Disabled, IoC
ingestion stops

Polling Frequency—frequency with which the data is updated from the feed, in hours

The Polling Frequency can be set for Custom and Premium feeds; for Built-in
feeds, the Polling Frequency is 24 hours

Retention Period—retention period of the feed, in days, after which feed data is
deleted

Backfill Days—number of backfill days. Backfilled data is information in the threat
database from the past few days, with an upper limit of 30 days.

Whenever a feed is re-enabled, TIP fetches all IOCs that it has not fetched
since the last time it was disabled, limited to a backfill buffer size

Description—description of feed

Descriptions of Custom feeds can be edited; Descriptions of Built-in and
Premium feeds are provided by Stellar Cyber and cannot be edited

Last Ingestion—timestamp of the last ingestion update from the feed

Actions—actions available on a feed, such as Delete this row, Edit this row, or Reset
Premium Feed:

Custom and Premium feeds can be edited; Built-in feeds cannot be edited

Custom feeds can be deleted; Built-in and Premium feeds cannot be deleted

Only Premium feeds can be reset

Using Search

Use the Search box to search for information about a feed.

Exporting CSV

Click Export CSV to export the table as a spreadsheet file. You can export Selected Columns
or All Columns.

The spreadsheet is downloaded to your Downloads folder.

Selecting View

Click Select View to preserve a table layout. See Saved View Configurations for details.

Using Filters

Click Filters to use defined filters.

To use defined filters:

For Name, select the name of a feed using the check boxes or Select All. The number
of feeds of each name is displayed on the right.

To see more Name fields, click View More.

For Type, select a type of feed using the check boxes or Select All. The number of
feeds of each type is displayed on the right.

For Status Message, select a status using the check boxes. The number of feeds with
each status is displayed on the right.

For Enabled, select a state, either Enabled or Disabled, using the check boxes or
Select All. The number of feeds with each state is displayed on the right.

For Polling Frequency, select a frequency using the check boxes or Select All. The
number of feeds with each frequency is displayed on the right.

For Retention Period, select a retention period using the check boxes or Select All.
The number of feeds with each retention period is displayed on the right.

For Backfill Days, select a number of days using the check boxes or Select All. The
number of feeds with each number of backfill days is displayed on the right.

For Description, select the description of a feed using the check boxes or Select All.
The number of feeds with each description is displayed on the right.

To see more Description fields, click View More.

For Last Ingestion, enter From and To dates and times using the calendars.

Select a date, select a time, then click the checkmark.

If a defined filter is unselected, you can click the search box under Add new filter to
select a filter from the dropdown.

To exit, click Filters again. The configured filters are displayed at the top of the table.

To clear an individual filter, click the icon to the right of the filter (

).

To clear all filters, click Clear All.

Using Columns

Click Columns to add or remove columns using check boxes.

Click Columns again to exit.

Disabling Feeds

To disable a feed, click the toggle in the Enabled column from Enabled to Disabled. The
following confirmation is displayed.

Click Yes, disable this feed.

Adding Custom Feeds

Custom feeds include TAXII and TSV. You configure custom feeds with credentials that you
provide, for example, credentials for a TAXII server or credentials to access a TSV file. The TAXII
version is 2.1.

You add Custom feeds by providing a Collection URL and entering basic HTTP authentication
credentials such as Username and Password.

You can add up to 30 Custom feeds per organization.

 Feeds may not work as expected if files are hosted on places where basic HTTP

authentication is not allowed by default (for example, Amazon S3). Caution is advised.

The following details are for the TSV feed:

The TSV source file should have a size less than 100 MB.

Stellar Cyber ingests up to 25,000 IoCs per day.

To poll data from the source, the HTTP request should complete within 30 seconds.

When you add a TSV feed, an emerging_threat tag is added to all the IoCs brought in by that
feed. Tags are displayed in the Tags column of the IoCs table.

For the rules and format of the TSV file, see TSV File Data Schema.

To add a custom feed:

1. Click Create and select Custom Feed.

2. The default Category is displayed, which is TAXII. Or select TSV.

3. Enter a Name. This is the name of the feed, which will be prepended with the

Category, either TAXII or TSV.

4. Enter a Collection URL.

a. For TAXII, enter a Collection URL. For details on how to obtain the
TAXII collection URL, see Obtaining the TAXII Collection URL.

b. For TSV, enter a URL to a TSV file.

5. Enter a Username and Password.

6. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed.

7. Select the number of Backfill Days, in days.

 The Backfill Days field is only available for TAXII feeds.

8. Select the Retention Period, in days, after which feed data is deleted. For details, see

Retention Policy.

9. Enter a Description.

10. Click Submit.

When the Custom feed is configured and enabled, the IoCs are fetched from the remote
feed and stored locally.

TSV File Data Schema

The rules for the TSV file are:

Delimiter: Must be a tab

Fields, Field order, and Syntax:

Each row in the TSV file must have fields in the order and syntax shown below. Rows
that do not meet this format are ignored.

The data schema of the TSV file is as follows:

F

I

E

L

D

P

u

r

p

o

s

e

S

y

n

ta

x

TYPE

VALUE

SOURCE

SCORE

Specify the type of address

Specify the address of the

Supply a name to identify

Assign a severity score to

that will be entered in the

threat. This value may be

the threat.

the threat.

next column.

associated with multiple

sources.

url

ip

domain

md5-hash

sha1-hash

sha256-hash

A url

A-Z a-z 0-9 _ -

Integer from 0-100

An IPv4 address

Alphanumeric, underscore,

Use 90 if you prefer not to

A fully qualified domain

name

dash. No spaces, no other

tune

symbols.

md5 hash value

sha1 hash value

sha256 hash value

C

yes

no

no

no

a

s

e

S

e

n

si

ti

v

e

?

Obtaining the TAXII Collection URL

Refer to the following definitions before using the procedure in this section to obtain the
TAXII collection URL.

TAXII Server: A server that implements the TAXII standards to share cyber threat
intelligence (CTI) over HTTPS. It hosts API endpoints for clients to access and
exchange CTI data.

Discovery URL: A specific endpoint on a TAXII server that provides information about
the server’s capabilities, available API roots, and other metadata. It is the starting point
for clients to interact with the server.

API Root: A base URL that groups related TAXII resources (for example, collections)
under a single namespace. Each API root represents a distinct set of data or services
provided by the TAXII server.

Collection ID: A unique identifier for a specific collection of data hosted on a TAXII
server. Collections are logical groupings of threat intelligence objects (for example,
STIX data).

Collection URL: The endpoint URL for accessing a specific collection of data on a TAXII
server. It is used to query objects from the collection.

The following example is for an AlienVault URL. The same format is used for other third-party
providers that host TAXII servers.

 The TAXII Collection URL does not support an alias for the TAXII collection name. Refer to

the following procedure and use <collection ID>.

To set up a TAXII feed, obtain the TAXII collection URL as follows:

1. Do a cURL command from the AlienVault discovery URL:

curl -k -X GET https://otx.alienvault.com/taxii/ -H "Accept:
application/taxii+json; version=2.1" --user username:password

This will produce something like the following:

{"title": "Open Threat Exchange TAXII Server", "description":
"Open Threat Exchange TAXII Server", "contact": "otx-
support@alienvault.com", "default":
"https://otx.alienvault.com/taxii/root", "api_roots":
["https://otx.alienvault.com/taxii/root"]}%

 The API root is https://otx.alienvault.com/taxii/root.

2. Add /collections to the API root, then do another cURL commands as follows:

curl -k -X GET https://otx.alienvault.com/taxii/root/collections
-H "Accept: application/taxii+json; version=2.1" --user
username:password

This will produce something like the following:

{"collections": [{"id": "<collection ID>", "alias":
"subscription", "title": "Your pulse subscription",
"description": "Your pulse subscription", "can_read": true,
"can_write": false, "media_types":
["application/stix+json;version=2.1"]}]}%

3. Add your <collection ID> to the previous URL, for example:

https://otx.alienvault.com/taxii/root/collections/<collection
ID>/

4. Use the collection URL to set up a TAXII feed in Adding Custom Feeds.

Retention Policy

When you configure a custom TAXII feed, you can select the Retention Period, in days, after
which feed data is deleted. The retention period is displayed in the Retention Period column in
the Feeds tab. If you then go to the IoCs tab and look at the Expiration Date column, you may
notice a difference.

The retention policy for custom TAXII feeds is as follows. If the data source has all the valid_from
and valid_until information, Stellar Cyber will use those dates. Otherwise, Stellar Cyber will do
some calculations based on the retention period. Therefore, the expiration dates of custom TAXII
feeds may not be based on the retention period.

Enabling Premium Feeds

Premium feeds are provided by Stellar Cyber and include Cybersixgill, Anomali ThreatStream,
RedSense, Recorded Future, SOCRadar, CrowdStrike, and ESET. You configure them with
credentials that you purchase.

Premium feeds are disabled by default. You edit the Premium feed and provide authentication
credentials such as Username and Password or API Key, then enable the feed. The configuration
of each premium feed differs.

To enable premium feeds:

Enabling Cybersixgill Premium Feed

Enabling Anomali Premium Feed

Enabling RedSense Premium Feed

Enabling Recorded Future Premium Feed

Enabling SOCRadar Premium Feed

Enabling CrowdStrike Premium Feed

Enabling ESET Premium Feed

Enabling Cybersixgill Premium Feed

To enable the Cybersixgill Premium feed:

You can subscribe to the Cybersixgill service by using TAXII 2.1 protocol.

1. Click the Edit icon (

) on the row for the Cybersixgill Premium feed. The

EDIT PREMIUM FEED dialog displays.

2. The Name cannot be changed.

3. Enter a Collection URL.

4. Enter a Username and Password.

5. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

6. Select the number of Backfill Days, in days. The minimum value is 1 day and the

maximum is 30 days.

7. The Description cannot be changed.

8. Click Submit.

9. Click Enabled on the row for the Cybersixgill Premium feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Enabling Anomali Premium Feed

You can subscribe to Anomali ThreatStream feed using your own username and API token.

To enable the Anomali Premium feed:

1. Click the Edit icon (

) on the row for the Anomali Premium feed. The

EDIT PREMIUM FEED dialog displays.

2. The Name cannot be changed.

3. Enter a Username.

4. Enter the API Key.

5. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

6. Select the number of Backfill Days, in days. The minimum value is 1 day and the

maximum is 30 days.

7. The Description cannot be changed.

8. Click Submit.

9. Click Enabled on the row for the Anomali Premium feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Enabling RedSense Premium Feed

You can subscribe to the Redsense feed using your own API key.

To enable the RedSense Premium feed:

1. Click the Edit icon (

) on the row for the RedSense Premium feed. The

EDIT PREMIUM FEED dialog displays.

2. The Name cannot be changed.

3. Enter the API Key.

4. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

5. Select the number of Backfill Days, in days. The minimum value is 1 day and the

maximum is 30 days.

6. Select the number of Retention Days, in days, after which feed data is deleted. The

minimum value is 1 day and the maximum is 360 days.

7. The Description cannot be changed.

8. Click Submit.

9. Click Enabled on the row for the RedSense Premium feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Enabling Recorded Future Premium Feed

You can subscribe to the Recorded Future feed using your own API key.

The Recorded Future data feed has a large IoC ingestion volume. Stellar Cyber ingests IoCs in a
constant manner, therefore it may take up to a week to ingest all the IoCs. The retention period is
fixed at 14 days.

To enable the Recorded Future Premium feed:

1. Click the Edit icon (

) on the row for the Recorded Future Premium feed. The

EDIT PREMIUM FEED dialog displays.

2. The Name cannot be changed.

3. Enter the API Key.

4. To ingest only the most malicious IoCs, select the checkbox for Filter to High-Value

IOCs. When selected, only top-scoring IPv4 (labels: very-malicious and malicious) and
top URLs are included, while lower value IPv4 and URL IoCs are excluded.

5. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

6. The Description cannot be changed.

7. Click Submit.

8. Click Enabled on the row for the Recorded Future Premium feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Enabling SOCRadar Premium Feed

You can subscribe to the SOCRadar feeds using the API Endpoint URL from the SOCRadar
platform.

You can configure multiple premium feeds for SOCRadar. You can have different feeds for
different use cases, such as by industry or by geo.

The following is supported:

Up to 10 SOCRadar premium feeds.

Up to 50,000 IoCs per poll.

Up to 100 MB input file size.

To enable the SOCRadar Premium feed:

1. Click Create and select Premium Feed or click the Edit icon (

) on the row for the

SOCRadar Premium feed. The EDIT PREMIUM FEED dialog displays.

2. Select a Category from the dropdown menu. The only selection in this release is

SOCRadar.

3. Enter a Name. It will have a prefix, for example, SOCRadar -.

4. Enter an API Endpoint. The SOCRadar endpoint must be in the following format:

https://platform.socradar.com/api/threat/intelligence/feed_list/<feed_collection_id>.json?
key=<api_key>&v=2

 You can copy and paste this from the SOCRadar platform.

5. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

6. Select the number of Retention Days, in days, after which feed data is deleted. The

minimum value is 1 day and the maximum is 360 days.

7. The Description cannot be changed.

8. Click Submit.

9. Click Enabled on the row for the SOCRadar Premium feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Enabling CrowdStrike Premium Feed

You can subscribe to the CrowdStrike feed using your own client ID and secret. The CrowdStrike
feed supports the CrowdStrike Falcon Intel service collection.

Up to 50,000 IoCs per poll is supported.

To enable the CrowdStrike Premium feed:

1. Click the Edit icon (

) on the row for the CrowdStrike Premium feed. The

EDIT PREMIUM FEED dialog displays.

2. The Name cannot be changed.

3. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

4. Select the number of Backfill Days, in days. The minimum value is 1 day and the

maximum is 30 days.

5. The Description cannot be changed.

6. Click Submit.

7. Click Enabled on the row for the CrowdStrike Premium feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Enabling ESET Premium Feed

You can subscribe to the ESET feed using your own username and password. The ESET feed is
provided via a TAXII server, where the term collection refers to a TAXII collection.

The retention period is fixed at 2 days.

To enable the ESET Premium feed:

1. Click the Edit icon (

) on the row for the ESET Premium feed. The

EDIT PREMIUM FEED dialog displays.

2. The Name cannot be changed.

3. Select a Polling Frequency, in hours. This is how often the data is updated from the

feed. The minimum value is 1 hour and the maximum is 24 hours.

4. The Description cannot be changed.

5. This premium feed has a two-step verification:

a. Enter a Username and Password, which are verified.

b. Click Next. The list of collections is fetched from the feed discovery.

c. Select Collections from the drop-down. You can select multiple collections or

Select All. The maximum number of collections is 10.

 If you select too many feeds from the drop-down, it may surpass the
maximum threshold of IoCs, so some IoC might not be ingested.

6. Click Submit.

7. Click Enabled on the row for the ESET Premium feed, from the selected collections of

the remote feed.

When the Premium feed is configured and enabled, the IoCs are fetched from the
remote feed and stored locally.

Resetting Premium Feeds

To reset a Premium feed:

1. Click the three dots (

) to the right of the Trash icon under Actions on a Premium

type of feed.

2. Select Reset Premium Feed. The following confirmation is displayed.

3. Click Yes, reset this feed.

Editing Feeds

You can edit Custom and Premium feeds.

Click the Edit icon (

) on a row in the table. A sample EDIT CUSTOM FEED is as follows:

For Custom feeds, the Category cannot be changed. The other fields can be edited.

Click the Edit icon (

) on a row in the table. A sample EDIT PREMIUM FEED is as follows:

For Premium feeds, the Name and Description cannot be changed. The other fields can be
edited.

About Feeds
The following sections provide more information about feeds.

Feed Descriptions

The following feeds are available, with their category and description.

Feed Name

Category

Description

AlienVault OTX

Built-in

The AlienVault OTX feed provides IoCs, including malicious IP addresses, domains,

URLs, and hashes that can be used to detect and investigate cyber threats.

Feed Name

Category

Description

DHS

Built-in

The Department of Homeland Security (DHS) feed provides IP addresses, domains,

URLs, and hashes. These IoCs help describe and identify potential cyber threats and

incidents.

Emerging Threat

Built-in

The Proofpoint Emerging Threat feed provides up-to-the minute IP address and domain

Pro IP, Domain

reputation. It is the industry’s most timely and accurate source of threat intelligence.

Emerging Threat

Built-in

The Proofpoint Emerging Threat feed provides a ruleset for detecting advanced threats

Pro Rules

using existing network security appliances, such as network Intrusion

Detection/Prevention systems (IDS/IPS).

PhishTank

Built-in

The Phishtank feed provides a database of known phishing URLs. It is a collaborative

clearing house for data and information about phishing attacks and fraudulent websites.

Abuse.ch (urlhaus

Built-in

The Abuse.ch feed shares malicious URLs and hashes that are being used for malware

and SSL certs)

distribution, and contains information about SSL certificates that have been associated

with malicious activities.

OpenPhish

Built-in

The OpenPhish feed focuses on phishing threats. It identifies zero-day phishing URLs

and provides comprehensive, actionable, real-time threat intelligence.

Emerging Threat

Built-in

The Emerging Threat feed provides IP addresses, domains, URLs, and file hashes.

Emerging Threat is a type of threat or risk that is newly identified, rapidly evolving, or

gaining prominence.

Cybersixgill

Premium

You can subscribe to the Cybersixgill service by using TAXII 2.1 protocol. Cybersixgill

covertly searches from clear, deep, and dark web sources, and offers Threat Intelligence

data and their exposure to risk.

Anomali

Premium

You can subscribe to the Anomali ThreatStream feed using your own username and API

token. Anomali ThreatStream helps to aggregate, correlate, and analyze threat

intelligence data from various sources to enhance cybersecurity posture.

RedSense

Premium

You can subscribe to the RedSense feed using your own API key. RedSense offers a

comprehensive and informed view of potential threats by integrating the various facets of

cyber threat intelligence.

Recorded Future

Premium

You can subscribe to the Recorded Future feed using your own API key. It allows

seamless interaction with various Recorded Future API endpoints (IP/Domain/URL/Hash

Risklists & Enrichment).

SOCRadar

Premium

You can subscribe to the SOCRadar feeds using the API Endpoint URL from the

SOCRadar platform. SOCRadar offers an extensive range of IoC feeds, with more than

130 feeds in total.

Feed Name

Category

Description

CrowdStrike (Crow

Premium

You can subscribe to the CrowdStrike feed using your own client ID and secret.

dStrike

Falcon Intel

service collection)

CrowdStrike enhances endpoint protection by combining malware sandboxing, malware

search and threat intelligence into an integrated solution that can perform

comprehensive threat analysis.

ESET

Premium

You can subscribe to the ESET feed using your own username and password.

ESET Threat Intelligence provides evidence-base information and actionable advice

about an existing or emerging threat.

Feed Error Messages

The following error messages are displayed in the Status Message column for Premium and
Custom feeds only.

Feed State

Detailed Error Message

Invalid Credentials

Please validate the credentials and then reconfigure the feed.

Invalid URL

Please validate the URL and credentials, and then reconfigure the feed.

Invalid collection URL

Please validate the URL and credentials, and then reconfigure the feed.

Connection Error

Fetching Data Error

Failed to connect to feed source. Please validate the feed input.

Please validate if the credentials are still valid or if the data source is still available.

Surpassed Query Limit

Reached the API rate limit. Please reduce the backfill day length.

 Some premium feeds also display a detailed error message in the Status Message column,

for example, if specific API URLs or collections are not working.

Setting Up Proxy for On-Premise Environments

The Threat Intelligence Platform supports HTTP/HTTPS proxy setup in on-premise
environments. This lets you successfully enable and use threat intelligence feeds in on-premise
environments with restricted Internet access.

Contact the Stellar Cyber Customer Support team if you need web proxy configured.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

