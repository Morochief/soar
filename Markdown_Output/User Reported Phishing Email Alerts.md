Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

User Reported Phishing Email Alerts

 The automatic triage of user-reported phishing is only supported on Stellar Cyber in SaaS
deployments and requires an add-on license, which you can request from your sales
representative. If you used this feature through participation in the Early Access Program,
contact your sales representative to continue with an add-on license or to request that the
service be disabled.

User Reported Phishing Email Documents Table

Alert Details Side Panel

Recommended Actions in Response to Email Phishing

Phishing Email Analysis and Risk Scoring

Multi-Factor Evaluation

Standardized Risk Score

Manage Phishing Email Triage

When users report suspicious emails—typically via a "Report Phishing" button in their mail client
—these submissions initiate an automated phishing triage workflow within the Stellar Cyber
Platform. Reported emails are first collected in a centralized mailbox on your email system,
which then forwards them to a Stellar Cyber–provisioned inbox that's unique to your tenant.

The phishing email triage agent, embedded in the Stellar Cyber Platform, retrieves each reported
email and performs AI-driven analysis to assess its risk. The agent parses the email to extract
observables and enriches them through three sources: its own internal processing logic, direct
integration with the Stellar Cyber Threat Intelligence Platform, and third-party threat intelligence
services. Based on this multi-source analysis, the agent determines a verdict and generates a
structured alert in the Stellar Cyber UI. Each alert includes triage results, a threat score, and
enriched observables—providing your analysts with actionable insight for investigation and
response.

To view these alerts, go to the Alerts page and select View for a User Reported Phishing Email
alert. Stellar Cyber displays the Alert Details page with visual summaries, a detailed documents

table, and an expandable side panel with complete contextual and forensic data. The entries in
this table are individual alerts, each one the result of a user-reported phishing email.

At the top of the Alert Details page, four visual widgets provide a quick overview of alert volume
and characteristics:

Events Over Time by Fidelity – Displays alert trends over time, broken down by
fidelity level (High Fidelity vs Other).

Raw Event Count – The total number of correlated raw events that contributed to this
alert type.

Events by Fidelity (Pie Chart) – Graphical summary of alert fidelity distribution (e.g.,
number of high-fidelity alerts).

Source Locations Map – Shows geolocation data of source IPs, when available. A
legend indicates the volume range per region.

These widgets help you assess the scope, trust level, and origination of reported phishing activity
at a glance.

 If you want to rearrange these widgets and the table below them, select Edit, drag them into

different positions on a grid layout, and the Save your changes.

User Reported Phishing Email Documents Table
Beneath the widgets is the User Reported Phishing Email Documents table, which lists individual
alert instances and their key components:

Time – Timestamp indicating when the alert was created.

Alert Score – Numeric severity rating (typically 100 for critical phishing alerts).

Email Subject – The subject line from the reported email.

Source User ID / User Email – The user who reported the phishing message, along
with their email address.

Actions – Selecting the More Info icon opens the Alert Details side panel, where you
can perform in-depth investigation.

Row Expansion: Selecting the arrow to the left of a row expands it to reveal its property
metadata. You can then use the Quick Filters or Search for Details field to locate specific fields.

Alert Details Side Panel
The Alert Details side panel for a User Reported Phishing Email alert consists of four tabs:
Overview, Observables, Activity, and JSON. Together these four tabs provide both a high-level

summary and a detailed technical breakdown so you can investigate and respond to alerts
efficiently and accurately.

 To expand the side panel to a full-page view, select the Maximize icon at the top of the

panel. When expanded, the Overview tab appears on the left in a persistent display while
the Observables, Activity, and JSON tabs appear on the right so you can switch between
them and view their content while keeping the Overview tab open as well.

Overview tab: This tab provides a summarized view of the classification, severity, and threat
intelligence findings of the alert.

Verdict – A verdict is the classification that Stellar Cyber assigns to a suspected
phishing attempt after analyzing evidence gathered during the automated security
investigation. It represents its judgment about the nature of an alert or case following
the triage process.

There are four different verdict values and the state during review before a verdict is
rendered:

True Positive: This verdict is for a security event that accurately identifies a
real threat or malicious activity.

Benign True Positive: This is for an event that’s correctly identified as
legitimate but non-malicious, such as a penetration test or legitimate software
activity.

False Positive: A benign event was incorrectly flagged as a threat.

Inconclusive: The available evidence is insufficient to determine whether the
event is malicious or benign.

Pending: The event has not yet been reviewed; this is the default status prior
to classification.

Score and Severity – Displays the risk level as a numeric score, such as 100 for a
critical threat.

Stellar AI Summary – Explains why the system generated the alert based on its
analysis.

Findings – Findings are the key insights derived from the automated security checks
performed during the triage process. Each one contributes to the overall classification of
an alert and is supported by specific pieces of evidence. Findings are structured and
categorized to enhance clarity and traceability.

In every case, Stellar Cyber provides a concise explanation of the identified issue, such
as a suspicious behavior, failed validation, or known threat indicator. These insights
collectively justify the final verdict assigned to the alert. Every finding corresponds to a
distinct type of security check and is accompanied by a security value, which reflects its
relative importance or associated risk level.

