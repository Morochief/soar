✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Stellar Cyber 6.6.0s Release Notes
Software Release Date: June 25, 2026
Release Note Updated: June 26, 2026
The Stellar Cyber 6.6.0s release delivers the following updates to the Stellar Cyber Open XDR
platform.
The release notes are organized into the following sections:
Highlights
Actions Required
Behavior Changes
Deprecated Features
Autonomous SOC
Detection/ML
Stellar Cyber Platform
Sensors
Connectors
Parsers
Usability
Early Access Program
Resolved Issues
Known Issues
Highlights
Autonomous SOC / Auto Triage
AI Assistant (Early Access Program): Added AI Assistant to every automatically triaged
case so you can investigate cases and alerts in plain language, asking why a case
received its verdict, clarifying alert details, and exploring follow-up hypotheses against

the case data and Verdict Signal Check (VSC) context that Auto Triage has already
assembled.
Auto Triage Verdict Visibility: Auto Triage verdicts now appear as filterable columns in
the Alert Table and Threat Hunting views. In addition, a response action panel was
added to the Auto Triage alert page (including phishing email alerts) so analysts can
see and act on triage outcomes without opening individual cases.
System / Platform
Platform Health Monitoring in the System Action Center (Early Access Program):
Centralized platform health monitoring alerts in the System Action Center for improved
visibility and faster response to platform issues.
License Enforcement and Usage Notifications: Added API actions for license
enforcement and usage notifications.
Detections/Machine Learning
Improved Login Anomaly Fidelity: Alert suppression for Impossible Travel Anomaly
and User Login Location Anomaly is now customizable, Impossible Travel prioritizes
records with usernames, and ASN enrichment fields were added to Impossible Travel
Anomaly alerts.
Improved User Counting Accuracy: Improved the accuracy of license user counting
by integrating external data sources for Microsoft Entra ID.
Integrations
New Integrations: Added Liongard integration for cyber asset attack surface
management, the Ironscales connector for incident ingestion, and response actions for
Check Point Smart-1 Cloud Management.
Usability
Watchlists for All Alert Fields: Enabled Add to Watchlistfor all alert fields.
Selective Parser Port Activation: Parser ingestion ports can now be enabled on-
demand and parsers added after 6.5.0 are inactive by default, reducing false alerts from
unused listeners.
Actions Required
There are no actions required in this release.
Behavior Changes
Changes that affect the way users interact with the product or interpret results are listed below.
DATA-3412: The totalbytes field in the Fortinet FortiAnalyzer parser is now calculated
as the sum of inbytes_total and outbytes_total, consistent with how other parsers
calculate this field. Previously, the FortiAnalyzer parser calculated totalbytes as the
sum of inbytes_delta and outbytes_delta, which significantly underreported
session volume when delta values differed from totals. Dashboards, detections, or

queries that rely on totalbytes from FortiAnalyzer data may return different values
after this change.
AELDEV-71104: Built-in legacy parsers added in 6.5.0 and later releases are now
inactive by default for new tenants and must be explicitly activated in Parser Studio
before use. Previously added legacy parsers retain their existing active status and are
not affected by this change. You can activate or deactivate any individual parser at any
time from Parser Studio, and the configuration is applied to sensors on the next
deployment.
AELDEV-64683: The Google Workspace log collector no longer maps the
metadata.customerId field to user.id. The customerId value is a Google account
identifier for the organization, not a user identifier, so this mapping was incorrect and
caused confusion in alert context. Existing events already indexed with this
normalization are not affected. Newly ingested Google Workspace events no longer
populate user.id from this field.
Deprecated Features
There are no deprecated features in this release.
Autonomous SOC
Improvements
ASOC-142: Added Auto Triage verdict columns to the Alert Table and Threat Hunting views.
Added Auto Triage verdicts as columns to both the Alert Table and Threat Hunting views,
enabling visibility and filtering of verdicts such as True Positive and False Positive. You can
now see triage outcomes directly in these views without navigating to individual cases,
improving the workflow efficiency for alert analysis.
Detection/ML
Improvements
AELDEV-68980: Improved External/Internal Suspected SQL Injection alert types.
Improved External/Internal Suspected SQL Injection alert types by adding a Key Field listing
suspected queries from the source host observed in the time window. The top 5 are shown
when more than 5 are detected.
AELDEV-68304: Updated the User Login Location Anomaly to prioritize login records that
include a username.
Updated the User Login Location Anomaly to prefer login records that include a username
when multiple records are available for the same login event. Previously, the detection might
use a record containing only a system identifier such as a Windows SID, causing alerts to
display an unreadable identifier instead of a username. User Login Location Anomaly alerts
now display a recognizable username when one is available in the correlated login data.
Existing prioritization of Entra ID and MFA records continues to take precedence over this
change.

AELDEV-68301: Added ASN enrichment fields to Impossible Travel Anomaly.
Added srcip2_asn and srcip2_asn_org fields to the Impossible Travel Anomaly, exposing
ASN information for the second source IP address. This update lets you use ASN-based
filtering, automation, and alert exclusion logic with Impossible Travel detections.
AELDEV-67315: Added more alert integrations through Microsoft's Graph Security API.
Added 6 alert integrations through Microsoft's Graph Security API. The alert integrations are:
Microsoft App Governance, Microsoft Data Loss Prevention, Microsoft Defender for Identity,
Microsoft Defender for Office 365, Microsoft Entra ID Protection, and Microsoft Threat
Intelligence. See Integration of Third Party Native Alerts.
AELDEV-61011: Improved user counting accuracy for Microsoft Entra ID environments.
Improved user counting accuracy for Microsoft Entra ID environments by reducing duplicate
counts when the same user has multiple email addresses. This update helps make license-
related user counts more accurate.
 This feature is available as part of the Early Access Program (EAP) for customers who
