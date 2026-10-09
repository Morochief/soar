Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Available Commands in the Sensor CLI
Access Window

This topic summarizes the commands available in the Sensor CLI Access window available from
the System | DATA SOURCE MANAGEMENT | Sensors | Sensors page. See the following
sections for details:

Sensor CLI Access Command Types

Arguments for the "show" command in the Sensor CLI Access Window

Arguments for the "set" Command in the Sensor CLI Access Window

Arguments for the "set" Command in the Sensor CLI Access Window

Arguments for the "exec" Command in the Sensor CLI Access Window

Other Commands in the Sensor CLI Access Window

Sensor Management Commands in Local CLI

 Refer to Using the Sensor CLI for a summary of how to display and use the Sensor CLI

Access window.

Sensor CLI Access Command Types
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

 When connected to the local CLI, you can also use the help, help all, and help

<command> commands to see command descriptions and syntax.

The tables below summarize the available arguments for the show/set commands.

Additional Commands for IDS PCAP Capture

Refer to Capturing Trace Files for IDS Signature Matches for information on the
CLI commands used with the IDS PCAP Capture feature. Additional copy captured_pcap and
copy live_pcap commands are available to copy trace files to either the DP or an external host
for further analysis.

About Logging for CLI Commands

CLI commands that execute actions rather than displaying information are logged with
timestamps. Each log entry records the executed command and parameters in JSON format with
a timestamp, letting you review administrative activity for auditing and troubleshooting. Logs can
be viewed through the CLI or accessed in the aella_cli_set.log file for offline analysis.

Arguments for the "show" command in the Sensor
CLI Access Window
You can use the show command with any of the arguments listed and described in the table
below.

 Some of the show commands return a hardcoded maximum number of entries (for example,

128 for the show metalist command). In situations such as this, you can add the all
parameter to ensure that the CLI returns all available entries in paged output. For example,
the show metalist all command returns all entries across a set of pages, each of which has
a maximum of 128 entries.

show

command

description

aflow

Shows AFIX AFlow Information.

aggregator Shows information on Data Aggregators used by the sensor, if any. Also reports CM Controller IP address and

connection status.

Shows asset information.

Shows CM Controller IP address and connection status.

asset

cm

show

command

customer_l

og

description

Shows information on Customer Log Parsers, if applied.

data-port-ip Shows MAC and IP address for sensor data port(s) (where data is ingested by the sensor).

disk-

monitor

dns

dpi

drop

flood

Shows actions being taken to limit disk usage.

Shows the IP address of the sensor's DNS server.

Shows deep packet inspection information, including:

Categorization for different applications

Memory usage, flow count, and pool usage

Note that the output for this command can be lengthy. Use the all parameter to see all entries in paged output (for

example, show dpi all).

You can include the version argument (show dpi version) to see the following additional information:

DPI Engine version

DPI Protocol Bundle version

Use show dpi protocol custom metadata to list any user-defined DPI metadata entries that have been added

with the set dpi protocol custom metadata command.

Shows information on the number of packets dropped by the sensor broken out by Rx and Tx and interface.

Shows syn flood detection information.

gateway

Shows the IP address of the sensor's default gateway.

history

Shows a timestamped log of the most recent 25 CLI commands that executed actions. Show commands are

excluded.

hugepage_

Shows the hugepage_size currently configured for the sensor. Refer to the set hugepage_size entry in the table

size

below for details on what a hugepage is and why you might consider changing it.

ids

Shows the status of the IDS PCAP capture feature on the Modular Sensor. When enabled, this feature captures

trace files to the Sensor's storage when an IDS signature match is detected. The show ids output reports whether

the IDS PCAP feature is enabled, and, if enabled, the filenames of any saved PCAP files so you can copy them off

of the device for further analysis. This command only provides output when used with a virtual 6.0.0+ Modular

Sensor with the IDS feature enabled in its Sensor Profile.

 Refer to Capturing Trace Files for IDS Signature Matches for more information on enabling and configuring

the IDS PCAP feature.

interface

Shows equivalent output of the Linux ifconfig command with status, packets, drops, and bytes Rx and Tx broken

out by interface.

show

command

description

If a whitelist is configured for SSH connections to the Management port, allowed IP addresses/ranges appear in the

show interface output for the management interface.

Shows information on AFIX IPFIX classification engines.

