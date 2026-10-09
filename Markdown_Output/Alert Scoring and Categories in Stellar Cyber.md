Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Alert Scoring and Categories in Stellar Cyber

This topic describes scores assigned to alerts and definitions of the criticality of alerts.

Scores Assigned to Alerts
Scores are designed to help ranking and filtering alerts, understanding the significance and
security value of alerts, and facilitating prioritization of alert triage.

There are different scores in the Stellar Cyber platform as follows:

Alert Score – A comprehensive level of the risk and significance of an alert, reflecting
aspects of security, confidence, and intelligence.

Severity – The security component of Alert Score, reflecting the security value in terms
of security consequence and specificity.

Fidelity – The confidence component of Alert Score, reflecting the likelihood of an alert
being a true positive.

Threat Intel – The intelligence component of Alert Score, reflecting the suspiciousness
of IP addresses, domains, and URLs in an alert. Threat intelligence is derived both from
threat intelligence feeds and from ML determinations about various users and assets.

Alert Score, Fidelity, Severity, and Threat Intel scores are displayed throughout the Stellar Cyber
user interface, particularly in Event Detail displays, as illustrated below in the Event Detail
Header.

Alert Score

The Alert Score field in the Interflow data is event_score.

Alert Score has the following details:

It is computed from Severity (the security component), Fidelity (the confidence
component), and Threat Intel (the intelligence component).

It reflects a comprehensive level of the risk and significance of an alert from the three
components.

It is designed for global ranking and filtering of alerts from all alert types, where alerts
with higher scores are worth more attention and should be prioritized and investigated
immediately.

Alert Scores are determined primarily by severity, with adjustments made based on the
associated fidelity and threat intelligence scores. This means that an alert's Alert Score is
typically in the vicinity of its severity.

If an alert's fidelity or threat intelligence has a strong confidence, its Alert Score will be
higher than the base severity score.

If an alert's fidelity or threat intelligence score is low, the Alert Score will be lower than
the base severity score.

The exact algorithm is different for different types of alerts, based on the expertise of Stellar
Cyber's Machine Learning team. For example, a DNS Tunneling Anomaly starts with a severity of
98, but if your Red Team has been practicing DNS Tunneling for a while and the activity is quite
common, the fidelity might be 4, and the private addresses may have no threat intelligence
(Threat Intel: N/A). The final Alert Score might be 97 because data exfiltration is a great threat.
On the other hand, SMB Username Enumeration begins with a Severity of 30. The first time it's
seen on a network (Fidelity 100), the risk score of that event might be 55.

Severity

The Severity field in the Interflow data is severity.

Severity has the following details:

It reflects the security consequence and specificity of an alert type or a Sigma rule that
detects a certain type of attack, serving as the security component in Alert Score.

Alerts in later Kill Chain stages generally get higher severity scores due to the
significance of possible consequences; for example, stealing credentials (in a later Kill
Chain stage) has a higher severity score than scanning behavior.

Alerts that carry more specific security information generally get higher severity scores
than those that do not. For example, alerts on a known Command & Control IP address
would get a higher severity score than those on an unspecific suspicious IP address.
For example, the Command & Control Reputation Anomaly has a severity of 70,
whereas the Bad Source Reputation Anomaly has a severity of 30.

An alert with a high severity score indicates that it would either cause severe impact
and/or carry very specific security meanings.

Severity is documented for all Machine Learning (ML) and rule-based alert types. Refer to
Machine Learning Alert Type Details and Rule-Based Alert Types.

Fidelity

The Fidelity field in the Interflow data is fidelity.

Fidelity has the following details:

It reflects the confidence of an alert being a true positive, serving as the confidence
component in the Alert Score.

Non-ML based alerts have a fixed Fidelity, and ML based alerts have a variable Fidelity
computed by the ML model to reflect the model’s confidence.

Fidelity is useful in ranking and filtering alerts from the same alert type with the same
Severity for prioritization. Alerts with high fidelity scores should be prioritized as they are
more likely to be true positives.

For details on ML models, see Machine Learning Model Summary.

Threat Intel

The Threat Intel field in the Interflow data is threat_score.

Threat Intel has the following details:

It reflects the reputation of the IP addresses and URLs as assessed by the threat intel
sources. The higher the Threat Intel Score, the worse the reputation.

If Threat Intel is high, it drives the Alert Score higher. If Threat Intel and Fidelity are low,
it drives the Alert Score lower.

Alert Criticality Definitions
This section describes the definition of the criticality of alerts for Alert Score and Fidelity
categories.

Alert Score Categories

Stellar Cyber uses a consistent set of categories throughout the user interface to group alerts
based on their Alert Score:

Alert Severity

in Stellar

Best Practices for Monitoring and Investigation

Cyber

Critical

Alerts of high severity and fidelity that must be investigated immediately

A

l

e

rt

S

c

o

r

e

Al

er

t

S

c

or

e

≥

Alert Severity

in Stellar

Best Practices for Monitoring and Investigation

Cyber

Major

Alerts that are likely to be true positives or that could have significant security consequences and should be

given priority to investigate

Minor

Alerts of lesser severity and/or fidelity that should be investigated if time permits; or otherwise be

investigated together with correlated alerts in cases

Notice

Alerts of weak abnormal signals that are likely false positives or of less security concern, and may be

investigated together with related alerts and events, such as alerts in the same cases and relevant events

A

l

e

rt

S

c

o

r

e

7

5

Al

er

t

S

c

or

e

≥

5

0

a

n

d

<

7

5

Al

er

t

S

c

or

e

≥

2

5

a

n

d

<

5

0

Al

er

Alert Severity

in Stellar

Best Practices for Monitoring and Investigation

Cyber

identified in threat hunting

A

l

e

rt

S

c

o

r

e

t

S

c

or

e

<

2

5

Additional details:

The Alert Score range varies by alert type. Alerts from earlier Kill Chain stages may not
ever reach the Critical level, but it does not mean that they are not security significant.

For certain alert types and/or attacks of interest, depending on individual SOC
practices, we recommend a mixed strategy of using both Alert Score Categories and
Fidelity Categories to further help the prioritization of investigation effort.

Alert categories are displayed throughout the Stellar Cyber user interface, particularly in the
XDR Kill Chain dashboard and loop, as illustrated below:

Fidelity Categories

Stellar Cyber categorizes Fidelity Scores consistently throughout the user interface as follows:

Fidelity Level in Stellar Cyber

High Fidelity

Other Fidelity

Additional details:

Fidelity Score

Fidelity Score ≥ 75

Fidelity Score < 75

High Fidelity alerts are those likely to be true positives. They are reported either by rules
that are specific to certain attack signals, or by ML models with high confidence.

Monitoring and investigating High Fidelity alerts, despite their Severity, is highly
recommended for certain alert types of interest. For example, to catch account takeover
attacks, which may cause significant security impact if not contained promptly, the SOC
team may specifically prioritize the investigation of High Fidelity alerts of Impossible
Travel Anomaly and User Login Location Anomaly.

Fidelity categories are displayed throughout the Stellar Cyber user interface, particularly in the
Detections | Alerts page and its associated tables and graphs. For example, you can see the
High Fidelity column in the Alerts display below indicating the quantity of alerts for the
corresponding Alert Type with a Fidelity Score of 75 or greater.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