Metadata: This includes workflow details like status, assignee, and tags; MITRE
ATT&CK classification, including the tactic (Phishing) and technique (Initial Access); and

email details such as sender, recipient, reporter, and any associated investigation
cases.

Observables tab: Observables are the individual data artifacts that can be detected on a system
or network and might indicate malicious activity, policy violations, or other security-relevant
behaviors. They serve as foundational elements of analysis—building blocks that underpin the
creation and context of each alert.

This tab shows detailed technical information of the observables extracted from the email that
triggered the alert:

Preview – Safely displays the email subject, sender, recipient, and body.

Download Raw Email – Download the original email for further inspection.

Downloading raw emails for analysis

In some cases, further investigation of a user-reported phishing email requires
reviewing the complete raw message. Stellar Cyber provides a Download Raw
Email option in the Observables section of the alert details to support this type of
analysis.

To download and open a raw email:

1. Select Download Raw Email.

A warning prompt appears.

2. Select Copy password, select Proceed with Caution, and then download
the email file to a local system and save the copied password in a secure
location.

For security reasons, the password is obscured in the UI.

3. When you open the downloaded email, enter the password you copied to

decrypt and view the content.

The password is consistent for each email. If you download the
same email multiple times, Stellar Cyber uses the same password.
This ensures you can recover the password later if you forgot to
copy it during the first download, or reuse a previously saved
password if you download the same email again.

The password is not confidential and is intended to prevent the
accidental downloading and running of malicious code in an email
file.

The email file is encrypted using AES-256 and cannot typically be
opened using the native file extraction tools built into client
operating systems. Whenever you experience a decompression

issue when opening a downloaded file, use a third-party tool like 7-
Zip or WinRAR.

Analyzing the raw email enables you to review the full message headers for
anomalies such as spoofed sender addresses or unusual relay paths, examine
embedded URLs and attachments for malicious indicators, and identify patterns that
automated parsing might miss.

For deeper inspection, you can upload the downloaded email into the Malware
Sandbox available in Stellar Cyber. The sandbox executes the email in a secure,
isolated environment to detect hidden payloads and suspicious behavior, providing
additional insight into potential threats.

 For instructions on enabling the Malware Sandbox and uploading files for

analysis, see the Malware Sandbox Details and Configuration section in the
Configuring Modular Sensor Profiles topic.

Domains & URLs – Lists email sender domains and any web links found in the
message. It also includes threat scores and intelligence about the links, such as when
they were first and last seen.

Headers – Shows the original email headers used for tracing the email’s delivery path.

Attachments – Provides file names and threat assessment data from integrated tools.
Includes hash values (MD5, SHA1, SHA256) and links to external virus scanners like
VirusTotal.

Raw Message – Displays the full original structure of the email (MIME content) for in-
depth inspection.

Activity tab: This tab records all actions taken on the alert, including system updates and
analyst comments.

All – Combines all recorded entries from both the Comments and History in a single
view.

Comments – Shows notes entered by analysts during their review.

History – Lists system-generated updates, such as when the alert status changes (for
example, from "New" to "In Progress") and when tags or assignments are modified.

Each entry includes a date, time, and the name of the user or process that made the change.

JSON tab: The JSON tab presents the full structured data for the alert using JSON format, which
is a standard for storing and sharing technical information. It displays the complete data record
that Stellar Cyber used to create the alert and includes technical fields such as the email source,
alert provider, severity level, and MITRE ATT&CK tactic and technique identifiers. This tab is a
particularly useful reference for automating workflows, validating individual data fields, or
exporting structured alert information. If the JSON content is too long to display in its entirety, a
“Show more” option is available to expand and reveal the full record.

Recommended Actions in Response to Email Phishing
In addition to reviewing the analysis in the Stellar Cybertellar Cyber UI, consider taking the
following actions to respond effectively to validated instances of email phishing. You can perform
the first action through ATH playbooks in the Stellar Cyber Platform. The remaining actions must
be carried out using features in your email service or integrated security tools.

Notify Stellar Cyber users – Trigger an automated notification to yourself or other
Stellar Cyber users through an ATH playbook. This ensures that relevant security
personnel are immediately aware of the phishing incident and can take further steps as
needed.

Isolate the email – Quarantine the phishing email to prevent recipients from opening or
interacting with it. Act quickly to limit exposure and reduce the chance that others in
your organization engage with the message.

Delete the email – Remove the phishing message from all affected inboxes. This
eliminates the risk of users accessing the email after initial detection and helps contain
the incident.

Search for similar messages – Use search tools in your email system to identify other
messages that match the characteristics of the phishing email, such as sender address,
subject line, or embedded URLs. This helps you assess the scope of the attack and find
additional users who may have been targeted.

Notify affected users – Alert users of your email service who received or interacted
with the phishing email. Provide clear instructions on what to do next, such as avoiding
links, deleting the message, or reporting suspicious activity.

Block sender – Add the sender’s email address or domain to a blocklist within your
email platform. Apply the block at the user level or organization-wide, depending on the
risk level and your internal policy, to prevent similar emails from being delivered in the
future.