Shows information on AFIX JSON metadata transfer.

ipfix

json

ldap-

Shows the state of the ldap-metadata feature is enabled (enabled or disabled).

metadata

logcollector Shows information on the configuration of and records sent by different log collectors.

logforwarde

r

Shows information on logs received and forwarded, including the following:

Receiver IP address/hostname and port.

Status of specific log forwarding features, such as the HTTP JSON Parser, forwarding to an external server,
or TLS log forwarding.

Number of workers provisioned for the sensor by the system.

Name of custom log forwarder certificate used with the TLS log forwarding feature, if in use.

You can include the all parameter (that is, show logforwarder all) to see additional information, including the

Top 5 Error Types sorted by count along with the Start Time for each error type. Counts are provided based on the

current td-agent log file and update each time you run the command. This provides quick visibility into frequent td-

agent runtime errors without accessing raw logs.

Include the parser parameter (that is, show logforwarder parser) to see the list of currently enabled Log

Forwarder parsers.

loglevel

maltrace

memory

metalist

Shows the log level for different Stellar Cyber modules. Note that you can also set the log level for different

modules from the CLI Access window using the set loglevel command; see the table below.

Shows detailed statistics on malware sandbox usage, including the total number of IDS events broken out by the

number of events buffered by the sensor and the number already sent to the DP.

Note: When NFS file assembly is enabled, the output also shows the current NFS Assembly status.

Shows information on control and data plane memory availability and usage.

Shows information on the black list of metadata applications (traffic explicitly excluded from ingestion/evaluation in

the sensor profile).

Note that the output for this command can be lengthy. The following tips can help you see the entries that interest

you:

Use the all parameter to see all entries in paged output (for example, show metalist all).

Use a regex filter to exclude aella_log_forwarder entries and see only user-defined applications. For
example:

show metalist regex ^(?!.*aella_log_forwarder).*

show metalist all regex ^(?!.*aella_log_forwarder).*

show

command

description

mtu

mirror

Shows the current Maximum Transmission Unit (MTU) setting for each interface on the sensor.

Shows information on configured traffic mirroring.

module

Modular Sensors only. Shows which modular features are enabled on a modular sensor (for example, log

collector, aggregator, Tenable scanner, and so on), as well as its current CPU, RAM, and disk provisioning.

module

Modular Sensors only. Shows the amount of CPU, RAM, and disk required to support different combinations of

request

modular sensor features.

netstat

Modular Sensors only. Shows standard netstat output for the modular sensor's management port.

The syntax is as follows:

show netstat [all | delta | rate] protocol [tcp | udp | all]

all – returns all statistics available from the Linux kernel.

delta – returns statistics from the previous time netstat was run, the current value, and the difference
between the two.

rate – returns just those statistics that are different from the previous time netstat was run.

protocol – choose whether to view statistics for TCP, UDP, or both.

nic

Lists the NICs installed in the sensor along with their names, driver names, driver versions, firmware versions, and

bus information.

Lists the configured NTP servers for this sensor in order of use.

Shows packet processing settings, including slicing and deduplication.

Shows detailed information on internal AFIX process mapping, including NUMA register mapping.

Shows information on proxies configured for the sensor, if any.

Shows information on the configured data receiver for the sensor, including the following:

ntp

packet

process

proxy

receiver

IP Address or hostname

Port number

Receiver type (JSON or Packet)

Transport (HTTPS or HTTP)

Status, including response time

Currently configured compression level for Windows Server Sensor event and FIM logs.

You can also use the expanded show receiver debug command to see additional details on the sensor's

SSL certificate connectivity. The certificate details provided can help you identify SSL inspection or certificate

mismatches.

This command is supported for Windows Server Sensors as of the 6.2.0 release.

ring

Shows information on the AFIX ring.

show

command

description

route

rules

scan

service

Shows static route table entries.

Shows information on configured maltrace rules.

Shows detailed scan information on sensor.

Provides the service to AppID mapping for the sensor, including the NUMA register for each. Note that the output

for this command can be lengthy. Use the all parameter to see all entries in paged output (for example, show

service all).

session

Provides a session table for the sensor listing ongoing sessions and their NUMA mappings and summary statistics.

You can filter this command by source/destination IP addresses and ports using the following syntax:

show session [source ip [port]] [dest ip [port]]