requested it.
AELDEV-59125: Added alert suppression options for Impossible Travel and User Login
Location anomalies.
Added alert suppression options for the Impossible Travel Anomaly and User Login Location
Anomaly when customizing these alert types in the Detection Management System. Select
Attributes for DMS Alert Suppression to set how profile-based alert suppression in the
Detection Management System (DMS) interacts with alerts from the Impossible Travel and
User Login Location anomalies. Previously, alert suppression applied a single scope across all
detections, one alert per user per interval, which caused the global alert suppression to
interact with each detection's own alert suppression in undefined ways. For the Impossible
Travel Anomaly, if Alert Suppression is enabled in DMS with a defined interval (default: 24
hours), the following attributes will rate limit or filter the alerts from this detection: Unique User
and Unique Locations For User. For Unique User, a maximum of one alert per user will be
triggered within the interval set in DMS. This is the previous behavior. For Unique Locations
For User, a maximum of one alert per unique pair of locations per user will be triggered within
the interval set in DMS. There may be multiple alerts for a single user. The User Login
Location Anomaly also has Unique User as well as Unique Location For User, in which a
maximum of one alert per location per user will be triggered within the interval set in DMS. See
Using the Detection Management System.
Stellar Cyber Platform
New Features
AELDEV-68802: Added detailed condition evaluation reasons for array comparisons.
Implemented detailed reason codes for condition evaluation when you use array comparisons.
New reasons include ARRAY_COMPARE_PATH_MISSING, ARRAY_COMPARE_PATH_EMPTY,
ARRAY_COMPARE_SUBPATH_MISSING, ARRAY_COMPARE_QUANTIFIER_NOT_MET, and
ARRAY_COMPARE_MATCH_FOUND. Each reason provides a precise message indicating whether

the condition path was not found, exists without buckets, has no matching values, or matches
with a given quantifier. These reasons help you diagnose mismatches in aggregation query
paths and verify that conditions are functioning correctly.
AELDEV-66618: Enabled OpenAPI 3.1 specification generation for the Auto Triage API.
Enabled OpenAPI 3.1 output for the Auto Triage API. The generated swagger.json conforms to
JSON Schema draft 2020-12 and supports $ref to external schemas. Existing paths and
operations remain unchanged. Access the specification at /swagger.json for integration with
code generators and validation tools. Regenerate software development kit (SDK) artifacts or
update validation tooling to adopt OpenAPI 3.1 features.
AELDEV-66617: Enabled OpenAPI 3.1 specification output for API documentation.
Added OpenAPI 3.1 document generation with JavaScript Object Notation (JSON) Schema
draft 2020-12 compatibility and external $ref support. Models, parameters, and responses
now include expanded type information for more precise validation and client and server
generation. Tools that support only OpenAPI 3.0 must be updated before consuming the
document. You can access the specification at /swagger.json or through the API
documentation page.
AELDEV-62965: Implemented API actions for license enforcement and usage notifications.
Introduced API capabilities to create actions for license enforcement and usage monitoring,
including notifications for exceeding asset and ingestion thresholds. This helps automate
responses and manage licensing effectively through remote APIs.
Improvements
AELDEV-69894: Updated the log collection agent on Modular Sensors to version 1.1.2.
Updated the log collection agent on Modular Sensors to version 1.1.2 to align with the 6.6.0
release. This update includes changes to the build pipeline to ensure compatibility and stability
across deployment environments.
AELDEV-69635: Updated timestamps in Last Scheduled Run and Last Manual Run to
reflect actual execution times.
Updated the timestamps shown in Last Scheduled Run and Last Manual Run so they reflect
when the playbook check, condition evaluation, and actions actually occurred rather than the
scheduled run time. This change makes run details more accurate and improves
troubleshooting, auditing, and status review.
AELDEV-62593: Clarified system diagnostics availability in Report | Observability
dashboards.
Clarified the availability of system diagnostics in Report | Observability. Dashboards in this
section present system information, health status, and configuration indicators for monitoring
platform operations. You can review ingestion metrics, sensor status, and configuration signals
using filters such as Time Range, Data Source, and Category. No configuration change is
required.
Sensors

New Features
AELDEV-71145: Added Fedora Linux 40 support for the Linux Server Sensor.
Added support for installing the Linux Server Sensor on Fedora Linux 40 and later. Previously,
the installer did not apply the required compatibility libraries on Fedora 40, causing sensor
services to fail to start after installation. The installer now correctly handles Fedora 40 and
later releases using the same compatibility library approach used for other supported Red Hat-
based platforms.
AELDEV-70754: Added Oracle Linux 10 support for the Linux Server Sensor.
Added support for installing the Linux Server Sensor on Oracle Linux 10. Systems running
Oracle Linux 10 can now connect to Stellar Cyber and begin collecting data without requiring
additional configuration changes.
Improvements
AELDEV-68328: Updated the DPI protocol bundle to version 1.830.0-21 for enhanced traffic
analysis.
Updated the Deep Packet Inspection (DPI) protocol bundle to version 1.830.0-21. This update
adds support for extracting prompts from decrypted traffic associated with AI tools such as
ChatGPT, Copilot, and Claude, enabling more detailed traffic categorization and analysis for
these platforms. The DPI engine version remains at 5.10.0-47.
AELDEV-64505: Upgraded Suricata to version 8.0.1 to address multiple vulnerabilities.
Upgraded Suricata to version 8.0.1, which resolved vulnerabilities related to the handling of
entropy, ldap.responses.attribute_type, and tls.subjectaltname keywords, and detection
bypass issues. These updates enhance stability and security by rectifying segmentation fault
and buffer overflow occurrences in earlier versions.
AELDEV-58588: Secured UDP socket communications in local services to prevent
unauthorized access.
Secured internal socket communications used by sensor services on Linux Server Sensor
(agent) deployments. Previously, these communications used unauthenticated connections,
which could allow non-privileged users on the host server to perform unauthorized actions
such as restarting services or triggering upgrades. Local service communications now require
authentication, ensuring that CLI commands and service operations are accessible only to
authorized users.
Connectors
New Features
AELDEV-61583: Introduced the Check Point Smart-1 Cloud connector.
Added the Check Point Smart-1 Cloud firewall connector. This responder supports
blocking/unblocking IP addresses across gateways managed by Check Point Smart-1 Cloud
by manipulating host objects and groups referenced in firewall access policies. See
Configuring Check Point Smart-1 Cloud Connectors.
AELDEV-61569: Introduced the Liongard connector.

