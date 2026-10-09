Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Machine Learning Model Summary

Stellar Cyber uses Machine Learning (ML) to detect both unknown bad or risky behavior
(primarily through anomaly detection) and known bad or risky behavior where a rule based alert
is incapable of performing the detection. Use this topic to understand the different ML concepts
and models employed within Stellar Cyber.

Machine Learning Models
The machine learning models are Unsupervised and Supervised.

Unsupervised

The following are Unsupervised ML models:

Time Series Analytics (TSA) Model
Population Time Series Analytics (PTSA) Model
Threshold Random Walk (TRW) Model
Graph Model
Rare Model

Time Series Analytics (TSA) Model

The TSA model uses the historical distribution for a given detection key (for example, user,
source IP address, and so on) to predict its current behavior. The model maintains statistical
evidence of each detection key. The number of alerts for each key becomes consistent as the
model collects more statistical evidence.

TSA model based detection involves three different types of detections:

1. spike detection

2. continuous low detection

3. rare detection

The spike detection determines whether a data point’s value is a spike by comparing it to a
threshold calculated statistically from historical data points. The continuous low detection checks
if a key’s value stays low for a period of time. The rare detection checks if a detection key
suddenly shows up after a long time of silence (for example, greater than 14 days).

Examples of alert types using this model:

Outbytes Anomaly

Long Application Session Anomaly

Population Time Series Analytics (PTSA) Model

The PTSA model looks at the whole population in contrast to individual keys. It learns periodic
population statistics from historical peer data and looks for anomalies that deviate from typical
behavior in corresponding time periods. If the behavior change is significant, an alert is raised.
As the model collects more historical evidence, accuracy improves.

Examples of alert types using this model:

External/Internal SMB Read/Write Anomaly

Application Usage Anomaly

Threshold Random Walk (TRW) Model

The TRW model follows the distribution of data that may change constantly, without the need of a
separate training period. It accumulates positive and negative scores based on activities. If the
score passes the given upper or lower bound, an alert is raised. For example, if the number of
failed login activities keeps increasing in several continuous time buckets, an alert is triggered.
The number of alerts does not solely depend on the time window in which the data is collected.

Examples of alert types using this model:

External/Internal User Login Failure Anomaly

External/Internal IP/Port Scan Anomaly

Graph Model

The graph model measures the relationship of parent-child pairs (such as, parent and child
processes) to detect behavior (or relation) change. It monitors the parent in particular, which has
high stability and low diversity. If the change of stability and diversity status is larger than a
predefined threshold, an alert is raised. (Stability is the number of days that the parent does not
have a new child. Diversity is the number of unique children a parent has.) With more data (for
example, the longer the model runs), the number of alerts will decrease.

Examples of alert types using this model:

Abnormal Parent/Child Processes

Outbound Destination Country Anomaly

Rare Model

The rare model checks if the presence of a given detection key appears in the past 14 days or
not. If not, an alert will be reported. The number of alerts will decrease as the rare model collects
more evidence over longer periods of time.

Examples of alert types using this model:

Uncommon Process Anomaly

External/Internal Firewall Policy Anomaly

Supervised

The following are Supervised ML models:

Support Vector Machine
Long Short-Term Memory

Support Vector Machine

Support Vector Machine (SVM) is a supervised classification model that determines a decision
boundary among benign and suspicious data points based on a set of indicators. We deliver pre-
trained SVM models specific to individual Alert Types.

Examples of alert types using this model:

DNS Tunneling Anomaly

External/Internal Suspected Malicious User Agent

Long Short-Term Memory

Long Short-Term Memory (LSTM) is a deep recurrent neural network that takes a sequence of
input data and determines the suspiciousness of the input sequence based on a set of indicators
that the network explores. We deliver pre-trained LSTM models specific to individual Alert Types.

Examples of alert types using this model:

Domain Generation Algorithm (DGA) Anomaly

Approach To Data And Training
The following are approaches to data and training for Unsupervised and Supervised Machine
Learning.

Unsupervised Machine Learning

Unsupervised Machine Learning models do not leverage labeled data to operate. Instead, they
learn historical patterns in data, and can make judgements on future data’s fitting to past
patterns. Before an Unsupervised ML Alert Type triggers alerts in Stellar Cyber, it must meet two
data conditions:

Two weeks of baselining

Enough occurrences of certain detection keys (for example, user, source IP address,
and so on) relevant to each Alert Type (this will vary from Alert Type to Alert Type)

Simply put, for the first condition, no Unsupervised ML Alert Type will trigger alerts upon two
weeks of initiating an organization in Stellar Cyber. For the second condition, Stellar Cyber
studies all of its models and encodes thresholds on certain detection key occurrences before it
triggers alerts. Alert Types with this second condition in place are:

User Login Location Anomaly requires at least 20 past logins for a user and a time span
of 14 days for each user, beginning from their first login.

Login Time Anomaly requires at least 20 past logins for a user and a time span of 14
days for a user, beginning from their first login.

 Versions prior to 5.X.X, do not require a time span of 14 days for a user.

All TSA-based Alert Types with “spike detection” require a minimum of 20 data points on
each detection key and a minimum time span of 14 days to build the statistical
evidence.

 Versions prior to 5.X.X, do not require a time span of 14 days.

All PTSA-based Alert Types (Scanner Reputation Anomaly, External/Internal SMB Read
Anomaly, External/Internal SMB Write Anomaly, External/Internal Firewall Denial
Anomaly, Application Usage Anomaly) require per-tenant 14-day baselining.

 Versions prior to 5.X.X, required 14-days of per-deployment baselining, not per-

tenant.

The reason for these conditions is that without adequate data for baselining, the predictive
confidence would be very low, thus creating detection noise.

Supervised Machine Learning

Supervised Machine Learning models leverage labeled data for training purposes, and then
make predictions on future data based on the learning from that training data. Stellar Cyber
trains its Supervised ML Alert Type models offline and then ships a complete model within Stellar
Cyber. These models may be updated based on new offline training performed.

Stellar Cyber acquires its labeled data through a variety of means:

Manually created datasets from real environments

Manually created datasets from simulated environments

Open source datasets

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