system

Shows the status of key Stellar Cyber services on the sensor, including service uptime.

If a given service is down, you can use the restart service <service_name> command to restart it.

This command is supported for Windows Server Sensors as of the 6.2.0 release.

task

Shows information on JSON tasks requested on the sensor by the DP (for example, restarting an internal sensor

service).

tcpreset

Shows information on tcpreset actions configured as part of scripts in ATH playbooks. The available commands are

as follows:

show tcpreset – Displays the list of tcpreset traffic files. Each file provides a timestamped record of the
tcpreset traffic sent by the sensor as part of a script action.

show tcpreset [file] – Displays the contents of a specified tcpreset traffic file. You can get the list of
available file names with the show tcpreset command.

show tcpreset script-actions – Shows the tcpreset actions sent from the DP to this sensor. For example:

Sensor> show tcpreset script-actions
[2025-11-01 22:44:11] tcpreset ad5600505689fdce -i eth1 -o eth0 -h 10.33.5.184 -d 15

tech-

support

Not supported.

tenable

Available if tenable nessus is enabled in the sensor profile. Shows status of the scanner.

thread

Shows information on CPU threads.

time

top

Shows system time.

Shows top resource usage by process.

upgrade

Shows information on upgrades for this sensor. The syntax is as follows:

show upgrade

Shows a history of upgrades along with log entries documenting their success or failure and details on the image

applied.

show

command

description

show upgrade kernel status

Shows the current status of a kernel and package upgrade, including recent log output. If no upgrade has been

started, reports whether the upgrade service has failed or was never started.

 This command is only available on Modular Sensors.

show upgrade kernel packages

Shows a diff of package changes made by the last kernel and package upgrade, organized into three sections:

packages that were updated (with old and new versions), packages newly installed as upgrade dependencies, and

packages removed during the upgrade.

 This command is only available on Modular Sensors.

userapp

Shows information on user-defined applications for this sensor.

Note that the output for this command can be lengthy. The following tips can help you see the entries that interest

you:

Use the all parameter to see all entries in paged output (for example, show userapp all).

Use a regex filter to exclude aella_log_forwarder entries and see only user-defined applications. For
example:

show userapp regex ^(?!.*aella_log_forwarder).*

show userapp all regex ^(?!.*aella_log_forwarder).*

version

Shows the sensor software version, license status, features, platform, basic configuration settings, and sensor up

time. Note that values for some of these options can also be seen in the Sensor List, depending on which fields you

add to the display.

 Note: The statistics displayed by the show version command can vary depending on your sensor type and

version. The statistics listed below are current for the latest sensor software version.

 Note: Windows Server Sensors show only the following fields in their show version output – AOS Version,

Product Model, License Status, Product EngineID, Internal ID, Running Mode, Running Feature,

Aggregator, CM Controller,, Ctrl Plane Status, Platform OS, and Platform Type.

AOS Version – The version of the Stellar Cyber operating system on the sensor.

You can use the AOS Version to determine whether the sensor is operating in SaaS or on-prem/pre-SaaS
mode:

Sensors operating in on-prem/pre-SaaS mode include a p at the end of their AOS Version in the
show version output. For example:

AOS Version : 5.2.0_99e79ab-p

Sensors operating in SaaS mode do not include the p in their AOS Version.

Product Model – Shows Data_Sensor for Device Sensors and either Windows Agent Sensor or Linux
Agent Sensor for Server Sensors.

License Status – Shows whether the license on the sensor is valid.

This field does not appear for physical Photon Sensors.

Product EngineID – The unique system ID assigned to this sensor by Stellar Cyber.

Product Tenant ID – The unique system ID assigned to this sensor's tenant.

Platform Type – The type of platform on which this sensor is installed. For a virtual sensor, this can be
VMware, QEMU, Virtual Machine, Microsoft, and so on. For physical sensors, a hardware revision is shown.

show

command

description

Platform OS – The operating system in use on the sensor.

Hostname – The sensor's hostname.

Running Mode/Feature – Indicates whether the sensor is a device sensor or a server sensor (agent), as
well as the type of sensor profile enabled.

Photon Sensors show device/modular.

Virtual Modular Sensors show device/modular.

Linux Server Sensors show agent/ds.

Windows Server Sensors show agent/wds, but broken out on separate lines.

