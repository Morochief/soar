Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Understanding Alert Auto Triage Performance

 The Alert Auto Triage feature is only supported on Stellar Cyber in SaaS deployments and
requires an add-on license, which you can request from your sales representative. If you
used this feature through participation in the Early Access Program, contact your sales
representative to continue with an add-on license or to request that the service be disabled.

Understand what happens during the Alert Auto Triage process, why it can take several minutes
to complete, and how to interpret the observed latency in production environments.

What Happens During Auto Triage

Why Auto Triage Takes Several Minutes

Observed Production Latency

Interpreting Latency in Context

What Happens During Auto Triage
When the Stellar Cyber Platform processes an alert through Auto Triage, it does not perform a
single check. Instead, it launches AI agents that execute a comprehensive sequence of
investigative steps—comparable to the work a Tier 1 SOC analyst would perform manually. The
investigation includes these steps:

Enriching observables (IP addresses, domains, file hashes, URLs) against threat
intelligence feeds and reputation services such as VirusTotal, AbuseIPDB, and
URLscan.

Querying endpoint telemetry from integrated sources such as SentinelOne Deep
Visibility and Microsoft Defender to retrieve process-level context, device compliance
status, and event history.

Performing real-time identity lookups against platforms such as Okta and Entra ID to
retrieve user profile metadata, activity history, and VIP status indicators.

Running Verdict Signal Checks (VSCs) across process, network, file, and identity
observables.

Correlating findings across multiple data sources and detection layers.

Synthesizing all evidence into a verdict (True Positive, Benign True Positive, False
Positive, or Inconclusive) with a structured narrative explaining the reasoning.

Each of these steps involves external API calls, data correlation, and AI reasoning. The depth of
this analysis is what enables high-confidence verdicts and reduces the need for manual
investigation.

Why Auto Triage Takes Several Minutes
The time required for Auto Triage reflects the depth and breadth of the investigation being
performed. This is similar to how modern AI assistants take several minutes when performing
complex research tasks. The system is reasoning, gathering information from multiple sources,
and synthesizing results rather than returning a cached or precomputed answer.

A Tier 1 analyst typically spends two to four hours per case on a manual investigation of
equivalent depth. Alert Auto Triage completes the same work in minutes, and it does so
continuously, 24/7, without fatigue or capacity constraints.

Observed Production Latency
The following table shows observed latency percentiles from production environments as of April
2026. These values represent real-world performance across a range of alert complexities and
case sizes.

Case Triage Latency

Case triage latency measures the time to complete the case-level summary and narrative after
all associated alerts have been triaged. The following table presents case triage latency by
percentile.

Percentile

Latency

Description

p50 (median)

~2.4 minutes

Half of all cases are fully triaged in under 2.5 minutes.

p95

p99

~6.4 minutes

95% of cases complete within approximately 6 minutes.

~10.6 minutes

Only 1% of cases exceed approximately 10 minutes.

Case triage latency is generally lower at the high percentiles than alert triage latency because
the case-level summary synthesizes the investigation work already completed at the alert level. It
performs aggregation and narrative generation rather than repeating the underlying investigation
steps.

Interpreting Latency in Context
When evaluating Auto Triage performance, consider the following factors to interpret latency in
context:

Speed vs. depth – Latency reflects the thoroughness of the investigation. Faster
results would require reducing the number of enrichment sources or validation checks,
which would lower verdict confidence.

Minutes vs. hours – The relevant comparison is not against instant classification, but
against the 2–4 hours a human analyst would need to perform the same investigation

manually. Auto Triage delivers equivalent depth in a fraction of the time.

Continuous operation – Auto Triage runs 24/7 without breaks, fatigue, or capacity
limitations tied to analyst availability. This means that even alerts arriving outside
business hours or during peak volume periods receive the same depth of analysis.

External dependencies – A portion of the latency—particularly at the p95 and p99
levels—is attributable to external API response times from threat intelligence and
enrichment providers. These are outside the control of the Stellar Cyber Platform but
are necessary for high-confidence verdicts.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

