Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using the Sensor Overview

 Learn more at Stellar Cyber Academy.

The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.

M03 Modular Sensor Concepts and Configuration (08h:56m)  

Modular Sensors Introduction (10m:00s)

Discover how Modular Sensors integrate into the Stellar Cyber Platform architecture.
Learn about different types of Modular Sensors, their deployment in virtual and
hardware forms, and their roles in data collection and analysis.

M06 Open XDR Linux Server Sensor Installation and Configuration (01h:21m)  

Server Sensor Authorization (15m:00s)

Learn how to authorize the Linux Server Sensor within the Stellar Cyber Platform, then
follow a practical demonstration of the complete authorization workflow in the data
processor. Explore how to configure sensor profiles to enable secure data transfer,
assign custom settings for tailored data monitoring, and confirm sensor status to
establish real-time data flow into the data lake.

The first time you access a link on the portal during a session, you must log in to access
content.

The System | DATA SOURCE MANAGEMENT | Sensors | Sensors page provides a list of all
known sensors that are connected to the Stellar Cyber Platform.

When a sensor is installed, it is configured with the IP address of the Stellar Cyber Platform.
When the sensor comes up, it connects to the Stellar Cyber Platform and appears in the Sensor
table automatically.

The Sensor table provides the following functions:

List the known sensors with basic information such as host name, sensor ID, IP
address, and software version

View information such as operational status, authorization, and traffic counters
Use Quick Filters to focus the display temporarily on just those sensors you need to see
(for example, all Windows Server Sensors)
Configure sensors with the use of Sensor Profiles
Remote upgrade of sensors
Remote downgrades of sensors (rollbacks)
Remove a sensor from the system
Launch the CLI for sensors.
Apply CA certificates to sensors.
Assign primary and secondary aggregators to sensors.
Download sensor logs for troubleshooting

From here, you can also navigate to the Scheduled Upgrades tab to keep track of pending
updates for sensors.

Sensor Overview List
When the Sensor Overview page appears, it shows a table of known sensors. The table is
scrollable and provides standard table functionality. In addition, you can click the Sensor Name
for any listed sensor to drill to its Sensor Details page, with detailed performance metrics and
configuration information. You can also use the Quick Filters at the top of the display to focus the
display temporarily on just those sensors you need to see (for example, all disconnected
servers).

Each sensor is listed in the table with its own row. The columns include:

[ ] – Check box to select sensors to Upgrade, open CLI Access, or Manage. Buttons for
these features appear above the table appear when one or more sensors are selected.

Name – The host name where the sensor is located. This value may not be unique
within the system since it depends on the configuration done on the system where the
sensor runs. Click the name to see sensor details.

Sensor Status – The current status of the sensor is indicated with a color-coded LED.
Refer to About the Sensor Status LEDs for details on the different conditions each of
the sensor status LEDs can indicate.

Messages – Status message, if any, for the sensor.

Internal Sensor ID – A unique ID of the sensor, as assigned by the Data Processor.

Sensor ID – A unique ID of the sensor, as configured by the user.

Authorization – The authorization status of the sensor.

IP Address – The current IP address of the sensor in use. Communication from the
Data Processor to the sensor will use this address.

Traffic Input – Total number bytes the Sensor has received. This represents the raw
data received by the sensor.

Traffic Metadata Output – Total number of bytes sent from the Sensor to the DP. This
is the amount of data sent after the raw data received has been enriched, deduplicated,
and converted to Interflow.

License – The current license type.

Security Sensor License – Indicates whether the sensor is either a physical
(device) Security Sensor, or a Modular Sensor with Security Sensor features enabled in
its Modular Sensor Profile (IDS and/or Malware Sandbox).

 Adding this column is a handy way to keep track of which sensors are consuming

your purchased Security Sensor licenses.

Sensor Profile – The sensor profile that is applied to the sensor. A sensor profile
contains configuration information that is shared between any number of sensors. See
the Sensor Profiles page for more information.

Software Version – The version of software that is running.