Added the Liongard connector to ingest devices, detections, and identities data though the
Liongard API. See Configuring Liongard Connectors.
AELDEV-46279: Introduced the Ironscales connector.
Added the Ironscales connector to query data related to incidents through the Ironscales
Management API. See Configuring Ironscales Connectors.
Improvements
AELDEV-69891: Huntress connector fix for mapping exception.
Fixed a mapping exception that caused Incident Reports promoted to alerts to be dropped
from the Assets index for the Huntress connector. The
huntress.remediations.items.parameters is now correctly parsed as an array of objects
instead of text.
AELDEV-69470: Implemented mapping of azure_ad.ipAddress to src_ip in Service
Principal Sign-in Logs.
Added normalization to map azure_ad.ipAddress to src_ip in Service Principal Sign-in
Logs. This update enables consistency with other log types and supports additional ML
detections, such as detecting sources with bad source reputations.
AELDEV-69160: Mapped the Structured Azure Firewall Log content type to the Traffic index.
In Azure Event Hub , mapped the Structured Azure Firewall Log content type to the Traffic
index, aligning its behavior with the legacy Azure Firewall content type.
AELDEV-68502: Added a query_window_start field to Microsoft Office 365 connector
events.
Added a query_window_start field, which is a timestamp added to all Microsoft Office 365
connector events. It records the start of the polling window during which Stellar Cyber
collected the event from Microsoft's API, reflecting when Microsoft made the event available
for retrieval. The field is stored as a Unix timestamp in milliseconds in the raw event, and is
displayed as a datetime object in the Stellar Cyber user interface. The query_window_start
field is consistent with existing fields such as timestamp and write_time. See Configuring
Office 365 Connectors.
AELDEV-68427: The srcip field is now populated in Palo Alto Networks CORTEX XDR
endpoint events.
Corrected population of the srcip field in the Palo Alto Networks CORTEX XDR connector.
Endpoint events that include a source IP now populate the srcip field, enabling generation of
Assets for the Endpoints content type.
AELDEV-66221: Enhanced the OCI connector to normalize Apache logs streamed via the OCI
log stream.
Normalized Apache HTTP Server logs from Oracle Cloud Infrastructure (OCI) to standard
fields. The originating client IP is normalized to srcip so that further enrichment can be
performed, such as geolocation and threat intelligence reputation.
AELDEV-65062: Upgraded OAuth library for the Sophos Central connector to support the
Sophos API.

Updated the OAuth library for the Sophos Central connector to a newer version for
compatibility with the Sophos API.
AELDEV-64683: Removed an incorrect user id mapping for Google Workspace events.
Removed mapping from metadata.customerId to user.id for Google Workspace events.
Previously, the organization identifier from metadata.customerId could populate user.id,
which made tenant information appear as if it were a user identifier. Now, user.id is
populated only when an actual user identifier is present; otherwise, it remains empty.
AELDEV-52408: Added API Token authentication for the Universal Webhook Responder.
Added an authentication method called Stellar Cyber API Token to the Universal Webhook
Responder, in addition to Basic, OAuth2, and Header authentication methods. For the Stellar
Cyber API Token, enter Hostname, Port, and Protocol, then enter a Platform URL (the public
Application Programming Interface endpoint) and an API Token (the user-scoped API key).
See Configuring Universal Webhook Responder Connectors.
Parsers
New Features
DATA-3472: Introduced a parser for ingesting Radware WAF logs.
Added a built-in parser for ingesting Radware WAF logs in JSON format on port 6208. The
parser extracts web application firewall event fields including source IP addresses, destination
hosts, attack names, threat categories, rule identifiers, and application details. This parser
improves visibility into web application attack activity and supports investigation of threat
events and policy enforcement.
DATA-3464: Introduced a parser for ingesting ManageEngine Endpoint Central logs.
Added a built-in parser for ingesting ManageEngine Endpoint Central logs in RFC 5424 syslog
format on port 6203. This parser extracts endpoint management event data including endpoint
identifiers, event categories, and activity details. This parser improves visibility into endpoint
management activity and supports investigation of endpoint configuration and compliance
events.
DATA-3453: Introduced a parser for ingesting Safetica Data Loss Prevention logs.
Added a built-in parser for ingesting Safetica Data Loss Prevention (DLP) logs in RFC 5424
syslog format on port 6202. This parser extracts DLP event fields including event ID, type,
user, computer, rule name, and event details. This parser improves visibility into data loss
prevention activity and supports investigation of policy violations and user behavior related to
sensitive data.
DATA-3447: Introduced a parser for ingesting ONV Switch logs.
Added a built-in parser for ingesting ONV Switch logs in RFC 5424 syslog format on port
6100. This parser extracts switch event data including source and destination IP addresses,
ports, and protocol information. This parser improves visibility into ONV Switch network activity
and supports traffic analysis and investigation.
DATA-3445: Introduced a parser for ingesting Oracle Audit Trail logs.

Added a built-in parser for ingesting Oracle Audit Trail logs in JSON format on port 6204. This
parser extracts database audit fields including user identity, database actions, and affected
objects. This parser improves visibility into Oracle database activity and supports investigation
of privileged access, schema changes, and data access events.
DATA-3438: Introduced a parser for ingesting Forcepoint Web Security logs.
Added a built-in parser for ingesting Forcepoint Web Security (Filebeat) logs in RFC 5424
syslog format on ports 6101–6201. This parser extracts web security event data including
source IP addresses, ports, and web security category information. This parser improves
visibility into web traffic filtering activity and supports investigation of policy enforcement and
blocked request events.
DATA-3431: Introduced a parser for ingesting Trend Micro Worry-Free Business Security
Service logs.
Added a built-in parser for ingesting Trend Micro Worry-Free Business Security Service logs in
CEF format with a custom header on port 6209. The parser extracts endpoint security event
fields including threat detections, source and destination IP addresses, ports, protocols, rule
names, actions, and device identifiers. This parser improves visibility into endpoint security
activity and supports investigation of threat events and policy enforcement across managed
endpoints.
DATA-3425: Introduced a parser for ingesting Avaya IP Office logs.
Added a built-in parser for ingesting Avaya IP Office logs in RFC 3164 syslog format on port
6099. This parser extracts VoIP event data including source IP addresses, ports, and call
activity information. This parser improves visibility into Avaya IP Office telephony activity and
supports traffic analysis and investigation of VoIP events.
DATA-3424: Introduced a parser for ingesting Custom Application JumpTo logs.
Added a built-in parser for ingesting Custom Application JumpTo logs in JSON format on port
6098. This parser extracts application event data including source IP addresses, ports, and
session activity. This parser improves visibility into JumpTo application activity and supports
traffic analysis and investigation.
DATA-3409: Introduced a parser for ingesting Cowrie SSH/Telnet Honeypot logs.
Added a built-in parser for ingesting Cowrie SSH/Telnet Honeypot logs in JSON format on port
6206. The parser extracts honeypot event fields including attacker source IP addresses, event
types, session identifiers, captured credentials, and commands entered during sessions. This
parser improves visibility into honeypot activity and supports investigation of unauthorized
access attempts and attacker behavior.
DATA-3398: Introduced a parser for ingesting Kaspersky Secure Mail Gateway logs.
Added a built-in parser for ingesting Kaspersky Secure Mail Gateway logs on port 6205. This
parser extracts email security event data including sender and recipient information, threat
classifications, and policy actions. This parser improves visibility into email security activity
and supports investigation of malware detections, spam filtering, and blocked message
events.
DATA-3373: Introduced a parser for ingesting Fudo Privileged Access Management logs.