Management Port – The device interface designation for the management port on the sensor (for example,
eth0).

Management IP – The IP address of the management port on the sensor.

CM Controller – The IP address of the Stellar Cyber platform that manages this sensor.

Ctrl Plane Status – Can be Authorized or Unauthorized. Indicates the status of the authorization
handshake between the sensor and its managing Stellar Cyber Platform's Configuration Management
module (CM). Once the handshake has established management communications and the Control Plane is
authorized, the Stellar Cyber Platform pushes sensor profile settings to the sensor.

Sensor Boot Time – The time at which the sensor was last booted. Note that this field only appears for
physical Photon Sensors.

Sensor Up Time – The amount of time the sensor has been running since the last time it was booted.

Data Plane Status – Can be Online or Offline. Indicates whether the sensor is successfully sending
ingested data to its managing Stellar Cyber Platform.

vtep

vxlan

Shows interfaces available for use as a VXLAN tunnel destination.

Shows Information on VXLAN tunnel configuration.

whitelist

Shows information on whitelist configuration.

Arguments for the "set" Command in the Sensor
CLI Access Window
You can use the set command with any of the arguments listed and described in the table below.
If you need help on command syntax, type set <command> ? to see the context-sensitive help.

set

command

description

afix-ring-size Lets you configure the AFIX ring buffer size. AFIX is used on the sensor to extract flow and metadata information

from sessions.

Must be a specified as a power of 2 with a default size of 8192.

aggregator

Lets you specify the IP address of the aggregator for the sensor, if any.

cm

Lets you set the IP address to reach the management interface of the Data Processor from the sensor or

aggregator. For a DP cluster, this is the IP address of the DL-master's management interface. For a single DP

deployment, this is simply the DP's management IP address. You can supply either an IP address or a hostname.

Running this command from the Sensor CLI Access window can be useful when migrating sensors from one DP

to another.

Note: Using this command from the Sensor CLI Access window disconnects the sensor from its current DP.

Because of this, you need to manually close the Sensor CLI Access window once the disconnection occurs.

set

command

description

The syntax is as follows:

set cm <cm_addr> [safe | force]

cm_addr – the IP address or hostname of the managing DP.

safe – reverts the CM address to the previous address if connection to the new one is not successful. This
parameter is automatically used by Stellar Cyber when set cm is executed from the Sensor CLI Access
window regardless of whether you included it in the command line.

force – sets the CM address to whatever you specify, regardless of connection success. Be careful when
using this option.

 Stellar Cyber strongly recommends that you always use the safe argument with set cm in order to prevent

yourself from accidentally orphaning a sensor by assigning an incorrect IP address.

As a safeguard, the safe option is used automatically when you run set cm from the Sensor CLI Access

window.

data-port-ip

Lets you assign an IP address to a data port on a sensor. For example, you can set the IP address of a data port

using the following command:

DataSensor> set data-port-ip 1 100.100.100.100/24

This command changes the data port IP configuration, setting the IP address of data port 1 to

100.100.100.100/24

dpi

Adds a user-defined metadata attribute for the specified DPI protocol.The syntax is as follows:

set dpi protocol custom metadata <proto> <attr> [<alias>] [<level>]

Supported protocols and example attributes:

smb – session_id

ssl – server_supported_version, key_share_group, ext_ec_supported_groups_list,
ext_ec_supported_groups_type, client_hello_extension_type, client_hello_extension_value,
server_hello_extension_type, server_hello_extension_value, ext_sig_algorithms,
ext_sig_algorithm_scheme, ext_sig_algorithm_hash, ext_sig_algorithm_sig,
certificate_subject_key_algo_oid, certificate_signature_algo_oid

The optional alias argument specifies an alternative name for the attribute in output.

The optional level argument sets the metadata collection level (default: 2).

After adding entries, run restart service aella_flow for changes to take effect. A maximum of 100 user-defined

entries are supported. Enabling additional metadata can increase ingestion volume and storage requirements.

geneve

Lets you configure options related to parsing of GENEVE-encapsulated traffic from Netskope's Cloud

TAP stitcher.

The Netskope Cloud TAP stitcher can be used to pull data stored by the Netskope Cloud TAP from AWS S3,

stitching connections back together , performing TLS decryption, and exporting the traffic to a Stellar Cyber

