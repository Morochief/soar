✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Understanding Asset-Based Licensing
As described in Licensing Overview, the DP can be licensed based on a count of the number of
daily active assets. This topic provides details on asset-based licensing, including how assets
are discovered, managed, and counted for licensing purposes. Refer to the following topics for
details:
Overview of Entity-Based Licensing
Asset Discovery in the Entity-Based Model
About Asset Count Timing
Asset Counting Example
Frequently Asked Questions on Entity-Based Asset Counting
Volume Policy for Asset-Based Licenses
Asset Counting and License Violations
See also:
Frequently Asked Questions on Entity-Based Asset Counting
Understanding License Compliance provides details on how Stellar Cyber enforces
license policies
The Reporting | Reports | License Usage page lets you schedule and export PDF/CSV
reports for Asset and Ingestion licenses
Overview of Entity-Based Licensing
For licensing purposes, entities are defined as the combination of unique devices and users
discovered across the environment on any given day. Entities counted for licensing purposes are
also referred to as assets.
 Keep in mind that this definition of an asset for licensing purposes is different from the
security assets found under Asset Analytics.
Asset discovery is performed differently for licensing than it is for security workflows:

Asset Discovery for Licensing – Designed for simplicity, leveraging only high-
confidence sources for attributing entities against the subscribed license count..
Asset Discovery for Security Workflows – Resolved through a more complex
process to catch corner cases useful for analysts.
 Refer to MAC or IP-Identified Assets for details on how assets are discovered for
security workflows.
Asset Discovery in the Entity-Based Model
The design goal for asset-based licensing in the entity-based model is to count assets with the
simplest method possible. The design relies on simplicity because it is easy to understand,
predict, trust, and scope. Although certain corner cases won’t be counted perfectly due to this
simplicity, this is by design.
The total number of licensed assets per tenant per day is the total number of unique devices
(measured by internal Source IP addresses) plus the total number of unique users (measured by
email addresses). From a high level, these are counted as follows:
Devices – any private IP address observed in the sample window (either from a trusted
data source or inferred from observed traffic; see below for details).
 Public IP addresses designated as private in the System | DATA MANAGEMENT |
Enrichments page are counted as assets for licensing purposes.
Users – any logical account with a valid email address as an identifier observed in the
sample window, including accounts assigned to non-human actors such as service
accounts.
Device Discovery in the Entity-Based Model
Devices can be identified either from trusted data sources or inferred from certain types of
network data. The total device entity count is the sum of all unique IP addresses from both sets
of data, as described below.
Trusted Endpoint Data Sources
Some data sources, such as EDR solutions, provide an inventory of their assets. In this model,
the discovered hosts’ private IP addresses are reported as assets. Data from a managed list of
sources that are known to produce less accurate results is excluded from consideration. For
example:
IF (msgtype == "Asset Record" AND msg_origin.source IN trusted_data_source)
AND NOT (msg_origin.category == "firewall" OR msg_origin.category ==
"traffic"):
return(asset)
Inferred Devices (From Sensors, Firewalls, VPNs, and Traffic)
For data originating from sensors, firewalls, and other network devices, asset IP addresses are
inferred from network flow data, subject to the following rules:

The IP address must belong to one of the following groups:
Private address spaces defined in RFC-1918
CGNAT address space defined in RFC-6598
Customer-defined IP ranges
The IP address must be observed to send traffic twice within a sample period.
User Discovery in the Entity-Based Model
Users are identified either from trusted user data sources or inferred from observed activities
from specific productivity platforms. The total count is the sum of all unique email addresses from
these sources.
For data originating from Microsoft 365 or Google Workspaces, user entities are extracted from
activity logs in connected Microsoft 365 and Google Workspaces environments.
Microsoft 365
For user entities discovered using email addresses from Microsoft 365, either the UserId or
MailboxOwnerUPN field must be a valid email address.
Google Workspaces
For user entities discovered using email addresses from Google Workspaces, the following must
all be true:
The email field is a valid email address
The profileId field has a value
The owner and calendar_id fields are not populated (this omits certain accounts
created by third party applications that have integrated with Google Directory or Google
SSO).
User Discovery Pseudocode
Stellar Cyber uses filtering logic to ensure that identified users represent real user accounts
(is_valid_user_account) and not an alias or something of no security value. The simplified
logic for user discovery is as follows:
IF (msg_origin.category == "identity" OR msg_origin.category ==
"office_suite" OR msg_origin.category == “directory”):
IF (record.is_valid_user_account()):
return(record.email)
Each data source has a different implementation of is_valid_user_account(). Stellar Cyber
studies each data source and employs conservative discovery methods. For example, the
implementation for Google Workspace is as follows:
// Exclude non user records like 3rd party calendar apps
IF (gsuite.actor.profileId.exists()
AND gsuite.email.is_valid_email()
AND NOT event_detail.owner.exists()
AND NOT event_details.calendar_id.exists()):
return(True)

