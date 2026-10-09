Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Detection and Correlation Overview

Stellar Cyber uses a multi-modal detection and automated correlation strategy within the
platform. This approach leverages optimal detection techniques depending on the use case and
automatically investigates to yield greater Detection & Response performance.

Detection Pipeline Overview
Multi-modal detection is defined by multiple detection techniques employed at multiple locations,
specifically in edge environments and in the central data platform. Stellar Cyber, through its
sensors, deploys IDS, File AV, and Malware Sandbox (MW SB) into edge environments. Putting
detections closer to key infrastructure yields faster Mean Time To Detect (MTTD) and lowers
data volume requirements for central processing. The multiple techniques employed by the
Sensor are signatures (IDS), Machine Learning (File AV), and active detonation (Malware
Sandbox).

In the central data platform of Stellar Cyber, telemetry from all sources, both third party products
and from Stellar Cyber sensors, is leveraged to run hundreds of built-in Alert Types. These built-
in Alert Types use both Machine Learning (Supervised: that look for complex known bad, and
Unsupervised: that look for unknown bad), and Rules (filter based, correlation, and aggregate).
All Alert Types are documented in the Alert Type Model Summary. More details on the Machine
Learning Models employed are documented in the Machine Learning Model Summary, and more
details on the Rule Framework is documented in the Rule Framework Summary.

Finally, third party native alerts (for example, an alert created from an EDR), are integrated into
Stellar Cyber and processed alongside Stellar Cyber built-in alerts. Stellar Cyber can not only
passthrough these third party native alerts (after normalization and deduplication), but also use
Machine Learning models on them to produce net new alerts. Third party controls are typically
“at the edge” (for example, EDR), which also aids in the multi-modal detection strategy. The
handling of third party native alerts is documented in Integration of Third Party Native Alerts.

In summary, Stellar Cyber has detections at the edge and in its central platform, it uses different
analytical techniques and commands, and controls third party tools in the same platform. This is
a multi-modal detection strategy. This approach is important because Machine Learning based
alerts are not inherently superior to Rule based alerts, same with detecting at the edge versus in

a central location. The greatest detection performance and efficiency comes from employing
different techniques in multiple locations.

Automated Correlation Overview
The automated correlation that happens in Stellar Cyber is through a feature called Cases. A
Case represents a grouping of potentially related alerts (regardless if it came natively from Stellar
Cyber or from a Third Party Tool) in a single data structure. Cases provide holistic context,
allowing the analyst to examine the Case and its associated alerts to assess whether the Case
represents a real attack, true high-risk behavior, or event connections without security
significance.

Cases use Graph Machine Learning to automatically associate alerts together based on
connection strength (for example, shared assets or shared properties). The underlying algorithm
is outlined in Understanding Cases.

To understand why a Case's alerts are potentially related, consider the following example – a
trojan alert and a traffic anomaly alert found on the same asset within an hour of one another.
This could represent real malware or it could just be a coincidence. Additional related alerts and
scoring will help distinguish the difference. The analyst can work with the algorithm
collaboratively to apply context and investigate what is potentially threatening or risky.

Cases accelerate complex detection workflows by providing a higher-level construct to analyze
instead of individual alerts. Compared to the triage of individual alerts, a Case provides more
context of correlated behaviors to help analysts make a more holistic evaluation during triage.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