Added a built-in parser for ingesting Fudo Privileged Access Management (PAM) logs in RFC
3164 syslog format on port 6096. This parser extracts PAM event data including user identity,
session activity, and access details for privileged account operations. This parser improves
visibility into privileged access activity and supports investigation of administrative sessions
and access policy enforcement.
DATA-3372: Introduced a parser for ingesting Ubika Web Application Firewall logs.
Added a built-in parser for ingesting Ubika Web Application Firewall (WAF) logs in RFC 5424
syslog format on port 6097. This parser extracts WAF event data including source IP
addresses, ports, HTTP methods, and web security category information. This parser
improves visibility into web application firewall activity and supports investigation of attack
attempts, policy violations, and blocked requests.
Improvements
DATA-3494: Expanded ATH calculation support for the Fortinet FortiWeb parser.
Updated the Fortinet FortiWeb built-in parser to parse the http_request_bytes and
http_response_bytes fields as numeric types rather than strings. The parser previously
emitted these fields as string values, which prevented their use in ATH calculations. They are
now available as numeric fields, letting you use HTTP request and response byte counts in
threshold-based detections and analytics.
DATA-3489: Updated the Microsoft IIS parser to support an extended log field set.
Updated the Microsoft Internet Information Services (IIS) built-in parser to handle log entries
that include an extended field set, in addition to the field layout supported in earlier releases.
The parser extracts source and destination IP addresses, ports, HTTP method, URL, and
response code from both field layouts. The extended field set additionally includes the URI
query string, authenticated username, HTTP referrer, and request and response byte counts,
providing greater visibility into web request patterns and user activity. These additional fields
are now normalized and searchable, supporting more detailed investigation of IIS web traffic.
DATA-3463: Improved Citrix ADC login failure event parsing.
Improved Citrix ADC parser support for login failure events by extracting additional details from
the event description, including the client IP address and username. The update also added
parsing for browser type when present in the log. This enhancement provides better
normalization for Citrix ADC authentication failures and improves investigation context for user
activity and source attribution.
DATA-3456: Expanded A10 vThunder ADC parser support for additional syslog traffic log
formats..
Expanded the A10 vThunder Application Delivery Controller (ADC) parser to support additional
firewall syslog traffic log formats, including FW-TCP-*, FW-UDP-*, and FW-IC4-* events that
use src_ip:src_port<-->dst_ip:dst_port message patterns and embedded key-value
fields such as ACT (action), RT (timestamp), IN-INTF, OUT-INTF, POLICY, RULE, and DUR
(duration). This update improves parsing and normalization for A10 traffic and session events
so they can be investigated more consistently.
DATA-3451: Updated the Cisco ACI parser to support additional syslog header formats and
event messages.

Updated the Cisco ACI parser to handle additional syslog header patterns for fault, event,
session, and NX-OS–style messages. The update also added support for more Cisco ACI
SYSTEM_MSG event types and improved extraction of details from events such as VMware
controller connection failures, SOAP login errors, job status changes, NTP faults, and fabric
link changes. This improvement helps ensure that more Cisco ACI logs are parsed and
normalized correctly for investigation.
DATA-3449: Updated the Arbor Peakflow SP parser to support additional syslog header
formats and event message patterns.
Updated the Arbor Peakflow SP parser to handle additional syslog header variants, including
RFC 3164, RFC 5424, and Arbor custom header formats. The update also added support for
more Arbor event message patterns and improved extraction of details from alert lifecycle,
router leadership, interface threshold, flow-count, and configuration change events. This
improvement helps ensure that more Arbor Peakflow SP logs are parsed and normalized
correctly for investigation.
DATA-3439: Added Snort intrusion event log support to the KVH CommBox Edge Gateway
parser.
Extended support to include Snort-formatted intrusion event logs in the KVH CommBox Edge
Gateway parser. The update parses Snort alert identifiers, message text, Classification,
Priority, protocol, and source and destination IP address and port information, including
repeated-message wrappers. This improvement helps ensure that Snort detection events
forwarded by KVH CommBox Edge Gateway devices are parsed and normalized correctly for
investigation.
DATA-3437: Moved fields from msg_data to the vendor field in the Fortinet FortiAnalyzer
parser.
Moved additional Fortinet FortiAnalyzer parser fields from msg_data into the Fortinet vendor
field namespace. This update improves field organization and makes those Fortinet-specific
values easier to access consistently during search, analysis, and downstream content
development.
| advpnsc     | dstserver       | init         | rcode        |
| ----------- | --------------- | ------------ | ------------ |
| bandwidth   | dstswversion    | lease        | role         |
| cloudaction | error           | masterdstmac | setuprate    |
| clouduser   | espauth         | mem          | srcfamily    |
| cpu         | esptransform    | mode         | srchwversion |
| dhcp_msg    | exch            | nas          | stage        |
| dir         | faclogindex     | newvalue     | sysuptime    |
| disk        | fazlograte      | oldvalue     | totalsession |
| disklograte | freediskstorage | out_spi      | useralt      |
| dstdevtype  | healthcheck     | peer_notif   | userip       |
| dsthwvendor | in_spi          | probeproto   | waninfo      |
| dstosname   |                 |              |              |
DATA-3427: Improved FortiWeb CEF field mapping in the Common Event Format (CEF)
parser.
Improved the Common Event Format (CEF) parser for FortiWeb logs by promoting recognized
FortiWeb extension fields to the Fortinet vendor namespace instead of leaving them in generic

