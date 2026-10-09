Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Understanding Cases

 Learn more at Stellar Cyber Academy.

The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.

J02 Introduction to Features in the User Interface (02h:24m)  

Case Management (48m:00s)

Watch a demonstration of Case Management workflows in the Platform, covering how to
interact with, filter, and sort cases using the Top Cases view and toolbar filters. Explore
the search tool and other filtering options that support efficient investigation workflows
across the data lake. Follow along as a case is investigated using detailed analysis
options and visualizations, tracking the progression of an attack through kill chain
stages. Learn how machine learning and threat intelligence surface relevant Interflow
records and contextual insights to help analysts understand and respond to security
incidents.

J03 Investigations and Workflows (05h:48m)  

Workflow Tools in the Stellar Cyber UI (35m:00s)

Explore workflow tools within the UI, including case management, knowledge sharing,
task assignment, and alert triage. Discover ways to enhance collaboration, automate
notifications, and integrate the UI tools into efficient SOC workflows.

Built-In Investigation Views (25m:00s)

Get familiar with built-in investigation views within the Platform, such as case views,
alerts, and kill chain views. Learn how to prioritize and sort cases and alerts for effective
triage, using these views to drive incident response.

Building Workflows in Stellar Cyber - In Practice (18m:00s)

Dive into practical considerations for creating workflows, including best practices for
workflow consistency and efficiency. Explore tips for building workflows that adapt to
real-world security operations and SOC needs.

Case Investigation (45m:00s)

Watch a step-by-step investigation of a case in the Platform from start to finish. Follow
an example case through detailed analysis and evidence gathering, learning how to
apply tools and techniques — including toolbar filters, the search tool, and threat
intelligence — to build a cohesive incident narrative. Explore how to enrich cases with
context drawn from Interflow data lake records and different stages in the kill chain for a
more comprehensive investigation using Case Management.

The first time you access a link on the portal during a session, you must log in to access
content.

Stellar Cyber leverages ML to correlate disparate alerts into coalesced cases.

A case represents a grouping of potentially related alerts in a single data structure. Cases
provide holistic context, allowing the analyst to examine the case and its associated alerts to
assess whether the case represents a real attack, true high-risk behavior, or event connections
without security significance.

To understand why the alerts in a case are potentially related, consider the following example: a
trojan alert and a traffic anomaly alert found on the same asset within an hour of one another.
This could represent real malware or it could just be a coincidence. Additional related alerts and
scoring will help distinguish the difference. The analyst can work with the algorithm
collaboratively to apply context and investigate what is potentially threatening or risky.

Cases accelerate complex detection and response by providing a higher-level construct to
analyze instead of individual alerts. Compared to the triage of individual alerts, a case provides
more context of correlated behaviors to help analysts make a more holistic evaluation during
triage.

Refer to the following sections for details:

How Case Correlation Works

About the Correlation Timeout

How Connection Strength Works

Case Correlation Details

Case Correlation and Manually Generated Events

Customizable Case Correlation Strategies

Selecting and Evaluating a Case Correlation Strategy

About Multi-Entity Case Correlation

How Case Scores Are Calculated

Score Calculation Details

Cases in the Stellar Cyber User Interface

How Case Correlation Works

Stellar Cyber uses a risk-centric algorithm for case correlation by default. The risk-centric
algorithm works as follows.

 You can experiment with alternative case correlation strategies as part of the Early Access

Program.

1. Stellar Cyber generates an alert.

2. The case correlation algorithm attempts to associate the alert with a case in real time.

If there is a strong connection with an existing case, the alert is grouped and
correlated with that case. One alert can belong to multiple cases; the algorithm
attaches the alert to any case as long as there is a strong enough connection.

For system-created cases, the Stellar Cyber Platform does not create a case
activity entry when an alert is correlated and added to an existing case.
Instead, it records changes to the case activity history when the case score,
which indicates how critical a case is, increases or decreases by 3 points or
more.

For user-created cases, the case activity history tracks alerts being added to or
removed from the case.

If there is no strong connection with an existing case, what happens next
depends on whether Case Filters are enabled in your deployment:

Case Filters Not Enabled – A new case is created containing this
alert. The result is a new case with this single alert.

 This is the same behavior as in previous Stellar Cyber releases.

Case Filters Enabled – A case candidate (sometimes referred to as
a "proto-case") is created with this single alert. The case candidate is

evaluated against the current Case Filter settings.

