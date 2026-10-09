Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring a Central Windows Log Collector

You can configure a single Windows computer to collect logs from source computers and forward
them to the sensor. The collector and source computers must be able to communicate, and must
be on the same Active Directory domain.

To configure a central windows computer to collect logs from source computers and forward
them to a sensor, you will:

Configure a central Windows computer (collector) to collect logs.

Configure the source Windows computers to forward their logs to the collector.

Configure the sensor in Stellar Cyber.

 Our examples use Windows 10. Other versions of Windows might have different field

names or locations.

Configuring the Collector to Collect Logs
You must configure the collector to:

start the event collector service

subscribe to the events

Starting the Collector Service

To start the collector service:

1. Log in to the collector.

2. Run a terminal session as an administrator.

3. Run the wecutil quick-config command.

4. Enter Y to proceed. The Windows Event Collector service begins.

5. Enter exit to end the terminal session.

Subscribing to Events

To subscribe to events:

1. Log in to the collector.

2. Open the Computer Management app.

3. Open System Tools | Event Viewer.

4. Right-click on Subscriptions.

5. Click on Select Subscriptions.... The Subscription Properties screen appears.

6. Enter a Subscription name.

7. Enter a Description.

8. Click Select Computers. The Computers dialog box appears.

9. Choose the source computers you want to receive logs from. Click Test to test the

connection if you want.

10. Click OK.

11. Click Select Events.... The Query Filter screen appears.

12. Select the events you want to receive. Note the names of the events you selected, as

you'll need to configure the source computers to send those events.

13. Click the Event logs dropdown.

14. Select Windows Logs.

15. Open Applications and Service Logs | Microsoft.

16. Select Windows.

17. Click outside of the dropdown to close it.

18. Click OK.

19. Click OK. You should now see events in the Event Viewer.

Configuring Source Forwarding Computers
You can configure multiple Windows computers to send logs to the collector. You must configure
the source forwarding computers to:

enable remote management

set the collector as the destination for the logs

send logs to the collector

Enabling Remote Management

To configure a source forwarding computer for remote management:

1. Log in to the forwarding computer.

2. Run a terminal session as an administrator.

3. Run the winrm quickconfig command.

4. Enter Y to start the service with delayed auto start.

5. Enter Y to enable the exception.

6. Enter exit to end the terminal session.

Setting the Collector as the Log Destination

To configure the source forwarding computer to send logs to the collector:

1. Log in to the forwarding computer.

2. Open the Computer Management app.

3. Open System Tools | Local Users and Groups | Groups.

4. Right-click on Event Log Readers.

5. Click on Add to Group.... The Event Log Readers Properties dialog box appears.

6. Click Add.... The Select Users dialog box appears.

7. Click Object Types.... The Object Types dialog box appears.

8. Ensure that Computers is enabled.

9. Click OK.

10. Select the collector.

11. Click OK.

12. Click OK.

Sending Event Logs to the Collector

To configure the source forwarding computer to send the event logs to the collector:

1. Log in to the forwarding computer.

2. Run a terminal session as an administrator.

3. Run the wevtutil gl command for each event name. For example, for security

events:

wevtutil gl security

A display similar to the following appears.

Note the string following channelAccess.

4. Run:

wevtutil sl Security /ca:O:BAG:SYD:(A;;0xf0007;;;SY)(A;;0x7;;;BA)
(A;;0x1;;;BO)(A;;0x1;;;SO)(A;;0x1;;;S-1-5-32-573)(A;;0x1;;;S-1-5-20)

5. Run the wevtutil gl security command again. The channelAccess string should

now match the new string.

6. Repeat for each event category.

7. To verify that the logs are enabled, run:

get log ForwardedEvents

get log Microsoft Windows TCPIP/Operational

8. Reboot the computer.

Configuring the Sensor
To configure the sensor to receive the logs from the collector, on Stellar Cyber:

1. Click System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles. The

Sensor Profile Configuration page appears.

2. Click  to edit the profile used by the sensor. The Edit Sensor Profile screen appears.

3. Open the Windows options.

4. Open the Other Channels options.

5. Enter Microsoft Windows TCPIP/Operational in the Types field.

6. Click Add. Microsoft Windows TCPIP/Operational appears in the Added box.

7. Click Submit.

The sensor can now receive the events forwarded by the collector.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

