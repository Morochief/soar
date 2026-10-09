Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Detection Timing Summary

Alerts and Cases generated in Stellar Cyber have different timing depending on the Alert Type
and the data sources involved. Use this topic to understand the expected timing and potential
delays associated with Alerts and Cases.

Detection Timing
The end-to-end detection pipeline, which is the process between event occurrence (for example,
a user logs in), to the Data Platform receiving associated records, to relevant Alerts being
generated, to Alerts being correlated with Cases, has different forms of latencies introduced that
affect timing. The different steps of that pipeline and rough orders of timing magnitude are
depicted as follows.

Timing 1 - Source To Platform

The timedelta between the Data Platform receiving a record compared to its event occurrence
varies significantly by data source. The latency introduced in this stage is on the third party data

source, and not Stellar Cyber. The exception to that is Stellar Cyber sensors where Stellar Cyber
controls the end telemetry source.

Examples of High Latency Sources are:

Office 365 (2 - 60 min)

Microsoft Entra ID (formerly Azure Active Directory) (2 - 60 min)

Okta (60 min+)

Examples of Low Latency Sources are:

Stellar Cyber Network Sensors (< 5 min)

Stellar Cyber Windows and Linux Sensors (< 5 min)

Most Syslog sources (for example, Firewall) (< 5 min)

Timing 2 - Platform to Alert

The timedelta between an Alert being generated compared to when the Data Platform received
the relevant data. This timing is controlled by Stellar Cyber.

The timing is between 5 - 30 min, depending on the detection methodology.

With the exception of some UBA detections, this latency is ~5 minutes for all detections.

Certain UBA detections take between 15 - 30 min due to the nature of needing to wait for a
certain amount of heterogeneous data sources while maintaining order by timestamp.

Timing 3 - Alert to Case

The timedelta between an Alert being associated with a Case compared to when the Alert is first
generated. This timing is controlled by Stellar Cyber.

The timing is < 5 min.

UBA Detection Latency Explained

User Behavior Analysis (UBA) detections sometimes require temporal ordering of source records
from heterogeneous sources (multiple different data sources). An example of such detection
methodology is the Impossible Travel Anomaly.

For a visual representation of why the latency may be 15 - 30 min for Alert Types using this
detection methodology, see the following diagram.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