Log Forwarder – Log forwarding is enabled.

Edit – Edit the settings for a selected sensor. Details are
below..................................................................................................................................
........

Delete – Discard the selected sensor.

More options - Click this  button to display a menu option to Download Debug Logs.
Select this menu to download a gzip of the debug logs available for that sensor. The
download is saved according to your browser settings for download files. The unpacked
zip will appear similar to this example:

You can also use this menu to recollect the latest debug logs for the sensor before
downloading them.

Additional columns, not displayed by default,

are available.

APT

Feature

Feedback

IDS

Last Seen

Location

Log Forwarder

Malware Analyze Result

Mode

Need Upgrade

Note

OS

Packet Forwarding Interface

Platform (for example, Virtual_Machine)

Reduction Ratio

SSH Tunnel

Tenant ID

Tenant Name

Timezone

Tunnel info

Upgrade Result

VM Name

See the Tables page for more information on working with Tables.

About the Sensor Status LEDs

The Sensor Status column displays color-coded LEDs indicating the health of each sensor at a
glance:

Green – The sensor is operating normally and there are no danger or warning
conditions detected.

Yellow – At least one warning condition is affecting the sensor.

Click here to see the possible warning conditions:

Sensor disk usage exceeds 90%.

 Windows Server Sensors check the usage of the system disk every 15
seconds using the Python psutil library. If the disk usage is over 90%,
the system displays the Disk usage more than 90% warning condition.

Sensor CPU usage exceeds 99%.

Sensor feedback contains a config mismatch error message.

Sensor has not updated its status in at least five minutes.

Sensor feedback shows a failure to apply a profile with the Tenable Nessus
feature enabled to a sensor running version 4.3.3 or lower. (Tenable Nessus
support was introduced in 4.3.4.)

Sensor feedback contains at least one warning message .

Red – At least one danger condition is affecting the sensor.

Click there to see the possible danger conditions:

Sensor has an invalid Engine ID (engid)

Sensor has a conflicting Engine ID (engid)

Sensor configuration is out of sync (either the ver_sent does not match
received ver_ack or one of the two messages is missing)

Sensor memory usage exceeds 95%

Sensor feedback contains a config failure message

Sensor feedback shows at least one failure during the application of a new
sensor profile.

 The exception to this is a failure to apply a modular sensor profile with
the Tenable Nessus feature enabled to a sensor running 4.3.3 or lower.
Those failures are reported as warnings and only display the yellow
LED, as described above.

Using Quick Filters in the Sensor List

The Sensor List includes a handy set of Quick Filters at the top of the table that let you
temporarily focus the display on just those sensors you want to see for your current workflow.
Selecting one of the Quick Filters automatically limits the display to just those sensors matching
the filter (for example, all connected sensors).

Remove an applied Quick Filter by selecting it again, returning the display to an
unfiltered state.

Apply a new Quick Filter to see a different set of sensors. Quick Filters are not
cumulative; only one is applied at a time.

The following Quick Filters are available:

Online – Shows only those sensors that are currently online and connected to the
Stellar Cyber Platform.

Disconnected – Shows only those sensors that are currently disconnected from the
Stellar Cyber Platform.

Agent-mode – Shows all Server Sensors (Linux and Windows). Server Sensors are
sometimes referred to as "agents," because they are installed co-resident on a
monitored host.

Modular Sensor – Shows all sensors with a modular sensor profile applied.

Linux Agent Sensor – Shows all Linux Server Sensors.

Windows Agent Sensor – Shows all Windows Server Sensors.

Device-mode – Shows all device sensors. Device sensors include all sensors that are
not Server Sensors

Security Sensor – Shows all Security Sensors. Security Sensors are a legacy sensor
type with IDS and malware sandboxing enabled. These features are now enabled in a
Modular Sensor profile.

 Refer to Sensors for a discussion of the different types of sensors used in a Stellar Cyber

deployment.

Editing a Sensor's Settings

Some of the information associated with each sensor can be edited by clicking the
the right side of a sensor entry in the table:

 button at