About Asset Count Timing
The Asset Discovery process happens in real time as new data comes into the system. Each day
at 11:59 PM UTC, Stellar Cyber counts the total of all the unique assets (devices and users) per
tenant for that given day. Importantly, if an IP address is discovered across multiple sources on a
given day, it is only counted once for that day. The results are reported in the System |
ORGANIZATION MANAGEMENT | Licensing | Asset Usage page.
Asset Counting Example
The following example shows how this works for a sample customer with two tenants:
Tenant A has a Crowdstrike connector and a Modular Sensor deployed
Tenant B has an Office 365 connector and three Windows Server Sensors deployed
Tenant A Asset Data
Tenant A has the following asset data from it sources on Day 1:
CrowdStrike Connector
Assets – 192.168.0.1, 192.168.0.2
Modular Sensor
Discovered one traffic event sourced from 192.168.0.3 and ten traffic events
sourced from 192.168.0.1
Tenant B Asset Data
Tenant B has the following asset data from its sources on Day 1:
Office 365 Connector
Valid Users - bob@tenantb.com, alice@tenantb.com
Windows Server Sensors
Deployed on three devices – 192.168.0.1, 192.168.0.2, 192.168.0.3
Total Day 1 Discovered Assets
The total number of discovered assets across all tenants on Day 1 is 8, as summarized in the
table below:
| Day | Tenant | Asset | Type Sources |
| --- | ------ | ----- | ------------ |
Day 1 Tenant A 192.168.0.1 Device CrowdStrike, Modular Sensor
| Day 1 | Tenant A | 192.168.0.2       | Device CrowdStrike    |
| ----- | -------- | ----------------- | --------------------- |
| Day 1 | Tenant A | 192.168.0.3       | Device Modular Sensor |
| Day 1 | Tenant B | bob@tenantb.com   | User Office 365       |
| Day 1 | Tenant B | alice@tenantb.com | User Office 365       |
| Day 1 | Tenant B | 192.168.0.1       | Device Windows Sensor |
| Day 1 | Tenant B | 192.168.0.2       | Device Windows Sensor |
| Day 1 | Tenant B | 192.168.0.3       | Device Windows Sensor |

Day Tenant Asset Type Sources
TOTAL ASSETS Tenant A & Tenant B 8 n/a n/a
Tenant Allocation for Assets
When the Platform license is based on assets, the Tenant Allocation tab shows how the
licensed asset count is distributed across tenants. In the table in the Tenant Allocation tab, use
the Allocation Quota column to assign asset quotas and then monitor the Usage and Usage
Level columns to ensure no tenant exceeds its allocation.
Checking Entity Counts in the API
You can use the Entity Usage endpoint in the Stellar Cyber API to check entity-based asset
counts. The Entity Usage endpoint is available here:
/connect/api/v1/entity_usages/entity_list/tenant?date=<YYYY-MM-DD>&cust_id=
<tenant id>
For example, the following endpoint retrieves the entity usage for the tenant with the ID of
088428cf6adf4920b8dfde8636124c6b on October 22, 2024:
/connect/api/v1/entity_usages/entity_list/tenant?date=2024-10-
22&cust_id=088428cf6adf4920b8dfde8636124c6b
You can also work with the Entity Usage endpoint in the reference material from the API's
swagger.json file, as illustrated below:
Frequently Asked Questions on Entity-Based Asset
Counting
The following section provides answers to frequently asked questions on Entity-Based Asset
Counting.
 You can also click here to open a downloadable PDF  summarizing entity-based licensing
and these frequently asked questions.
How are devices with multiple IP addresses handled?
If you have a device with multiple IP addresses, each unique IP address is considered to be a
unique entity for asset counting purposes. Each unique IP address often has a unique set of
applications listening on the address, even when it is assigned to a host with other IP addresses.
Each unique IP address has a unique fingerprint and security profile and is treated as a unique
entity. The logical association at the host level is only used contextually.

