Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Best Practices and System Design Guidance

Your success is very important, both to you and to us. The following best practices help ensure
your success with Stellar Cyber:

Deploying
Upgrading
Disaster recovery
Data durability and availability
Capacity planning

Deployment Best Practices
When you deploy Stellar Cyber you need:

HTTPS access to the user interface
Firewall (or proxy) configurations

To get data from network and security sensors
To communicate with and get updates from Stellar Cyber

In your deployment we strongly recommend:

Configure an Active Directory connector. This provides user profile details for our User
Behavior Analytics.
Install a Windows Server Sensor or modular sensors with coverage of:

Your domain controller. This enriches data with IP addresses for users.
Your DHCP server. This provides IP addresses for host names, so we can
track assets when IP addresses change.

Configure a playbook to get notifications about:

Sensor ingestion problems (no new data from a sensor for 15 minutes)
No alerts (no new security events for 15 minutes)
No ingestion (no new raw events for 15 minutes)

When there is no clear need for session deduplication (one sensor per a network
segment in general), disable the data deduplication on DA to eliminate performance
impacts.

Upgrade Best Practices
Upgrade procedures are documented in the release notes.

To prepare for the upgrade:

Back up the data and configuration
Make sure the sensors are up and running
Take note of the ingestion rate
Take note of the number of alerts
Make sure the system health indicator shows 
Run the pre-upgrade check

New features, updated ML algorithms, and enhanced configurations may change ingestion and
detection patterns. We recommend the following to ensure a smooth upgrade:

Upgrade sensors with the Sandbox and IDS features enabled before sensors with the
only the Network Traffic feature enabled. Sensors with Network Traffic enabled send
data to sensors with Sandbox and IDS enabled for additional processing.
Upgrade sensors in batches instead of all at once.
For server sensors (agents):

Upgrade a small set of sensors that cover non-critical assets.
After 24 hours, ensure that your ingestion is as expected, then upgrade a
larger set.
After 24 hours, ensure that your ingestion is as expected, then upgrade the
remaining server sensors.

To verify that the upgrade was successful:

Check the Current Software Version on the System | ORGANIZATION
MANAGEMENT | Software Upgrade page.
Make sure the sensors are up and running.
Check the ingestion rate and make sure it is as expected.
Check the number of alerts and make sure it is as expected.
Check the system health indicator:

 indicates a perfectly healthy system.
 indicates minor issues. Monitor the system for 30 minutes. If the issues
remain, investigate further.
 indicates major issues. Contact Technical Support.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