Most fields are read-only. The available fields include:

Sensor ID – The internal ID for the sensor.

Tenant Name – The tenant for the sensor.

 Note that if you change a sensor's tenant assignment, any CA certificates assigned
to the sensor are automatically cleared without any notification in the user interface.

IP Address – The IP address of the sensor.

Host Name – The host name of the sensor. This value will be used in the first column of
the sensor list described above. This field does not support multibyte characters.

DNS Name – The DNS Name of the sensor. This field does not support multibyte
characters.

VM Name – The name of the VM in which the sensor is running.

Sensor Profile – This field is a dropdown menu of the available sensor profiles.

Primary Aggregator – This field is a dropdown menu of the available data aggregators.
Once you assign a Primary Aggregator, a new Secondary Aggregator field appears,
allowing to specify the aggregator to use in situations where the primary aggregator is
unreachable.

 You can also assign aggregators from directly within the Sensor Overview. Start by
checking the box for the sensor to which you want to assign an aggregator. Then,

click the Assign Aggregator button that appears at the top of the table to open a
dialog box where you can assign both a primary and secondary aggregator. See
Assigning Aggregators to Sensors for details.

Location ID – The gateway IP address. Stellar Cyber automatically detects the gateway
IP address, but this lets you set it manually.

Timezone – The timezone in which the sensor is operating.

 You can only change the timezone for device sensors. The Timezone option is

hidden for Server Sensors.

 See Timezones and Log Ingestion for information on how the sensor's timezone

is used during log ingestion.

PKT Forwarding Interface – The VXLAN interface number.

Syslog TLS Enabled – Enable to ingest TLS-encrypted logs. See Ingesting Logs over
TLS for more information. In general:

Click the adjacent CA Certificate button to download the self-signed certificate
from the sensor for installation on your log source.

If your log source does not support the self-signed certificate, you can apply a
commercial server certificate to the sensor for TLS log ingestion by first
uploading the certificate to Stellar Cyber in the Certificates page and then
applying it to the sensor on this page using the Apply Certificate | Apply
Certificate to Log Forwarder button.

 Disabling the Syslog TLS Enabled option for a Modular Sensor that is using a

server certificate removes the association between the sensor and the certificate. If
you then re-enable Syslog TLS Enabled, the sensor reverts to using the self-
signed certificate instead of using the server certificate that was previously
configured. If this happens, you can just reapply the server certificate using the the

Apply Certificate | Apply Certificate to Log Forwarder button.

AWS Mirror – Enable this to monitor traffic from a mirror port you configured on AWS.
See Configuring AWS Port Mirroring for details.

If you enable AWS Mirror, the following additional fields appear:

Physical Ethernet Port – This is the index number of the physical interface
the UDP traffic arrives on.

Port – The UDP port for the traffic.

VNI – This is the VXLAN ID you configured on AWS.

Note – Use this to keep notes about the sensor. This field does not support multibyte
characters.

To make changes, edit the fields as desired and click SUBMIT to save.

Timezones and Log Ingestion

Stellar Cyber converts all log timestamps to UTC during log ingestion. Timezones are handled as
follows:

If a log includes the timezone, Stellar Cyber preserves that time setting during the
conversion to UTC.

If a log does not include a timezone, Stellar Cyber uses the timezone of the receiving
sensor.

 During installation, the timezone for sensors are automatically set to UTC+0. Since the logs
for some security products might only include the local time without a timezone, Stellar Cyber
recommends that you set the sensor timezone to the same timezone as your security
product.

Refer to Best Practices for NTP and Timezones for more information.

Deleting a Sensor

You can click the
you delete the sensor, the sensor is removed from the list, and the sensor deletes its
configuration so it will not be discovered by Stellar Cyber.

 button at the right of a sensor's entry in the table to remove it from the list. If

Removing (Uninstalling) a Server Sensor
You can select one or more Server Sensors and click the Remove button to uninstall them from
their host(s). When you remove a Server Sensor from the Sensor List, Stellar Cyber uses a
managed uninstall workflow instead of deleting the sensor record immediately.