message data. This update makes important web application firewall context, such as request
details, client application data, device identifiers, outcomes, and reasons, easier to access
consistently in searches, detections, and investigations.
DATA-3420: Added RFC3164 syslog support to the Penta Security WAPPLES parser.
Added support for RFC 3164-formatted syslog messages in the Penta Security WAPPLES
parser, including key-value log content sent by the web application firewall. This update
improves compatibility with WAPPLES syslog output and helps ensure that more web
application firewall and system monitoring events are parsed consistently.
DATA-3413: Moved the bssid field to the vendor field for the Fortinet FortiGate parser.
Moved the bssid field from the top level into the Fortinet vendor namespace in the Fortinet
FortiGate parser. This update improves field organization by keeping FortiGate-specific
wireless access point information with related vendor fields, which makes the data easier to
interpret and use consistently in searches, content, and investigations.
DATA-3391: Updated the VMware ESXi parser to extract additional authentication event fields.
Updated the VMware ESXi built-in parser to normalize additional fields from authentication-
related log events, including user name, source IP address, login result, and event action.
These fields were previously unparsed and unavailable for search or investigation. They are
now normalized and searchable, improving visibility into ESXi authentication activity and
supporting investigation of login events and access patterns.
DATA-3371: Added BSD syslog format support for the Citrix ADC parser.
Added support for BSD syslog-style headers in the Citrix ADC parser, including logs that use
DD/MM/YYYY:HH:MM:SS GMT timestamps instead of RFC 5424 headers. This update improves
compatibility with Citrix ADC SSLVPN session and connection statistics logs, such as
TCPCONNSTAT and UDPFLOWSTAT, so those events can be parsed more reliably for access
monitoring and troubleshooting.
DATA-3365: Enhanced Efficient IP parser to prevent potential BufferOverflow issues.
Updated the Efficient IP parser with enhancements to improve performance and prevent
potential BufferOverflow conditions. These changes include time parser optimizations for GC
efficiency, expanded regex for client IP matching to capture non-standard IP formats, and
improved record normalization processes. Support for correct base class initialization logic
was added to align parser behavior with the implemented processing paths. These updates
address performance and normalization requirements, effectively reducing risk without
compromising processing integrity.
DATA-3355: Added JSON-over-HTTP Kubernetes log support to the HTTP Google Kubernetes
Engine parser.
Added support for a new HTTP-ingested JSON log format in the HTTP Google Kubernetes
Engine parser, including Kubernetes container logs forwarded with nested docker and
kubernetes metadata. This update improves compatibility with Google Kubernetes Engine log
payloads so container, pod, namespace, host, and image context can be ingested more
reliably for Kubernetes monitoring and investigation.
DATA-3351: Added blocked-host threat log support to the Arbor Peakflow SP parser.

Added support for an additional Arbor Peakflow SP log format used for blocked-host threat
events generated by arbor-networks-aps. The update adds parsing for ATLAS threat-
category logs and extracts related threat context, including threat name, threat category,
protection group details, match type, and reference identifiers. This improvement helps
surface Arbor blocking and reputation activity more clearly.
AELDEV-72115: Added a required field validation message for the Custom Namespace field in
Parser Studio.
Added a "This field is required" validation message for the Custom Namespace field in Parser
Studio when it is left empty.
AELDEV-72105: Added Raw Log Capture support for modular parsers in Parser Studio.
Added Raw Log Capture support for modular parsers in Parser Studio, aligning modular
parser capabilities with the existing feature set available for legacy parsers.
AELDEV-71516: Removed the HTTP JSON parser from Parser Studio.
Removed the HTTP JSON parser from the Parser Studio parser list. The HTTP JSON parser
continues to use a sensor profile configuration and is not managed through Parser Studio.
AELDEV-71104: Set new built-in parsers added in 6.5.0 and later to inactive by default.
Built-in legacy parsers added in 6.5.0 and later releases are now inactive by default for new
tenants and must be explicitly activated in Parser Studio before use. Previously added legacy
parsers retain their existing active status and are not affected by this change.
AELDEV-70853: Updated the CLI command to show readable names for modular parser
activity counters.
Updated the show logforwarder CLI command to show readable names for modular parser
activity counters. When you view parser activity in the command output, input counts now
display the parser name and output counts now display the index name instead of internal
identifiers. This update makes it easier to understand which modular parsers are receiving
data and where that data is being sent.
AELDEV-68064: Updated the Parser Studio UI to support enabling parser ports on demand.
Updated the Parser Studio user interface to support enabling and disabling parser ports on
demand. This capability is available to all users, while the broader Early Access Program-only
Parser Studio features for creating and managing custom parsers remain limited to customers
participating in the Early Access Program.
AELDEV-67224: Added input and output record counters for modular parsers, reported
through the CLI.
Added statistics to the show logforwarder command for modular parsers, including input
record counts aggregated by parser and output record counts aggregated by index. This
update extends CLI visibility to modular parser pipelines and reports counters for input and
output activity. It helps you validate log flow more quickly, confirm parser health, and identify
configuration issues or dropped-record conditions.
AELDEV-66922: Added automatic and manual timestamp normalization options in Parser
Studio.

Enhanced the Normalization step in Parser Studio to support the automatic detection and
normalization of multiple timestamp formats, including epoch in seconds and milliseconds, ISO
8601, and other common date and time string formats. A manual override option was added
that lets you specify the timestamp field and format when automatic detection does not
produce the expected result. This update improves timestamp handling accuracy and helps
ensure that ingested events appear at the correct time in the Stellar Cyber Platform.
AELDEV-56360: Enabled selective parser port activation to reduce false alerts.
Enabled selective activation and opening of parser ports per tenant.You can now choose
which parser ports are active in Parser Studio, which helps prevent unwanted data from being
ingested and reduces false alerts caused by unused listeners.
Usability
New Features
AELDEV-68843: Fixed an issue that caused manually triggered rules to be incorrectly marked
as inactive failures.
Resolved an issue in which manually triggered rules were incorrectly shown as inactive
failures in their status display. Manual trigger statuses are now recorded accurately and reflect
the actual input status.
AELDEV-68524: Added new platform health alerts to the System Action Center.
Integrated platform monitoring alerts into the System Action Center to improve early detection
and response coordination. Alert types include ingestion drops, authentication errors, and
cluster health issues. Alerts include severity values, support filtering by time range, severity,
and type, and can be enabled or disabled individually per tenant. Alert records are retained for
at least 30 days.
 This feature is available as part of the Early Access Program (EAP).
