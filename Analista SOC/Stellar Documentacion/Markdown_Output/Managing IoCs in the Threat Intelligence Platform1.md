✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Managing IoCs in the Threat Intelligence
Platform
 You must have Root scope to use this feature.
Use the IoCs tab on the Threat Intelligence Platform page to manage Indicators of
Compromise (IoCs). See Using the IoCs Tab.
To configure and manage Feeds, see Configuring Feeds in the Threat Intelligence Platform.
See also:
Reputation-based ML Alert Types and Rules
File Hash Data Sources
Reputation Field Mapping
Using the IoCs Tab
The IoCs tab displays all the latest IoCs that are present in storage, along with data associated
with each IoC, such as expiration date, source, and confidence score.
The IoCs table displays all IoCs ingested from all feeds, except those IoCs that are expired or
revoked. In addition, the table displays IoCs imported by the user.
The IoCs table has the following columns:
Name—name of the IoC
Type—type of the IoC: IP address, URL, domain name, and file hash

 The RedSense premium feed includes IoC types: Hostname and Network-Traffic.
Confidence—confidence, provided by the source
 Internally in the Threat Intelligence Platform, IoCs have priorities for ingestion.
This means that when IoCs are imported, IoC operations with lower confidence
scores cannot overwrite IoC operations with higher confidence scores.
Score—score, provided by the source
Creation Date—creation date of the IoC
Sources—sources of the IoC, such as etpro, alienvault, or emerging_threat (an IoC
could be ingested from multiple sources)
Modification Date—modification date of the IoC
Tags—shared attributes of IoCs, such as malware or CnC
Expiration Date—expiration date of the IoC
Actions—actions available on an IoC, such as Delete this row
Using Search
Use the Search box to search for an IoC by name.
Importing from a File
You can import new IoCs from a file. The supported IoC types are IP address, URL, domain
name, and file hash (MD5, SHA1, and SHA256).
 When you import file hash IoCs, if you select an expiration time of less than 90 days, it will
be set to 90 days.
1. Click Upload.
2. (Optional) Click Download Template.
a. Select Download CSV Template or Download Text Template.
b. Depending on your browser and system, the file is either immediately
downloaded to your Downloads folder or you are prompted for a location. You
can edit the template to add IoCs.
3. Browse to select a file. The file type must be either .csv or .txt.
4. Set an Expiration Time and select in Hours, Days, or Months.
5. Click Next.

6. The IoCs extracted from the file are displayed. Unselect any IoCs you would like to
exclude from the import.
7. Click Submit.
Exporting CSV
Click Export CSV to export the table as a spreadsheet file.
You can export Selected Columns or All Columns to a maximum of 10,000 IoCs. If there are
more than 10,000, use filters and sort to select the 10,000 you want to export.
The spreadsheet is downloaded to your Downloads folder.
Selecting View
Click Select View to preserve a table layout. See Saved View Configurations for details.
Using Filters
Click Filters to use defined filters.
To use defined filters:
For Type, select a type using the check boxes or Select All.
To see more Type, click View More.
For Score, enter Min and Max using the up and down arrows.

The limits are from 1 to 100. The Min must be less than the Max.
For Creation Date, enter From and To dates and times using the calendars.
Select a date, select a time, then click the checkmark.
For Sources, select a source using the check boxes or Select All.
To see more Sources, click View More.
For Tags, select a tag using the check boxes or Select All.
To see more Tags, click View More.
If a defined filter is unselected, you can click the search box under Add new filter to
select a filter from the dropdown.
To exit, click Filters again. The configured filters are displayed at the top of the table.

To clear an individual filter, click the icon to the right of the filter ( ).
To clear all filters, click Clear All.
Using Columns
Click Columns to add or remove columns using check boxes.
Click Columns again to exit.
Deleting IoCs
To delete an IoC, click the Trash icon ( ) in the Actions column for a row in the table. The
following confirmation is displayed.
Click Yes, permanently remove this IoC.
You can also click a check box on the left to select an IoC and then click the Trash icon ( ).
Reputation-based ML Alert Types and Rules
If there are IoCs in your domain, IP address, or URL-related fields, then fields such as
source_reputation are enriched. The following IoC-based detection behavior is for Machine
Learning (ML) alert types as well as rules.

