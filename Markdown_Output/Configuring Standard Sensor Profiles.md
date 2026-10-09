✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Standard Sensor Profiles
Learn more at Stellar Cyber Academy.
The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.
M06 Open XDR Linux Server Sensor Installation and Configuration (01h:21m)  
Enhanced FIM (18m:00s)
Learn how to enable and configure File Integrity Monitoring (FIM) on Linux Server
Sensors within the Stellar Cyber Platform, setting up detection for file creation, deletion,
and modification events to strengthen security monitoring. Follow along with a hands-on
demonstration that walks through the configuration process and validates file monitoring
accuracy, confirming that FIM events are captured correctly and surfaced as Interflow
records in the data lake for analysis.
M05 Open XDR Windows Server Sensor Installation and Configuration (02h:45m)  
Advanced Configuration - Sensor Profile (18m:00s)
Customize sensor profiles using predefined templates that align with specific security
requirements, enabling granular control over data collection and processing. Watch a
demo on selecting and applying templates, fine-tuning event settings, and monitoring
enhanced data flow to the data processor within the Stellar Cyber Platform.
Advanced Configuration - File Integrity Monitoring (FIM) (18m:00s)
Enable File Integrity Monitoring (FIM) on the Stellar Cyber Platform to track and detect
unauthorized modifications to critical files on Windows Servers. Learn to configure FIM
settings for accurate file change tracking, then follow a hands-on demo to validate the
setup and confirm that file change events are captured and forwarded correctly within
the data lake for further analysis.
The first time you access a link on the portal during a session, you must log in to access
content.

Whether you add or edit a standard sensor profile you have the same options, except you cannot
edit the profile name. Standard sensor profiles can only be applied to standard sensors. To add a
standard sensor profile:
1. Select System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles.
The Sensor Profile Configuration page appears.
2. Select Create and choose Add Standard Sensor Profile.
The ADD SENSOR PROFILE screen appears.
3. Enter the Profile Name.
Stellar Cyber recommends that you establish a naming convention, so you can
understand the intent of each profile by looking at the name. This field can only contain
alphanumeric characters, underscores, spaces, and dashes.
4. Choose at least one Receiver.
Each sensor profile must have at least one receiver, which is the destination of the data
it collects.
See the Receiver configuration page for more information on working with receivers.
5. Customize your profile settings in the available tabs. The available settings are
explained below.
a. CPU Limit (%) – Specify the amount of CPU per core that the sensor can use.
To get the total for the sensor, multiply this percent by the number of cores. For
example, if you set this at 5% and you have 8 cores, the sensor could use up
to 40% of the CPU, as reported by the top and htop utility (distributed). If you
have 32 cores, the sensor could use up to 160%. A total above 100% might
seem impossible, but it’s the sum of the usage percent on all the cores, each
of which can have a maximum limit up to 100%.
Note that the aella_flow process uses multiple threads. When using the top
or htop utility with thread-mode enabled (top H or htop H), the output will
show the percent that both the aella_flow process and its children threads
use. At first, this might look like the CPU is processing twice as much as is
configured because the individual threads add up to the same amount as their

parent process and they’re all shown. To see the output displayed
hierarchically so you can visually distinguish data for the parent process from
data for its children threads, enable tree view mode (top V or htop F5).
The commands to use:
In top, press H to show threads and V to enable tree view.
In htop, press H to show threads and F5 to enable tree view.
By enabling the thread display along with tree view, you can clearly see which
threads are associated with which parent processes, providing a detailed and
organized view of CPU usage.
 The Server Sensor uses a minimum of 300 MHz, even if the value
specified for CPU Limit (%) results in a smaller value based on the host
CPUs. For example, if the Server Sensor is installed in a host with 2 CPUs
running at 2.2 GHz and you specify a value of 5% for CPU Limit (%), the
arithmetic of 5% * 2 CPUs * 2.2 GHz would indicate an assignment of 220
MHz for the Server Sensor. However, in a situation such as this, the
Server Sensor uses its minimum assignment of 300 MHz, even though it
is greater than the specified value.
6. Use Restore Windows Profile to Template to apply an available template to your
profile settings in the Windows tab.
Separate templates let you apply Low, Medium, and High volume settings for
Windows Server Sensors, depending on your deployment needs. Refer to Windows
Server Sensor Customizations for details on the available settings.
7. Select Submit.
The profile is immediately active.
Customizing Standard Sensor Profile Features
The available customizations are grouped into tabs under Feature Customization, providing
control over:
Network Tab – Network traffic analysis settings for device sensors and Linux Server
Sensors
Sensor Tab – Buffering settings
Linux Tab – Settings for Linux Server Sensors
Windows Tab – Settings specific to Windows Server Sensors
To enable or disable an option or group of options within the tab, use the toggle for that option.
To open a group of options to fine-tune your customization, select the name of the group (or
anywhere else away from the toggle).
Sensor Profile Customizations in the Network Tab
These settings apply to network sensors and Linux Server Sensors.

Network Traffic
You can toggle the analysis of Network Traffic on and off as a whole in the Network tab:
With Network Traffic disabled, the sensor operates as a Log Forwarder. None of the other
features in the Network tab are available for selection or configuration. In addition:
Malware Sandbox is disabled in the Sensor tab.
IDPS is disabled in the Sensor tab.
You can see the differences in the system processes running on a sensor before and after
disabling Network Traffic in a sensor's Sensor Details page, as shown in the illustration below:
You can see similar information with the show system command in the sensor CLI. For example,
the show system processes at left are for a sensor with all main sensor features enabled
(Network Traffic, Malware Sandbox, IDPS, and Log Forwarder). By contrast, the show
system output at right shows a sensor after Network Traffic has been toggled off:
 When you disable Network Traffic, Stellar Cyber ask you to confirm your decision and
provides you with the option of saving or clearing buffered data for affected sensors.
Traffic Filtering (Pre-DPI Filters)
Enable this option to optimize sensor performance by removing unnecessary traffic before
performing Deep Packet Inspection (DPI). For configuration details, see Pre-DPI Filters .
Application Identification
Enable this option for the sensor to identify applications associated with events.
Application Session

Enable this option for the sensor to identify the length of individual network sessions. The
parameters specify how often to report the session information and what timeout to apply when
determining that a session has ended.
If you disable Application Session, network and server sensors stop sending data to
the DP. Data sensors continue to process traffic.
If you enable Session Combine, UDP sessions from the specified ports to the same
destination are combined into a single session.
Application Metadata
Enable this to control how application information is collected and which applications are
included.
You can disable the collection of application metadata to increase sensor performance and save
storage space, but that limits collected data to:
Basic session information
Packet and byte counts
IP address
Port
You can set the Metadata Collection Level to Limited Visibility, Minimum Recommended,
Standard, or Maximum. This controls how many of the information fields are collected.
Click to see the fields collected by Limited Visibility:
0zz0 login
0zz0 password
activesync login
aim_express contact_login
aim_express login
aims login
archive login
archive password
badongo login
badongo password

badoo contact_login
badoo login
badoo password
bebo login
bebo password
dhcp agent
dhcp chaddr
dhcp ciaddr
dhcp client_fqdn
dhcp domain_name
dhcp dns_server
dhcp end
dhcp end_status
dhcp giaddr
dhcp host_name
dhcp inherit_parent
dhcp ip_lease_time
dhcp message_type
dhcp option
dhcp option_type
dhcp option_value_buffer
dhcp request
dhcp router
dhcp siaddr
dhcp sname
dhcp subnetmask
dhcp xid
dhcp yiaddr
dimp login
dimp password
dns dns_entry
dns dns_query
dns end
dns tunneling
dns flags
dns host
dns host_addr
dns host_addr6
dns host_type
dns message_type
dns name
dns query
dns query_type
dns reply_code
dns reverse_addr
dns reverse_addr6