Modular Sensor in a GENEVE-encapsulated tunnel.

As part of the configuration of the GENEVE tunnel, you can enable Netskope-proprietary USER_ID or

SITE_ID options. When enabled, additional TLVs are included in the outer GENEVE header of each packet. The

Modular Sensor extracts the USER_ID or SITE_ID TLV added by the Netskope Cloud TAP stitcher from the outer

GENEVE header and associates each identifier with its corresponding flow inside the tunnel. Because parsing

occurs at the packet level, multiple users sharing the same tunnel are correctly recognized. Normalization maps

the Netskope user identifier to srcip_username and the Netskope site identifier to srcip_siteid.

set

command

description

Settings for GENEVE parsing on the sensor are preconfigured to match the Netskope defaults and only need to

be changed in the rare situation where you have modified them on the Netskope side. You can configure the

following options for this feature with set geneve <parameter> <value>:

netskope_port – Specifies the UDP port used by GENEVE traffic. By default, this is set to the default
GENEVE port of UDP 6081.

netskope_class – Specifies the Netskope option class. By default, this is set to 65484 (0xffcc).

netskope_user_id_type – Specifies the Netskope User ID type. By default, this is set to 12 (0xc).

netskope_site_id_type – Specifies the Netskope Site ID type. By default, this is set to 13 0xd).

Lets you specify the hostname for the sensor. You can also specify hostnames in the Sensor List.

 This is an advanced setting that you should only configure with the assistance of Stellar Cyber Customer

Success team.

hostname

hugepage_si

ze

Lets you change the hugepage size configured for the sensor.

The syntax is as follows:

set hugepage_size <auto | 2m | 1g>

The default is auto. Note that changes to this setting only take place after restarting aella_flow.

In Linux, a hugepage is a larger-than-normal memory page that helps reduce the overhead of managing memory.

By mapping larger chunks of memory at once, hugepages can improve sensor performance

In most deployments, you do not need to change the hugepage size from its default setting of auto. However,

you might consider changing the hugepage size with the assistance of Stellar Cyber Customer Success in

situations where your ingestion rates are very high and packet drops are observed. In these cases, adjusting the

hugepage size can help reduce CPU overhead, improve memory allocation for large buffers, and maintain

consistent performance under load.

ids pcap

Enables and configures the IDS PCAP capture feature on the Modular Sensor. When enabled, this feature

captures trace files to the Sensor's storage when an IDS signature match is detected.

 Refer to Capturing Trace Files for IDS Signature Matches for more information on enabling and

configuring the IDS PCAP feature.

interface

<ifn_name>

Lets you set IP configuration for a sensor interface by name, including its IP address, default gateway, and

DNS server. Start by using show interface to get the name of the interface you want to configure. For example,

to configure the management interface, you would use set interface management <arguments>

 This command is only supported on sensors running Ubuntu 22.04.

The syntax is as follows:

set interface <ifn_name>

ip [<IP Address/Netmask> | dhcp]
gateway <IP Address>
dns <IP Address>

Configuring an SSH Whitelist for the Management Port

set

command

description

You can use the CLI to configure a whitelist of IP addresses and/or ranges that are allowed to access the

Management port via SSH. When a whitelist is configured, SSH connections to the Management port are only

allowed from whitelisted addresses. SSH connections from all other IP addresses are rejected.

The syntax is as follows:

ssh interface management ssh-whitelist <IP/CIDR> [<IP/CIDR> ...]

For example, the following command allows SSH connections from all addresses in the 10.34.22.0 subnet:

Sensor> set interface management ssh-whitelist 10.34.22.0/24

Similarly, the following command allows SSH connections from only 192.168.1.25 and 192.168.1.50:

Sensor> set interface management ssh-whitelist 192.168.1.25 192.168.1.50

 Note that changes to the SSH whitelist are not cumulative. Every time you use the set interface

management ssh-whitelist command, it completely replaces the previous whitelist settings. You can verify

the current whitelist by looking at the entry for the management interface in the show interface output.

Clearing the SSH Whitelist

You can clear the currently configured SSH whitelist with the unset interface management ssh-whitelist

command.

ldap-

Enables structured handling for LDAP search and modify request fields. You must enable this option for

metadata

generation of the Suspicious LDAP Search Request alert and its subtypes of Domain Trust Enumeration, All