If the candidate matches any of the case filters, the case is
suppressed and is not displayed. It remains a candidate until
it meets one of the thresholds in the next step. Until the
candidate ages out according to one of the thresholds in the
next step, it can still become a full case if filter criteria
change.

If the candidate does not match any of the case filters, it is
promoted to a full case and is displayed in the Cases list.

3. A Case continues to accept new correlated alerts and grow until whichever of the

following happens first:

The case is closed by a user (Status is set to either Resolved or Cancelled).

The number of alerts associated with the case reaches the maximum specified

by the Alerts Per Case threshold (5,000, by default).

No new alert is associated with the case within the time window specified by
the global Correlation Timeout.

The duration of a case exceeds 30 days.

This means that the maximum duration for a case is 30 days (the time between the first
and last alerts) as long as new alerts come in more frequently than the Correlation
Timeout and the case is not closed by a user.

4. Alerts with a status of Closed or Ignored are not correlated to cases.

About the Correlation Timeout

An alert can be correlated into an existing case if it occurs within a specific time window of the
case. This time window is determined by Correlation Timeout, which is the amount of time that
has passed after the latest alert that was correlated into the case or before its earliest correlated
alert. The figure below illustrates how this works:

As summarized in the figure above:

A new alert is not considered for correlation if it occurs after the amount of time
specified by the Correlation Timeout has passed since the last correlated alert for the
case. An alert such as this has occurred too late for correlation.

A new alert is not considered for correlation if it occurs earlier than the amount of time
specified by the Correlation Timeout before the earliest alert associated with the case.
An alert such as this has occurred too early for correlation into the case.

The default Correlation Timeout is three hours; the maximum is 24 hours.

Refer to Setting the Correlation Timeout for details on configuring a global correlation window
for your organization.

How Connection Strength Works

The connection strength between an alert and a potential case has to do with shared entities (for
example, assets or users), shared properties (for example, hashes or URLs) and time (close time
windows), which are also considered to evaluate how to build strong context. The algorithm is
trained on real-world attacks and data; that training is what informs the level of connection
strength necessary for correlation. The algorithm continues to improve as more data is
incorporated into training, thereby improving case output as well.

Case Correlation Details

Stellar Cyber correlates both asset and user-based alerts into cases. In general, if an alert has
any of the fields in the tables below populated, it is correlated into a case:

Asset-Related Fields for Case Correlation

Alerts that have any of the following asset-related fields populated are correlated into cases:

Category

Asset ID

IP

Fields

dstip_assetid

hostip_assetid

srcip_assetid

dstip

host.ip

hostip

srcip

 IP-based correlation is performed for internal IP addresses and not public IP addresses. If no

internal IP addresses are found as part of an alert, Stellar Cyber uses other fields for

correlation (for example, the user fields listed in the table below). Stellar Cyber uses private

IP addresses for case correlation to track activities and identify compromised systems within

the boundaries of an organization, allowing incident responders to focus on assets and

endpoints under their jurisdiction. This approach also excludes external IP addresses that

change frequently and can be shared across multiple users, (for example, CDN or proxy

servers), making attribution unreliable and potentially leading to inaccurate or incomplete

results. Stellar Cyber does, however, use external IP addresses for threat intelligence and

geolocation tracking.

Host Name

computer_name

dstip_host

host.name

hostip_host

srcip_host

Cloud Resource ID

cloud.resource.id

 Stellar Cyber can correlate alerts to cases based on matches in the Cloud Resource

ID using data from integrations with Microsoft Defender for Cloud, AWS GuardDuty, AWS

CloudTrail (SigmaHQ rules), and Azure Activity Logs (SigmaHQ rules). You may see alerts

correlated to cases from other cloud sources (for example, OCI CloudGuard), but those will

be based on matches in other fields (IP addresses and user names, for example) rather

than Cloud Resource IDs.

User-Related Fields for Case Correlation

Alerts with any of the following user-related fields populated are correlated into cases:

Category

User SID

Fields

dstip_usersid

User ID

Username

event_data.SubjectUserSid

event_data.TargetUserSid

hostip_usersid

srcip_usersid

user.id

dst_name

dst_user

dstip_username

event_data.SubjectUserName

event_data.TargetUserName

hostip_username

principal_name

secondary

src_user

srcip_username

user.name

username

wineventlog_user.name

Email

email.message_id (when msg_origin is either proofpoint_tap or mimecast_email)

user.email

 Case correlation uses advanced user identity matching to associate alerts that

reference the same individual, even when different data sources provide varying or incomplete
user identifiers. This ensures that alerts linked to a single user are grouped into one correlated
case, giving you a unified view of user activity and associated risks.