dns section_type
dns transaction_id
dns ttl
ebuddy contact_login
ebuddy login
ebuddy password
facebook login
facebook password
facebook_mail login
friendster login
friendster password
ftp content_type
ftp data_port
ftp filename
ftp filesize
ftp index
ftp loadway
ftp login
ftp password
ftp method
ftp return_code
ftp transfer_duration
gmail_basic login
gmail_chat login
gmail_mobile login
gmail_mobile password
gmx login
hi5 login
hi5 password
http auth_username
http auth_password
http code
http index
http method
http proxy_auth
http proxy_login
http proxy_realm
http referer
http server
http uri
http filename
http file_type
http forward_addr
http forward_addr6
http host
http mime_type

http part_content_type
http user_agent
ica login_info
ica login_info_utf16
icmp code
icmp message
icmp rtt
icmp type
kakaotalk login
krb5 error_code
krb5 login
krb5 server
krb5 message_type
krb5 service
laposte_webmail login
ldap hostname
ldap name
linkedin login
live_groups login
live_hotmail login
livemail_mobile login
mailru login
maktoob login
mimp login
mimp password
msn contact_login
msn login
mysql login
mysql query
mysql request
mysql result_set
mysql sqlstate_code
mysql number_columns
mysql number_rows
mysql query_id
netflix login
netlog login
netlog password
nfs filename
nfs filesize
nfs type_string
nfs symlink_name
nfs uid
niconico_douga login
nntp login
nntp password

odnoklassniki login
odnoklassniki password
oovoo login
orangemail login
owa login
paltalk contact_login
paltalk login
paltalk_transfer login
pap login
pap password
perfspot login
perfspot password
pop3 password
postgres authentification_type
postgres error
postgres login
postgres password
postgres query
postgres query_id
postgres sqlstate_code
postgres number_columns
postgres number_rows
qq contact_login
qq login
qq_transfer login
radius login_ipv6_host
radius login
rambler login
rambler password
rambler_webmail rambler_webmail
rapidshare login
rapidshare password
rdp default_username
rdp username_ascii
rdp username_raw
rlogin client_login
rlogin server_password
rsh login
rsh remote_login
rsync login
rsync password
rtmp page_url
secondlife login
skyblog login
skyblog password
slsk login

slsk password
smb login
smb user_id
smb nt_status
smb command_string
smpp receiver
smpp sender
smtp login
smtp password
smtp response_code
snpp login
snpp password
socks5 login
socks5 password
spdy server_agent
spdy user_agent
squirrelmail login
squirrelmail password
ssh version
ssl common_name
ssl issuer
ssl subject_alt_name
ssl validity_not_after
ssl version
ssl validity_not_before
tagged login
tagged password
tango login
tchatche login
tchatche password
tds login
tds password
tds sqlstate_code
tds query
tds query_id
tds number_columns
tds number_rows
teamspeak login
teamspeak password
telnet login
telnet password
tftp filename
tftp filesize
tftp query
tftp request_filename
tns login

tns password
tns query
tns sqlstate_code
twitter login
twoo login
twoo password
ustream login
ustream password
viadeo login
viadeo password
vkontakte login
vkontakte password
winmx login
yahoo_groups login
yandex login
yandex password
yandex_webmail login
ymail2 login
ymail_classic login
ymail_mobile_new login
ymail_mobile_new password
ymsg_conf login
ymsg contact_login
ymsg login
ymsg_transfer login
ymsg_video login
ymsg_webmessenger contact_login
ymsg_webmessenger login
youtube login
youtube password
zimbra login
zimbra password
zimbra_standard login
zimbra_standard password
Minimum Recommended collects everything in Limited Visibility. There is currently no
difference between Minimum Recommended and Limited Visibility.
Standard collects everything in Minimum Recommended and:
amqp class
amqp type
amqp method
amqp replyto
amqp routing_key
dhcp circuit_id
dhcp remote_id
dhcp remote_id_subtype

dhcp remote_id_type
dns web_application_info
dns ancount
dns arcount
dns nscount
dns opcode
dns qdcount
ftp return_content
ftp offset
ftp inherit_parent
ftp data_port_end_offset
ftp data_port_start_offset
ftp_data inherit_key
http cache_control
http connection_header
http content_disposition
http content_encoding
http content_len
http cookie
http date
http end
http etag
http expires
http image_type
http is_webdav
http location
http ntlm_domain
http ntlm_user
http ntlm_workstation
http part_filename
http part_header_name
http part_header_value
http part_name
http request
http request_size
http server_agent
http set_cookie
http smb_client
http version
http video_type
http video_url
icmp seq
icmp typeval
icmp wrong_crc
krb5 err_cname_name
krb5 err_sname_name

krb5 realm
ldap krb5_enc_data
ldap krb5_enc_data_type
ldap krb5_err_cname
ldap krb5_err_cname_name
ldap krb5_err_cname_type
ldap krb5_err_crealm
ldap krb5_err_data
ldap krb5_error_code
ldap krb5_err_realm
ldap krb5_err_sname
ldap krb5_err_sname_name
ldap krb5_err_sname_type
ldap krb5_err_text
ldap krb5_kdcoptions
ldap krb5_message
ldap krb5_message_type
ldap krb5_pa_data
ldap krb5_pa_data_type
ldap krb5_pa_data_value
ldap krb5_realm
ldap krb5_server
ldap krb5_service
ldap krb5_ticket
ldap krb5_ticket_enc_part
ldap krb5_ticket_name
ldap krb5_ticket_name_type
mysql end
mysql bind_variable
mysql variable_id
mysql variable_type
mysql variable_value
nfs current_state
nfs gid
nfs mode
nfs procedure
nfs status
nfs type
nfs version
pop3 attach_filename
pop3 file_type
pop3 login_server
pop3 login
pop3 received_by_name
pop3 received_date
pop3 receiver

pop3 received_from_name
pop3 receiver_email
pop3 sender
pop3 sender_email
pop3 subject
postgres variable_format
postgres variable_id
postgres variable_type
postgres variable_value
postgres base
postgres proto_version
postgres server_version
rpc message_type
rpc procedure
rpc program
rpc xid
sip authorization_username
smb filename
smb filesize
smb file_type
smb directory
smb domain
smb file_id
smb host
smb krb5_error_code
smb krb5_err_text
smb krb5_ticket
smb loadway
smb native_os
smb path
smtp attach_filename
smtp attach_size
smtp file_type
smtp received_by_name
smtp received_date
smtp received_from_name
smtp receiver
smtp receiver_email
smtp sender
smtp sender_email
smtp server
smtp subject
snmp method
snmp name
snmp oid
snmp value_raw

snmp version
spdy location
spdy mime_type
ssl certif_sha1
ssl handshake_type
ssl organization_name
ssl parent_common_name
ssl protocol_version
ssl server_name
syslog code
tds bind_variable
tds variable_id
tds variable_type
tds variable_value
telnet term_type
tftp mode
tns client_hostname
tns server_hostname
tns bind_variable
tns variable_id
tns variable_type
tns variable_value
Maximum collects everything in Standard and:
amqp correlation_id
amqp exchange_type
amqp revision
amqp server_major_version
amqp server_minor_version
ica application
ica application_utf16
ica priority
ica service
mysql base
pop3 attach_disposition
pop3 attach_transfer_encoding
pop3 date
pop3 received_by_ip
pop3 received_from_ip
pop3 received_server_agent
pop3 received_with
pop3 receiver_alias
pop3 receiver_type
pop3 sender_alias
pop3 user_agent
rpc program_version
rpc state

