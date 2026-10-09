Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Understanding the Stellar Cyber Risk Model

This topic explains how risk scores are calculated, as well as how Importance and Vulnerability
scores contribute to the overall risk score. See the following sections for details:

Understanding Risk Scores

Understanding Importance in Risk Scores

Understanding Vulnerability in Risk Scores

Understanding Risk Scores
Stellar Cyber assigns dynamic risk scores to assets or users to quantify how risky they are. The
risk score shows how likely a user or asset (such as a server, endpoint, or application) is to pose
a security risk based on recent security events, vulnerabilities, and asset importance (criticality).
The higher the risk score, the greater the concern.

Risk scores are recalculated every ten minutes and reflect the most recent 24 hours of activity,
so they always represent current conditions. In addition, Stellar Cyber maintains a score history
in the Asset Details page so you can monitor trends in score changes.

What Data Feeds the Risk Score?

The system brings together information from several key sources to calculate risk scores:

Security Events – Alerts and detections showing unusual or suspicious activity.

Vulnerability Data – Known weaknesses from scans, such as missing patches or
misconfigurations.

Contextual Importance – How important the asset is to the organization (for example,
a critical production server vs. a test machine).

How Security Events are Evaluated

Each event is assessed on three dimensions:

Severity – How damaging the alert could be if the event is real.

Confidence – How reliable the detection is.

Threat Level – How likely it is that attackers will try to exploit the event.

These factors are combined so that high-severity, high-confidence, and high-likelihood events
contribute more strongly to the risk score. In addition, events are grouped so the system doesn’t
double-count repeated alerts. For each group, the “worst case” values (such as the highest
severity) are carried forward.

Adding Vulnerability and Importance to Risk Scores

Once events are scored and grouped, the system combines them with:

Vulnerability information – Assets with more weaknesses naturally carry higher risk.

Asset importance – More critical assets are weighted so that even smaller risks count
more.

Combining risk scores with Vulnerability and Importance scores ensures that multiple smaller
risks can add up and elevate the overall score, reflecting the real-world chance that something
could go wrong.

Understanding Importance in Risk Scores
Stellar Cyber assigns each asset an importance level that reflects its criticality to the
organization. By default, the system treats assets as medium importance unless otherwise
specified.

Importance values are mapped to numeric multipliers, which influence how sensitive the risk
score is to security events:

Critical – most sensitive (smaller multiplier)

High – more sensitive

Medium – balanced (default)

Low – less sensitive (larger multiplier)

Setting Asset Importance

The importance level can be assigned or updated in several ways:

Manual updates – Users with the appropriate RBAC privileges can change an asset's
importance in the Asset Details page. Manual values take priority over other sources.

File imports – Importance can be assigned when assets are imported in the Asset
Imports page.

Automated discovery – Asset discovery and monitoring tools may provide initial
importance values, which can later be overridden by higher-precedence updates.

When multiple sources define an importance value, the system applies a precedence rule so that
manual settings override imported values, which in turn override automatically detected ones.

Impact on Risk Scoring

Asset importance directly influences the final risk score calculation. The importance level of an
asset acts as a criticality multiplier for the eventual risk score:

Higher importance assets (for example, critical or high) are scored more aggressively,
meaning the same set of security events will produce a higher risk score compared to
lower-importance assets.

Lower importance assets (for example, low) are scored more conservatively,
producing relatively lower risk scores for the same set of events.

This design ensures that security teams see a more accurate picture of risk in business context.
Critical systems rise to the top of the queue when exposed to threats, while lower-priority assets
do not generate disproportionate noise.

Understanding Vulnerability in Risk Scores
The system incorporates vulnerability data from two primary sources:

Full vulnerability scans – These provide comprehensive reports of all weaknesses
detected on an asset.

Individual vulnerability events – These capture details of specific Common
Vulnerabilities and Exposures (CVEs), along with their severity scores (e.g., CVSS).

Data is refreshed on a scheduled basis. Only vulnerabilities associated with known assets are
processed.

Before scoring, vulnerability data is linked to assets using available identifiers, such as MAC
addresses, hostnames, or IP addresses. This ensures each vulnerability is correctly attributed to
the right asset in the environment.

Score Calculation

Each asset receives a vulnerability score based on the weaknesses associated with it. The
scoring model has three key characteristics:

High sensitivity to severe issues – Higher-severity vulnerabilities contribute
disproportionately more to the score, ensuring that even a single critical weakness
raises the asset’s overall rating significantly.

Compounding effect of multiple vulnerabilities – Assets with multiple vulnerabilities
compound exponentially rather than linearly.

Score range – Final vulnerability scores are scaled to a range of 0–100, making them
directly comparable across assets.

This approach ensures that assets with multiple high-severity vulnerabilities receive appropriately
high vulnerability scores that significantly affect their overall risk assessment.

Impact on Risk Scoring

The vulnerability score is an integral part of the overall risk score. It acts as a baseline indicator
of inherent weaknesses:

Assets with multiple or severe vulnerabilities will start from a higher-risk position, even before
security events are considered. This means that the same set of alerts or behaviors may push a
vulnerable asset to a higher risk score compared to an asset with fewer or less severe
vulnerabilities.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

