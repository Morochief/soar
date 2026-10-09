Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Understanding Volume-Based Licensing

As described in Licensing Overview, the DP can be licensed based on the amount of data
ingested across all tenants in your organization on a daily basis. This topic provides details on
volume-based licensing.

 You can schedule and export PDF/CSV reports for Asset and Volume licenses from the

Reporting | Reports | License Usage page.

 Refer to Understanding License Compliance for details on how Stellar Cyber enforces

license policies.

Volume-Based Licensing Overview
Stellar Cyber collects data from a number of sources including its own Sensors, Log Sources,
and Connectors. This data is normalized, enriched, and then compressed before it is saved on
disk. The Stellar Cyber volume license is applied after these processes take place, each of which
affects the quantity of data:

Normalization – Increases or decreases data volume, depending on the source

Enrichment – Increases data volume

Compression – Decreases data volume

Example

Consider a sample customer with two tenants with the following on-disk collection volumes for a
single day after normalization, enrichment, and compression has taken place:

Tenant

Tenant A

Tenant B

SUM

Day

On-Disk Collection

1

1

1

5GB

10GB

15GB

For this customer's example, the total licensing volume for Day 1 across all tenants is the sum of
their individual collection volumes for the day – 15GB.

Tenant Allocation for Volume
When the Platform license is based on ingestion volume, the Tenant Allocation tab shows how
the daily GB threshold is distributed across tenants. You can edit quotas in the Allocation Quota
column. If total usage exceeds the License Threshold in the Licenses tab, the License State
changes to Warning and a warning banner appears in the UI.

Frequently Asked Questions on Volume-Based
Licensing

How can I reduce the data being counted against my licensed total?

The best way to reduce ingestion is to set filters that decrease the amount of data you bring into
the Stellar Cyber platform.

Why does the ingestion shown for a day continue to change after the day is complete?

Keep in mind that it takes 24 hours to complete the volume usage calculations for a given
UTC day. When a day ends in UTC time, its volume calculations are not final and may show
small changes until the end of the next day in UTC time.

For example, consider the day of March 15, 2023. Stellar Cyber shows ingestion values for this
day as soon as it concludes in UTC time. However, those values can and will show small
changes for another 24 hours and are not complete until the end of March 16, 2023 in UTC time.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