The correlation engine evaluates multiple identifiers in a prioritized sequence to determine
whether alerts refer to the same user. When the user.email and user.name identifiers overlap
across data sources, Stellar Cyber merges the alerts into a single user entity and groups them
into one case. This approach consolidates investigations that span endpoints, networks, and
cloud services, allowing you to see a complete picture of a user’s behavior across environments.

The correlation engine also uses this normalized user identity when constructing correlation

graphs.
across multiple data sources even when the user appears under different fields such as

 As a result, detections, timelines, and pivots can reference a single user node

user.name, user.id, principal_name, src_user, or dst_user. This reduces fragmented user
nodes and helps preserve relationships that might otherwise be missed during investigation.

User identity correlation extends to Microsoft security products, including Microsoft Defender,
Azure Active Directory Risk Detection, and Office 365 Audit for Azure Active Directory. For these
integrations, Stellar Cyber normalizes user identifiers such as user.name, username,
user.email. It also converts all email usernames to lowercase before evaluation to ensure
consistent matching across data sources. Variations in capitalization—such as
John.Smith@Company.com and john.smith@company.com—are treated as the same user.

Example – A user named John Smith appears in different alerts from Microsoft services using
several identifiers:

In Microsoft Defender, as user.name: John.Smith

In Azure Active Directory Risk Detection, as username: john.smith@company.com

In Office 365 Audit for Azure Active Directory, as user.email:
JOHN.SMITH@COMPANY.COM

Although the identifiers differ in format and capitalization, case correlation recognizes them as
belonging to the same individual. The alerts are merged into a single case, allowing you to view
all related activity for John Smith in one place and assess whether it represents a coordinated
compromise attempt.

 For alerts from office365_audit_azureactivedirectory and

azure_ad_risk_detection, case correlation prioritizes user identity over host identity. This
ensures that alerts referencing the same user are grouped together, even when host
information differs.

Correlation for Alerts with Multiple Observables

Many Stellar Cyber alerts have multiple associated observables. Alerts with multiple observables
are sometimes referred to as summarized alerts.

Case Management's ability to correlate and display multiple observables from summarized alerts
is described in the table below:

Summarized Alert

Correlation/Display Support

Internal IP Port Scan Anomaly

Display of multiple destination IP addresses as case observables.

Internal SMB Read Anomaly

Internal SMB Write Anomaly

Internal Credential Stuffing

External Credential Stuffing

Internal Password Spraying

External Password Spraying

Display of multiple SMB paths as case observables.

Correlation and display of suspicious IP addresses in alerts.

Correlation and display of target users in alerts.

Password Resets Anomaly

Correlation and display of target users in alerts.

Summarized Alert

Correlation/Display Support

Account Creation Anomaly

Correlation and display of users in alerts.

Cloud Drive Data Exfiltration Anomaly

Display of multiple files as case observables.

Alerts Correlated to Cases

Stellar Cyber creates cases for all alerts, including those without any observables. Only the
following alerts are not correlated into cases:

Alerts from the Sensor index (Data Ingestion Anomaly and Sensor Status Anomaly).

Alerts from correlation-based ATH rules.

This means that Stellar Cyber creates single-alert cases for the following situations:

Alerts where no user or asset can be found.

Alerts from third-party cloud alert integrations, such as AWS GuardDuty.

Alerts from automated threat hunting with only raw data.

 All alerts that can be correlated to cases can also be synchronized to ServiceNow via an

active InSync, when configured.

Searching for Alerts Without Correlated Cases

You can use the following search in the Lucene Search bar in either the Alerts or Threat Hunting
page to see alerts that have not been correlated to cases in the current time window:

(NOT ( (_exists_:(xdr_event.name OR event_name) AND _exists_:orig_index) OR

(stellar.ath.type:raw AND stellar.ath.to_incident:true))) OR xdr_event.name:

(ade_outbytes_anomaly OR ade_outbytes_anomaly_flip)

Cases with Cloud Observables from Third-Party Alert Integrations

Stellar Cyber identifies and presents cloud observables for cases based on alerts from the
following third-party cloud integrations:

Microsoft Defender for Cloud

AWS GuardDuty

SigmaHQ rules for AWS CloudTrail

SigmaHQ rules for Azure Activity Logs

In addition, Stellar Cyber correlates alerts to cases using matching Cloud Resource IDs from
Microsoft Defender for Cloud, AWS GuardDuty, AWS CloudTrail, and Azure Activity Log alerts, as
described in Case Correlation Details.