Object Enumeration, and Wildcard Query. You can turn off the feature with unset ldap-metadata.

logforwarder Lets you configure the logforwarder feature.

Use set logforwarder apply-custom-parser to force the Sensor log forwarder to redownload and apply custom

parsers. This lets you refresh parser and configuration files without manual intervention, ensuring that updated or

corrected parsers are immediately applied. If no custom parser exists or a parser is invalid, the command reports

the condition and skips changes. This capability helps maintain parser consistency across tenants.

logforwarder

parser

Lets you manage the list of active Log Forwarder parsers on the sensor. Use this command with Stellar Cyber

personnel to reduce memory usage on hosts with limited resources by enabling only the parsers required for your

environment. The syntax is as follows:

set logforwarder parser add <parser> | remove <parser|all> | restore_default

add <parser> – Enables a specific parser. Tab completion is available for parser names.

remove <parser> – Disables a specific parser.

remove all – Disables all parsers.

restore_default – Restores the built-in default parser set.

After making changes, run restart service td-agent for the changes to take effect. Note that parser configuration

changes may not persist across platform upgrades and can be overwritten by UI management.

loglevel

Lets you set the log level for different modules. The syntax is as follows:

set loglevel <service> <level>

set

command

description

You can also set the loglevel timeout with the following command:

set loglevel timeout <timeout value in minutes>

 Stellar Cyber recommends that you only change the log level for modules while working with Custom

Success personnel. If you do decide to change log levels, a good way to start is by checking the current log

levels with the show log level command. The default log level for all modules is info.

The available modules (services) for which you can set the log level are as follows:

audit (aella_audit)

conf (aella_conf)

ctrl (aella_ctrl)

flow (aella_flow)

mon (aella_mon)

The available log levels are as follows, from least to most severe:

debug

info

warning

error

critical

As an example, you can set the log level for aella_flow to warning with the following command:

set loglevel flow warning

When you specify a log level, Stellar Cyber records events of the specified severity and above. So, for example, if

you specify a log level of error, only events with a severity of error and critical are logged.

The log level setting also directly affects the quantity of events logged. For example, if you specify a log level of

debug for a service, all events for that module are logged, regardless of severity.

Log Level Tips

Keep in mind the following tips when making changes to the log level:

Stellar Cyber strongly recommends that you consult with Customer Success before changing log levels
for a service.

If you do make changes to the log level, Stellar Cyber recommends that you also set a loglevel timeout
so that the log level returns to its normal state after whatever testing you are performing.

Stellar Cyber recommends that you keep track of the time at which you change the log level. This can
help the Customer Success team assist you with troubleshooting.

maltrace

Enables or disables NFS file assembly in Suricata for Sophos malware inspection. The syntax is as follows:

set maltrace nfs-assembly {enable|disable}

 This feature is resource-intensive. Only enable when working with Stellar Cyber personnel.

When enabled, Suricata reconstructs files transferred over NFS sessions and forwards them to Sophos for

malware analysis. Supports NFSv3 and NFSv4; NFSv4 may not provide reliable file name metadata due to

handle-based protocol operations.

To ensure Suricata can detect the NFS application layer, start packet capture before the NFS client mounts the

share. If capture begins after the mount, session establishment is not observed and application-layer detection

set

command

description

may not initialize.

This setting persists across sensor upgrades.

malware_upl

Lets you configure the malware upload feature. Refer to Forwarding Malware to an External HTTPS Server for

oad

mtu

ntp

details.

Lets you set the MTU for a specified interface. The syntax is as follows:

set mtu <mtu_value> <ifn_name(s)>

You can specify multiple interfaces in a single command. For example, the following command sets the MTU to

5500 bytes for eth0, eth1, and eth2:

Sensor> set mtu 5500 interface eth0,eth1,eth2

Lets you specify an NTP server for the sensor. The syntax is as follows:

set ntp <ntp server name or address>

 Specifying an NTP server does not configure a time zone for the sensor. During installation, the timezone for

a sensor is automatically set to UTC+0. Since the logs for some security products may only include the local

time without a timezone, Stellar Cyber recommends that you set the sensor timezone to the same timezone

as your security product. Set the time zone for a sensor from the Sensor List. Refer also to Best Practices

for NTP and Timezones .

password

Lets you change the password for the sensor.

proxy

