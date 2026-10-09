Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring ERSPAN Ingestion

You can configure a Modular Sensor to ingest GRE traffic mirrored with ERSPAN.

 During installation, the timezone for sensors are automatically set to UTC+0. Since the logs
for some security products might only include the local time without a timezone, Stellar Cyber
recommends that you set the sensor timezone to the same timezone as your security
product.

To ingest ERSPAN:

1. Configure ERSPAN on your Cisco switch.
2. Configure your sensor to ingest from the Cisco switch.
3. Verify Ingestion.

Configure ERSPAN on Your Cisco Switch
To configure ERSPAN on your Cisco switch:

1. Configure GRE.
2. Configure ERSPAN to mirror traffic to a specific port.
3. Note the IP address of the switch and the port you're mirroring to.

Configure Your Sensor to Ingest Logs from the Cisco
Switch
To configure your sensor to ingest ERSPAN traffic from the Cisco Switch:

1. Log in to the Modular Sensor CLI and enter the following command:

2. set interface ethernet<interface#> ip <IP address of the Cisco

switch>/<network mask>

The interface# in the command above corresponds to the monitor port label on the
sensor itself (for example, Ports 1..7 on a Photon 300).

For example:

set interface ethernet1 10.1.10.27/24

3. Verify with the show interface command.

You should see the link up for the interface (ethernet1 in this example) and the IP
address of the mirror port (10.1.10.27).

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Set Indices as Traffic.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