Cases with Observables from Cloud-Based Email Integrations

Stellar Cyber identifies and presents observables for cases based on alerts from the following
third-party email integrations:

Mimecast

Proofpoint

 Refer to Observables from Cloud-Based Email Security Integrations for information on
the observables Stellar Cyber extracts and displays in the Case Analysis workspace based
on email alerts from these sources.

 Case observables from cloud-based email integrations are available as part of an Early

Access Program and might not be available in your version of the Stellar Cyber Platform.

Case Correlation and Manually Generated Events

 Considerations for manual event generation: Due to the nature of Stellar Cyber's alert

correlation and machine learning models, manually generated or ad-hoc events may not
always trigger the expected alert or case creation. The Stellar Cyber platform is designed to
analyze and correlate multiple events over time, assessing patterns and context to
determine the severity of a potential threat. As a result, isolated or artificial events might not
meet the criteria for high-severity alerts or case generation, and may not be representative
of the system's full detection capabilities in real-world threat scenarios.

Customizable Case Correlation Strategies

 This section describes a feature that is currently only available as part of an Early Access

Program and may not be enabled in your version of the Stellar Cyber Platform. Contact your
sales representative for information on enabling this feature and comparing its results to
those of the traditional risk-centric model.

Stellar Cyber provides support for multiple case correlation strategies as an EAP feature,
allowing teams to evaluate and experiment with different approaches to grouping alerts into
cases. Each strategy provides a distinct investigative perspective:

Multi-Entity Correlation links alerts across interconnected hosts and actions to form a
single case, offering a holistic view of extended or lateral attack campaigns.

Attacker-Centric Correlation groups alerts by the source (attacker) host, making it easier
to track adversary behavior across multiple targets.

Victim-Centric Correlation organizes alerts by the destination (victim) host, enabling
focused protection and visibility on high-value assets.

The flexibility to choose a case correlation strategy enables security teams to tailor investigations
based on their operational priorities, whether that’s identifying persistently targeted endpoints,
tracing threat actor movements, or capturing full-scale intrusion campaigns. To join the EAP and
begin testing these correlation strategies, contact your Stellar Cyber Customer Success
representative.

Selecting and Evaluating a Case Correlation Strategy

You must work with Stellar Cyber Customer Success to change the case correlation strategy for
your deployment – you can't change it by yourself. Regardless of the strategy you select, plan on
allowing at least a week to evaluate a given case correlation strategy. During the evaluation

period, monitor your deployment for sudden changes in case graphs or volumes. In addition, pay
attention to the following key metrics to determine which strategy is best for you:

Metric

Why it Matters

Primary Case

Correlation Strategy

Number of Cases

A sharp drop signals successful consolidation of alerts. This is especially desirable

Multi-Entity

Created

when evaluating the Multi-Entity strategy.

Average Alerts per

Case

Higher averages indicate stronger grouping of alerts, which is crucial for the Multi-

Multi-Entity

Entity strategy.

Threat-Actor

The percentage of cases tied to a single source host can measure how well case

Attacker-Centric

Isolation Rate

correlation is locking onto one attacker.

Asset-Impact

The percentage of alerts per destination host grouped together shows the

Victim-Centric

Grouping

effectiveness of Victim-Centric mode.

Case Resolution

Faster turnaround of cases reflects overall workflow efficiency. This is a useful

All

Time

Analyst

barometer for comparing all strategies.

Direct feedback on clarity and usability, which is valuable across every correlation

All

Confidence

strategy.

(qualitative)

False-Negative /

Track any gaps where alerts should have been grouped but weren’t. This is important

All

Missed Events

for detection quality.

True Positive Ratio

Monitor the proportion of alerts or cases each analyst confirms as true positives. This

All

per Analyst

can help you understand how alert grouping affects accuracy.

About Multi-Entity Case Correlation

 This section describes a feature that is currently only available as part of an Early Access

Program and may not be enabled in your version of the Stellar Cyber Platform. Contact your
sales representative for information on enabling this feature and comparing its results to
those of the traditional risk-centric model.

This release includes multi-entity case correlation as an Early Access Program feature, allowing
a given alert to be correlated to cases based both on its associated assets (hosts) and its
associated users. This is a contrast to the current single-entity model that identifies the most
important asset or user for an alert and correlates it to cases based on that entity. The table
below summarizes the differences in the two approaches:

Single-Entity Correlation

Multi-Entity Correlation

For each new alert, Stellar Cyber:

When multi-entity correlation is enabled, Stellar Cyber

1. Identifies all hosts and users (entities) associated with

the alert.

2. Chooses one of the associated entities as the most

essential for correlation based on an assessment of its
risk. This is the entity that is most concerning from a
security perspective and is more often a host than a
user because of its relative importance as a vector for
attacks (for example, a host used in a port scan).

3. Checks for other active cases that involve the same

entity.

maintains an internal Correlation Entities list for each

case. This list contains all of the hosts and users associated

with the alerts in the case. Then, for each new alert Stellar

Cyber:

1. Identifies all hosts and users (entities) associated with

the alert.

Single-Entity Correlation

Multi-Entity Correlation

If a match is found, associates the alert with
those cases.

2. Checks for other active cases that have a matching

host or user in its Correlation Entities list.

If no match is found, creates a new case based
on the entity.

If a match is found, the alert is added to the
case. In addition, all other hosts and users
associated with the alert are added to the
case's Correlation Entities list.

If no matches are found, creates a new case
for the alert and adds all of its hosts and users
to the case's Correlation Entities list.

Multi-Entity Case Correlation in Action

Multi-entity case correlation enables Stellar Cyber to correlate alerts to cases based on matches
in either a host or a user. For example, consider the following alerts:

Alert 1 – Involves user-x

Alert 2 – Involves user-x and host-a

Alert 3 – Involves host-a and host-b

In the single-entity model, alerts such as these would result in separate cases. The multi-entity
model, however, can create a single case that includes all of the alerts. The intent of this
approach is to capture the entire path of an attack, including the interactions between hosts and
users. For example, multi-entity correlation can give you a coalesced view of a phishing attack
that results in a compromised host, displaying both the affected hosts and users in a single case.

The figure below provides an example of multi-entity correlation in action, with both hosts and
users in the same case graph:

How Case Scores Are Calculated
Stellar Cyber assigns scores to cases based on how critical they are. The score updates in real
time as events and entities are added to or removed from the case. This section explains how
case scores are calculated.

In general, the score of a case is determined by the number of different alert types associated
with it. The score typically increases as the number of distinct alert types associated with it also
increases.

In addition to alert diversity, case scores are influenced by the characteristics of the associated
alerts. In particular, the fidelity and severity of alerts have a significant impact on the calculation
of a case score:

Fidelity – The confidence in the analysis. Higher fidelity indicates greater confidence
that a malicious event was correctly identified and increases the alert score. Lower
fidelity, especially when combined with low Threat Intel scores, reduces the alert score.

Severity – The importance of the category of the event. Higher severity reflects greater
potential impact. In general, later-stage events have higher severity.

Case severity levels correspond to the following case score ranges:

Case Severity

Critical

High

Medium

Low

Case Score

75 and higher

50–74

25–49

1–24

If an alert filter adjusts an alert score, the updated value is included in the case score calculation. Open cases recalculate

automatically to reflect the updated alert score.

Score Calculation Details

Stellar Cyber begins to assign a case score by calculating an Event Score for each different
alert type associated with the case. Stellar Cyber does this by summing the maximum Alert
Score, Severity, and Fidelity for all individual alerts of a given type. For example, consider the
case illustrated below:

This case has only two different alert types associated with it: Private to Public Exploit
Anomaly and Uncommon Application Anomaly.

There is only one Private to Public Exploit Anomaly alert, so Stellar Cyber uses the
only Alert Score available, which is 74. Similarly, it also uses the Severity and Fidelity
scores from this alert. You can't see those in the table, but you can by selecting the
More Info button in the table for the alert. For example:

There are five different Uncommon Application Anomaly alerts associated with the
case. As you can see in the table, the highest Alert Score across those five alerts is 33,
which is the value Stellar Cyber uses to calculate the score. Similarly, it also takes the
highest Severity and Fidelity score across these five alerts.

Once done, there are separate Event Scores for both the Private to Public Exploit Anomaly
and Uncommon Application Anomaly alert types. To arrive at a final score for the case, Stellar
Cyber performs the following steps:

Calculates a combined total score using the Event Scores for all alert types associated
with the case. Because of this, the more different alert types that are associated with a
case, the higher the score for the case will generally be.

Normalizes the total score to a final score using the following equation: final_score =
(total_score * total_score) / 100.0

Cases in the Stellar Cyber User Interface
Stellar Cyber reports cases in the XDR Kill Chain dashboard, as well as in the Cases interface,
giving you a powerful tool to understand and respond to ongoing attacks.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

