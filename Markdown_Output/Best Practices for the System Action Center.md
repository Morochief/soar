Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Best Practices for the System Action Center

The System Action Center helps you receive different types of notifications when important
system events take place; for example, when a connector isn't seeing data or when your license
limits have been exceeded. The best practices covered in this topic can help you get the most
out of the System Action Center. See the following sections for details:

General Best Practices

Best Practices for License Monitoring

Best Practices for Connector Monitoring

General Best Practices

Understand the Types of Notifications Available – Familiarize yourself with the
available notification mechanisms. All notifications appear in the Stellar Cyber built-in
Notification Center. In addition, you can also set up notifications using email. Eventually,
you'll also be able to configure both Slack and API notifications. These mechanisms let
you receive alerts and notifications related to Connector performance, Case
Management, and License data integrity.

Perform Historical Notification Analysis – Use the System Action Center to review
recent and historical notifications. Analyzing past notifications can provide insights into
recurring issues or patterns, helping you take proactive measures to prevent data
integrity problems.

Collaborate – Determine the appropriate response to notifications with your team.
Work to establish a process for investigating and resolving data integrity issues. Ensure
that clear communication channels are in place to escalate critical alerts and facilitate
timely actions.

Fine-Tune Continually – Regularly review and refine your notification settings based
on the changing needs of your organization. As you add or modify connectors and log
sources, be sure to adjust the monitoring settings and notification thresholds
accordingly. Continual fine-tuning ensures that your data integrity monitoring remains
effective and aligned with your evolving requirements.

By following these best practices, you can leverage the System Action Center to monitor
Connector data integrity effectively. The timely detection of data flow issues will enable you to
maintain the integrity of your security operations and ensure uninterrupted data analysis.

Best Practices for License Monitoring
Configure License Enforcement and Usage Notifications – As an Operations Analyst or
MSSP Operations Manager, it is crucial to monitor license usage. Set up notifications to receive
alerts when license limits are exceeded. This helps you track usage and take necessary actions,
such as provisioning additional licenses or optimizing resource allocation. The tables below
provide some sample license enforcement and usage notifications for common situations.

License Enforcement Examples

The Need

The Notification

I want to monitor our entire account license status overall and

I configured a notification to send myself an email when the

need to configure a license enforcement notification.

license state drops to warning, violation, or out-of-compliance.

I want to monitor our entire account license usage overall and

I configured a notification to send myself an email when the

be notified if the usage is exceeded.

license limit is exceeded on a given day.

License Usage Examples

The Need

The Notification

I have multiple customers with different licenses and

I configured a notification for each individual tenant to send myself an

need to track their license usage.

email when the assets exceed a limit on a given day.

I have multiple customers with different licenses and

I configured a notification for each individual tenant to send myself an

need to track their license usage.

email when ingestion exceeds a limit on a given day.

Best Practices for Connector Monitoring
Observing the following best practices for connector monitoring can help alert you to potential
data integrity issues as they take place:

Monitor Connector Data Flow – Extend your data integrity monitoring to include connectors.
Identify critical connectors and set up notifications to receive alerts when a connector fails to
send data within the specified time window. For example, you can configure a notification for
connectors that do not provide data for more than 12 hours.

Customize Notification Windows by Connector Type – Understand the requirements of your
organization and tailor the notification windows accordingly. Some connectors may require tighter
notification windows (for example, an hour) while others may be more tolerant and can be
monitored with longer windows (24 hours, for example). Adjust the notification thresholds based
on the criticality of the data and the potential impact of its absence.

Examples

The Need

The Notification

I have a connector (for example, Crowdstrike) configured

to collect logs every five minutes. I want to know when it

is not sending data.

I configured a System Action to send myself an email when data isn’t

received on this connector for longer than 12 hours.

The Need

The Notification

Next steps: Once the email is received, check the connector status

and data. If you continue to have issues, reach out to the Stellar

Cyber Customer Success Team.

Choosing a Sensible Interval for Connector Monitoring

Most connectors have a customizable time interval for pulling data. Generally speaking, a good
place to start when configuring notifications for connectors that haven't sent data is at an interval
of 12 hours. Monitor both your notifications and the Visualize | Ingestion dashboard to keep an
eye on how much data is coming in on each connector and whether your settings are providing
the visibility that you need. Then, adjust as needed. For example, if a given connector has a lot
of data ingestion, you may need to use a smaller interval to see data integrity issues in real time.

When configuring connector monitoring notifications, keep in mind that the following connectors
have static run times:

MSSQL – 5 min

Mimecast – 5 min

Proofpoint on Demand – 1 min

Azure Eventhub – 2 min

AWS CloudTrail – 5 min

Broadcom WSS – 5 min

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

