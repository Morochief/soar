Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

ATH Example: Blocking a Port Scanning Source
IP

Create an Automated Threat Hunting (ATH) playbook that notifies you when a source IP address
is detected pinging a specified destination IP address on more than 20 destination ports. This is
known as port scanning and is a common technique used to identify open ports on a target host.
While port scans are often used during legitimate security assessments, they can also indicate
hostile reconnaissance. Any alert triggered by this playbook requires further investigation, such
as checking whether the source IP address belongs to a known vulnerability scanner or an
unrecognized external system.

This example also includes instructions on how to use nested calculations in an ATH playbook.

Configure the Alert
Create an alert that runs a query every 5 minutes on the Traffic index.

1. Navigate to Automation | Automation and select the Create button to add a playbook.

2. Enter the following in the Alert Configuration section:

Name: Port Scan Block

Description: Alert when a possible port scan is detected

Schedule type: interval

Run every: 5 minute(s) over all selected tenants

Schedule: Toggle off (default setting)

Mute: Toggle off (default setting)

Tenants: All Tenants

Indices: Traffic

Rule Type: Query

Build a Query
Create a query that looks for new records with a dstip of 10.16.8.131. This is the IP address that
appears to be the target of port scans.

1. Select New Query.

2. Enter the following:

Query Name: Port Scan

Description: Query for possible port scan activity

Find documents where ALL of the following criteria are met.

Select + Add condition and enter dstip, within, 10.16.8.131.

3. Select Save to save your query.

Add Calculations to the Query

In the Calculations section, build a series of nested calculations to match the top five source
IP addresses that are probing 10.16.8.131 on more than 20 destination ports. This behavior is
characteristic of intentional port scanning, where a source attempts to discover open or
responsive services on a target host by sweeping across multiple ports.

1. Toggle Calculations on.

2. Select  to add a calculation.

3. Enter the following to match the top five source IP addresses probing 10.16.8.131:

Name: First_srcip_agg

Calculation type: Top

Field to calculate on: srcip

Calculation By: count

Size: 5

4. Select Add Subgroup and add a nested calculation for the top destination IP address:

Name: Second_dstip_agg

Calculation type: Top

Field to calculate on: dstip

Calculate By: count

Size: 1

 Because this query is for just one destination IP address (10.16.8.131), the size is
1. If your query is for multiple destination IP addresses, you can set this to a larger
size.

5. Select Add Subgroup to add a third nested calculation that matches source IP

addresses probing more than 20 destination ports.

Name: Third_dstport_agg

Calculation type: Metric

Calculate By: unique count of dstport

Configure a Condition
To look for hosts probing 10.16.8.131 on more than 20 ports, add a condition that triggers if the
count of the third calculation (Result of Third_dstport_agg) is greater than or equal to 20.

Condition Name: Match

Type: Compare List

Comparison: At least one, Result of Third_dstport_agg, is greater than or equal to, 20

Configure Actions
Finally, you must configure a Firewall/Security Switch action to block the IP address when the
Match condition you configured in the previous section is detected. Refer to Configuring
Firewall/Security Switch Actions for details on configuring this type of action.

When you have finished, select Submit to save and immediately run the playbook.

The new playbook appears in the Automated Threat Hunting Playbooks list.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

