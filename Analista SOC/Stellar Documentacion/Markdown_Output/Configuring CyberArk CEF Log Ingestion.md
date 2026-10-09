Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring CyberArk CEF Log Ingestion

For CyberArk CEF log ingestion, configure CyberArk to forward the Syslog messages (in CEF
format) to the Stellar Cyber sensor IP address on port 5143/UDP.

To ingest CyberArk CEF:

1. Configure CyberArk Enterprise Password Vault
2. Verify Ingestion

Configuring CyberArk Enterprise Password Vault
To configure CyberArk Enterprise Password Vault to send Syslog messages (in CEF format) to
the Stellar Cyber sensor:

1. In the DBParm.ini file, configure the following parameters:

SyslogServerIP — Enter the IP address of the Stellar Cyber sensor.

SyslogServerPort — Enter port 5143/UDP to forward the logs to the Stellar
Cyber sensor.

SyslogMessageCodeFilter — Specify the message codes that will be sent
from the CyberArk Enterprise Password Vault to the Stellar Cyber sensor
through the Syslog protocol. You can specify message numbers (separated by
commas), ranges of numbers, or both. For example, to specify messages 1, 2,
3, 30, and 5-10, use the following: 1,2,3,5-10,30.

SyslogTranslatorFile — Specify the XSL file used to parse CyberArk audit
records data into the Syslog protocol. The Syslog subfolder in the CyberArk
Server installation folder contains sample XSL translator files.

2. Copy the Arcsight.sample.xsl XSL translator file from the Syslog subfolder of the

CyberArk Server installation folder to the location specified in the
SyslogTranslatorFile parameter in the DBParm.ini file.

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Set Indices as Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

