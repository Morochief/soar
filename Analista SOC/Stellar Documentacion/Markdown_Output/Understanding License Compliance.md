✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Understanding License Compliance
Stellar Cyber is committed to helping you monitor the data you need to maximize your security
while staying within the limits of your platform license. This topic helps you understand how
Stellar Cyber keeps track of license compliance, the consequences of being out of compliance,
and how to return to compliance should you find yourself outside the limits of your license.
In addition, the topic also provides guidance on how to implement connectors, sensors, and data
filtering strategies that achieve your security goals while also keeping you within the limits of your
license. See the following sections for details:
License States
Tips to Help Stay in Compliance
License States
Stellar Cyber runs a daily license report to evaluate compliance for your organization based on
the previous day's activities. For both asset and volume-based licenses, your compliance state
after this report is run is one of the following:
In Compliance – Activity is within license limits.
Warning – Initial notification that license limit has been exceeded
Violation – Notification that license limit has been severely exceeded.
Out of Compliance – Multiple license violations requiring a new license request.
The specifics on each of these states are provided in the table below:
Lice
nse
Trigger Result Returning to Compliance Example
Stat
e
In Activity is within Normal operations. N/A A user with a 100GB daily ingestion
Com license limits, license does not ingest over a daily
plian remaining below average of 110GB over the last
ce 110% of the limit. three or seven days.

Lice
nse
| Trigger | Result | Returning to Compliance | Example |
| ------- | ------ | ----------------------- | ------- |
Stat
e
| Warn License limit has | Removable warning banner |                            |                                     |
| ---------------------- | ------------------------ | -------------------------- | ----------------------------------- |
|                        |                          | Return to compliance after | A user with a 100GB daily ingestion |
ing been exceeded by appears in the user interface, staying under 110% of license ingests over 110GB per day
more than 10% on informing you that the license has license limit on average for on average for three days.
| average for three | been exceeded. |     |     |
| ----------------- | -------------- | --- | --- |
three consecutive days.
days.
Viola License limit has Non-removable violation banner. Banner is removed after A user with a 100GB daily ingestion
| tion been exceeded by | Email sent to account admin. |                            |                                    |
| --------------------- | ---------------------------- | -------------------------- | ---------------------------------- |
|                       |                              | returning to compliance by | license ingests over 110GB per day |
more than 10% on
|                   |     | staying under 110% of the    | on average for seven days. |
| ----------------- | --- | ---------------------------- | -------------------------- |
| average for seven |     | license limit on average for |                            |
days.
seven consecutive days.
| Out License limit has | Services cease. License bill sent |                             |                                     |
| --------------------- | --------------------------------- | --------------------------- | ----------------------------------- |
|                       |                                   | License bill paid. Refer to | A user with a 100GB daily ingestion |
of been in a violation to cover ingestion trends since Additional Billing to Cover license ingests on average
Com state for more first violation. Refer to License Violations for a 110GB or more for 21 days (7 to
| plian than 21 days. | Understanding License |                                |                                       |
| ------------------- | --------------------- | ------------------------------ | ------------------------------------- |
|                     |                       | description of how the bill is | trigger the violation, followed by an |
ce Compliance for details on bill calculated. additional 14 days in a state of
calculation.
violation).
The figure below summarizes how this cycle works:

Who Can See License Warning/Violation Banners?
 Notification banners for license warnings and violations are visible only to users with Root
scope and either the Super Admin or Platform Admin role assigned.
Additional Billing to Cover License Violations
If your organization's platform license reaches Out of Compliance status, Stellar Cyber will
submit to you a prorated invoice for the remainder of the license term. The invoice covers the
gap between your current usage since the start of the first Violation and the licensed limits. Your
current usage is defined as the average daily ingestion since the start of the first Violation.
For example, consider the following example:
Organization with a 100GB daily ingestion license that started its annual term on
January 1, 2025.
Organization reaches Out of Compliance status on July 1, 2025, after remaining in a
Violation state for 21 days.
First Violation occurred on June 10, 2025. This is a total of 21 days before July 1, 2025
– 7 days to enter the Violation state and 14 days in a Violation state to reach Out of
Compliance.
Average daily ingestion during this 21 day period since first Violation was 150GB/day.
Resulting bill covers additional 50GB of daily ingestion, prorated from June 10, 2025 to
the end of the annual term on December 31, 2025.
Next license term reflects 150GB/day of daily ingestion, assuming no further license
violations.
Tenant Allocation and Compliance
The Tenant Allocation tab provides visibility into how licensed capacity is distributed across
tenants. Allocations can be set higher than the License Threshold, but when total usage
exceeds the threshold, the License State changes to Warning and a banner notifies you that
licensed limits have been exceeded. Reviewing allocations can help you bring the system back
into compliance by adjusting tenant quotas or reducing ingestion.
Tips to Help Stay in Compliance
You can use the following resources to help you adjust the data you are collecting and stay within
your license limits:
Managing Log Filters
Managing Traffic Filters: Applications
Pre-DPI Filters

Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  