Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring RSPAN Ingestion

Remote SPAN (RSPAN) is an extension of the SPAN port mirroring technology that uses a
dedicated internal VLAN to mirror L2 traffic from multiple switches to a single SPAN port. All L2
traffic included as part of the RSPAN session flows out of the SPAN port and can be ingested by
a connected Modular Sensor without any special configuration.

To ingest RSPAN:

1. Configure RSPAN on your Cisco switch.
2. Connect your Sensor to the SPAN port.
3. Verify Ingestion.

Configuring RSPAN on Your Cisco Switch
To configure RSPAN on your Cisco switches, configure RSPAN to mirror specified traffic from
one or more switches to a specific SPAN port.

Connect Sensor to SPAN Port
Connect one of the data ports on a Modular Sensor to the SPAN port used as the destination for
the RSPAN session.

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Set Indices as Traffic.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

