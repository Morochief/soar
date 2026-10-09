Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

ATH Example: Half-Opened Sessions

Create an Automated Threat Hunting (ATH) playbook to detect devices that formed unusually
high numbers of half-opened sessions in a short period of time. A surge in half-opened sessions
over a limited timeframe might indicate unstable communication behavior, misconfigured
services, or the early stages of malicious activity. This example shows how to query traffic
records for these patterns and configure the playbook to trigger when thresholds are exceeded.

Configure the Alert
Set up the alert to run at regular intervals so that the playbook can consistently identify devices
exhibiting suspicious connection behavior. By querying for half-opened sessions every 30
minutes, you ensure timely detection of anomalies as they emerge in the network traffic.

To configure the alert:

1. Navigate to Automation | Automation and select the Create button to add a playbook.

2. Enter the following in the Alert Configuration section:

Name: Too Many Half-Opened Sessions

Description: Detect excessive numbers of half-opened sessions

Schedule type: interval

Run every: 30 minute(s) over all selected tenants

Schedule: Toggle off (default setting)

Mute: Toggle off (default setting)

Tenants: All Tenants

Indices: Traffic

Rule Type: Query

Build a Query
Construct a query that identifies traffic in the half-opened state. This state occurs when a
connection attempt is initiated but not completed—behavior that might suggest
misconfigurations, network instability, or evasion tactics. To keep the query results manageable
and actionable, limit the number of source IP addresses returned to the top 1,000 by frequency.

1. Select New Query.

2. Enter the following and then select Save:

Query Name: Half-Opened State

Description: Query for devices that have an inordinately high number of half-
opened sessions

Find documents where ALL of the following criteria are met.

Select + Add condition and enter state, is, HalfOpened.

3. Toggle Calculations on.

4. Select  to add a calculation.

5. Enter the following:

Name: Top List

Calculation type: Top

Field to calculate on: srcip

Calculation By: count

Size: 1000

Configure a Condition
Define a threshold that indicates when the observed behavior merits attention. In this example, if
the number of unique source IP addresses generating half-opened sessions exceeds three, the
condition triggers. This allows actions to be taken only when the behavior appears persistent or
widespread enough to justify investigation.

Condition Name: More than 3

Type: Compare List

Comparison: At least one, Result counts of Top List, is greater than or equal to, 3

Configure Actions
You can configure any number of actions to take place if your playbook gets the specified
number of hits. Remember to set the Trigger on condition to the condition you created (which is
automatically selected). In this example, it's More than 3.

See Configure Actions for details on configuring each type of action.

Save & Run the Playbook
Select Submit to save and immediately run the playbook.

The new playbook appears in the Automated Threat Hunting Playbooks list.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

