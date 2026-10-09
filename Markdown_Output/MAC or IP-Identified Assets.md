Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

MAC or IP-Identified Assets

Stellar Cyber tracks assets in your system and analyzes their behavior to detect security events.
Stellar Cyber can discover both IP and MAC addresses and associate them with hosts. If you're
using DHCP, host IP addresses change over time, creating challenges for asset management
and behavior analytics.

Stellar Cyber sensors analyze DHCP traffic and associate host names with both IP addresses
and MAC addresses. When the IP address changes, Stellar Cyber continues to track the asset
as an individual asset. Stellar Cyber can also ingest logs from an IP address management
platform, providing the same continuity.

 Refer to Understanding Asset-Based Licensing for information on how Stellar Cyber
discovers and classifies assets, as well as how assets are counted for the purposes of
asset-based licensing.

Identified Assets
Stellar Cyber automatically identifies assets by discovering MAC addresses and IP addresses.
To see assets identified by their MAC addresses, click the Assets | Asset Analytics |
 MAC Identified Assets tab.

To see the asset identified by their IP addresses, click the IP Identified Assets tab.

Both tables are similar. Each table has a row for each known asset that was active in the period
specified.

The default columns include:

Friendly Name – The host name, or the IP address of the asset if the name is not
known. Select the Friendly Name entry to see the Asset Details page.

Risk – The risk score of the asset.

State – New, Approved, Unapproved, or Ignored.

Status – Active (seen in the last two hours), No recent activity (not seen in the last two
hours), Unapproved, or Ignored.

MAC – The MAC address of the asset. For an IP-identified asset, this is a unique
address assigned by Stellar Cyber, starting with a2.

IP – The IP address of the asset.

Sensor – The sensor where the asset was last identified.

Data Sources – The types of data sources used to identify the asset.

Type – The type of asset, such as server or client.

Vendor – The known vendor of the asset.

Vulnerability – The count of vulnerabilities of the asset detected by Stellar Cyber. More
information can be found on the Asset Details page.

Location – The location of the asset.

Tag – Tag values, if any, assigned to the asset.

Importance – The relative importance assigned to the asset.

Reputation – The reputation associated with the asset.

STATIC – Present on the IP-identified assets tab only, indicates whether the IP address
is static or dynamic.

CVE List – A known security flaw associated with the asset, if any.

Performing Bulk Actions

To perform actions on one or more assets:

1. Select one or more assets using the check boxes on the left of each row.

2. Select one of the actions at the top of the table.

The following actions take effect immediately:

Approve – Approve assets that are new, unapproved or ignored. By
default assets enter the system as New.

Unapprove – Unapprove the assets. Unapproved assets generate
one Unapproved Asset alert each day.

Ignore – Ignore assets, so no Unapproved Asset events are
generated for the corresponding assets.

 Refer to Understanding Asset-Based Licensing for

information on how Stellar Cyber discovers and classifies assets,
as well as how assets are counted for the purposes of asset-
based licensing. Keep in mind that the state of an asset
(approved, unapproved, or ignored) has no effect on whether an
asset is counted against daily totals for asset-based licensing.
The only way to exclude an asset from counting against your
licensed total, is to set filters to remove that asset before
ingestion for each data source where it could be discovered.

The following actions are available from the dropdown menus and take effect
after you click Apply.

 You can monitor the progress of any of these actions in the Task List

,

available from the top of the user interface.

Type – Set to router so that Stellar Cyber knows that this asset can
have multiple IP addresses associated with the MAC address. The
asset is moved to the Router tab, which displays all identified routers.
Stellar Cyber automatically recognizes routers, but that can take time.

Tags – Assign tags to the assets. You can use an existing tag or
define a new one.

Location – Assign a location to the assets. You can use an existing
location or define a new one.

Importance – Assign a value to the assets, which informs the
security score. For example, a test printer would have a low value,
while a domain controller would have a critical value.

Static IP – IP Identified Assets Tab Only. Identify this IP address as
static. Stellar Cyber keeps the asset ID associated with the
IP address regardless of the DHCP lease period configured in the
Admin Settings. This is only available on IP-identified assets. MAC-
identified assets always retain the same asset ID.

 Use the check box in the header of the table to check or uncheck all rows.

See the Tables page for more information on working with tables.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

