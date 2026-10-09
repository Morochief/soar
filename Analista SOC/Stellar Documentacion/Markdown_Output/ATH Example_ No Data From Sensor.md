Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

ATH Example: No Data From Sensor

Create an Automated Threat Hunting (ATH) playbook that notifies you when the Data Processor
(DP) has not received any data from a sensor for 15 minutes. This condition might indicate a
network disruption, sensor misconfiguration, or sensor failure. Use the alert to initiate an
investigation—such as checking sensor connectivity, verifying its configuration, or escalating to
network infrastructure support.

Configure the Alert
Create an alert that runs a query every 5 minutes on the Monitoring index.

1. Navigate to Automation | Automation and select the Create button to add a playbook.

2. Enter the following in the Alert Configuration section:

Name: No Data from Sensor

Description: Notify when the DP hasn't received data from a sensor for more than
15 minutes

Schedule type: interval

Run every: 5 minute(s) over all selected tenants

Schedule: Toggle off (default setting)

Mute: Toggle off (default setting)

Tenants: All Tenants

Indices: Sensor Monitoring

Rule Type: Query

Build a Query
Create a query that looks for no change in bytes transmitted from a specific sensor.

1. Select New Query.

2. Enter the following:

Query Name: Sensor Data Outbytes

Description: Query for sensor activity

Find documents where ALL of the following criteria are met.

Select + Add condition and enter engid, is, <sensor_id>.

Select + Add condition and enter outbytes_delta, is, 0.

3. Select Save to save the query.

Configure a Condition
In the Condition Configuration section, configure a condition that triggers one or more actions
if there are 3 consecutive hits, indicating no change in data from the sensor for 15 minutes.

Condition Name: 3 Consecutive Hits

Type: Compare Value

Comparison: Total Hits, is greater than or equal to, 3

Configure an Email Message as the Action
You can configure any number of actions to take place if your playbook gets the specified
number of hits. In this example, the action is to send an email notification.

1. Set the Trigger on condition to Three Consecutive Hits.

2. Enter the following to set up email messages:

Type: Email

Recipients: Either type in an email address to use or choose a previously configured
recipient from the drop-down list.

 Refer to Adding a Recipient for information on managing recipients globally.

Subject: Sensor Down?

Priority: Normal

Include Interflow: (select to attach Interflow records to the email)

Email Body: Enter the following:

We have {{ctx.payload.hits.hits.total}} records over 15 minutes.

Mute: (disable)

See Configure Actions for details on configuring each type of action.

Save & Run the Playbook
Select Submit to save and immediately run the playbook.

The new playbook appears in the Automated Threat Hunting Playbooks list.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