See the following:
ML Alert Types
Rules
Handling Alerts when Bad Reputation is True
ML Alert Types
Bad Source Reputation Anomaly
This alert type detects generic bad source reputations, which are other than Brute_Forcer,
Scanner, and Command and Control (CnC). For example, if there is a spike of records that have
srcip_reputation: malicious, an ML alert is triggered.
The query is as follows:
_exists_:srcip_reputation AND (NOT srcip_reputation:Good AND NOT
srcip_reputation:Brute_Forcer AND NOT srcip_reputation:Scanner AND NOT
srcip_reputation:CnC) AND NOT _exists_:event_source
The IoC source is any feeds or user-ingested IoCs.
Bad Destination Reputation Anomaly
This alert type detects generic bad destination reputations. If there is a spike of records that have
such bad destination reputations, an ML alert is triggered.
The query is as follows:
_exists_:dstip_reputation AND NOT dstip_reputation:Good
The IoC source is any feeds or user-ingested IoCs.
Command & Control Reputation Anomaly
This alert type detects Command and Control-related reputations. If there is a spike of records
that have such reputations, an ML alert is triggered.
The query is as follows:
(dstip_reputation:CnC OR dstip_reputation:SpywareCnc OR
dstip_reputation:P2Pcnc OR dstip_reputation:Mobile_CnC OR
dstip_reputation:Mobile_Spyware_CnC) AND (state:Closed OR
state:Established)
The IoC source is Alienvault, ETPro IP, ETPro domain, or user-ingested IoCs that have the IoC
tags that satisfy the query.
Scanner Reputation Anomaly
This alert type detects the Scanner, Phishing, or Spam reputations from the source IP address. If
there is a spike of records that have such reputations, an ML alert is triggered.
The query is as follows:
(srcip_reputation:Scanner OR srcip_reputation:Phishing OR
srcip_reputation:Spam) AND (state:Closed OR state:Established OR
state:Aborted OR state:HalfOpened) AND NOT _exists_:event_source

The IoC source is Alienvault, DHS, ETPro IP, ETPro domain, Openphish (only Phishing),
Phishtank (only Phishing), or user-ingested IoCs that have the IoC tags that satisfy the query.
Rules
Bad Reputation Login
This rule detects generic bad source reputations, which are other than Brute_Forcer and
Scanner, under the condition of successful logins. For example, if a record has
srcip_reputation: malicious, and has successfully logged in to some places, this rule is
triggered.
The query is as follows:
'login_result:success AND (_exists_:srcip_reputation AND NOT
srcip_reputation:Good AND NOT srcip_reputation:Scanner AND NOT
srcip_reputation:Brute_Forcer)'
The IoC source is any feeds or user-ingested IoCs.
Emerging Threat
This rule detects the emerging_threat reputations that potentially come from domain, IP
address, URL, or file hash IoCs.
The queries are as follows:
'srcip_reputation:emerging_threat', 'dstip_reputation:emerging_threat',
'domain_reputation:emerging_threat', 'url_reputation:emerging_threat'
File hash reputations may come from multiple potential fields, depending on the data sources
such as:
file.threat_indicator.labels:emerging_threat,
process.threat_indicator.labels:emerging_threat,
process.parent.threat_indicator.labels:emerging_threat,
file_list.threat_indicator.labels:emerging_threat,
process_list.threat_indicator.labels:emerging_threat, and
process_list.parent.threat_indicator.labels:emerging_threat
The emerging threat file hash detection query will be OR combinations of the above conditions.
The IoC source is the Emerging threat feed, custom TSV feeds, or user-ingested IoCs that have
the IoC tags that satisfy the query.
Using the source IP address emerging threat as an example:
"srcip_reputation": "EvilProxy_Phishing;emerging_threat;scanner",
"srcip_reputation_source": "emerging_threat;ETPro",
The alert description will be as follows:
The traffic from \"IP/name: <IP address>\" to \"IP/name: <IP address>\" has one or more
emerging threats (Reputation: EvilProxy_Phishing;scanner. Extra sources: ETPro) on the source
IP <IP address>.

where Reputation: EvilProxy_Phishing;scanner. Extra sources: ETPro is new in the
description.
Malicious Site Access
This rule detects the MalAccess reputation that comes from the URL IoCs.
The query is as follows:
'url_reputation:"MalAccess"'
The IoC source is Abuse.ch (urlhaus) feed or user-ingested IoCs that have the IoC tags that
satisfy the query.
Phishing URL
This rule detects the phishing reputation among HTTP records. The reputation could come from
either the destination IP address or the URL IoCs.
The query is as follows:
'url_reputation:"Phishing" OR (dstip_reputation:"Phishing" AND
appid_name:"http")'
The IoC source is Alienvault, DHS, ETPro IP, ETPro domain, Openphish, Phishtank, or user-
ingested IoCs that have the IoC tags that satisfy the query.
Handling Alerts when Bad Reputation is True
For the External/Internal User Login Failure Anomaly alert type, when the source IP address is
flagged with a bad reputation, the system handles alerts as follows:
User Login Failure Anomaly Detection:
The system evaluates incoming login events against known behavioral
indicators of suspicious or excessive failures.
If the anomaly thresholds are met (for example, there is an unusually high
failure rate), an alert is generated.
Parallel Reputation Check:
In parallel, the system checks the source IP (or domain, URL, or file hash)
against reputation databases, including Emerging Threat IoCs.
If the source IP is known to be malicious or bad, and it meets the criteria for a
standalone Bad Reputation alert (such as the Bad Reputation Login alert type),
that alert will also be raised.
Separate Alerts, Independent Scoring:
The reputation-based finding does not adjust or boost the anomaly’s existing
score. Each detection type (behavior-based vs. reputation-based) retains its
own logic and thresholds.
As a result, there may be two parallel alerts:
User Login Failure Anomaly, reflecting the behavioral anomaly, and
Bad Reputation Login, triggered by the IP’s malicious reputation