After you click Remove, the sensor enters a Deleting status while Stellar Cyber waits for the
uninstall result. The uninstall request is tracked in the Task Management page under the sensor
uninstall task.

If the uninstall succeeds, Stellar Cyber removes the sensor from the list automatically. If
the uninstall fails, the sensor shows an error status with the message Sensor
uninstallation failed.

If the uninstall fails, you can choose one of the following actions:

Retry to start another uninstall attempt
Delete Anyway to remove the sensor record without attempting another
uninstall

This workflow gives you visibility into sensor removal progress and lets you confirm whether the
uninstall completed successfully before the sensor record is removed.

Upgrading Sensor Software
Sensors can be upgraded manually:

Manual Upgrades – You can use the instructions in this section to upgrade sensors
manually, selecting one or more sensors in the Sensor List and clicking the Upgrade
Software button.

Use the following procedure to upgrade sensors manually:

1. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors | Sensors list

and inspect the Software Version column. Sensors that have an upgrade available are
listed with a distinctive icon in this column, as shown below:

 The system also automatically identifies sensors that are eligible for an upgrade
and informs you with a banner showing the total and including an Upgrade Now
button you can use to streamline the process.

2. Check the boxes of the sensors you want to upgrade in the Sensor List and click the

Upgrade Software button at the top of the list.

3. Stellar Cyber displays a confirmation prompt listing the sensors you've selected for the

upgrade. Verify the sensors and click the Upgrade button, as illustrated below.

4. Stellar Cyber evaluates the sensors selected for the upgrade. If one of the sensors you

selected for the upgrade already has been scheduled for an upgrade, the system
informs you of the situation and queues the remaining sensors for an upgrade.

5. Once the sensors are scheduled for an upgrade, you can keep track of the progress in

the Scheduled Upgrades tab. The illustration below shows an example of the
Scheduled Upgrades tab:

What Happens Next?

Once a sensor is selected for upgrade, behind the scenes, Stellar Cyber identifies the correct
software version to apply and schedules the upgrade to take place during a period of low activity.
If the sensor was offline when the upgrade was requested, Stellar Cyber continues to

    Note that when you upgrade a sensor from the Sensor Overview page, all configuration
settings are preserved across the upgrade, including the DP's IP address, aggregator
addresses, tenant ID, log level settings, and DHCP server log settings.

Downgrading Sensor Software (Rollbacks)

 This section describes a feature that is currently only available as part of an Early Access

Program and may not be enabled in your version of the Stellar Cyber Platform. Contact your
sales representative for information on enabling this feature and trying it out with Stellar
Cyber's Customer Success team.

You can downgrade sensor software from the Sensor List. This may be useful in situations where
an upgrade produces unexpected results or when working with Stellar Cyber Customer Success
to troubleshoot an issue.

Keep in mind the following when downgrading sensor software:

Downgrades are supported for Windows Server Sensors, Linux Server Sensors, and
Modular Sensors.

Downgrades are only supported from version 6.0.0 to version 5.5.0.

When you launch the Software Downgrade interface, it lists only those sensors that are
currently eligible for a downgrade.

Use the following procedure to downgrade sensor software:

1. Select the Manage | Software Downgrade option. A dialog box similar to the following

appears:

2. Select the version for the downgrade from the Available Software list.

 The only supported downgrade path in this release is from 6.0.0 to 5.5.0.

3. Select the sensors to downgrade from the Target Sensors list. Only sensors supported

for downgrade to the selected version are listed.

4. Click Submit. The downgrade begins.

 The downgrade takes approximately five minutes. No logs are collected by the

sensor while the downgrade takes places. Log collection starts again automatically
once the downgrade concludes.

5. Refresh the Sensor table to see the results. If you do not see the Upgrade

Resultcolumn:

a. Click the Columns tab available at the left of the Sensor List.

b. Scroll to the bottom of the list.

