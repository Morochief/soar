Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

About the Threat Intelligence Platform

Stellar Cyber's Threat Intelligence Platform (TIP) provides multiple threat intelligence feeds that
bring in Indicators of Compromise (IoCs). TIP provides primary operations on the IoCs, such as
import and export, as well as a variety of feeds. Using TIP, you can collect IoCs from the sources
you like and you can create your own feeds.

The objective of the Threat Intelligence Platform is to minimize the time between the first
identification of malware or threats and the ingestion of corresponding IoCs into the Stellar Cyber
platform. Swift IoC ingestion enhances a proactive defense and helps to stay ahead of emerging
threats.

Why TIP Matters

When a new threat is detected, whether it is malware, a phishing domain, or other malicious
activity, the clock starts ticking. Various sources such as OS intelligence, vendors, and platforms
like VirusTotal might catch the first glimpse of the threat. This initial detection is crucial as it sets
the stage for further analysis and response.

Once a threat is identified, the next step involves threat research. This is where threat reports
and CERT advisories assist the cybersecurity community in gathering more intelligence on the
evolving threat. The quicker these IoCs are transferred into the Stellar Cyber platform, whether
they are URLs, IP addresses, domains, or file hashes, the faster the platform can start protecting
against these threats.

    

By default, the Threat Intelligence Platform (TIP) is not fully enabled. While built-in threat
intelligence feeds are activated by default, the ability to configure these feeds, add new
premium feeds (otherwise known as "bring your own threat intelligence feed") such as
Anomali, Cybersixgill, RedSense, Recorded Future, SOCRadar, CrowdStrike, or ESET, or
integrate custom feeds is disabled by default. This is because the performance and
resource requirements must be carefully evaluated before enabling these features.

If you are interested in utilizing this feature, please reach out to Stellar Cyber customer
support or your sales representative for a technical evaluation of your needs and resource
requirements.

Key performance considerations include:

Message Rate/Data Volume: The impact will vary depending on the overall data
throughput on the platform.

Resources Available: The performance is dependent on the computing power and
storage capacities available, including the number of nodes.

Ingested IoCs: The number and types of Indicators of Compromise ingested can
significantly influence the performance.

How TIP Works in Stellar Cyber
The speed and efficiency of the TIP process are crucial for reducing exposure windows and
enhancing your overall security posture. By streamlining IoC ingestion and enabling faster
reputation enrichment, we ensure that your defenses remain robust and responsive to emerging
threats.

This process, as illustrated in the following diagram, highlights the seamless flow from external
threat intelligence feeds to event enrichment and alert computation, providing a comprehensive
defense strategy against malicious actors.

1. Data Sources and Fields Mapped to IoCs:

Data is mapped from multiple fields (Network, Endpoint, SaaS, Cloud,
Vulnerability Scanner, Identity) to IoCs such as IP addresses, domains, URLs,
and file hashes.

2. Feed Ingestion:

TIP aggregates IoCs from the following feeds:

Built-in Feeds: Free sources like AlienVault, PhishTank, OpenPhish,
and government entities such as DHS.

Premium Feeds: Paid sources like Anomali, Cybersixgill, RedSense,
Recorded Future, SOCRadar, CrowdStrike, and ESET, providing
advanced threat intelligence.

Custom Feeds: User-configurable sources using TAXII or TSV
formats.

3. Event Enrichment:

Once IoCs are ingested, they enrich ingested events within Stellar Cyber,
allowing for better threat context.

4. Alert Severity Score Computation:

The enriched threat data contributes to more accurate alert severity scores,
helping security teams prioritize their response.

The score calculation takes three factors into account: the original score
provided by the data source, the confidence, and the creation time.

User Interface
The user interface for the Threat Intelligence Platform page has two tabs, one for IoCs and one
for Feeds.

The IoCs tab displays all the latest IoCs that are present in storage, along with data associated
with each IoC, such as expiration date, source, and confidence score.

The Feeds tab displays the threat intelligence feeds, which have three types:

Built-in feeds are provided by Stellar Cyber. They include AlienVault OTX, DHS,
Emerging Threat (ET) Pro IP, ET Pro Domain, ET Pro Rules, PhishTank, Abuse.ch
(urlhaus and SSL certs), OpenPhish, as well as Stellar Cyber's Emerging Threat feed.

Premium feeds include Cybersixgill, Anomali ThreatStream, RedSense, Recorded
Future, SOCRadar, CrowdStrike, and ESET. They are provided by Stellar Cyber. You
configure them in TIP with credentials that you purchase.

Custom feeds include TAXII and TSV. You configure them in TIP with credentials that
you provide, for example, credentials for a TAXII server or credentials to access a TSV
file.

To manage IoCs, see Managing IoCs in the Threat Intelligence Platform.

To configure and manage Feeds, see Configuring Feeds in the Threat Intelligence Platform.

To manage role-based access control at the System level, see Configuring Role-Based Access
Control.

 The Threat Intelligence Platform (TIP) is configured globally for an organization.

Architecture
The following simplified architecture diagram shows the user interface (UI), Threat Intelligence
(TI) Controller, and TI Engine.

The user interface sends data to the TI Controller through the TI Feeds API. The TI Controller
performs management of the feeds for the TI Engine. Feeds management includes actions such
as, Create, Delete, Enable/Disable, as well as the configuration of feeds.

The solid lines in the diagram are for control flow and the dotted lines are for data flow. For
example, the UI communicates with the TI Engine to fetch and push IoCs, and for other
operations, such as import and export of IoCs.

All the feeds run periodically to push IoCs. The interval period is configurable for Premium and
Custom feeds.

The IoCs from the feeds are used in the enrichment of Stellar Cyber's Interflow records, such as
for reputation.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

