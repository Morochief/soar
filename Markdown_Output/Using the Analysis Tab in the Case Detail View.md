✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Using the Analysis Tab in the Case Detail View
The Analysis tab in the Case Detail view (Cases | <case-name> | Analysis) provides a
graphical display that helps you visualize a coalesced view of an ongoing attack. Separate
entries in the display represent internal or external hosts, as well as URLs , files
, users , services , processes , registry keys , and sensor status alerts
.
Solid lines between the displayed entities represent events taking place between different
entities, while dotted lines represent parent/child relationships. The nodes themselves represent
objects, users, hosts, or services.
 In versions before 6.3.0, the Analysis tab displays a connection of a user node to a host
node only when the event is classified as User Behavior Analytics (UBA). From 6.3.0, if a
user node already appears and the related host node has no existing connections, Stellar
Cyber connects them even when the event is not UBA. This provides a more complete view
of user–host relationships while keeping the default behavior of hiding user nodes when no
correlated user context exists.
Consider the sample Analyze workspace for a case involving an Internal Ransomware attach
shown below:
The graphical interface on the Analysis tab helps you quickly understand the entities involved in
a case and how they relate to each other:
The Observables legend at the left lists each entity type (such as hosts, files, users,
and services) along with a count. Select an entity type to expand the list.

In the main workspace, entities are displayed as icons. Lines represent interactions,
and circles show the number of related alerts.
Select any entity to display a context menu with additional drilldown options for further
analysis. The figure above shows the context menu for the 10.0.1.194 internal host.
The case includes 23 alerts between 10.0.1.151 and various internal hosts, external
hosts, and the Office 365 service.
Select any of the circular alert indicators in the display to view a Timeline of when
events occurred and how the attack unfolded. Then select the  button for any alert in
the Timeline to see its associated Event Display, including the supporting Interflow data.
Automated Hypotheses and Summaries in the Analysis
Tab
When AI Case Analysis is enabled in Global Settings, you can run AI Case Analysis to accelerate
investigations with AI-generated narratives, insights, and suggested incident responses in the
Detection, Analysis, and Response tabs in the Case Detail view.
After running AI Case Analysis on a case, the Analysis tab in the Case Detail view includes a
new Hypothesis panel and adds AI-generated summaries to the existing Timeline, and
Observables panels, helping summarize alerts into a case-level story, reconstructing timelines,
and explaining relationships between entities. These additions transform raw alerts into
structured narratives and visual relationships, making it easier to interpret attacker intent and
scope.
AI Case Analysis adds the following features to the Analysis tab:
Hypothesis panel – This entirely new panel provides an analyst-style narrative that
explains what likely occurred, connecting multiple alerts into a storyline. For example,
brute force → reconnaissance → exploitation → insider-like activity. The Hypothesis
tab also maps to MITRE ATT&CK tactics and techniques, as you can see in the figure
below:
Timeline panel – The existing Timeline panel is augmented with an AI-generated
summary that reconstructs the attack in chronological order, step by step, with plain-
language context for each stage. This helps you validate the progression of events and
identify when compromise began.

Observables panel – The existing Observables panel is updated with an AI-generated
summary of key entities (accounts, hosts, IP addresses) and the relationship dynamics
between them. In addition, AI Case Analysis highlights suspicious patterns of behavior
across entities in this panel.
Next Steps with AI Case Analysis
To return to the case's high-level summary, you can click on the Detection tab.
For next steps and actionable response guidance for the case, see the Response tab.
Rearranging the Analysis Workspace
You can rearrange and adjust the Analysis workspace to suit your needs using any of the
following techniques:
Select and drag any node in the display to change its position. This is handy when you
want to zero in on an particular host that's part of a case with many other hosts.
Select and on the background of the workspace to move the entire collection of nodes
and lines around the workspace.
Use the controls at the top of the display to resize, reset, and zoom the display:
Solid Lines vs. Dotted Lines in the Analysis Workspace
The Analysis workspace represents events taking place between different entities with solid
lines, while dotted lines represent parent/child relationships. For example, the dotted lines in the
figure below indicate a parent/child relationship between a host and a process:

Observables from Third-Party Cloud-Based Integrations
Stellar Cyber integrates natively with many third-party Cloud Detection and Response services,
including Microsoft Defender for Cloud and AWS GuardDuty. Stellar Cyber displays alerts
generated from these services in its own displays. In addition, Stellar Cyber automatically
extracts and displays observables based on alerts from the following Cloud sources:
Third-Party Integrations
Microsoft Defender for Cloud
AWS GuardDuty
Rule-Based Alerts
SigmaHQ rules for AWS CloudTrail
SigmaHQ rules for Azure Activity Logs
The entities illustrated in the table below can appear in the Case Analysis workspace, depending
on the nature of the alert and the data present:
| Cloud |     | Source in AWS | Icon in Analysis |
| ----- | --- | ------------- | ---------------- |
Source in Microsoft
| Observable |     | GuardDuty | Workspace |
| ---------- | --- | --------- | --------- |
Sources from Azure Activity Logs are listed in
|     | "Microsoft.<xxx>/<yyy>" format |     |     |
| --- | ------------------------------ | --- | --- |
All others are from Microsoft Defender for Cloud
| Virtual Machine |     | Instance |     |
| --------------- | --- | -------- | --- |
Virtual Machine
Microsoft.Compute/virtualMachines
| Function   | n/a | Lambda            |     |
| ---------- | --- | ----------------- | --- |
| Kubernetes |     | KubernetesCluster |     |
AWS EKS Cluster
Service
Kubernetes Service
Kubernetes - Azure Arc
Microsoft.Kubernetes/connectedClusters

| Cloud |     | Source in AWS | Icon in Analysis |
| ----- | --- | ------------- | ---------------- |
Source in Microsoft
| Observable |     | GuardDuty | Workspace |
| ---------- | --- | --------- | --------- |
Sources from Azure Activity Logs are listed in
"Microsoft.<xxx>/<yyy>" format
|     |     |     |     |
| --- | --- | --- | --- |
All others are from Microsoft Defender for Cloud
| Container | Microsoft.ContainerRegistry/registries | Container |     |
| --------- | -------------------------------------- | --------- | --- |
| App       | App Service                            | n/a       |     |
Container Service
|     | Microsoft.ContainerService/managedClusters | ECSCluster |     |
| --- | ------------------------------------------ | ---------- | --- |
SQL Database
|      | SQL Database | RDSDBInstance |     |
| ---- | ------------ | ------------- | --- |
| Non- |              | n/a           |     |
Azure Cosmos DB Account
SQL Database
Object Storage
|              | Storage Account | S3Bucket |     |
| ------------ | --------------- | -------- | --- |
| File Storage |                 | n/a      |     |
Azure Files
| Virtual Network |     | n/a |     |
| --------------- | --- | --- | --- |
Virtual Networks
Microsoft.Network/virtualNetworkGateways
Microsoft.Network/virtualNetworks

| Cloud |     | Source in AWS | Icon in Analysis |
| ----- | --- | ------------- | ---------------- |
Source in Microsoft
| Observable |     | GuardDuty | Workspace |
| ---------- | --- | --------- | --------- |
Sources from Azure Activity Logs are listed in
"Microsoft.<xxx>/<yyy>" format
|     |     |     |     |
| --- | --- | --- | --- |
All others are from Microsoft Defender for Cloud
VPN
|     | VPN Gateway | n/a |     |
| --- | ----------- | --- | --- |
Microsoft.Network/p2svpnGateways
Microsoft.Network/vpnGateways
DNS
n/a
Microsoft.Network/dnsZones
| API Management |     | n/a |     |
| -------------- | --- | --- | --- |
API Management Service
Service
Key and Secret
|     | Key Vault | n/a |     |
| --- | --------- | --- | --- |
Microsoft.KeyVault/vaults
| Identity and | n/a |     |     |
| ------------ | --- | --- | --- |
AccessKey
Access
Management
| Firewall | Microsoft.Network/azureFirewalls | n/a |     |
| -------- | -------------------------------- | --- | --- |
Microsoft.Network/firewallPolicies
Miscellaneous
All unrecognized cloud.resource.type values start out as Miscellaneous and
remain so until they are classified into one of the categories above.