c. Check the box for Upgrade Result. The column is immediately added to the

table.

 Even though the column is named Upgrade Result, it provides

information on both upgrade and downgrade operations.

d. Click the Result button in the Upgrade Result column to see information on

the success or failure of the operation.

  Note that when you downgrade a sensor, all configuration settings still available in the
downgraded version are preserved across the transition, including the CM IP address,
aggregator addresses, tenant ID, log level settings, and DHCP server log settings. However,
any settings that were only available in the newer software version will not be available in
the downgraded version.

Using the Sensor CLI
You can select one or more sensors in the Sensor Overview table and click the >_CLI Access
button to open a command line session with the corresponding sensor(s) in the Sensor CLI
Access window, as illustrated in the figure below:

Note the following:

The available CLI commands are a superset of the CLI commands available when
connected directly to a sensor. Refer to Available Commands in the Sensor CLI
Access Window for a summary of the available commands.

You can only use the CLI Access feature with sensors that are connected and running a
minimum version of 4.2.x. Sensors do not need to be authorized for CLI access.

You can use your browser's right-click context menu to copy text from the Sensor
CLI Access window and paste it for use elsewhere. The window is scrollable, too, so
you can see the output of commands that do not fit entirely in the window.

You can select multiple sensors before clicking the >_CLI Access button. When you
use this technique, the CLI issues any command to all connected sensors and returns
the results under a heading indicating each sensor's name. For example, the illustration
below show the results of a show system command issued to three separate sensors
simultaneously.

Sensor CLI Access Commands

The following types of commands are available in the Sensor CLI Access window:

show – See the settings and statuses for different options on the sensor.

set – Enable and configure options on the sensor.

unset – Disable options on the sensor.

copy – Copy specified trace files or support files.

exec – Execute a specified JSON task or a tcpreset-stop action.

You can use the ? or help parameter with any of these commands to see the available
commands of the corresponding type. For example:

set ? or set help

You can also use the ? with a specific command to see its available arguments. For example:

mysensor > set ntp ?

<NTP server> Specify NTP server name or IP address

 The Sensor CLI Access window supports copy-and-paste functionality.

Refer to Available Commands in the Sensor CLI Access Window for a summary of the
available commands.

Applying CA Certificates to Sensors
You can select one or more sensors in the Sensor Overview table and click the Apply
Certificate | Apply CA Certificate button to assign a CA certificate to them. In response, a
dropdown appears listing the CA certificates you've added to Stellar Cyber in System | Saved
Objects | Certificates that match the selected sensor's tenant, allowing you to click the one you
want to apply.

 Prior to the 5.1.1 release, the button was just named Apply CA Certificate.

 If you are assigning the same CA certificate to multiple sensors belonging to the same

tenant, you can use the Change Columns button to add the Tenant Name column to the
display, click in the column heading to sort on it, and then select all of the tenant's sensors to
which you want to apply the CA certificate.

You only need to apply CA certificates to those sensors that sit behind firewalls using an
SSL inspection service. Without the CA certificate from the SSL inspection service applied, the
sensor cannot retrieve the necessary package for upgrading. Make sure you choose the CA
certificate used by the SSL inspection service on the firewall protecting the sensor(s).

 Note that it is possible that your sensors may be behind a different firewall than the DP.

Make sure you assign the CA certificate from the correct firewall to the sensor(s).

 DPs behind firewalls using an SSL inspection service also require a CA certificate. You

assign certificates to DPs using the CA Certificate entry in the Data Processor section of
System | ORGANIZATION MANAGEMENT | Settings.

 If a certificate you expect to see doesn't appear when you select the Apply CA Certificate
option, make sure you uploaded it with the correct tenant assignment in System | Saved
Objects | Certificates.

Automatic Handling of MS-Windows Carriage Returns in Certificate and

Key Files

Stellar Cyber automatically handles certificates and key files that include the MS-Windows
carriage return character (\r, or 0x0D in hexadecimal). You do not need to remove them
manually.