Many devices on my network use DHCP. Is each device counted multiple times for each IP
lease it receives?
Yes, each observed IP that meets the criteria listed above is counted as a unique entity. Stellar
Cyber recommends the following approaches to limit this:
Eliminate double-counting by using IP reservations with DHCP where possible.
Set DHCP lease periods to at least 24 hours to limit this to only counting devices twice
My network consists of many mobile devices. When a device switches wireless access
points, it may receive a new IP address. Are these counted as unique entities?
Yes, each observed IP address that meets the criteria listed above is counted as a unique entity.
Stellar Cyber recommends configuring 802.1x session persistence to reduce the number of
duplicate entities. This can also be configured to eliminate double-counting when a device
changes connectivity mediums (for example, a devices switches from a wired to a wireless
connection).
I have multiple sites with overlapping IP spaces. Are each site’s IPs counted
independently?
No. If two separate sites with overlapping IP spaces are sent to the same Data Processor (DP),
two devices with the same IP address are counted as a single entity. Because this can cause
confusion in correlation models, Stellar Cyber recommends using globally unique IP spaces
where possible. In cases where this is unavoidable, we recommend creating separate tenants for
the sites with duplicate IP address spaces to ensure the address spaces do not collide in
correlation models.
I use auto-scaling groups. Is each ephemeral instance’s IP counted uniquely?
Yes. Each unique observed IP is counted as a unique entity. Stellar Cyber recommends
configuring the auto-scaling group to use sequential IP addressing in specific ranges to ensure
double-counting does not occur. If you are using DHCP, choose a scheme that reissues the
lowest available address in the pool.
I use eBPF to monitor network traffic from Kubernetes. Are the IP addresses of my
containers counted as entities?
Yes. Each container’s IP address (including shared addresses on virtual interfaces) is considered
a unique entity. Stellar Cyber recommends using predictable addressing in Kubernetes to avoid
double-counting.
I have multiple domains registered in Microsoft 365 and users have email aliases in each
domain. Are these counted multiple times?
Yes, if activities are observed for the same user but with duplicate email addresses, the number
of unique email addresses is used to determine the entity count. Stellar Cyber recommends
encouraging your users to use only the primary domain for authentication – all subsequent
actions will be associated with a single identifier.
Are service accounts counted as entities?
If the service account has a valid email address, it is counted as a user entity. In most cases,
monitoring these non-human user accounts is important (for example the AWS root account).

The presence of a valid email address is the simplest determining factor and this is used by the
asset counting model.
Volume Policy for Asset-Based Licenses
Asset-based licenses include an aggregated data volume of 60 MB per licensed asset, per day.
This volume is averaged across all licensed assets on the account. Should the average data
ingestion exceed this limit, Stellar Cyber will partner with you in good faith to help identify and
tune unnecessary data sources to reduce volume. If the average data volume consistently
exceeds the included 60 MB/day per asset after a collaborative tuning period of 30 days, you will
be required to purchase additional Asset licenses to bring your account into compliance. The
number of additional assets required will be calculated to align your total data volume with the
included data rate; that is, one additional asset license will be charged for every 60 MB over the
total data volume, rounded up to a minimum of 300 assets.
Five percent of your cumulative hot storage volume is available for import into cold storage. For
Asset Licenses, your cumulative volume is calculated using a conversion of 60 MB per asset per
day.
Asset Counting and License Violations
Every day, Stellar Cyber takes a snapshot of the assets that were active during the previous day
and reports the results in the System | ORGANIZATION MANAGEMENT | Licensing | Asset
Usage page.
Keep in mind that the total number of assets reported in the System | ORGANIZATION
MANAGEMENT | Licensing | Asset Usage page is typically less than the sum of the assets
shown in the MAC Identified Assets and IP Identified Assets pages. This is because the
Asset Usage page reports only those assets that were active the previous day, while the
MAC Identified Assets and IP Identified Assets pages report both active assets and ones that
were seen previously but were not active during the previous day. Only those assets that were
active the previous day count against your licensed total.
Asset license violations are reported as follows:
Stellar Cyber reports a warning if the count of active assets during a three day period
exceeds the license limit by 10% or more.
Stellar Cyber reports a violation if the count of active assets exceeds the license limit
by 10% or more for seven days in a row.
Stellar Cyber reports an out of compliance violation if the count of active assets
exceeds the license limit by 10% or more for more than 21 days.
 Refer to Understanding License Compliance for details on the different license states, as
well as compliance guidance.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  