Reset password – If a user’s credentials may have been compromised—especially if
the phishing email included a credential harvesting link—require the affected user to
reset their password. Enforce multifactor authentication where possible to reduce the
likelihood of account misuse.

Block URL – Block any malicious URLs identified in the phishing message to prevent
users from accessing harmful content. Coordinate this effort with your firewall, secure
web gateway, or DNS filtering solution to ensure that the block is enforced across your
network.

Phishing Email Analysis and Risk Scoring

After a user reports a suspicious message and the email reaches Stellar Cyber for inspection,
the phishing email triage agent works with integrated threat intelligence services to strengthen
detection accuracy and perform a layered analysis. This process evaluates the content,
structure, metadata, and embedded elements in the message. the agent validates potential
threats, determines the level of risk, assigns a comprehensive risk score, and generates a
detailed report that summarizes the findings and recommends appropriate actions.

Multi-Factor Evaluation

The Stellar Cyber phishing email triage agent evaluates each email using a variety of critical
signals. The system focuses on the following areas:

Attachment Security

The auto triage agent inspects every file attachment for signs of malware, obfuscated
payloads, or evasive encoding techniques. It identifies risky file types, embedded
scripts, password protection, and abnormal formatting.

Sender and Header Analysis

The agent verifies the authenticity of the sender using three industry-standard email
authentication mechanisms:

Sender Policy Framework (SPF): SPF determines whether a message
comes from an IP address authorized by the domain owner. This helps identify
forged sender addresses. The auto triage agent uses SPF results to detect
mismatches between the sending IP and the domain’s published policy.

DomainKeys Identified Mail (DKIM): DKIM confirms that the content of an
email has not been modified in transit and that it was cryptographically signed
by the originating domain. The auto triage agent uses DKIM to validate
message integrity and domain authenticity.

Domain-based Message Authentication, Reporting, and Conformance
(DMARC): DMARC interprets the results of SPF and DKIM and provides policy
instructions for handling unauthorized messages. The auto triage agent
evaluates DMARC alignment to detect domain spoofing and policy violations.

URL and Link Analysis

The auto triage agent inspects all hyperlinks in the email to identify mismatches
between displayed and actual destinations. The agent evaluates known malicious
domains, redirect chains, and infrastructure attributes such as domain age, registration
history, and hosting location.

Language and Content Indicators

The agent analyzes language, structure, and tone to detect phishing techniques such
as impersonation, urgency, credential harvesting, and financial fraud. It evaluates
sentence construction, salutation format, and embedded calls to action.

Standardized Risk Score

Stellar Cyber assigns each email a risk score out of 100, based on weighted contributions from
all evaluated components. One key component of this score is the Threat Intel Score, which

reflects results from external intelligence sources such as VirusTotal. When the system
encounters a file hash, domain, or IP address in the email, it queries VirusTotal. If the query
returns a known malicious result, the threat intel score increases and contributes significantly to
the overall risk. Low-confidence or clean findings reduce the score contribution from this
category.

Based on the final total, Stellar Cyber assigns the email to one of four severity levels:

Severity Level

Score Range

Description

Critical

Major

Minor

Notice

≥ 75

50–74

25–49

< 25

High severity and high confidence. Immediate investigation is required.

Likely to be a true positive or carry significant impact. Investigate promptly.

Lower confidence or impact. Investigate as resources allow.

Weak signals or low concern. Often used to support contextual analysis.

These levels help your team assess which threats require the most urgent attention.

Manage Phishing Email Triage
After a user reports a phishing email and your mail system forwards it to the Stellar Cyber inbox,
phishing email triage agent automatically retrieves the message, parses it to extract observables,
enriches data using threat intelligence sources, and creates an alert. Each alert includes a threat
score, observables, findings, a system-assigned verdict, and a static screenshot of the email
body—enabling safe visual inspection without risk of triggering embedded threats.

You can review alerts from user-reported phishing emails directly in the Alerts panel. Use filters
to identify relevant events by alert type, verdict, severity, or associated observables. Select an
alert to open its detailed view, where you can examine the findings, preview the static
screenshot, and assess the enriched indicators. The correlation ID enables navigation to related
data across Threat Hunting, Interflow, and other investigation views.

Stellar Cyber generates one alert for every phishing report, even if multiple users report the
same email. Each alert also results in the automatic creation of a case. You can access these
from the Case Management interface, where you can assign ownership, add comments, or
attach additional alerts manually if needed. Case records include a timeline of investigative
activity and support collaborative tracking throughout the incident lifecycle.

You can take response actions directly on a user-reported phishing email alert, and you can also
configure ATH playbooks to route alerts, notify analysts, or assign cases automatically. For
validated threats, follow the standard response procedures in your organization to contain
exposure and inform affected users.

To maintain an effective triage process, regularly monitor phishing alerts, review open cases, and
ensure that your analysts understand how to use correlation IDs, case views, and alert
summaries. With these tools, you can manage phishing reports efficiently while preserving full
visibility and control throughout the triage workflow.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