Lets you specify an HTTP proxy for the sensor. The syntax is as follows:

set proxy http://[username:password@]<proxy_ip>[:<proxy_port>]

Note: The CLI prevents you from entering non-printable characters as part of the username or password for the

proxy, as well as the proxy itself.

The set proxy command works differently depending on whether the sensor is operating in NG-SaaS mode or as

an on-premises sensor:

When a modular sensor is running in NG-SaaS mode with an aggregator configured, it cannot use an
external HTTP proxy. In NG-SaaS mode, the set proxy command works only when an aggregator is not
configured.

When a modular sensor is running in on-premises mode, the set proxy command does allow the sensor
to use an external proxy for downloading updates from the internet. In this configuration, direct
communication between the sensor and the DP is disabled.

receiver

Lets you change the receiver configured for the sensor in its sensor profile.

Configuring Event Log and FIM Timeouts for Windows Server Sensors

By default, Windows Server Sensors send Windows Event Log and File Integrity Monitoring (FIM) payloads with a

timeout setting of 90 seconds. You can use the set receiver timeout command to fine-tune timeout settings

independently for the two source types. The syntax is as follows:

set receiver timeout <seconds> [winlog | fim]

set

command

description

Note the following:

A setting of 0 disables timeouts for the specified data source types.

If you leave out the winlog | fim argument, the timeout setting applies to both data source types.

Restore the default timeout of 90 seconds with the unset receiver timeoutcommand.

Use show receiver to see the currently configured timeout settings for each data source type.

 This setting helps you address high-latency or bandwidth-constrained environments, improving log delivery

reliability and reducing premature timeout failures in variable network conditions.

Configuring the GZIP Compression Level for Windows Server Sensors

By default, Windows Server Sensors send Windows Event Log and File Integrity Monitoring payloads over

HTTPS with a GZIP compression level of 1. You can use the set receiver compression command to fine-tune

the compression level independently for the two source types. The syntax is as follows:

set receiver compression <level> [winlog | fim]

Note the following:

Valid settings for level are from 0-9. A setting of 0 disables compression.

If you leave out the winlog | fim argument, the setting applies to both source types.

Restore the default compression level of 1 with the unset receiver compression command.

Use show receiver to see the currently configured compression settings for each data source type.

 Higher compression levels reduce bandwidth consumption while increasing CPU usage. This enhancement

provides flexibility for environments with network constraints without requiring sensor profile changes.

smb-meta-

Lets you toggle the SMB Reduction feature. Enabling this option reduces the amount of metadata collected for

profile

SMB commands. This is especially helpful in increasing your compression ratio if your network has a great deal of

SMB traffic. If you enable this, metadata is only collected for:

session setup
logoff
read
write

time

Lets you set the system date and time in <YYYY-MM-DD HH:MM:SS> format, if you are not using NTP.

token

Lets you apply a token to a sensor in a SaaS installation. The syntax is as follows:

Copy and Paste

Copy the token string from the Tokens tab and paste it into the CLI command. The syntax

Token String

is as follows:

set token string <pasted string>

Upload Token

File to Sensor

Download the token as a file from the Tokens tab, upload it to the sensor, and reference it

in the set token command. The syntax is as follows:

set token file <path to local file>

For example, the following command points to the token.text file stored in the /tmp

folder:

set token file /tmp/token.text

set

command

description

 This technique only works for Server Sensors. There isn't a way to upload the

token.text file to a newly installed modular sensor virtual machine.

Host Token on

HTTP Server

Download the token as a file from the Tokens tab, upload it to an HTTP server, and

reference it in the set token command. The syntax is as follows:

set token url http://<url to token>

You can also use an HTTPS server. In that case, the specified URL must also include the

username and password for the server.

Arguments for the "unset" Command in the Sensor
CLI Access Window
You can use the unset command with any of the arguments listed and described in the table
below. If you need help on command syntax, type unset <command> ? to see the context-
sensitive help.

set command

description

aggregator

Lets you remove aggregator settings from the sensor.

dns

dpi

Lets you remove DNS settings from the sensor.

Lets you remove a user-defined DPI metadata attribute for the specified protocol and attribute or

removes all user-defined entries with the all argument. The syntax is as follows;

unset dpi protocol custom metadata <proto> <attr> | all

Run restart service aella_flow for changes to take effect.