rpc version
sip inherit_key
sip inherit_parent
sip method
sip reply_code
sip request_call_id
sip user_agent
smb attributes
smb ext_attributes
smb file_attributes
smb file_chunk_data_offset
smb file_chunk_len
smb krb5_enc_data
smb krb5_enc_data_type
smb krb5_err_cname
smb krb5_err_cname_name
smb krb5_err_cname_type
smb krb5_err_crealm
smb krb5_err_data
smb krb5_err_realm
smb krb5_err_sname
smb krb5_err_sname_name
smb krb5_err_sname_type
smb krb5_kdcoptions
smb krb5_message
smb krb5_message_type
smb krb5_pa_data
smb krb5_pa_data_type
smb krb5_pa_data_value
smb krb5_realm
smb krb5_server
smb krb5_service
smb krb5_ticket_enc_part
smb krb5_ticket_name
smb krb5_ticket_name_type
smb search_attributes
smb search_pattern
smb security_blob
smb service
smb service_data
smb session_key
smb share_access
smtp attach_disposition
smtp attach_transfer_encoding
smtp content_language
smtp content_transfer_encoding

smtp date
smtp received_by_ip
smtp received_from_ip
smtp received_server_agent
smtp received_with
smtp receiver_alias
smtp receiver_type
smtp replyto
smtp sender_alias
smtp server_agent
smtp start_time
smtp stop_time
smtp user_agent
tns base
tns client_os
tns client_program_name
tns client_program_path
tns response_size
tns server_os
tns server_port
tns version
Collection Scope allows you to filter specific metadata that is sent to the Data Processor.
Select All applications for no traffic filtering
Select Exclude certain applications to collect metadata for all content except the
applications and application groups you specify in the selector box. .
Select Only collect certain applications to exclude all metadata except that for the
applications and application groups you specify in the selector box.
When you select an option other than All applications, the user interface updates for you to
then Exclude or Include the following applications or application groups. Begin typing in the
selector box to display a list of configured Application Groups and Applications. Applications
Groups are listed first. Scroll through the list to get to the set of Applications. When you select
an Application Group, the label for it is has a prefix (Group: ) to distinguish it from Applications.
In the image above, there is one application and one group.
 In previous releases, Application Groups were referred to as Tags.
Metadata Summarization allows you to reduce traffic to the DP. If you enable this, the sensor
groups similar metadata from chatty applications into a single JSON file before sending to the
DP.

Finally, you can enable SMB Reduction to reduce the amount of metadata collected for SMB
commands. This is especially helpful in increasing your compression ratio if your network has a
great deal of SMB traffic. If you enable this, metadata is only collected for the following:
session setup
logoff
read
write
Process Correlation
Enable this to build correlations between processes running on the sensor and host, and the IP
address/port visible in traffic. The processes monitored include:
log forwarder
IDS
maltrace
aella_flow
SSHD
HTTP
You can set the sampling time interval.
Packet Deduplication
Enable this for the sensor to perform packet deduplication. This reduces storage by removing
duplicate data. However, it uses processing power on the sensor to analyze the data, and can
significantly slow system performance. When you enable it, you can set the deduplication time
window.
Enable with caution.
If you have no need for this (for example, if you have a sensor for every network segment),
disable it.
Stream Slicing

