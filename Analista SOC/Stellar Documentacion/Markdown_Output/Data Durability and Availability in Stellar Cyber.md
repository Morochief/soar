✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Data Durability and Availability in Stellar Cyber
Your data is important to you, and it's also important to us. This topic helps you understand how
Stellar Cyber stores your data in the managed version of the product, describing how your
licenses determine data availability and restoration speed, as well as how to request a data
restore. See the following topics for details:
License Types and Data Availability
About Cold Storage
Data Backup and Restore
External Storage Destinations in On-Premises vs. Managed Deployments
Using Data Sinks
License Types and Data Availability
The managed version of Stellar Cyber uses a platform license based on either ingestion volume
or monitored assets:
Volume – The license allows you to ingest a specified amount of data per day.
Assets – The license allows you a specified number of daily active assets.
The platform license also determines the following:
How long raw data is kept in hot storage.
How long alerts and cases are kept in hot storage.
Convenient Starter Pack Licenses
Stellar Cyber provides convenient Starter Packs that provide a solid foundation on which to grow
your deployment:
The volume-based starter pack provides 30 days of hot storage for raw data, one year
of hot storage for alerts and cases, and 100 GB of daily ingestion.
The asset-based starter pack provides 30 days of hot storage for raw data, one year of
hot storage for alerts and cases, and support for 3,000 monitored assets on a daily
basis.

Extending the Starter Pack
Because the managed version of Stellar Cyber is cloud-based and provided as a service from
Stellar Cyber, it's easy to add additional capacity as you grow:
Add support for additional daily ingestion or assets.
Add support for additional hot data in 30-day units.
Contact your Stellar Cyber account representative for help adding these features to your
account.
About Cold Storage
Cold storage is not included in the Starter Pack but is available as an additional purchase with a
default duration of one year. You can enhance your cold storage with the following features:
Add support for additional cold storage in 1-year units.
Increase the speed of data restore from cold storage.
 By default, data can be restored from cold to hot storage at the same speed at
which it was ingested. So, if your account has support for 100 GB of daily ingestion,
that means that Stellar Cyber can restore data from cold storage to hot at the rate
of 100 GB per day. If that's not fast enough for your needs, contact your account
representative to purchase accelerated restoration.
Choosing a Location for Cold Storage Export
By default, the managed version of Stellar Cyber stores cold data in OCI Object Storage
managed by Stellar Cyber. If you prefer to store cold data in an external destination, submit a
support request to Stellar Cyber Customer Success. You do not need to purchase the Cold
Storage SKU, but Stellar Cyber charges a fee for managing the export. Contact your account
representative for pricing details.
Data Backup and Restore
Data is purged from hot storage so that only the number of days corresponding to your license is
kept in hot. As described above, the Starter Packs keep 30 days of raw data in hot storage, but
you can always purchase space for more.
If you have purchased a Cold Storage license, Stellar Cyber stores incoming raw data in both hot
and cold storage simultaneously. The default Cold Storage license keeps raw data in cold
storage for a year by default. As with hot data, you can enhance your Cold Storage license to
keep data in cold storage longer.
Alerts, cases, and assets remain in hot storage for a year, by default. You can search for any of
these items without importing data from cold storage. However, searches that require
aggregation on multiple fields require import from cold storage to extend beyond the raw data
that's in hot storage. So, for example, if you want to perform a search showing the IP address
that triggered the most alerts in the last 12 months, you must import the raw data from cold
storage for those 12 months. Without doing so, the search could only show you that data for the
IP address exists over the last 12 months.

