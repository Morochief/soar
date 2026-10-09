Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Asset Details

Stellar Cyber keeps track of assets in your system, using both imported and discovered data.

The Asset Details page shows all information related to the asset, including an embedded map
that shows the asset's location. To see the details on an asset:

1. Select Assets | Asset Analytics.

The asset dashboard appears.

2. Select either MAC Identified Assets or IP Identified Assets.

The associated table of assets appears.

3. Select the FRIENDLY NAME of the asset that interests you.

The Asset Details page appears. The following is an example for a MAC-identified
asset:

The following is an example for an IP-identified asset:

On the Asset Details page you can:

View discovered data
View statistics for the asset
Do further analysis on the friendly name, hostnames, and IP addresses
Edit some of the fields

You can also view a table at the bottom of the Asset Details page listing associated Alerts,
Related Users, Vulnerabilities, Commands, Logins, Login Failures, Files, and Server Statistics for
the current asset. Keep in mind that the entries in these tables are all filtered by the global Filter
settings at the top of the page (Alert Score, Sensor, Time, Tags, and so on).

Viewing Discovered Data
To see what Stellar Cyber has discovered about an asset, simply select Discovered. This tab
displays all of the information that Stellar Cyber has gathered, as opposed to imported
information. Following is an example of the Discovered tab for a MAC-identified asset:

Following is an example of the Discovered tab for an IP-identified asset:

Viewing Asset Statistics
The lower section of the Asset Details page shows several counts, as well as the calculated risk
score of the asset.

The calculated asset risk score is an overall assessment of how likely the asset is going to be
involved in a security breach. The asset risk score:

is calculated every 10 minutes

includes open security events from the last 24 hours (if you close an event, it is
removed from the next calculation)
considers the vulnerability and importance level of assets
weights the presence of many different alert types more highly than large numbers of
the same alert

 Refer to Understanding the Stellar Cyber Risk Model for details on how Stellar Cyber

calculates risk scores.

Below the counts is a table listing events. This table is linked to the counts; you can click or tap
one of the counts to display the associated events in the table. You can also select the tabs
above the table to change the display.

The available categories include:

Alerts – This table contains a searchable list of alerts associated with the asset.
Related Users – Displays user accounts that most recently logged in to or interacted
with the asset. This table remains empty if no recent user activity is detected.

Vulnerabilities – This category provides a list of all detected vulnerabilities of the
current asset. The table includes a column for accessing CVE records.

Commands – Any captured commands of interest are listed in this section.
Logins – Successful login events are shown in this table.
Login Failures – Unsuccessful login events are shown in this table.
Files – This table shows captured events involving files that might be associated with
malware or exfiltration events.
Client Statistics or Server Statistics – This category displays a set of graphics similar
to the display in the image below. This provides a condensed assessment of the level of
activity of the asset.

Doing Further Analysis on the Friendly Name,
Hostnames, and IP Addresses
To do further analysis on an asset using the friendly name:

1. Select the  next to the name.

The analysis menu appears.

2. Select an option.

To do further analysis on an asset using the hostnames or IP addresses:

1. Select the hostname or IP address.

Additional hostnames or IP addresses appear.

2. Select one of the hostnames or IP addresses.

The analysis menu appears.

3. Select an option.

Depending on the data displayed, the following options may be displayed:

360 Panoramic View – Opens the Dashboards | Panoramic view with the
selected friendly name, hostname, or IP address as the filter.

VT VirusTotal Lookup – Performs a lookup on virustotal.com  for the
selected friendly name, hostname, or IP address.

 Copy to Clipboard – Copies the field value to the clipboard so it can be
pasted elsewhere.

Copy as Query – Copies a pre-built Lucene query that searches for related
activity involving the IP address of the asset across multiple fields. Use this
query in tools like Threat Hunting or Search to investigate communications
where the IP appears as source, destination, or host.

Editing Asset Information
You can edit some asset information:

1. Select Investigate | Asset Analytics.

The assets dashboard appears.

2. Select either MAC Identified Assets or IP Identified Assets.

The associated table of assets appears.

3. Click on the FRIENDLY NAME of the asset that interests you.

The Asset Details appear.

4. Select Edit.

You can now edit fields such as the friendly name, importance, tags, description, and
others.

5. Select Save.

Your changes are applied.

 You can monitor the progress of any edits to an asset in the Task List, available from the top

of the user interface.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