AELDEV-65225: Enabled Add to Watchlist for all alert fields.
Removed the field restriction and enabled Add to Watchlist for all alert fields. You can now
select any value in Alerts | Alert Detail and add it to a watchlist. Supported types include IP,
Domain, URL, Hash, Hostname, and Username. Fields such as host.ip and
dns.question.name now qualify automatically. Entries that do not match the selected type
display a validation message.
AELDEV-64450: Added a filtered JSON attachment to ATH calculation rule alert notifications.
Added the option to attach a JSON-formatted file containing filtered calculation results to alert
notification emails that ATH calculation rules generate when triggered. The JSON attachment
contains the same filtered records as the CSV attachment, limited to entries that meet the
calculation condition threshold. Including the results as an attachment in JSON format lets you
process or integrate ATH calculation results programmatically in addition to reviewing them in
spreadsheet format.
AELDEV-57363: Updated auto-triaged alert details with a redesigned view.

Updated the auto-triaged alert details view with a redesigned layout that preserves existing
alert information and investigation workflows. The updated view continues to provide access to
key fields, details, JSON view, rules, and comments and activity, while adding new Auto Triage
sections such as a Simple Summary and Findings to make results easier to review.
AELDEV-53674: Added a response action panel on the Auto Triage alert page.
Added a response action panel to the Auto Triage alert page. You can initiate supported
response actions directly from an alert without leaving the triage view. Available actions match
the response actions configured through your current integrations. Action execution records
appear on the Activity page for audit and follow-up.
Improvements
AELDEV-72095: Added new PDF export options to the Exported Dashboards schedule form.
Added new options to the Exported Dashboards schedule form in Reports. A new Default
PDF type is now available, along with new fields for PDF Table Size and CSV Table Size
(visible when CSV export is enabled), and a Color Charts option for selecting PDF chart color
palettes.
 This feature is available as part of the Early Access Program (EAP).
AELDEV-72021: Updated the Dashboard Share dialog to use tenant and tenant group badges.
Updated the Dashboard Share dialog to display tenant and tenant group identifiers using
design-system badges instead of a plain text "[Tenant]" prefix.
AELDEV-71898: Improved feedback for time series visualization widgets in dashboards when
a data volume limit is reached.
Updated time series visualization widgets in dashboards to display a clear indicator when
query results exceed the volume that the widget can process for the selected time range.
Previously, widgets silently rendered partial data without indicating that results were
incomplete, which could give a misleading view of the selected time period. Widgets now
communicate when a data limit has been reached, helping you identify when query
adjustments or a shorter time range are needed for accurate results.
AELDEV-67591: Updated the Case Detail page to preserve existing functionality in a
redesigned experience.
Updated the look and feel of the Case Detail page to preserve existing functionality in a
redesigned experience. The Associated Alerts table now includes Quick Filters while also
preserving previous features.
AELDEV-67377: Added quick filters for enriched and non-enriched fields in alert details.
Added quick filters to alert detail views that let you display only enriched fields, only non-
enriched fields, or all fields. This helps you distinguish original detection data from enrichment
data added later, supporting clearer triage and communication.
Early Access Program

If you're interested in testing out new features ahead of general availability, consider joining the
Early Access Program (EAP) by contacting your Stellar Cyber Customer Success representative
and telling them which EAP feature you want to test. Once you've agreed to the EAP terms and
signed up, the EAP feature is unlocked for you.
The purpose of this program is to boost performance and reliability through real-world customer
insights, giving you a hands-on role in shaping a Stellar Cyber feature. In return, you'll receive
early access to upcoming releases and the chance to guide product development.
The following EAP features are in this release:
AI Assistant
AI Assistant is a natural-language investigation workbench built into every automatically triaged
case. It converts your plain-language questions into answers grounded in the specific case data,
alert details, and Verdict Signal Check (VSC) context that Auto Triage has already gathered.
While the automated verdict tells you what Stellar Cyber concluded, AI Assistant explains why,
and it supports follow-up questions in your own words, with no query syntax to learn. AI Assistant
is included with every Auto Triage license at no additional cost and is available on SaaS
deployments only.
Exportable Dashboards — Report Integration
Exportable Dashboards lets you schedule dashboards created with the Dashboard Builder as
recurring PDF reports. The schedule form includes a new Default PDF type that renders the
dashboard as it appears in the Dashboard Builder, along with options to control table row counts,
chart color palettes, and optional CSV exports. This capability lets you generate consistent,
configurable reports from new dashboards while preserving the settings and PDF types used by
existing scheduled reports.
MCP Server
The Stellar Cyber MCP Server connects supported AI clients to the Stellar Cyber Platform
through the Model Context Protocol (MCP). The MCP server lets AI clients retrieve case and
alert data, review investigation context, perform tenant-aware operations, and update selected
case fields. This capability helps teams extend AI-assisted investigations by giving approved
clients structured access to operational security data and workflows.
Parser Studio
Parser Studio lets you create and manage custom log parsers for data ingestion by cloning
existing parsers, testing parser behavior before deployment, and activating parsers for
production use. This capability helps you accelerate onboarding of custom log sources while
reducing parser development effort and improving validation before live ingestion.
XDR Connector Webhook Ingestion
This is a simple webhook framework that lets you post JSON data directly from any external
system into Stellar Cyber, accelerating custom integrations and expanding your visibility across
the entire security stack. The XDR Connector is in Public Preview in this release.
Customizable Case Correlation Strategies

This EAP feature introduces support for multiple case correlation strategies, allowing teams to
evaluate and experiment with different approaches to grouping alerts into cases. Each strategy
provides a distinct investigative perspective:
Attacker-Centric Correlation groups alerts by the source (attacker) host, making it
easier to track adversary behavior across multiple targets.
Victim-Centric Correlation organizes alerts by the destination (victim) host, enabling
focused protection and visibility on high-value assets.
Multi-Entity Correlation links alerts across interconnected hosts and actions to form a
single case, offering a holistic view of extended or lateral attack campaigns.
This flexibility enables security teams to tailor investigations based on their operational priorities
—whether that’s identifying persistently targeted endpoints, tracing threat actor movements, or
capturing full-scale intrusion campaigns.
Alert for Suspicious OCI Tenant-to-Tenant Communication
This EAP feature introduces a new alert type that detects cross-tenancy communications in the
Oracle Cloud Infrastructure (OCI). By analyzing tenantId fields in audit logs, the feature identifies
requests that target resources in a different tenancy. This provides accurate visibility into
potentially unauthorized cross-tenancy activity and strengthens oversight in OCI environments.
To join the Early Access Program and begin testing these features, contact your Stellar Cyber
Customer Success representative.
Resolved Issues
The following issues have been resolved in this release.
DATA-3313: Fixed an issue that caused the CEF parser to drop user agent information from
Check Point logs.
Fixed a normalization issue in the CEF parser that prevented the user_agent field in Check
Point logs sent to port 5143 from being retained in parsed data. The issue occurred because
the previous normalization logic did not correctly handle mapping user_agent to
user_agent.original. After this fix, logs that include user_agent preserve the value
correctly so it remains available for investigation and search.
DATA-3312: Resolved incorrect quote handling by the Netscaler parser.
Resolved a parsing issue in the Netscaler parser that incorrectly removed double quotation
marks contained within the command field value. The parser now preserves quotation marks
that are part of the original command content while still handling wrapper quotation marks
correctly. This fix ensures that parsed command values remain accurate for investigation and
review.
AELDEV-70897: Resolved security vulnerabilities in the Stellar Cyber CLI that allowed
privilege escalation.
Resolved three security vulnerabilities in the restricted CLI shell on Data Processor
deployments. An authenticated CLI user could reach unprotected code paths that allowed
operating system commands to run with elevated privileges. A local service interface was also
reachable without authentication, providing an additional path to execute arbitrary commands.

