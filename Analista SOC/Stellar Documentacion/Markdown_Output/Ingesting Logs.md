Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Ingesting Logs

Log ingestion is always enabled for Modular Sensors. Use this topic to configure log ingestion
from your source devices to your sensors. Keep in mind the following:

Logs that include a security event are sent to the security index.

Logs that include source or destination IP addresses or ports are sent to the traffic
index.

All other logs are sent to the syslog index.

Stellar Cyber limits the number of log sources you can point at a given sensor as
follows:

Sensors with 8 GB or less of memory accept a maximum of 100 log sources.

Sensors with more than 8 GB of memory accept a maximum of 200 log
sources.

 Log sources beyond the limit are aggregated under the special source IP address

of 0.0.0.0.

To configure log ingestion:

1. In general, configure your source device to send logs to a Stellar Cyber Modular Sensor

with the following information:

The IP address of the sensor as the destination for the logs

The port on which to send the logs if the device uses a standard format

The port on which to send the logs if the device uses a vendor specific format

Formatting for the logs, which should correspond to the formatting defined for
the port selected

(See the example configuration for SentinelOne.)

 Logs sent to the generic 514/6514 syslog ports on the sensor can be relayed to

vendor-specific parser ports. Using this approach helps you minimize the ports you

need to open in your firewall. See the Specific Port Destinations or Port Relay?
section below for details.

2. Configure any firewalls between the device and the Modular Sensor to open the ports

the logs are sent over.

3. Verify that Stellar Cyber is receiving log events:

a. Select Threat Hunting.

The Threat Hunting page opens with the Interflow Search tab active.

b. Select Syslog from the Indices drop-down list.

Syslog events are displayed.

c. Check the table at the bottom of the page for events from your device.

 If you're ingesting Windows logs, you can configure a central Windows computer to collect
the logs and forward them to the sensor. You can also use a Windows Server Sensor to
forward syslog records to a Modular Sensor for eventual parsing, filtering, and shipment to
the Stellar Cyber Platform.

Specific Port Destinations or Port Relay?
It's a best practice in Stellar Cyber to send logs to their vendor-specific parsers whenever
available. In previous releases, this was accomplished by referring to the list of supported
vendor-specific ports, pointing your log sources to that port on the sensor IP address, and
opening the port in your firewall.

This approach is still available and can be used. As an alternative, however, you can configure
your sensors to accept log traffic on the generic syslog ports of 514 (non-TLS) or 6514 (TLS) and
relay that traffic to vendor-specific ports internally based on the IP address of the source traffic.

Configure port relay in the System | DATA SOURCE MANAGEMENT | Parsers | Log Sources
page.

Timezones and Log Ingestion
Stellar Cyber converts all log timestamps to UTC during log ingestion. Timezones are handled as
follows:

If a log includes a timezone, Stellar Cyber preserves that timezone during the
conversion to UTC.

If a log does not include a timezone, Stellar Cyber uses the timezone of the receiving
sensor.

 During installation, the timezone for sensors are automatically set to UTC+0. Since the logs
for some security products might only include the local time without a timezone, Stellar Cyber
recommends that you set the sensor timezone to the same timezone as your security
product.

Monitoring Log Ingestion

Sensors send statistics to the Data Processor quantifying the data being sent and its source
once per minute. This data is stored in the Sensor Monitoring (aella-ade) index on the Data
Processor. You can use the Threat Monitoring interface to review this data and add it to charts
and dashboards. For example:

1. Log in to Stellar Cyber and navigate to Threat Hunting.

2. Select the Indices drop-down list and select Sensor Monitoring.

3. Scroll down to the Interflow records table, enter msgtype:39 in the Search field, and

press Enter to filter on just this msgtype.

This is the msgtype that quantifies log ingestion by sensor.

The table updates to show all entries passing the global filters at the top of the display
for Message Type 39.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