Observables from Cloud-Based Email Security
Integrations
Stellar Cyber integrates natively with many cloud-based email security services, including
Mimecast and Proofpoint. Stellar Cyber displays alerts generated from these services in its own
displays. In addition, Stellar Cyber automatically extracts and displays the following observables
in the Case Analysis workspace of cases created for these alerts:

Observable Normalized Field Required?
srcip No
IP address of the email sender
Unique ID of the email email.message_id Yes
Email, identified using its subject line email.subject Yes
The address responsible for the actual transmission of the email email.sender.address No
The email addresses of the recipients email.recipient.addresses No
Potentially malicious links in the email url or url_list No
Potentially malicious attachments in the email file or file_list No
The figure below illustrates a typical arrangement in the Case Analysis workspace of these
observables for a Case based on an email alert:
Note the following regarding the hierarchical arrangement shown above:
A top-level user node is labeled with the email address that sent the email.
A host node is connected to the user node and shows the IP address of the sender.
An email node is connected to the user node for the IP address and shows the subject
of the email.
The recipients of the email are shown with user nodes connected to the email node.
They are labeled with their email addresses.
Any potential malicious attachments or links are shown with their own nodes connected
to the email node. They are labeled with either the filename of the attachment or the
URL of the link, depending on what is being displayed.
About the Observables Panel
When you first display the Analysis tab, the Observables panel appears by default at the left of
the Analysis workspace, summarizing the different types of entities associated with the case,
along with a count of each:

You can cascade open the entry for any of the entities associated with the case to see a list of
the actual constituent entities. Depending on the type of entity, you can select the button
adjacent to an entry to display a context menu where you can drill to further details elsewhere in
the Stellar Cyber interface. For example, the figure below illustrates the context menu for a
drilldown on a host. You could also see users, services, URLs, files, processes, and registry
values listed in Observables, depending on the nature of the case.
 If you have AI Case Analysis enabled as part of an Early Access Program, the Observables
panel includes an AI-generated summary of key entities for the case and the relationship
dynamics between them, as well as a Hypothesis tab. Refer to Automated Hypotheses
and Summaries in the Analysis Tab for details.
About the Timeline Panel
You can toggle the Analysis tab between displaying the Observables or Timeline panel by
selecting the corresponding button at the top left of the workspace.
By default, the Timeline panel shows all alerts associated with the case in descending
chronological order, from newest to oldest, along with an indication of the elapsed time between
each event. You can reverse the sort order by selecting the arrow at the top of the Timeline, as
illustrated below:
You can also select any of the circular alert indicators in the graphical display to filter the Timeline
so it shows just those alerts associated with the corresponding relationship.
 If you have AI Case Analysis enabled as part of an Early Access Program, the Timeline tab
also includes an AI-generated Timeline Summary, as well as a Hypothesis tab. Refer to
Automated Hypotheses and Summaries in the Analysis Tab for details.
Understanding Alert Entries in the Timeline
Alerts are displayed in the Timeline in individual panels. Panels appear initially as collapsed
summaries, but can be toggled open by selecting the ˅ button at the right of an alert entry, as
illustrated below:

Alerts are displayed in the Timeline with the following information:
XDR Kill Chain Stage/Alert Type – A distinctive icon indicates either the XDR Kill Chain
stage of the alert or the alert type. For example:
Initial Attempts
Persistent Foothold
Exploration
Propagation
Exfiltration & Impact
Score – A color-coded numerical score indicates the severity of the case. Scores are
updated dynamically as new events are added to the case or you remove alerts.
Name – The name of the alert.
Timestamp – The date and time at which the alert was reported by Stellar Cyber.
Event Display  – Select the  button for any alert in the Timeline to see its
associated Event Display, including the supporting Interflow data.
Tactic – The tactic for the alert, based on the MITRE | ATT&CK framework  .
Technique – The technique for the alert, based on the MITRE | ATT&CK framework  .
Description – A one-line summary of the alert.
Drilling Down from the Analysis Tab
The Analysis tab provide multiple options for contextual drill-down to further analysis elsewhere
in Stellar Cyber:
When you select an entity in the Analysis tab or the button in the Observables list, a
context menu appears similar to the illustration in Observables, above. The exact
options available depend on the type of entity you selected and the additional
information available and include the following:

Asset Detail View – Opens the Assets | Asset Analytics | Asset Details tab
for the selected friendly name, hostname, or IP address as the filter.
360 Panoramic View – Opens the Dashboards | Panoramic view with the
selected friendly name, hostname, or IP address as the filter.
VT VirusTotal Lookup – Performs a lookup on virustotal.com  for the
selected friendly name, hostname, or IP address.
 Add as Including Filter – Creates a filter to display only those events
containing the value in the field.
 Add as Excluding Filter – Filters out those events containing the value in
the field.
 Copy to Clipboard – Copies the field value to the clipboard so it can be
pasted elsewhere.
Copy as Query – Copies a pre-built Lucene query that searches for related
activity involving the IP address of the asset across multiple fields. Use this
query in tools like Threat Hunting or Search to investigate communications
where the IP appears as source, destination, or host.
Event Display  – Select the  button for any alert in the Timeline to see its
associated Event Display, including the supporting Interflow data.
Group Details – Stellar Cyber might occasionally group entities to conserve on display
space. In cases like this, select a group and use the Group Details option in the
context menu that appears to display the grouped entities in the Observables panel.
Multiple IP Addresses in the Analysis Tab
When Stellar Cyber detects multiple IP addresses on the same host, it displays a short message
indicating the number of associated IP addresses. You can select the message to see a pop-up
listing each of the detected IP addresses, including a timestamp of when it was seen and drill-
downs for further analysis. The illustration below provides an example of a host with multiple
associated IP addresses.
Grouped IP Addresses and Domains in the Analysis Tab
To simplify the visual impact of complex charts, Stellar Cyber automatically groups related nodes
with a high number of alerts to or from a host node. For example, if there many alerts from a host
to several addresses on different hosts in the same domain, the workspace displays only one
icon for the whole domain.
The same grouping occurs for a high volume of alerts to hosts with IP addresses that can be
effectively represented as an IP address range. This differs from the grouping of multiple IPs on

a single host. In this case, the group is multiple, related IP addresses or domains on different
hosts.
Grouping is indicated as follows:
For domains: The address below the host icon is the abbreviated domain prefixed with
a wildcard (*.mydomain.com, *.corporate.otherdomain.net).
For IP addresses: The address below the host icon is replaced with a CIDR address,
reflecting the scope of the group.
To display the group details, select the domain or address below the icon. This opens a short
menu that lets you display Group Details. Select this menu to open a pane with a list of all the
observed node addresses.
Grouped Processes, Files, and URLs
Stellar Cyber performs similar grouping for processes, files, and URLs in the Analysis tab. In
situations where there are multiple files, processes, or URLs with the same alert type connecting
to the same node, Stellar Cyber may display them in a summarized container to improve
readability. You can always select the entry below the grouped entities to access the Group
Details menu and view the constituent members, complete with drill-down access for each. The
figure below shows examples of grouped processes and files in the Analyze workspace:
Summarizations in the Analysis Tab
Stellar Cyber optimizes the display of massive graphs with multiple levels of observables by
summarizing each level of a process tree with greater than 20 of the same observable type. For
example, consider the summarization shown in the figure below. Instead of showing separate
associations from each *.tmp process to System32cmd.exe, the associations are summarized to
improve display performance:

Login Failure Alerts in the Analysis Tab
Login Failure alerts can include multiple usernames under the same special UserSID of S-1-0-0.
This UserSID is used in Windows when a SID value is not known. The Analysis tab still shows all
the usernames associated with a Login Failure Alert under this SID. Keep in mind, however, that
these user entities are not real users.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  