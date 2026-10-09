Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rule Framework Summary

Stellar Cyber uses rule based detections to identify known bad or risky behavior and to get broad
coverage of general best practices. Use this topic to understand the rule framework architecture.

Rule Framework Overview
Built-in rules have a many-to-one mapping to Alert Types. For example, the Alert Type
“Suspicious Powershell Script” has 100+ rules all looking for different variations of behavior
related to Powershell that could indicate malicious or high risk behavior. These are logically
grouped under a single Alert Type because of their alignment to a single use case.

In some cases, the Rule Framework works together with other built-in Machine Learning Alert
Types, including Abnormal Parent / Child Processes and Uncommon Process Anomaly as of
4.3.6, to provide a coherent use case regardless of the underlying detection mechanisms. Stellar
Cyber uses Alert Subtypes to differentiate alerts from different underlying detection mechanisms.

The Rule Framework within Stellar Cyber works by taking groups of rules, typically associated
with a single Alert Type, that all require the same input fields necessary for detection, and
processing those together against data in the data lake every 2 minutes. This allows for less
queries to the data lake resulting in the ability to run more rules efficiently.

Built-in rules are authored and maintained in Sigma  format. Currently, when users author
custom rules through Automated Threat Hunting (ATH), those custom rules are not stored in
Sigma format. In the future, Stellar Cyber will allow users to author and maintain custom rules in
Sigma format.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

