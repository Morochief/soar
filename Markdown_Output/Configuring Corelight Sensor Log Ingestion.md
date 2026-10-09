Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Corelight Sensor Log Ingestion

For Corelight Sensor log ingestion, configure Corelight to export to the Stellar Cyber log
forwarder IP address and port.

Configuring Corelight Sensor
To configure the Corelight Sensor to ingest logs:

1. Choose Sensor.

2. Choose Export.

3. Choose EXPORT JSON OVER TCP.

4. For the JSON TCP SERVER, enter the IP address of the Stellar Cyber log forwarder

followed by a colon and port number 5575. For example, 192.168.1.9:5575.

5. Choose the logs to exclude. The recommended exclude list is: corelight_audit_log,

corelight_metrics_bro, corelight_metrics_cpu, corelight_metrics_disk,
corelight_metrics_docker, corelight_metrics_iface, corelight_metrics_memory,
corelight_metrics_s3, corelight_metrics_sftp, corelight_metrics_smartpcap,
corelight_metrics_suricata, corelight_metrics_system, corelight_metrics_utilization,
corelight_overall_capture_loss, suricata_stats, suricata_profiling

6. Select Apply Changes.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