interface management

Lets you remove the currently configured SSH whitelist for a sensor.

ssh-whitelist

ldap-metadata

Lets you disable the Metadata Summarization feature.

logforwarder

Lets you unset logforwarder settings.

malware_upload

Lets you remove malware_upload settings.

ntp

password

proxy

Lets you remove the configured NTP settings.

Lets you remove the configured password from the sensor, resetting it to its default of aella/changeme.

Lets you remove the configured HTTP proxy for the sensor.

receiver compression

Lets you restore the compression settings for event and FIM logs from a Windows Server Sensor to the

default level of 1.

Arguments for the "exec" Command in the Sensor
CLI Access Window
The table below lists the exec commands available in the Sensor CLI Access window.

command

description

task

Lets you execute predefined tasks specified in JSON files. The JSON files specify actions such as downloading

and executing scripts. Each tasks includes parameters and exception handling instructions.

This command is only supported in the Sensor CLI Access window; it is not available in the local CLI.

tcpreset-

stop

Lets you stop the tcpreset process for specified IP addresses. If you do not specify an IP address, all active

tcpreset processes on the sensor are stopped.

tenable

Regenerates the Tenable Nessus product UUID on the Modular SensorThis command helps prevent cloned

reset uuid

Modular Sensor images from reusing the same Tenable Nessus UUID as the original sensor, reducing registration

conflicts and simplifying redeployment from a golden image.The nessusd service restarts automatically and a new

Tenable UUID is generated; the sensor's system UUID is not affected.

If the Tenable Nessus integration is not enabled on the sensor, this command returns an error.

upgrade

Lets you perform on-demand upgrades of operating system packages and the kernel on Modular Sensors, fixing

OS-level vulnerabilities without affecting critical services. You can also use the rollback function for package

changes. The syntax is as follows:

exec upgrade kernel-and-package

Starts a background OS kernel and package upgrade on the sensor. The upgrade runs as a system service and

continues even if the CLI session disconnects. Before proceeding, the command verifies internet connectivity,

displays the number of pending package upgrades, and requires double confirmation. Critical sensor packages

(suricata and squid) are held during the upgrade and released on completion. After the upgrade completes, reboot

the Modular Sensor to apply kernel changes.

Use show upgrade kernel status to monitor progress and show upgrade kernel packages to review what

changed.

 This command is only available on Modular Sensors.

exec upgrade kernel packages rollback [<package> [<version>]]

Rolls back package changes made by the last kernel and package upgrade. Double confirmation is required before

the rollback proceeds.

Without arguments – Rolls back all changed packages to their pre-upgrade versions and purges any
packages that were newly installed by the upgrade.

With <package> – Rolls back only the specified package. If the package was changed by the upgrade, it
is downgraded to its pre-upgrade version. If it was newly installed by the upgrade, it is purged.

With <package> and <version> – Rolls back the specified package to the supplied version. Use this
form when the pre-upgrade version is no longer available in the package repository. To find available
versions, run apt-cache madison <package> from the sensor shell.

 This command is only available on Modular Sensors.

Other Commands in the Sensor CLI Access Window

The table below lists other commands available in the Sensor CLI Access window.

command

description

restart service

<service_name>

Restarts the specified sensor service.

To use this command, start by running the show system command to see the status of sensor services (for

example, aella_flow, aella_mon, maltrace, and so on). Then, find the service name you need to restart

in the show system output and include it as part of the restart service <service_name> command.

copy

Refer to Capturing Trace Files for IDS Signature Matches .

Sensor Management Commands in Local CLI
This section describes some useful sensor management commands that are only available in the
sensor's local CLI.

Factory Resetting a Sensor

Under some circumstances, you may want to reset a sensor to its factory settings before it was
associated with a specific DP using either the set cm command or a token. You can do this with
the factory_reset command.

Keep in mind the following when using the factory_reset command:

The factory_reset command is only available from the sensor's local CLI. It is not
available from the DP in the Sensor CLI Access window.

The factory_reset command removes all configuration settings except basic network
settings, allowing easy re-enrollment with a DP.

You must confirm the factory_reset when prompted before it is executed.

Uninstalling a Server Sensor

You can uninstall both Linux and Windows Server Sensors from the sensor's local CLI with the
uninstall command.

 The uninstall command is not available for Modular Sensors.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