Removing a Certificate from a Sensor
You can also remove an applied certificate from a Sensor in the Sensor Overview table. The
procedure is similar for both CA Certificates and Log Forwarder certificates.

1. Start by adding a column to the Sensor List of the type corresponding to the type of
certificate you want to remove. Click the Columns entry at the left of the table and
select one or both of the following, as illustrated below:

Log Forwarder Certificate

CA Certificate

2. Locate the sensor whose certificate you want to remove and right-click its entry in either
the Log Forwarder Certificate or CA Certificate column. Then, select the Remove

Certificate option from the context menu that appears, as illustrated below. Keep in
mind that you must remove all associations from a certificate before you can delete it in
System | Saved Objects | Certificates.

Assigning Aggregators to Sensors
You can assign an aggregators to sensors from directly within the Sensor Overview by selecting
their entries in the list and clicking the Assign Aggregator button at the top of the list.

 An aggregator is a Modular Sensor with the Aggregator feature enabled in its Modular

Sensor Profile. An aggregator forwards aggregated traffic received from other Stellar Cyber
sensors to the Stellar Cyber Platform configured in its modular sensor profile.

 You can also assign an aggregator to a sensor from the sensor's Edit Sensor dialog box, just
as you have in previous releases. The advantage of assigning aggregators directly from the
Sensor Overview is that you can assign the same aggregators to multiple sensors in one step
(a bulk edit, in other words). You also don't need to open any extra dialog boxes when you
assign aggregators from the Sensor Overview – it all happens right there in the table.

Use the following procedure to assign aggregators to sensors from within the Sensor Overview:

1. Check the boxes for the sensors to which you want to assign primary and secondary

aggregators.

The Assign Aggregator button appears with the other bulk edit controls at the top of
the Sensor Overview, as illustrated below.

 If you select multiple sensors, they must all belong to the same tenant in order to

be able to perform a bulk aggregator assignment. If the Assign Aggregator button
appears but is grayed out, you may have selected sensors from different tenants.

2. Click the Assign Aggregator button to open the Assign Aggregator dialog box.

If all selected sensors are already assigned to the same aggregators, the
dialog box shows the current assignments.

If any of the selected sensors are assigned to different aggregators (or are all
unassigned), the dialog box appears without any aggregator assignments

displays, allowing you to configure them now from scratch.

3. Use the Primary Aggregator dropdown to select the primary aggregator for the

selected sensors. The dropdown lists all available aggregators for the tenant to which
the sensors belong.

4. Once you have selected a Primary Aggregator, the Secondary Aggregator dropdown

appears, allowing you to specify the aggregator to use in situations where the primary
aggregator is unreachable. The dropdown lists all aggregators for the tenant to which
the sensors belong, except for the one you just assigned as the Primary Aggregator.

5. When you have finished choosing the aggregators for the selected sensors, click

Submit.

 Keep in mind that TCP Port 8080 must be open between the sensor and the aggregator for

successful communications.

 To understand how Windows and Linux Server Sensors handle scheduled update retrievals
when using an aggregator, see Server Sensor Update Behavior through an Aggregator.

Sensor Management Menu
The Manage button is located above Sensor Overview table. Clicking it displays the menu
shown below. These options are all related to the management of the sensors and each option
displays its own dialog box.

The following sections describe the available functions.

Sensor Assign Profile

All sensors must be assigned to a profile. Except for the default Profile, you create your own
profiles. For more information see the Sensor Profiles page.

To assign profiles, select the Manage | Assign Profile option.

A dialog box similar to the following appears.

Use the Assign Profile to Sensors dialog box as follows:

1. Available profiles are listed in the SENSOR PROFILES list. Select one with the radio-

button control.

2. Available sensors are listed in the SENSORS list. Select the sensor(s) to which you
want to apply the profile selected in the SENSOR PROFILES list by checking their
boxes.

3. Apply the selected profile to the selected sensor(s) by clicking the Submit button.

 Changes in this dialog box do not take effect until the Submit button is clicked. If the X

