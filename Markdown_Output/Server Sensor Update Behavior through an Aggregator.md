Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Server Sensor Update Behavior through an
Aggregator

In many deployments, Windows Server Sensors and Linux Server Sensors do not communicate
directly with the Data Processor (DP). Instead, they send and receive data through a Modular
Sensor configured as an aggregator. The aggregator serves as an intermediary between the
Server Sensors and the DP, forwarding data and retrieving update files when sensors request
them.

Some deployments use a single Modular Sensor as an aggregator, and some use two Modular
Sensors configured as a high availability (HA) pair. The use of an HA aggregator pair does not
change the update or upgrade behaviors described here. Windows and Linux Server Sensors
continue to retrieve updates and upgrades according to their operating system.

Each Server Sensor independently runs a scheduler, which periodically checks the DP for
updates. The scheduler operates on the Server Sensor itself, not on the aggregator or DP, and
initiates update requests. When an update is available, the sensor downloads the necessary files
through the aggregator. If the download fails, the sensor might attempt to retrieve the update
directly from the DP as a fallback.

In this section, you can learn how Server Sensors retrieve updates when an aggregator is in use,
what types of files are downloaded, and under what conditions a sensor might bypass the
aggregator to communicate directly with the DP.

Scheduled Updates through an Aggregator
When a Windows Server Sensor or Linux Server Sensor is deployed with an aggregator, the
update process follows four main steps:

1. A Server Sensor initiates a request to check for updates.

Every 30 minutes (by default), the scheduler runs on the Server Sensor and checks the
DP for available updates.

Download Operations: The Server Sensor attempts to retrieve updates by
first contacting the primary aggregator. If that fails, it attempts to contact the
secondary aggregator, and finally the Data Processor itself.

Upgrade Operations – Windows Server Sensor: Attempts the primary
aggregator, then the secondary aggregator, and finally the DP.

Upgrade Operations – Linux Server Sensor: Uses the configured
aggregator only. No fallback to direct DP connection.

Operation Type Sensor Type

Behavior

Download

Windows or Linux Attempts primary aggregator → secondary aggregator → DP

Upgrade

Windows

Attempts primary aggregator → secondary aggregator → DP

Upgrade

Linux

Uses aggregator only

2. The DP responds through the aggregator to the sensor with update tasks.

The DP provides information on available updates, including new software versions,
configuration files, and security rule updates.

3. The Server Sensor downloads update files through the aggregator.

Files are retrieved from the DP through the aggregator. The downloaded files are stored
in the C:\ProgramData\StellarCyber\Windows Agent Sensor\config and
C:\ProgramData\StellarCyber\Windows Agent Sensor\aella_update\tmp
directories on Windows and the /etc/stellarcyber/ directory on Linux.

4. The update process is logged in aella_update.log.

The sensor logs all download attempts and update executions. If the sensor fails to
download through the aggregator, it logs the fallback attempt to direct DP
communication.

Example log entries:

2025-04-15 12:14:03,316|aella_update|INFO|Downloaded from aggregator
192.168.5.5

2025-04-15 12:14:04,249|aella_update|INFO|Fallback to direct download
from cm-acmecorp.stellarcyber.cloud

Downloaded Update Files
During an update, a Server Sensor might download the following files:

Files

ds_tasks.json

.msi/.msp files

Purpose

Checks for pending update tasks on the DP.

Update packages for upgrading to a new software version

(Windows only). Also included is the download_image.exe file,

which is extracted after download and used to retrieve updates

from the DP.

Custom parsers

Files that update the ability of the sensor to process and

normalize logs.

Threat intelligence updates

Updated detection rules and heuristics for security analysis.

Fallback to Direct DP Communication
In certain situations, a Server Sensor might attempt to bypass the aggregator and connect
directly to the DP over TCP port 8443 to download updates. This is a fallback mechanism
triggered when the sensor can’t retrieve files through the aggregator.

Reasons to Fall Back

The sensor encounters an aggregator communication failure.

If the sensor fails to download update files through the aggregator, it retries directly from
the DP. The failure can be caused by network issues, misconfigured firewall rules, or
connectivity problems between the aggregator and DP.

TCP port 8443 is not open from the aggregator to the DP.

The aggregator must have TCP port 8443 open to allow update file transfers from the
DP. If this port is blocked, the sensor cannot download files through the aggregator and
must fall back to direct DP communication.

The aggregator is temporarily unavailable.

If the aggregator is down or undergoing maintenance, the sensor switches to direct
communication with the DP.

The sensor experiences a failed initial download attempt.

If the sensor attempts to download ds_tasks.json or an update package and
encounters an error, it automatically retries using the direct IP address of the DP.

Update Logging Behavior

The sensor records its update attempts in the aella_update.log, including whether the file was
successfully downloaded via the aggregator or if it switched to direct DP communication.

Example log entries:

2024-08-06
12:14:03,316|aella_update|INFO|"c:\ProgramData\StellarCyber\aella_updat
e\20231002_4.3.7_12c2f39\download_image.exe" -cm 192.168.5.5 -path
"C:/ProgramData/StellarCyber/Windows Agent Sensor/config" -image
ds_tasks.json -flag json_task

2024-08-06
12:14:04,249|aella_update|INFO|"c:\ProgramData\StellarCyber\aella_updat
e\20231002_4.3.7_12c2f39\download_image.exe" -cm cm-
acmecorp.stellarcyber.cloud -path "C:/ProgramData/StellarCyber/Windows
Agent Sensor/config" -image ds_tasks.json -flag json_task

In this example, the first attempt downloads ds_tasks.json from the DP via the aggregator at
192.168.5.5. When the aggregator download fails, the sensor tries to download the file directly
from the DP at cm-acmecorp.stellarcyber.cloud.

Preventing Direct DP Access

To ensure that all update downloads occur through the aggregator and avoid unexpected direct
connections to the DP, take the following steps:

1. Verify that TCP port 8443 is open between the aggregator and DP.

This allows the aggregator to retrieve update files from the DP successfully.

2. Check firewall rules and routing configurations.

Ensure that traffic between the Server Sensor and aggregator is not being blocked or
disrupted.

3. Monitor the logs for repeated fallback behavior.

Regularly check aella_update.log for signs that the sensor is bypassing the aggregator.

4. Ensure the aggregator is online and functioning.

If the aggregator is temporarily unavailable, sensors default to direct DP
communication.

Summary
Windows and Linux Server Sensors configured to use an aggregator should normally download
updates through it. However, if the aggregator becomes unavailable or encounters connectivity
issues, Windows Server Sensors fall back to direct communication with the Data Processor.
Linux Server Sensors, by contrast, always rely on the configured aggregator for updates and
upgrades even if connectivity issues occur. All fallback behaviors are recorded in
aella_update.log.

Keeping TCP port 8443 open, monitoring logs for unexpected behavior, and maintaining proper
firewall and network configurations ensures consistent and reliable update and upgrade
operations. For troubleshooting, refer to System | Logs in the Stellar Cyber UI or examine
aella_update.log on the Server Sensor host.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