Enable this to perform stream slicing, which truncates sessions at the specified length. This can
reduce the bandwidth used.
This has no effect if you use local file assembly.
Handshake Failure
Enable this to detect handshake failures and allocate resources for that effort:
Time(s) – Amount of time the sensor collects failures to get to the threshold
Threshold – The number of failures over the specified time before an alert on this is
triggered
Report Interval – Interval between reports to the DP if there are multiple failures
Memory Limit (%) – Maximum percentage of memory used by aella_flow for this
detection
Flood Attack
Enable this to report flood attacks:
Flood Threshold (Source) – The number of new session requests per second from a
single source before an attack is reported
Flood Threshold (Destination) – The number of new session requests per second
from any source before an attack is reported
Flood Expire Time – The number of seconds without new session requests after which
we stop considering it an attack, and the sensor sends a session_end message to the
DP
Flood Report Interval – During an attack, the interval at which the sensor reports the
attack to the DP (so that the DP isn't flooded with reports of the flood attack)

TCP Syn Flag Check – Only counts session requests if the SYN flag in the packet is
set
Sensor Profile Customizations in the Sensor Tab
The settings in the Sensor tab let you configure:
Buffering
Buffering
If you enable buffering, the sensor buffers the logs sent to Stellar Cyber. If the logs are received
successfully, the sensor deletes the buffered logs. If the buffer is full, the sensor stops buffering
logs.
 Windows events are buffered separately by winlogbeat and do not use the Buffering options.
Similarly, FIM events are also buffered separately.
You can set the following buffering options:
Sum Size (MB) – The total of all Traffic, Log Forwarder, and Maltrace logs buffered
Traffic – The amount, in MB, of traffic logs buffered
 When you disable buffering, any data in the buffer is immediately deleted. Ensure that the
sensor has had a stable connection to the DP for long enough to transmit all data in the
buffer.
Linux Server Sensor Customizations
The settings in the Linux tab let you specify settings for Linux Server Sensors:
Linux Auditing – When enabled, the sensor checks its files for signs of alteration and
monitors command executions.
 This option is separate from the dedicated FIM Linux options for file integrity
monitoring below.

Force Linux Auditd to Stop – Stellar Cyber uses the aella_audit process
to collect audit logs. Linux uses the auditd process. In most scenarios, the
two processes coexist with each collecting data successfully. However, on
older systems with pre-3.16 kernels, the processes can conflict, causing
aella_audit to stop. If aella_audit is enabled, but you see no data on the
DP, use this to stop the auditd process on older Linux systems.
 In some situations, the auditd configuration may be locked by the Linux
kernel (audit configuration is locked in the kernel
(enabled=2)), preventing this option from working. In these situations, if
you are running 4.3.7 sensor software, you must remove immutable flag
(-e 2) from the auditd config, followed by a reboot of the host system.
You do not need to do this in 5.1.1 – the Force Linux Auditd to Stop
option works correctly, even if the auditd configuration is locked.
Buffering – Enabling this allows you to set the size of the Traffic, Linux Event, and
Windows Event buffers.
 This option is deprecated but is still present to provide backwards compatibility
with legacy Server Sensors that have it enabled in their profiles. It can no longer be
enabled. However, legacy profiles that still have this feature enabled can use this
option to disable it.
Resource Allocation – You can set the following options:
Control CPU Affinity – Choose which CPU in a multi-core system the sensor
uses for the control thread.
Data CPU Affinity – Choose which CPU in a multi-core system the sensor
uses for the data processing thread.
CPU Limit (%) – Specify the amount of CPU per core that the sensor can use.
To get the total for the sensor, multiply this percent by the number of cores. For
example, if you set this at 5% and you have 8 cores, the sensor could use up
to 40% of the CPU, as reported by the top and htop utility (distributed). If you
have 32 cores, the sensor could use up to 160%. A total above 100% might
seem impossible, but it’s the sum of the usage percent on all the cores, each
of which can have a maximum limit up to 100%.
Note that the aella_flow process uses multiple threads. When using the top
or htop utility with thread-mode enabled (top H or htop H), the output will
show the percent that both the aella_flow process and its children threads
use. At first, this might look like the CPU is processing twice as much as is
configured because the individual threads add up to the same amount as their
parent process and they’re all shown. To see the output displayed
hierarchically so you can visually distinguish data for the parent process from
data for its children threads, enable tree view mode (top V or htop F5).
The commands to use:
In top, press H to show threads and V to enable tree view.

In htop, press H to show threads and F5 to enable tree view.
By enabling the thread display along with tree view, you can clearly see which
threads are associated with which parent processes, providing a detailed and
organized view of CPU usage.
 The Server Sensor uses a minimum of 300 MHz, even if the value
specified for CPU Limit (%) results in a smaller value based on the host
CPUs. For example, if the Server Sensor is installed in a host with 2 CPUs
running at 2.2 GHz and you specify a value of 5% for CPU Limit (%), the
arithmetic of 5% * 2 CPUs * 2.2 GHz would indicate an assignment of 220
MHz for the Server Sensor. However, in a situation such as this, the
Server Sensor uses its minimum assignment of 300 MHz, even though it
is greater than the specified value.
Memory Usage Limit (%) – Specify the amount of memory the sensor can
use.
FIM Linux – Enable this feature to monitor specified files and directories for changes,
creations, and deletions. See the next section for details.
Configuring File Integrity Monitoring (FIM Linux)
See the top of this page for recommended lessons about this section at Stellar
Cyber Academy.
Enabling the FIM Linux feature in a Sensor Profile lets you keep track of changes to specified
files and directories, including file changes, file creations, and file deletions.
When you enable the FIM Linux feature, a new table appears in the Sensor Profile dialog box
that lets you specify both the files and directories you want to monitor for changes, as well as the
types of changes for which you want to monitor. As you can see in the image below, the table is
preconfigured with a set of paths recommended for monitoring.
Click the + Add Row button to add new files/directories to the FIM feature. For each entry in the
table, you can configure the following:
Enabled – Specifies whether the indicated files/directories are enabled for monitoring.
This lets you toggle a given file/directory on or off for monitoring without needing to
delete it from the profile entirely.
Path – Specifies the directory to monitor.
Inclusions – Specifies the files within the directory to monitor. You can use the asterisk
(*) character for standard wildcarding. For example, *.sh. If you leave this field blank, it

is implicitly set to *, meaning that all files in the specified path are included for
monitoring.
Exclusions – Specifies the files within the directory to exclude from monitoring. You
may want to use this feature to exclude certain file types that are trusted and change
often. Standard wildcarding is supported here, too. By default, this field is set empty and
no files are excluded from monitoring.
Depth – Specifies how many directories below the specified directory to monitor.
 A depth of 0 means that you are monitoring only the specified directory and
nothing below it.
Change/Create/Delete – Use these check boxes to specify the types of changes to
track in the specified path.
 In general, it's a good idea to optimize performance by focusing your FIM settings on specific
files rather than large directories with many files and subdirectories. Refer to Best Practices
for File Integrity Monitoring (FIM) for performance guidelines and a set of system files
recommended for integrity monitoring.
The FIM feature works by recording a file hash for all files configured for monitoring in the Sensor
Profile. Once the initial hash is recorded, the FIM feature regularly monitors for changes to the
file hash and sends events to the DP if changes are seen.
You can keep track of events generated by the FIM feature in the following ways:
Use the predefined Dashboards | PREDEFINED | File Integrity Monitoring dashboard.
Use the Threat Hunting feature to search the Linux Events index for events with
msg_origin.source set to linux_agent and msg_origin.processor.type set to
FIM (or agent.type set to auditbeat). Once you find such an event, you can add it to
the Threat Hunting Documents table by using the Toggle add column to table button
adjacent to its entry and sort to see all such events.
Similarly, you can create ATH rules with queries based on the
msg_origin.processor.type field set to FIM.
The JSON for a FIM event indicates the type of change that took place. If the event indicates
either a change or a deletion, the JSON includes both old and current values. For example,
the illustration below shows a change in a file's hash between the old and current sections,
indicating that its contents changed. If the event indicates a file creation, only the current
section appears in the JSON.
Linux Server Sensor Installation Directories Excluded from FIM

Note that the following installation directories for the Linux Server Sensor are automatically
excluded from FIM monitoring. The user interface does not prevent you from adding these
directories; however, they are still automatically excluded from FIM monitoring:
/var/aella/
/var/log/aella
/opt/aella
/opt/aelladata
 Keep in mind that the FIM Linux feature can only monitor files and folders that exist when
the aella_audit service restarts. If you add a non-existent file or folder for monitoring in the
Sensor Profile and then create the folder later, it won't be monitored until aella_audit
restarts.
Windows Server Sensor Customizations
See the top of this page for recommended lessons about this section at Stellar
Cyber Academy.
You can configure Windows Server Sensors to collect specific logs. Logs are organized into
different predefined channels in the Windows tab, each with its own maximum log size. You can
toggle collection of the available logs and event types in each of the different individual channels,
or opt for the simple route and use one of the predefined templates for Windows Server Sensors
provided by Stellar Cyber. You can also apply filters configured in the System | DATA SOURCE
MANAGEMENT | Data Filters | Log Filters page as Event Filters, excluding or including matching
events.
Start with a Windows Server Sensor Template
Stellar Cyber recommends that you start configuration of a Windows Server Sensor profile by
using one of the predefined templates included with the system. These templates have been
carefully configured to match common deployment scenarios. Once you have reviewed the
settings in a template and seen how it operates in your environment, you can tailor the settings in
individual channels to fit your needs.
The following templates are available for options in the Windows tab of the ADD/EDIT
SENSOR PROFILE window:
Windows Detect Profile (Low Volume). The selection covers the minimal events
required for all native detections in Stellar Cyber.
Windows Context Profile (Medium Volume). Adds events commonly used by third-
party detection rules.

Windows Compliance Profile (High Volume). Covers all Windows events.
Each of these profiles collects a different set of logs/events and results in a progressively higher
volume of data ingestion from Low to Medium to High.

If you find that you are ingesting a higher volume of data than you would like relative to your
license limits, you may want to reconfigure these settings, keeping in mind that the Low
Volume profile provides enough coverage for all native Stellar Cyber detections.
Click here to see the differences in the logs/events collected by each of the available
templates:
Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
|          |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| Security |     |     |     |     |     |     |
Collect
|     | Account   |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
Windows
Logon
|                | Credenti | For |    |     |    |    |
| -------------- | -------- | --- | --- | --- | --- | --- |
| advanced       | Events   |     |     |     |     |     |
| security audit | al       | UEB |     |     |     |     |

| policy settings | Validatio | A   |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- | --- |

n alert
events.

s.

|     |         |     |    |     |    |    |
| --- | ------- | --- | --- | --- | --- | --- |
|     | Kerbero | For |     |     |     |     |
s UEB

Authenti A

cation alert

Service s

|     |     |     |    |     |    |    |
| --- | --- | --- | --- | --- | --- | --- |
Kerbero

s

Service

Ticket

Operatio
|     | ns  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- |
Other

Account
|     | Logon   |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- |
|     | Events  |     |     |     |     |     |
|     | Account |     |     |     |     |     |

|     | Manage |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |

|     | Applicati |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
ment

on
Events

Group

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
|     |   Manage |     |     |     |     |
| --- | -------- | --- | --- | --- | --- |
|     |   ment   |     |     |     |     |
|     |          |     |     |     |    |
|     | Comput   |    |    |     |     |
|     |   er     |     |     |     |     |
Account
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Manage

ment

|     | Distributi |     |     |     |    |
| --- | ---------- | --- | --- | --- | --- |

on

Group

Manage

ment


|     | Security |    |    |     |     |
| --- | -------- | --- | --- | --- | --- |

Group

Manage
|     | ment |     |     |     |     |
| --- | ---- | --- | --- | --- | --- |
|     |      |     |     |     |    |
User   

|     | Account |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |

Manage
ment

|     | Other |    |     |    |    |
| --- | ----- | --- | --- | --- | --- |

Account
|     | Manage |     |     |     |     |
| --- | ------ | --- | --- | --- | --- |
|     | ment   |     |     |     |     |
Events

Detailed
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Tracking
|     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- |
DPAPI A   
|     | Events |     |    |     |     |
| --- | ------ | --- | --- | --- | --- |

ctivity


|     |   PNP |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |

Activity

|     |   Process | For |     |     |    |
| --- | --------- | --- | --- | --- | --- |
|     |           |    |    |     |     |

|     |   Creation | alert |     |     |     |
| --- | ---------- | ----- | --- | --- | --- |

s

|     |     | relat |     |     |     |
| --- | --- | ----- | --- | --- | --- |
|     |     | ed to |     |     |     |
proc

Windo
ws
Note
Channel Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
ess
creat
ion
ano
malie
s.

Process 
Terminat
ion

RPC Ev
ents

Token
Right
Adjustm
ent
Events
DS
Access

Detailed
Events
Director
y
Service
Replicati
on
Director   
y
Service
Access
  
Director
y
Service
Change
s

Director
y
Service

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Replicati
on
Logon/L
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
ogoff

| Account |     |     |     |     |
| ------- | --- | --- | --- | --- |
Events
Lockout

| User/De |     |     |     |    |
| ------- | --- | --- | --- | --- |

vice

Claims

| Group |     |     |     |    |
| ----- | --- | --- | --- | --- |

Member

ship


|   IPsec |     |     |     |     |
| ------- | --- | --- | --- | --- |
Extende

d Mode


|   IPsec |     |     |     |     |
| ------- | --- | --- | --- | --- |
Main
Mode

| IPSec |     |     |     |     |
| ----- | --- | --- | --- | --- |
Quick
Mode

| Logoff |     |     |     |     |
| ------ | --- | --- | --- | --- |

| Logon | For  |    |     |     |
| ----- | ----- | --- | --- | --- |
UEB
A
alert
s

| Network |     |     |     |     |
| ------- | --- | --- | --- | --- |
Policy
Server
| Special |     |     |    |    |
| ------- | --- | --- | --- | --- |
Logon

| Other |    |     |    |     |
| ----- | --- | --- | --- | --- |
Logon/L

Windo
ws
Note
Channel Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
ogoff
Events
Object
Access

Applicati
Events
on
Generat
ed
Certificat   
ion
Services
Detailed   
File
Share
File   
Share
File   
System
Filtering   
Platform
Connecti
on

Filtering
Platform
Packet
Drop

Handle
Manipul
ation
Kernel   
Object
Registry   

Remova
ble
Storage

Windo
ws
Note
Channel Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
SAM  

Central
Access
Policy
Staging
Other   
Object
Access
Events
Policy
Change
Events Audit   
Policy
Change
Authenti   
cation
Policy
Change
Authoriz   
ation
Policy
Change

Filtering
Platform
Policy
Change

MPSSV
C Rule-
Level
Policy
Change

Other
Policy
Change
Events

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
| Privileg   |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
e Use
| Non-   |     |     |     |     |    |
| ------ | --- | --- | --- | --- | --- |
| Events |     |     |     |     |     |
Sensitiv

e

Privilege

Use

| Sensitiv |    |     |    |     |     |
| -------- | --- | --- | --- | --- | --- |
e
Privilege
Use

| Other |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- |
Privilege
Use
Events
| System   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
Events

| IPsec |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- |

Driver


| Security |    |     |    |     |     |
| -------- | --- | --- | --- | --- | --- |

State

Change


| Security |    |     |    |     |     |
| -------- | --- | --- | --- | --- | --- |

System

Extensio

n

| System |    |     |    |     |     |
| ------ | --- | --- | --- | --- | --- |
Integrity

| Log |    |     |    |     |     |
| --- | --- | --- | --- | --- | --- |
Clear

| Other |    |     |    |     |     |
| ----- | --- | --- | --- | --- | --- |
System
Events
| Specify  |               |    |               |    |     |
| -------- | ------------- | --- | ------------- | --- | --- |
| Exclude  |               |     |               |     |     |
| Event or | Include Only: |     | Include Only: |     |     |
IDs 1102, 1104, 4611, 4616, 4624-4625, 1102, 1104, 4611, 4616, 4624-

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Include 4648-4649, 4656-4658, 4660-4662, 4625, 4648-4649, 4656-4658,
Only 4663, 4673-4674, 4688, 4768, 4692, 4660-4663, 4672-4674, 4688-
|     |     | 4697-4699, 4701-4702, 4704, 4706,  |     | 4689, 4692, 4697-4699, 4701- |     |
| --- | --- | ---------------------------------- | --- | ---------------------------- | --- |
|     |     | 4713-4714, 4720, 4722, 4725-4732,  |     | 4702, 4704, 4706, 4713-4714, |     |
|     |     | 4734, 4738, 4741-4743, 4754, 4756- |     | 4718-4720, 4722, 4724-4734,  |     |
|     |     | 4758, 4765-4767, 4769, 4771, 4776, |     | 4738-4743, 4754, 4756-4758,  |     |
|     |     | 4781-4782, 4794, 4799, 4825, 4898- |     | 4765-4767, 4768-4769, 4771,  |     |
|     |     | 4899, 4905, 5030, 5034-5035, 5038, |     | 4776, 4781-4782, 4794, 4799, |     |
|     |     | 5136, 5140, 5145, 5156, 5379,      |     | 4825, 4898-4899, 4905, 5030, |     |
|     |     | 6281, 6416, 6423                   |     | 5034-5035, 5038, 5136, 5140, |     |
5145, 5156, 5379, 6281, 6416,
6423
| System |     |     |    |    |    |
| ------ | --- | --- | --- | --- | --- |
Collect
Windows
system events.
| Application |     |     |    |    |    |
| ----------- | --- | --- | --- | --- | --- |
Collext
Windows
application
events.

| Forwarded |     |     |    |    |     |
| --------- | --- | --- | --- | --- | --- |
Events
Collect
Windows
events
forwarded from
other Windows
machines.

| DHCP Client |     |     |    |    |     |
| ----------- | --- | --- | --- | --- | --- |
Collect
Windows
DHCP client
events
|         |     |     |    |    |    |
| ------- | --- | --- | --- | --- | --- |
| Windows |     |     |     |     |     |
Firewall

Windo
ws
Note
Channel     Windows Detect Profile Windows Context Profile Compli
s
ance
Profile
Collect
Windows
advanced
security firewall
events.
| Windows |     |     |     |     |     |    |
| ------- | --- | --- | --- | --- | --- | --- |
|         |     |    |     |    |     |     |
Defender
| Collect | Specify   |     |    |     |    |     |
| ------- | --------- | --- | --- | --- | --- | --- |
Event
| specified |     | Include Only: |     | Include Only: |     |     |
| --------- | --- | ------------- | --- | ------------- | --- | --- |
IDs
Windows 1006-1008, 1015, 1116-1119, 2013 1006-1008, 1013, 1015, 1116-
Defender
1119, 1121, 2013, 5001, 5010,
| events. |     |     |     | 5012-5013, 5101 |     |     |
| ------- | --- | --- | --- | --------------- | --- | --- |


| Sysmon |     |    |     |    |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
Collect
specified
|     | Specify   |     |    |     |    |     |
| --- | --------- | --- | --- | --- | --- | --- |
Windows
|     | Event | Include Only: |     | Include Only: |     |     |
| --- | ----- | ------------- | --- | ------------- | --- | --- |
sysmon events
IDs
|     |     | 1, 3, 10, 13 |     | 1, 3, 5, 7-8, 10-13, 15, 17, 20-21, |     |     |
| --- | --- | ------------ | --- | ----------------------------------- | --- | --- |
for process
23
anomaly
detections.


| PowerShell |     |    |     |    |     |     |
| ---------- | --- | --- | --- | --- | --- | --- |
Collect
specified
|     | Specify   |     |    |     |    |     |
| --- | --------- | --- | --- | --- | --- | --- |
Windows
|     | Event | Include Only: |     | Include Only: |     |     |
| --- | ----- | ------------- | --- | ------------- | --- | --- |
PowerShell
IDs
| operational |     | 4104 |     | 4103-4104, 40961-40962 |     |     |
| ----------- | --- | ---- | --- | ---------------------- | --- | --- |
logs.

| FIM | Not   |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- |
enabled
Configure and
| enable file | by  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
default in
integrity
any
monitoring.
template.

How to Apply a Windows Server Sensor Template
You apply a profile for settings in the Windows tab as follows:
1. Navigate to System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles,
select Create, and then select Add Standard Sensor Profile.
2. Navigate to Restore Windows Profile to Template and choose the Select Template
dropdown. Then, use the context menu that appears to select one of the available
Windows Server Sensor profiles, as illustrated below:
Note the following:
The Set to Template button is only available in the Windows tab of the
Add/Edit Sensor Profile window and only affects the options available in the
Windows tab.
When you select one of the templates in the Restore Windows Profile to
Template menu, all options in the Windows tab are reset according to the
selected template. All other profile options are left unchanged. For example, if
you have made customizations to the options in the Network tab, those
options remain at their current settings after applying a Windows template to
reset the options in the Windows tab.
You can reset the options in the Windows tab using a template as often as
you like, keeping in mind that all the options in the tab are reset to match the
template each time you do so. You can also start with a template and then
tweak individual settings as you see fit.
Applying Event Filters
You can use the Add Event Filters fields to Exclude or Include events matching the listed
filters, giving you fine-grained control on which events are processed. You can apply any of the
filters configured in the System | DATA SOURCE MANAGEMENT | Data Filters | Log Filters page
as Event Filters; when you click or tap in the panels, a list of the available filters appears. Select
any filters that you want to apply as Exclude or Include filters.
Keep in mind the following notes when using filters configured in the System | DATA SOURCE
MANAGEMENT | Data Filters | Log Filters page as Event Filters for a Windows Sensor Profile:
Event Filters apply to events in the following channels: FIM (File Integrity Monitoring)
, Security, System, Application, Forwarded Events, Microsoft Windows
DHCP Client, Microsoft Windows Firewall with Advanced Security Firewall,
Microsoft Windows Defender, Microsoft Windows Sysmon, Microsoft Windows
PowerShell Operational, and Other Channels.

Event Filters are joined with the Specify Event IDs entries in the other channels using
a logical AND. This means that a given event must match both the Event Filters and the
Specify Event IDs entries to pass the filter.
For example, consider the following configuration:
Event Filter is set to Exclude field process-id=100
Specify Event IDs is set to Include ID 1
In this situation the overall filter will ingest logs with an ID of 1 that do not have field
process-id=100.
This allows you to apply advanced log filters to refine the data ingested by the Stellar
Cyber platform, ensuring you focus on the most relevant events. For example, you can
filter out event logs with particular process IDs detected by File Integrity Monitoring
(FIM) while using a wildcard to match .exe filenames. If these processes are linked to
routine system processes, excluding these logs prevents irrelevant data from
consuming bandwidth and storage, while ensuring critical events from other processes
are still ingested. This targeted filtering reduces unnecessary noise in your logs, helping
you streamline investigations and focus on detecting meaningful threats.
Exclude filters are always applied before Include filters, in the order they are specified.
If you specify Include filters, only those logs matching the specified Include filters are
ingested. All logs that do not match the specified Include filters are dropped.
Only use Log Filters configured without the optional Log Source specified, as
demonstrated in the figure below. Log Filters with a Log Source configured won't match
any event logs on the Windows Server Sensor when used as Event Filters.
 Refer to Managing Log Filters for detailed instructions on configuring Log Filters.
You can apply a maximum of 100 Event Filters each in the Exclude and Include panels.
The Windows Server Sensor templates do not set any Event Filters.
Keeping Tabs on Log Filter Statistics
You can keep tabs on statistics related to log filters using the show logfilter and show
logfilter <filter-id> commands in the sensor CLI. The show logfilter-id command
shows the details of the last matching event during filtering and can be useful when evaluating
filter performance.
In addition, log filter statistics are sent to the Sensor Monitoring index (aella-ade-*) on the
DP using msgtype:41 and can be viewed in the Threat Hunting page with Indices set to Sensor
Monitoring. See below for the schema.
Expand to see the schema for log filter statistics

{
"msgtype": 41,
"msg_origin": {
"processor": {
"type": "log_forwarder", "winlog", "fim", "log_collector", or,
"aella_flow"
"name": # Optional. It is <connector_name> when type is "connector".
"id": # Optional. NG-SaaS, connector has id.
}
}
"engid": # For connector running on DP, it is <connector type>_<connector
name>
"engid_name": # For connector running on DP, it is <connector type>_<connector
name>
"tenantid":
"filter_id":
"filter_name":
"timestamp": # epoch ms
"exclude_hits_delta": # Optional. The number of exclude hits of the filter by
the processor since last report
"exclude_bytes_delta": # Optional. The size of excluded logs matched the
filter by the processor since last report
"include_hits_delta": # Optional. The number of include hits of the filter by
the processor since last report
"include_bytes_delta": # Optional. The size of included logs matched the
filter by the processor since last report
"last_log": # Optional. The string of the latest log which was matched the
filter
}
Event Storage (Retain Raw Events)
You can enable the Retain Raw Events option if you want the sensor to store both raw and
processed Windows event logs on the Stellar Cyber Platform (DP). This can be useful in
troubleshooting situations when you may want to compare a processed event log to its
corresponding raw log or when an investigation requires original event payloads.
You can search for raw Windows events by looking for the message field in the Windows Events
index in the Interflow Search tab.
 Keep in mind that when this feature is enabled, Windows Server Sensors store both raw
and processed events, requiring more storage resources on the DP proportional to event
volume.
About the Predefined Channels in the Windows Tab
The predefined channels allow you to collect events in the categories listed below:
Refer to Templates for Windows Server Sensors for details on the different Windows
Event IDs enabled in each of these categories for the available templates.
Refer to Alert Types That Use the Windows Index for information on the alert types
that use the events collected in these categories for alert generation.
Predefined Windows Channels:
Security – Collect specified Windows advanced security audit policy settings events.
System – Collect Windows system events.
Application – Collect Windows application events.
Forwarded Events – Collect Windows events forwarded from other Windows
machines.
DHCP Client – Collect Windows DHCP client events

Windows Firewall – Collect Windows advanced security firewall events.
Windows Defender – Collect specified Windows Defender events.
Sysmon – Collect specified Windows sysmon events for process anomaly detections.
PowerShell – Collect specified Windows PowerShell operational logs.
Other Channels – Collect additional specified Windows events that do not fit into the
other categories.
FIM (File Integrity Monitoring) – Perform FIM monitoring of specified files and
directories.
All of the channels are enabled by default, with the exception of FIM. Events for each channel
are stored in their own file. When a given file is full, older events are overwritten. If the sensor is
receiving events faster than it can send them to the DP, you can increase the log file size to store
more events or opt to exclude certain events.
Including or Excluding Specific Event IDs
Each of the preset channels in the Windows tab includes a Specify Event IDs option that lets
you either Exclude or Include specific Event IDs. (Note that the settings below these channels—
Collect logs no older than specified time (Hours), FIM Windows, and Filebeat—don't have
this option.) Use the following procedure:
1. Navigate to the channel from which you want to include or exclude specific Event IDs
and cascade its entry open.
2. Scroll to the bottom of the available options for the channel until you locate its Specify
Event IDs entry. For example, the illustration below shows the Specify Event IDs entry
for the System channel.
 Some of the channels have the Specify Event IDs option enabled automatically
with IDs supplied for you if you have selected one of the available templates for the
Windows tab options. Refer to Templates for Windows Server Sensors for a list
of the options and Event IDs included in each of the available profiles.
3. Toggle the Specify Event IDs option on and choose whether you want to Exclude or
Include specific IDs.
4. Supply the IDs you want to Exclude or Include by typing them into the Event IDs field,
as illustrated below.

 Note that the IDs you enter here are not validated. You can use the Event table in
the Threat Hunting display (enable the column for Event IDs) to identify noisy/low
value IDs, or refer to external resources, such as https://docs.microsoft.com/en-
us/windows/security/threat-protection/windows-defender-application-control/event-
id-explanations  .
5. Click Submit when you are finished with all settings for the Sensor Profile.
Configuring the Log Size for a Channel (Deprecated)
 This feature was deprecated in the 5.5.0 release but could still be used. Starting with the
6.0.0 release, this feature is disabled on the Windows Server Sensor itself. Because of this,
setting the Log Size Control option has no effect in sensor profiles applied to 6.0.0+
Windows Server Sensors.
To configure the log size for a channel:
1. Click on the name of the channel for which you want to customize log size.
2. Click on the Log Size Control toggle to enable it and to display size information.
3. Click Custom to enable a custom log size.
4. Enter the custom size.
5. Click Submit after you finish all configurations.
Adding Other Channels
To add other channels:
1. Click Other Channels.
The section expands.

You can either select from the available preset channels or type in your own.
2. To select from the preset channels, you choose one or more channels from the Types
drop-down list and choose Add.
The channel appears in the Added box.
The available preset channels are extensive and are best reviewed in the user
interface. In addition to many others, they include the following:
AD FS/Admin
Microsoft-Windows-AppLocker/EXE and DLL
Microsoft-Windows-AppLocker/MSI and Script
Microsoft-Windows-AppLocker/Packaged app-Deployment
Microsoft-Windows-AppLocker/Packaged app-Execution
Microsoft-Windows-GroupPolicy/Operational
Microsoft-Windows-Kernel-Boot/Operational
Microsoft-Windows-NetworkProvider/Operational
Microsoft-Windows-PowerShell/Admin
Microsoft-Windows-TCPIP/Operational
OpenSSH/Admin
OpenSSH/Operational
Windows Networking VPN Plugin Platform/Operational
3. You can also type in your own Windows event channel.
The user interface checks to make sure the channel exists and reports an error
message if it does not.
4. Select Submit after you finish all settings for the profile.
Limiting the Age of Collected Logs
To limit the age of the logs collected when you first enable:
1. Select Collect logs no older than specified time (Hours).

The section expands.
2. Enter the number of hours.
3. Select Submit after you finish all settings for the profile.
Disabling All Windows Event Log Channels
If you disable all Windows event log channels in the sensor profile, the sensor's Winlogbeat
service (aella_winlog) is automatically disabled, preventing unnecessary service execution. File
Integrity Monitoring is unaffected and can still be run without enabling Winlogbeat.
The Winlogbeat service starts automatically once you configure at least one Windows event
channel or a dependent feature requiring Windows logs is enabled. Note that disabling
Winlogbeat stops Windows event-based detections, including Object Access events.
Configuring File Integrity Monitoring (FIM Windows)
See the top of this page for recommended lessons about this section at Stellar
Cyber Academy.
Enabling the FIM Windows feature in a Sensor Profile lets you keep track of file and folder
creations, modifications, and deletions.
When you enable the FIM Windows feature, a new table appears in the Sensor Profile dialog
box that lets you specify both the files and folders you want to monitor for changes, as well as
the types of changes for which you want to monitor.
As you can see in the image below, the table is preconfigured with a set of files and folders
recommended for monitoring by industry-standard best practices.
Select + Add Row to add new files and folders to the FIM feature. For each entry in the table,
you can configure the following:
Enabled – Enable monitoring of the indicated files and folders. This lets you toggle
monitoring for a given file or folder on or off without needing to delete it from the profile
entirely.
Path – Specify the full path to the folder that contains files and subfolders you want to
monitor.
 A given path can only have one entry in the table. In addition, keep in mind that
Windows paths are case-insensitive. Because of this, Stellar Cyber prevents you
from adding, for example, both C:\Program Files and C:\program files. Because
paths are not case-sensitive, Stellar Cyber treats these two paths as the same.

Inclusions – List the files and subfolders within the specified folder to monitor. You can
use an asterisk (*) for standard wildcarding. For example, *.bat, *.cfg, and so on. If you
leave this field blank, it is implicitly set to *, meaning that all files and subfolders in the
specified folder are included for monitoring.
Exclusions – List the files and subfolders within the specified folder to exclude from
monitoring. You might want to use this feature to exclude certain file types that are
trusted and change often. Standard wildcarding is supported here, too. By default, this
field is empty and no files are excluded from monitoring.
Depth – Enter the number of subfolders below the specified folder to monitor.
 A depth of 0 means that you are monitoring only items in the specified folder and
nothing below it.
Change/Create/Delete – Select the types of activities to track in the specified folder.
 In general, it's a good idea to optimize performance by focusing your FIM settings on specific
files rather than large folders with many files and subfolders (C:\, for example). Refer to Best
Practices for File Integrity Monitoring (FIM) for performance guidelines and a set of
system files recommended for integrity monitoring by Microsoft.
The FIM feature works by recording a file hash for each file selected for monitoring in the Sensor
Profile. Once the initial hash is recorded, the FIM feature regularly monitors for changes to the
file hash and sends events to the if changes are seen. For subfolders, FIM monitors changes in
folder metadata to detect folder creation, deletion, and renaming.
You can keep track of events generated by the FIM Windows feature in the following ways:
Use the predefined Dashboards | PREDEFINED | File Integrity Monitoring dashboard.
Use the Threat Hunting feature to search the Windows Events index for events with
msg_origin.source set to windows_agent and msg_origin.processor.type set to
FIM. Once you find such an event, you can add it to the Threat Hunting Documents
table by using the Toggle add column to table button adjacent to its entry and sort to
see all such events.
Similarly, you can create ATH rules with queries based on the
msg_origin.processor.type field set to FIM.
The JSON for a FIM event indicates the type of change that took place. If the event indicates
either a change or a deletion, the JSON includes both old and current values. If the event
indicates a file creation, only the current section appears in the JSON. For example, the
JSON below shows a file creation event.

 Note that when the FIM Windows feature is enabled on a Windows Server Sensor, a new
windows agent sensor fim process is spawned on the host machine and can be viewed
with other running processes.
Windows Server Sensor Installation Folders Excluded from FIM
Note that the following installation folders for the Windows Server Sensor are automatically
excluded from FIM monitoring. The user interface does not prevent you from adding these
folders; however, they are still automatically excluded from FIM monitoring:
C:\ProgramData\StellarCyber\Windows Agent Sensor\config
C:\ProgramData\StellarCyber\Windows Agent Sensor\log
C:\ProgramData\StellarCyber\Windows Agent Sensor\run
 Keep in mind that the FIM Windows feature can only monitor files and folders that exist
when the windows agent sensor fim service restarts. If you add a non-existent file or
folder for monitoring in the Sensor Profile and then create the folder later, it won't be
monitored until windows agent sensor fim restarts.
FIM Inclusion and Exclusion Example for a Windows Server Sensor Profiles
This example shows how to configure FIM to monitor the contents in a specified folder,
exclude two subfolders, and monitor the contents of non-excluded subfolders.
1. Select System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles and
then either select Create | Add Standard Sensor Profile to create a new profile or
select the Edit icon to edit an existing profile for a Windows Server Sensor.
2. If you're creating a new profile, enter a profile name, choose a tenant, choose
default_receiver, and then select Windows.
3. Enable FIM Windows and then select Add Row.
4. In the newly added row, double-click or tap in the Path field and either type or paste
the full path to the folder that you want to monitor, such as c:\program
files\Microsoft SQL Server\MSSQL14.SERVER.
5. In the Inclusions field, leave the default setting ( * )to monitor all files and subfolders
in the MSSQL14.SERVER folder.
6. Double-click or tap in the Exclusions field and enter Log, DATA to exclude these two
subfolders from monitoring.
 The Exclusion setting takes precedence over Inclusion.
7. Set Depth at 1 to monitor all files in the MSSQL14.SERVER folder and all files and
subfolders in non-excluded first-level subfolders immediately below
MSSQL14.SERVER.
8. Leave Change, Create, and Delete enabled to monitor for all these activities, leave
the configuration as Enabled, and then Submit.

The monitoring behavior that these settings define is shown in the illustration below.
Configuring Filebeat Settings
You can configure a Windows Server Sensor to act as a syslog forwarder, using its built-in
Filebeat service to receive syslog records from a specified source and forward them to a Modular
Sensor for parsing, filtering, and eventual shipment to the DP.
This feature lets you collect and ingest syslog records in situations where it might not make
sense to deploy a dedicated Modular Sensor for syslog ingestion. The Filebeat feature is also
supported on both Windows desktop and server versions, allowing you to forward logs from sites
without server infrastructure.
 Using the Server Sensor as a lightweight log forwarder in a site without server infrastructure
is the only scenario where the Windows Server Sensor is supported on a Windows
desktop host. Deployments such as these support both Windows 10 and 11 desktop
versions. Keep in mind, however, that when using this feature on a Server Sensor installed
on a Windows desktop, you must enable only the Filebeat option in the Windows tab of the
Standard Sensor Profile applied to the sensor.
Use the following procedure to configure a Windows Server Sensor as a log forwarder for syslog
records:
1. Enable the Filebeat option.
Once you enable Filebeat, new options appear that let you configure both Input and
Outputsettings for the syslog forwarding feature.
2. The Input Settings (Log Receiver) options let you specify where the Windows Server
Sensor listens for incoming syslog records. Set the following options:
Receiver Address – Specify the IP address where the Windows Server
Sensor receives incoming logs.
By default, this option is set to 0.0.0.0, which means that the Windows Server
Sensor listens on all interfaces on the host Windows system. If your sensor is

installed on a Windows host with multiple interfaces and you only want to listen
on one of them, you can specify which one using this field.
Protocol – The transport protocol used for the syslog records. The default is
UDP but you can also use TCP if your log source uses that protocol.
Receiver Port – The port on which to receive syslog records. The default is
the standard syslog port of 514.
 You must open this port in any firewalls or access control lists between the
Windows Server Sensor and the sending log source.
Format – You can select format of the syslog records (RFC 3164 or
RFC 5424), or you can leave this option at its default value of Auto so that the
Sensor identifies the format automatically.
 You can check the Use Default Settings options if you want to return to
the Stellar Cyber defaults for the Input Settings.
3. The Output Settings (Log Forwarder) options let you specify where the Windows
Server Sensor forwards received syslog records. Set the following options:
Syslog TLS – Enable this option if you want to forward the logs with
TLS encryption. Use the following procedure:
a. Enable the Syslog TLS Enabled option in the Edit Sensor
Parameters dialog box for the Modular Sensor to which you want to
forward logs. Display this dialog box by selecting Edit for the Modular
Sensor in the System | DATA SOURCE MANAGEMENT | Sensors |
Sensors list.
b. Enable the Syslog TLS option here in the Filebeat options in the
Windows tab in the Standard Sensor profile.
 With these options configured, both the sending Windows Server Sensor
and the receiving Modular Sensor download a self-signed certificated from
the DP and use it for secure communications.
Forwarder Address – Specify the IP address of the Modular Sensor to which
you want to forward the logs received by the Windows Server Sensor.
Forwarder Port – Specify the port on the receiving Modular Sensor to which
the Windows Server Sensor should send the forwarded logs. You can leave
this field blank if you would like the Windows Server Sensor to send the logs
on the same port that the log source used.

4. Make sure the Receiver Port you specified for the Filebeat feature is open in the
Windows Defender Firewall for the Windows Server Sensor host system (or in any other
intervening firewalls or access control lists, depending on your implementation).
5. Configure your syslog source to send logs to the IP address and port specified in the
Input Settings for the Filebeat feature.
Notes on Using the Windows Server Sensor as a Log Forwarder
Keep in mind the following important points when using a Windows Server Sensor to forward
syslog records:
The Windows Server Sensor performs minimal parsing on received records, only
identifying the record format. Because of this, it cannot filter the syslog records it
receives and simply forwards them all to the Modular Sensor. You must consider
whether the convenience and cost savings of using a Windows Server Sensor instead
of a Modular Sensor for log forwarding outweighs the potential network costs of sending
all syslog records. The table below summarizes the pros and cons of each approach:
Sensor
Summary Con
Type
Windows Inexpensive per-instance. Can be installed in Cannot filter incoming records. All records
Server Windows workstation versions; no server forwarded to destination, potentially resulting in
Sensor infrastructure required. higher network costs.
Modular Can filter received records and only ship what's More expensive than Windows Server Sensor.
Sensor necessary to the Stellar Cyber Platform. Requires dedicated VM or physical sensor.
You must open the Receiver Port specified in the Filebeat Input Settings between the
Windows Server Sensor and the log source in order for records to reach the sensor.
When using the Filebeat feature on a Server Sensor installed on a Windows desktop,
enable only the Filebeat option in the Windows tab in the Standard Sensor Profile. All
other options must be disabled, as illustrated below:
Use following procedure to use a Windows Server Sensor as a log forwarder for syslog
records:
You can use the show logforwarder command from the Sensor CLI to keep tabs on
the configuration and performance of the feature.
Filebeat and dhcp_log are mutually exclusive.
The dhcp_log option is mutually exclusive with the Filebeat feature that lets Windows
Server Sensors act as a forwarder for syslog records. You can use one or the other, but
not both.

If you enable dhcp_log on a Server Sensor with the Filebeat option enabled, Filebeat
is silently disabled and the dhcp_log setting is used.
 Keep in mind that DHCP logs have been included with standard Windows Event
Logs since the Windows Server 2012 release.
Memory Usage and Windows Server Sensor Profiles
When applying a sensor profile to a Windows Server Sensor, the system compares the amount
of memory required by the profile to the amount of memory available on the target system and
reports success or failure in the Sensors list as follows:
Systems with ≥ 100 GB Total Memory: A Windows Server Sensor profile is applied
successfully if the amount of free memory on the target system minus the memory
required by the profile is ≥ 25 GB. If less, the failure is reported in the Sensors list.
Systems with < 100 GB Total Memory: A Windows Server Sensor profile is applied
successfully if the amount of free memory on the target system minus the memory
required by the profile is ≥ 25% of the total memory. If less, the failure is reported in the
Sensors list.
If you receive a memory warning in the Sensors list, you can either reduce the memory
footprint of the sensor profile (for example, by reducing the size of the Log Size Control
options) or provision additional memory for the Windows Server Sensor host.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  