Requesting a Restore from Cold Storage
You request a restore from cold storage by opening a Zendesk ticket with Customer Success .
In response, the Stellar Cyber DevOps team will work to help you determine what data you need
and start the restoration process.
Note the following:
You work with Customer Success to specify how much data to restore and how quickly
you need it.
Requests to restore more than 5% of the total hot storage provided by your platform
license incur additional charges.
Once you submit your data restoration request, data will begin processing within a few
hours.
How Quickly is Data Restored from Cold Storage?
By default, data can be restored from cold to hot storage at the same speed at which it was
ingested. So, if your account has support for 100 GB of daily ingestion, that means that Stellar
Cyber can restore data from cold storage to hot at the rate of 100 GB per day.
If that's not fast enough for your needs, you can work with Customer Success to purchase
accelerated restoration.
External Storage Destinations in On-Premises vs.
Managed Deployments
The table below summarizes the differences between external storage destinations available in
both the on-premises and managed (SaaS) versions of Stellar Cyber. Note that the available
destinations vary depending on your deployment type, as summarized below.
SnowFlake
|   Cold Storage | Data Sinks | Integration (Bring |
| -------------- | ---------- | ------------------ |
Your Own Data Lake)
| On- |     | N/A |
| --- | --- | --- |
User-configurable in the System | Available by default. User-configurable in the System | DATA
Prem
|  DATA MANAGEMENT | Data | MANAGEMENT | Data Sinks page. |     |
| ----------------------- | ----------------------------- | --- |
ises
Management tabs.
Mana Available upon request and approval by submitting a ticket to
| Available for purchase from |     | Available upon request |
| --------------------------- | --- | ---------------------- |
ged Customer Success. Requests will be reviewed for feasibility
| Stellar Cyber. Default storage |     | by submitting a ticket to |
| ------------------------------ | --- | ------------------------- |
(Saa and cost and, if approved, will incur additional costs. Stellar
| location is OCI Object Storage.  |                                                    | Customer Success     |
| -------------------------------- | -------------------------------------------------- | -------------------- |
| S)                               | Cyber will proceed with implementation upon mutual |                      |
| You can choose your own location |                                                    | (feature is in Early |
agreement.
| by submitting a request to   |     | Access Program |
| ---------------------------- | --- | -------------- |
| Customer Support. You do not |     | status).       |
need to purchase the Cold
Storage SKU in this case, but
Stellar Cyber charges a fee for
managing the export.

SnowFlake
Cold Storage Data Sinks Integration (Bring
Your Own Data Lake)
Prim Real-time export of logs/events to external systems. Real-time streaming to
Medium- to long-term data
ary Business
retention and restoration.
Purp Intelligence/analytics
Cold data must be restored to
ose platforms
Stellar Cyber before it can be
analyzed.
Expo Near real-time. Near real-time.
On-Premises – Data moves to
rt
cold storage after the user-
Timin
configured hot retention time
g
expires.
Managed (SaaS) – Data is saved
to Hot and Cold storage at the
time of ingestion.
Stora On-premises users can configure their own Data Snowflake Snowpipe
On-Premises – S3, OCI, and
Sinks using the destinations available in the Data
ge
Azure, among others. Sinks page.
Desti Managed (SaaS) users can submit a request to
Managed (SaaS) – OCI Object Customer Success for integration of their preferred
natio Data Sink location by Stellar Cyber.
Storage, by default. Choose your
n Requests will be reviewed for feasibility and cost.
own location by submitting a Stellar Cyber will proceed with implementation upon
mutual agreement.
request to Customer Support.
 SaaS users cannot configure their own Data
Sinks.
Data Raw data (snapshot-based data). Raw Data, Alerts, Assets, Users. Data collected from
Type network traffic, logs,
s endpoints, cloud
services, and threat
intelligence feeds.
Per- Configurable per-tenant. Tenant-level handling available with a limit on the number of N/A
Tena supported destinations.
nt
Hand
ling
Using Data Sinks
Data Sinks are available in managed (SaaS) deployments but require manual activation through
a support request to Stellar Cyber Customer Success. Stellar Cyber reviews requests for
feasibility and cost and, if approved, proceeds with implementation upon mutual agreement on
additional costs.
Use Data Sinks to export data to external storage systems or SIEMs.Stellar Cyber supports
tenant-level handling, but limits the number of export destinations at the site level. Contact

Customer Success to determine the destination limit for your deployment.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  