All three attack paths have been closed, and the restricted CLI shell now enforces access
controls consistently across all commands and interfaces.
AELDEV-70855: Fixed an issue that caused Windows Server Sensor uninstall tasks to remain
stuck in progress.
Resolved a task status tracking issue in which uninstall tasks for Windows Server Sensors
remained indefinitely in an In Progress state even after the sensor had successfully
uninstalled. The sensor was not sending a required identifier in its completion message, so the
Central Manager could not match the response to the original task and never updated its
status. Uninstall tasks now complete and reflect the correct status after the sensor is removed.
AELDEV-70728: Fixed issues that left residual files and incorrect package status after
uninstalling a Linux Server Sensor.
Resolved two related issues that occurred after you uninstalled a Linux Server Sensor from
the Stellar Cyber Platform UI. The sensor software directory was not fully removed, leaving
files on disk after the uninstall completed. Additionally, the system package database
continued to show the sensor package as installed rather than reflecting its removed state.
Both issues have been corrected: the sensor directory is now fully removed on uninstall, and
the package status correctly reflects the uninstalled state.
AELDEV-70629: Fixed an issue that caused sensor upgrades to stall indefinitely on Modular
Sensors running Ubuntu 22.04.
Resolved an upgrade issue on Modular Sensors running Ubuntu 22.04 in which the upgrade
process stopped responding and never completed. The upgrade stalled while attempting to
remove a legacy package repository reference that required contacting an external server. If
the sensor had limited or no access to that server, the process waited indefinitely, leaving most
sensor services down and the upgrade showing no result. The upgrade process no longer
waits indefinitely on this step and completes correctly.
AELDEV-70608: Fixed an issue that caused support sessions to close uncleanly when an
elevated shell was open.
Resolved a session management issue on on-premises Data Processor deployments. When a
timed support session expired while you had an elevated root shell open, the session did not
close cleanly. Instead, the CLI and the root shell interleaved, producing repeated error output
on every keystroke and preventing you from exiting normally. Support sessions now terminate
cleanly regardless of whether an elevated shell is active when the session expires.
AELDEV-70360: Resolved a security vulnerability in the PackageKit component on Ubuntu
22.04 sensors.
Resolved CVE-2026-41651, a security vulnerability in the PackageKit component present on
sensors running Ubuntu 22.04. The installed version of PackageKit fell within the affected
range, and the patched version was not available through the previously configured update
source. The sensor package has been updated to include the patched version, and sensors
can now apply the fix using the exec cve patch CVE-2026-41651 CLI command.
Vulnerability scanners such as Tenable and Qualys no longer flag this CVE on updated
sensors.

AELDEV-70298: Fixed an issue that caused file inspection on Modular Sensors to stop
capturing traffic.
Resolved an issue in which the file-inspection pipeline on Modular Sensor deployments
stopped capturing and analyzing files. The issue occurred because a build configuration error
caused Suricata to use an inefficient pattern-matching method that consumed excessive
memory, eventually causing the capture process to stop. Newly built sensors now include the
correct configuration, allowing file inspection to operate reliably within expected memory limits.
AELDEV-70296: Fixed a missing CLI command for viewing the external syslog server on
Modular Sensors.
Resolved an inconsistency in which the show logforwarder external-server command
was available on Network Sensors and Security Sensors but not on Modular Sensors. If you
configured an external syslog forwarding server on a Modular Sensor, you had no way to
verify the configuration from the CLI. The command is now available on Modular Sensors and
returns the configured external server address as expected.
AELDEV-70247: Fixed an issue that caused deleted InSync configurations to remain visible on
the Alerts page.
Resolved a display issue in which InSync configurations you had deleted continued to appear
on the Alerts page even after they had been successfully removed. The Alerts page was
retrieving InSync status data from a source that was not updated on deletion, so removed
entries continued to show with a Paused status. Deleted InSync configurations no longer
appear on the Alerts page after you remove them.
AELDEV-70104: Fixed a file inspection issue with back-to-back NFSv3 transfers.
Resolved an issue in which the file-inspection pipeline produced incorrect results when you
transferred two files over a Network File System (NFS) share in rapid succession using
NFSv3. The second file was not fully captured, resulting in an incomplete scan and an
incorrect file hash. NFSv4 transfers were not affected because that version handles file
boundaries differently. The fix ensures each file is inspected completely and independently
regardless of how quickly transfers follow one another.
AELDEV-69759: Fixed a memory issue that caused repeated crashes on memory-constrained
sensors.
Resolved a memory management issue on sensor deployments where available RAM was
limited, particularly on 8 GB hosts. Under sustained load, memory consumption across sensor
services exceeded available memory, causing traffic inspection to crash and restart
repeatedly. Sensors on VMware ESXi hosts were additionally affected when the hypervisor
reclaimed guest memory under host-level pressure. Memory limits are now calculated
dynamically based on the available RAM of the host, preventing the crash cycle and keeping
traffic inspection running reliably.
AELDEV-69389: Corrected an issue that prevented typed tags from being applied in bulk case
actions.
Resolved a bulk case action issue in which a typed tag was not applied if you selected Apply
without first confirming the entry. The tag input is now committed before the bulk action