In other words, a bad reputation source IP does not raise the score of the User Login Failure
Anomaly alert, rather, it triggers its own separate Bad Reputation alert, if all requirements are
satisfied.
File Hash Data Sources
The following data sources have file hash-related enrichment.
Alert Integrations
Acronis Cyber Protect Cloud
Avanan
Broadcom SES
Cato Networks
CrowdStrike
CyberArk EPM
Deep Instinct
ESET Protect
Fortinet Lacework
Halcyon
LimaCharlie
Microsoft Defender for Cloud
Microsoft Defender for Cloud Apps
Microsoft Defender for Endpoint
Mimecast
Netskope
Proofpoint Targeted Attack Protection (TAP)
SentinelOne Cloud
SonicWall Endpoint Security
Sophos Central
Trellix MVISION
Trend Micro Vision One
VMware Carbon Black Cloud
WithSecure Elements
Parsers
Centos Audit
Check Point Harmony Email & Collaboration

Check Point Harmony Endpoint
Cisco Umbrella
GTB Data Loss Prevention (DLP)
Linux Audit
Scx SmartEDR
ThreatLocker Zero Trust EPP
Wallix Bastion
Windows Event Parser
IBM WinCollect
Other
Trend Micro Cloud App Security
Reputation Field Mapping
The following table shows reputation enrichment. It lists all source fields run against IoCs and
mapped to reputation fields containing reputation metadata.
Mapping
| Source Field | Reputation Field | Data Source |
| ------------ | ---------------- | ----------- |
of Fields
1:1 Stellar Cyber sensor
| metadata.response.query | domain_reputation |     |
| ----------------------- | ----------------- | --- |
1:1
metadata.request.query domain_reputation Stellar Cyber sensor
1:1
Multiple sources
| domain_list | domain_reputation |                  |
| ----------- | ----------------- | ---------------- |
| 1:1         | dstip_reputation  | Multiple sources |
dstip
| dstip_source 1:1 | dstip_reputation_source |     |
| ---------------- | ----------------------- | --- |
Multiple sources
1:1
| hostip | hostip_reputation | Multiple sources |
| ------ | ----------------- | ---------------- |
1:1 Multiple sources
| hostip_source | hostip_reputation_source |     |
| ------------- | ------------------------ | --- |
1:1
| remote_ip | remote_ip_reputation | Multiple sources |
| --------- | -------------------- | ---------------- |
1:1
Multiple sources
| remote_ip_source | remote_ip_reputation_source |     |
| ---------------- | --------------------------- | --- |
1:1 Multiple sources
| srcip | srcip_reputation |     |
| ----- | ---------------- | --- |
1:1
| srcip_source | srcip_reputation_source | Multiple sources |
| ------------ | ----------------------- | ---------------- |
1:1
Multiple sources
| url | url_reputation |     |
| --- | -------------- | --- |

Mapping
Source Field Reputation Field Data Source
of Fields
file many:1 See Enriched Threat Intelligence. Multiple sources
file_list
process
process.parent
process_list
(if found within the threat_indicator object)
Enriched Threat Intelligence
For every hash found in a file or process, the threat intelligence data is enriched using the
threat_indicator field, which contains the following:
Name Type Description
threat_indicator object Can be a subfield of file, file_list, process, process.parent, or
process_list.
threat_indicator.labels list of strings The categorization labels for the threat indicator.
threat_indicator.sources list of strings The provider or source of the threat intelligence.
threat_indicator.score integer The threat score, which is optional.
(optional)
threat_indicator.file.has hash object The file hash associated with the threat indicator.
h
JSON Structure
An example of the JSON structure is as follows:
{
"file": {
"hash": {
"md5": "030753fb7a8eff726297c9dbd734c9ea",
"sha1": "c57e03c5865290efb13ff3e8505e229790cea835",
"sha256": "04ddd4cec63dfe1d221c8afa51306a5fcb92abdef70a7a18d1b2a8f11add625d"
},
"threat_indicator": {
"labels": [],
"sources": ["DHS"],
"score": 90,
"file": {
"hash": {
"md5": "030753fb7a8eff726297c9dbd734c9ea",
"sha1": "c57e03c5865290efb13ff3e8505e229790cea835",
"sha256":
"04ddd4cec63dfe1d221c8afa51306a5fcb92abdef70a7a18d1b2a8f11add625d"
}
}

}
}
}
Where threat_indicator is Found
The threat_indicator field may be present in the following:
file
file_list (a list of files)
process
process.parent
process_list (a list of processes)
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  