button is used to close the dialog box no changes are made.

Sensor Downgrade

You can use the Manage | Downgrade Software option to roll a sensor back to a specified
version.

Refer to Downgrading Sensor Software (Rollbacks) for details on using this feature.

Sensor Import Security Rules

You can use the Manage | Import Security Rules option to import custom Suricata
(IDS) security rules from an external file for use by sensors with the ML-IDS (Malware) feature
enabled in their sensor profiles.

Use the following procedure to import custom security rules:

1. From the Sensor table, select Manage and then select Import Security Rules.

A dialog box similar to the following appears:

2. Select a local file by using Choose File.

See below for details on the rule file format.

3. Select the sensors that will use the security rules from the SENSORS list.

4. Select Upload and Deploy to apply the imported security rules to the selected sensors.

Rule File Format

The rule file must follow standard Suricata rule format  with each rule on a single line. Here is
an example of a custom rule in the correct format:

alert tcp $HOME_NET any -> $EXTERNAL_NET any (msg:”ET TROJAN Likely Bot Nick
in IRC (USA +..)”; flow:established,to_server; flowbits:isset,is_proto_irc;
content:”NICK “; pcre:”/NICK .*USA.*[0-9]{3,}/i”;
reference:url,doc.emergingthreats.net/2008124; classtype:trojan-activity;
sid:2008124; rev:2;)

Note the following important points for custom rules:

Because Stellar Cyber sensors with the ML-IDS feature enabled operate as an IDS
rather than an IPS, the action for your security rules must be alert, as shown above.

The values for $HOME_NET and $EXTERNAL_NET are specified in the Sensor Profile:

Modular Sensor Profiles – Feature Customization | IDS | Networks

Once imported, custom rules are stored in the custom_defined.rules signature set.
They are enabled in the sensor profiles for all sensors to which you applied them by
default and can be seen in the Sensor Profile under Signature | Selected Rules, as
illustrated below.

You can toggle your custom rules on and off using the custom_defined.rules entry
shown below, as well.

 Each time you import custom security rules to a sensor, the new rules completely
overwrite any existing entries in the custom_defined.rules signature set. New
rules are not appended to the existing rules.

Troubleshooting Custom Security Rules

You can check the Sensor's ids feedback message to see the result of an upload and
deploy. For example, here is the result of a successful upload and deploy:

"ids": {
    "msg": "Success",
    "status": true,
    "timestamp": 1690000900,
    "datetime": "2023-07-21 21:41:40"
  },

You can keep track of IDS events and malware detections by using the show maltrace
command from the Sensor's CLI. For example:

DataSensor> show maltrace
Maltrace Event:
Captured:                                   0
Truncated:                                  0
Prefiltered:                                0
Verdict Found in Local Cache:               0
Verdict Found in Remote Cache:              0

Passed to Local Scan Engine:                0
Filtered on Local Scan Engine:              0
File Analyses Failure on Local Scan Engine: 0
Local Scan Engine Failure:                  0
Verdict Given by Local Scan Engine:         0
Uploaded to Sandbox:                        0
Failure Over Sandbox:                       0
Sandbox Scan Succeeded:                     0
Sandbox Timeout:                            0
Sent Result to Central Manager:             0

IDS Event:
Received:        67
Excluded:        0
Sent Result:     0
Unknown Score:   67

Output buffering:
Buffered:       67
Outputed:       66

Rebooting Sensors Remotely

Sensors can be rebooted remotely. Select the Manage | Reboot option to reboot one or more
sensors remotely. A dialog box similar to the following appears:

Select the sensors to reboot by checking their boxes in the SENSORS list and then select
Submit to start the reboot process on the selected sensors.

 Rebooting a sensor does not reboot the host on which the sensor is installed.

Using the Scheduled Upgrades Tab
The Scheduled Upgrades tab tracks the success or failure of sensor upgrades you have
launched.

For details on how Server Sensors retrieve updates and upgrades when an aggregator is
configured, see Server Sensor Update Behavior through an Aggregator.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