request is sent, so the complete tag list is applied to the selected cases. Existing tag
workflows that use Enter or an autocomplete selection continue to work as before.
AELDEV-69116: Improved Modular Sensor stability and throughput under high traffic loads.
Resolved multiple performance issues on Modular Sensor deployments that caused traffic
inspection to degrade or fail under sustained high traffic. Under heavy load, processing
threads competed for resources inefficiently, memory usage grew in a cycle that repeatedly
disrupted normal operation, and sessions were exported without full inspection data. These
issues combined to reduce the amount of traffic the sensor processed reliably. Processing
thread allocation, memory management, and session handling have all been improved,
resulting in more stable operation and significantly higher throughput under high traffic
conditions.
AELDEV-68933: Fixed an issue that caused the Cases API to stop responding when retrieving
case data.
Resolved an issue in which the Cases REST API endpoint stopped responding when a
request included one or more cases in the result set. Requests for case counts and metadata
continued to work normally, but any request that required retrieving actual case records would
never return. This affected users and integrations that relied on the Cases API to retrieve case
data, including SOAR integrations and automated workflows. The API now returns case data
reliably for these requests.
AELDEV-68926: Fixed a data placement issue for tenant indices created during high-volume
onboarding.
Resolved an issue in which indices created for new tenants during periods of high onboarding
activity did not receive the correct storage placement settings. When data arrived for a new
tenant before the regular index creation process completed, the resulting indices were placed
without the required constraints, meaning the data could land on unsuitable nodes. Affected
indices now receive the correct placement settings, ensuring data is stored on the appropriate
nodes as expected.
AELDEV-64142: Removed malware upload commands from sensor types that do not support
malware detection.
Resolved an issue in which the set malware_upload, show malware_upload, and unset
malware_upload CLI commands were visible and available on Network Sensors and Linux
Server Sensors running in agent mode, even though those sensor types do not support
malware detection. Running these commands on unsupported sensor types had no effect and
could cause confusion. These commands are now shown only on sensor types that support
malware detection.
AELDEV-63142: Fixed runtime handling of new log filters in the connector for Azure Event
Hub.
Implemented automatic reload of log filters in the connector for Azure Event Hub. New or
modified filters take effect during active ingestion without a process restart and no longer raise
exceptions.
AELDEV-57819: Fixed an installation error on Amazon Linux 2023 that produced a spurious
error message.

Resolved an issue in which installing a Linux Server Sensor on Amazon Linux 2023 displayed
a "No such file or directory" error during the setup process, even when the installation
completed successfully. The message appeared because the installer attempted to write to a
scheduler configuration file that did not exist on that platform. The installer no longer attempts
this step on Amazon Linux 2023, and the installation now completes without the misleading
error.
Known Issues
AELDEV-72543: Some migrated dashboards might require a manual layout adjustment after
conversion to the new dashboard framework.
Dashboards migrated to the new dashboard framework might display layout differences if they
used highly customized or complex arrangements in earlier releases. This behavior results
from changes in the underlying layout framework. If a migrated dashboard does not retain its
expected arrangement, manually adjust the dashboard layout to restore the intended
presentation.
Upgrading Sensors
Depending on the type of server sensor, you can upgrade your sensors directly to version 6.6.0
from these previous versions:
Linux Server Sensors: 6.4.0 or 6.5.0
Windows Server Sensors: 5.1.0 through 6.5.0
Upgrade the sensors to version 6.6.0 using the following process:
1. Prepare for the upgrade.
2. Upgrade the sensors.
3. Verify the upgrade.
Prepare for the Upgrade
To prepare for the upgrade:
Make sure the sensors are up and running
Take note of the ingestion rate for the sensors to be upgraded in the Sensor Details
page
Make sure the system health indicators in the Sensor Details page all show green.
Upgrade the Sensors
New features, updated ML algorithms, and enhanced configurations may change ingestion and
detection patterns. We recommend the following to ensure a smooth upgrade:
Upgrade sensors with the Sandbox and IDS features enabled before sensors with the
only the Network Traffic feature enabled. Sensors with Network Traffic enabled send
data to sensors with Sandbox and IDS enabled for additional processing.
Upgrade sensors in batches instead of all at once.
For server sensors (agents):
Upgrade a small set of sensors that cover non-critical assets.

After 24 hours, ensure that your ingestion is as expected, then upgrade a
larger set.
After 24 hours, ensure that your ingestion is as expected, then upgrade the
remaining server sensors.
CentOS 7.1 Prerequisite – Update curl to 7.29.0-59.el7_9.2 or Higher
Before upgrading any Linux Server Sensors running in CentOS 7.1, you must check your curl
version and update it to 7.29.0-59.el7_9.2 or higher to use the strong encryption required by
the Stellar Cyber Platform.
1. Check your curl version as shown below:
yum list installed curl
\* Loaded plugins: fastestmirror Loading mirror speeds from cached hostfile
Installed Packages curl.x86_64 7.29.0-19.el7
2. If the listed version is lower than 7.29.0-59.el7_9.2 (as it is in the example above),
use the following commands to update the curl package:
yum makecache
yum install curl
3. If installation of the curl package fails, it is most likely because CentOS is trying to use a
repo that has reached its end of life. Try updating the base URL and then reinstall curl.
The following sed command makes the necessary changes for most environments to
ensure that the updated curl package can be installed:
sudo sed -i.bak -e 's|^mirrorlist=|#mirrorlist=|' -e
's|^#baseurl=http://mirror.centos.org/centos/\$releasever|baseurl=http://arch
ive.kernel.org/centos-vault/7.9.2009|' /etc/yum.repos.d/CentOS-Base.repo
To upgrade sensors:
You can upgrade a sensor to the most recent release from the two previous releases. This
means that you can upgrade a sensor to the 6.6.0 release from any 6.4.x or 6.5.x release.
 If you are upgrading a Windows Server Sensor, complete any pending updates for the host
Windows machine before upgrading the Server Sensor.
1. Select System | DATA SOURCE MANAGEMENT | Sensors | Sensors.
The Sensor List appears.
2. Select Manage | Software Upgrade.
The Sensor Software Upgrade page appears.
3. Choose the target software version.
4. Choose the target sensors.
5. Select Submit.
Verify the Upgrade
To verify that the upgrade was successful:

Check the Software Version in the Sensor List.
Check the Sensor Status LED in the Sensor List.
Check the ingestion rate in the Sensor Details page for upgraded sensors and make
sure it is as expected.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  