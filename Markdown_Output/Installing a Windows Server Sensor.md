Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Installing a Windows Server Sensor

 Learn more at Stellar Cyber Academy.

The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.

M05 Open XDR Windows Server Sensor Installation and Configuration (02h:45m)  

Introduction (07m:00s)

Start with an overview of installing and configuring the Stellar Cyber Windows Server
Sensor. Explore how this sensor integrates with the Stellar Cyber Platform, covering
data collection, configuration, and advanced monitoring options like Sysmon and file
integrity.

Overview (15m:00s)

Learn about the role of the Windows Server sensor within the Stellar Cyber Platform,
including compatibility requirements and network configurations. Understand the
process for sending server event data—like security events and system logs—
through the data processor for analysis.

Software Installation (18m:00s)

Follow a step-by-step walkthrough of installing the Windows Server sensor software,
from downloading the package through the knowledge base to completing essential
configurations. Learn how to assign tenant IDs, bind the sensor to the Stellar Cyber
Platform, and verify connectivity to network and data processor endpoints.

Authorization (15m:00s)

Learn how to authorize the Windows Server sensor within the data processor, then
watch a live demonstration of the complete process in the data processor UI. Follow
the steps to set up a custom sensor profile, link and bind the sensor, and verify
authorization status to confirm connectivity and ensure data transfer readiness to the
Stellar Cyber Platform.

Validate Installation and Authorization (14m:00s)

Confirm the installation and authorization of the Windows sensor by checking for
active connections in both the Windows Agent CLI and the Stellar Cyber Platform UI.
Follow a hands-on demonstration to validate sensor functionality, verify sensor status
in the data processor, and monitor incoming Windows event data flowing to the data
lake.

Advanced Configuration - Audit Policy (14m:00s)

Discover how to expand the range of Windows events captured by adjusting audit
policies, then follow a hands-on demonstration of configuring those policies to
increase event visibility in the Stellar Cyber Platform. Learn to enable additional
security event types sent to the data lake, supporting more comprehensive threat
analysis and monitoring across your environment.

Advanced Configuration - Sensor Profile (18m:00s)

Customize sensor profiles using predefined templates that align with specific security
requirements, enabling granular control over data collection and processing. Watch a
demo on selecting and applying templates, fine-tuning event settings, and monitoring
enhanced data flow to the data processor within the Stellar Cyber Platform.

Advanced Configuration - Sysmon (28m:00s)

Learn how to install and configure Sysmon on Windows Server to enhance security
visibility through detailed event monitoring. Explore how Sysmon logs capture
process creation, network connections, and file changes, then follow a step-by-step
demonstration covering the configuration steps required to ensure Windows Server
events are captured and forwarded as Interflow records to the data processor for
ingestion into the data lake.

Advanced Configuration - File Integrity Monitoring (FIM) (18m:00s)

Enable File Integrity Monitoring (FIM) on the Stellar Cyber Platform to track and
detect unauthorized modifications to critical files on Windows Servers. Learn to
configure FIM settings for accurate file change tracking, then follow a hands-on demo
to validate the setup and confirm that file change events are captured and forwarded
correctly within the data lake for further analysis.

Advanced Configuration - Windows Channel Logging (28m:00s)

Configure Windows Channel Logging in the Stellar Cyber Platform to capture events
from various Windows Server functions and roles. Follow a demo walkthrough to set
up logging channels that target specific event types, improving data collection and
enhancing event visibility across your environment.

Troubleshooting (23m:00s)

Address common issues in sensor installation and configuration by exploring
troubleshooting techniques for connectivity problems, configuration errors, and other
sensor-related challenges within the Stellar Cyber Platform. Follow along with a step-
by-step demo that walks through diagnosing and resolving errors encountered during
installation and configuration workflows.

The first time you access a link on the portal during a session, you must log in to access
content.

This topic describes how to install a Windows Server Sensor in a supported target environment
using the installation file downloaded from the Download Images tab in the System | DATA
SOURCE MANAGEMENT | Sensors | Sensor Installation page. Refer to the following sections
for details:

About the Windows Server Sensor

Supported Windows Server Versions

Open Firewall Ports

Obtaining the Windows Server Sensor Installer

Obtaining a Token for the Installation

Installing the Windows Server Sensor

Configuring the Server Sensor in the CLI

Using a Proxy with the Windows Server Sensor

Uninstalling the Server Sensor

About the Windows Server Sensor
The Windows Server Sensor (agent) runs as a Windows service in a compatible Windows Server
system. The Server Sensor observes events within the Windows Server system and sends
Interflow data records to the data processor.

The captured events are:

Hardware
Security
System
Windows Firewall
Windows Defender
PowerShell

The Windows Server Sensor provides the following key capabilities:

If the sensor has coverage over the domain controller, Stellar Cyber enriches data with
the relationship between users and IP addresses.

If the sensor has coverage over the DHCP server, Stellar Cyber sees the relationship
between hostnames and IP addresses, and so can track assets when the IP address
changes.

Windows Server Sensor provides the data foundation for Stellar Cyber's machine
learning alerts that use the Windows Events index.

Although you can also provide coverage of Windows logs using other visibility tools
such as the ManageEngine Log Collector or Winlogbeat, the logs provided by these
tools are not normalized, enriched, and stored in the Windows Events index used for

machine learning alert generation (except for ManageEngine ADAudit Plus logs) and
cannot be used for machine learning alert generation.

In addition, the Windows Server Sensor provides the following advantages over
alternative solutions:

Windows Server Sensor provides easier deployment and maintenance.

Windows Server Sensor provides granular filtering at the edge through the
Stellar Cyber user interface.

By using the Windows Server Sensor, you do not need to deploy another
modular sensor to forward logs from ManageEngine or Winlogbeat.

Windows Server Sensor Processes

The Windows Server Sensor launches the following processes:

Name in Task

Name in Services

Manager

App

Description

aella_conf_win_sr

Windows Agent

Handles Windows Server Sensor configuration

v.exe

Sensor Conf

aella_ctrl_win_srv.

Windows Agent

Monitors other services, and can stop or start them based on the configuration

exe

Sensor Ctrl

aella_winlog.exe Windows Agent

Sends Windows events to DP

Sensor Logbeat

aella_filebeat.exe Windows Agent

Sends log files from Windows DHCP server (if installed and running) to DP or acts as

Sensor Filebeat

syslog forwarder if Filebeat is enabled in the Sensor Profile

aella_fim.exe

Windows Agent

Provides file integrity monitoring services, as configured in the Sensor Profile

Sensor FIM

aella_diagnostics_

Windows Agent

Sends Windows Server Sensor logs to DP

win_srv.exe

Sensor Phonehome

Windows Server Sensor Indices

Data collected by the Windows Server Sensor can feed the following Stellar Cyberindices:

Traffic (aella-adr-*)

Windows Event Log (aella-wineventlog-*)

Sensor Monitoring (aella-ade-*)

Supported Windows Server Versions
The Windows Server Sensor is supported in the following environments:

Windows Server 2008 R2, 2012, 2012 R2, 2016, 2019, 2022 21H2 (Server Desktop
Experience), and 2025.

The same .msi installation file is used for all Windows Server Sensor installations. The Server
Sensor is only available in 64-bit.

 When the system sleeps, the connection drops, and no data is collected. The connection is
re-established when the system wakes. To avoid this, configure Windows to Never sleep.

The host Windows Server into which the Windows Server Sensor is installed must meet the
following minimum requirements, regardless of whether it is a physical or virtual server:

Component

Host CPU

Host RAM

Available SSD Disk Space

Specification

Xeon Core 2 virtual cores (2.0 GHz or more)

8 GB

Minimum – 5 GB

Recommended – 8 GB

Update Windows Server Software Before Installing Windows Server Sensor

Stellar Cyber recommends that you use Windows Update to make sure your Windows Server
software is up to date before installing the Windows Server Sensor.

Clean Up Existing 4.3.x Installations in Windows Server 2008 R2 or 2012 R2
Before Installing 6.6.0

Stellar Cyber recommends that you fully uninstall any 4.3.x Windows Server Sensors from
Windows Server 2008 R2 or 2012 R2 environments before installing the 6.6.0 software. Note the
following:

Use the uninstall procedure provided in Uninstalling the Server Sensor.

Make sure you check the following boxes during the uninstall:

Remove Data Files

Remove Scheduler Task

Remove Stellar Syswatcher

When the uninstallation completes, manually delete the C:\ProgramData\StellarCyber
folder.

PowerShell Not Required

PowerShell is not required for Windows Server Sensor installations.

Exclude Server Sensor from AV/EDR Scanning

Stellar Cyber recommends that you prevent potential conflicts by configuring any anti-virus or
EDR software installed on the same host as the Server Sensor to exclude the Server Sensor
installation directories from scanning. The directories to exclude for a Windows Server Sensor
are as follows:

Server Sensor Type

Folders/Files to Exclude from AV/EDR Scanning

Windows

C:\ProgramData\Stellarcyber

Server Sensor Type

Folders/Files to Exclude from AV/EDR Scanning

C:\Program Files\Aella

C:\Windows\Stellar_syswatcher.exe (sensors running pre-4.2.2 versions)

Possible False Positives from FireEye PROCGUARD

During installation of the Windows Server Sensor, it is possible that FireEye PROCGUARD may
report the following alert – Attempted LSASS access by aella_conf_win_srv.exe
detected. After investigation, Stellar Cyber has determined that this is a false positive and that
the aella_conf_win_srv.exe service does not interact with
C:\\Windows\\system32\\lsass.exe on the host machine.

Open Firewall Ports
The sensor requires open firewall ports in order to communicate.

Obtaining the Windows Server Sensor Installer
You download the installation file for the Windows Server Sensor from the System | DATA
SOURCE MANAGEMENT | Sensors | Sensor Installation page. Use the following
procedure:

 Only users with the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Sensor Image Download privilege assigned to their profile in the System |
 ORGANIZATION MANAGEMENT | Role-Based Access Privileges interface can download
images.

1. Navigate to System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation.

2. Set the Sensor Type dropdown to Windows Server Sensor.

The display updates to show you the size of the files to be downloaded.

3. Click Download.

The system downloads the .msi installation file to the system's Downloads folder.

The next step is to use the Tokens tab to obtain the token you will use to install the downloaded
sensor, as described below.

Obtaining a Token for the Installation
Tokens are required to authorize and configure the installation of a sensor image downloaded
from the DP in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation page. Tokens point the installed sensor to the correct DP, assign the selected
tenant and sensor profile, and authorize the sensor installation.

Use the following procedure to obtain a token in the Tokens tab:

1. Navigate to System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation and click on the Tokens tab.

2. If a token already exists for the target tenant for the sensor installation, Copy it to the

clipboard or Download it as a file.

Copy the token if you plan on pasting it into an msiexec command or the
installation wizard's dialog box.

Download the token as a file if you plan on referring to it in the msiexec
command, hosting it at a URL, or pointing to it in the installation wizard's dialog
box.

 Refer to Assigning Tokens for a summary of the different ways in which tokens

can be applied to a sensor installation.

3. If there is not already an unexpired token for the target tenant that you want to use, click

the Generate button.

The Generate Installation Token dialog appears:

4. Select the Sensor Profile to be assigned to all sensors authorized with this token from
the Sensor Profile dropdown. The dropdown lists all sensor profiles available in the
System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles page for the
selected Tenant.

 If you do not want to assign a Sensor Profile with a token, you can set this field to

None (no sensor profile selected). This is also the setting for any tokens migrated
from a pre-5.3.0 release as part of an upgrade.

5. Use the Expiration dropdown to select an expiration date for this token. You can select

specified expiration dates ranging from two weeks to three months.

 You can also select Never expires for the expiration date. However, Stellar Cyber
recommends that you specify expiration dates for your tokens in order to improve
the security of your deployment.

 Remember that when a token expires, sensors authorized with the token

continue to operate as normal. Once a sensor successfully registers with the
Stellar Cyber platform, it no longer uses the token. It is only used for the initial
authorization, registration, and configuration of the sensor.

6. Click the Generate button.

The system generates the token and displays its contents in the Token field. The dialog
also updates to display the expiration date for the token, as illustrated below.

7. You can use the Copy button to copy the token to the clipboard immediately, or simply

close the dialog and retrieve the token from the Tokens tab later on.

8. You can use the Copy button to copy the token to the clipboard immediately, or simply

close the dialog and retrieve the token from the Tokens tab later on.

Installing the Windows Server Sensor
You can install the Windows Server Sensor using any of the following techniques. Each
technique requires the use of the token you obtained in the previous section to authorize and
configure the installation.

Single Installation

This is the simplest scenario, where you are installing a single Windows Server Sensor

Using Wizard

interactively on a target machine using the GUI-based installation wizard.

Refer to Installing the Windows Server Sensor Using the Wizard.

Single Installation from

You can also install a single Windows Server Sensor using an msiexec command and the .msi

Command Line

installer downloaded from the Download Images tab in the System | DATA SOURCE

MANAGEMENT | Sensors | Sensor Installation page. The proper syntax for the msiexec

command, including a selected token, is provided in the MSI File Installation section of the

Batch Deployment tab in the Sensor Installation page.

Refer to MSI File Installation.

Bulk Installation Using

You can create your own scripts for bulk installations using the msiexec command provided in the

a Script

MSI File Installation section of the Batch Deployment tab in the Sensor Installation page. As

described in About Tokens, the same token can be reused to authorize multiple sensor

installations for the same tenant.

Refer to MSI File Installation.

Bulk Installation Using

You can also use Microsoft Group Policy Object (GPO) to deploy the Window Server Sensor to

GPO

multiple systems at once. You do this by using the GPO Bulk Installations tool in the

Batch Deployment tab in the Sensor Installation page. This tool helps you download a zip file

containing a batch file preconfigured with a selected token. You can use the contents of the zip file

to generate an MST file that can be used with GPO to deploy the Window Server Sensor to

multiple systems at once.

Refer to GPO Bulk Installations

Installing the Windows Server Sensor Using the Wizard

Use the following procedure to install the Windows Server Sensor interactively using the wizard:

 During the installation, a Windows command prompt window may appear. Do not close this
window manually – the installation wizard closes it automatically when the installation is
complete.

 To avoid installation issues, complete any pending updates for the host Windows machine

before upgrading the Server Sensor.

1. Open the folder where you downloaded the .msi installation file from the Download

Image tab in System | DATA SOURCE MANAGEMENT | Sensors | Sensor
Installation.

2. Right-click the .msi file and select Properties from the context menu that appears.

3. Select Unblock in the Security section.

Some Windows systems automatically block downloaded files.

4. Select OK.

5. Double-click the .msi file to open it and start the installation. Accept any system

warnings presented by User Account Control

6. Click Next on the Welcome screen.

7. Choose the path for the installation when prompted by the wizard and click Next.

8. Select the Token option and supply the token to be used for the installation. You can

use either of the following techniques:

Paste the token you copied from the Token tab in the System | DATA
SOURCE MANAGEMENT | Sensors | Sensor Installation page into
the Token field.

Select Token File and navigate to the location of the token file you
downloaded from the Token tab in the System | DATA SOURCE
MANAGEMENT | Sensors | Sensor Installation page.

The figure below shows a token pasted into the Token field:

 Do not use the CM options. These options are only used with Stellar Cyber

platforms that do not have an "s" in their version number. If your Stellar Cyber
platform includes the Sensor Installation page and the Tokens tab, use the Token
option with the token file you already obtained.

9. (Optional) Configure a Primary and Secondary aggregator:

Primary Aggregator – If you are configuring this Server Sensor to forward
data to an aggregator before it is sent to the DP, you can enter the primary
aggregator's IP address here.

Secondary Aggregator – If you are configuring this Server Sensor to forward
data to an aggregator, you can enter the secondary aggregator's IP address
here.

 The wizard does not prevent you from specifying a Secondary Aggregator
if the Primary Aggregator is left empty. However, a Secondary Aggregator
specified without a Primary Aggregator is ignored and not applied to the
installation.

10. Select Install to begin the installation.

The installer installs the Server Sensor to C:\Program Files\Aella\, displaying a
confirmation dialog box when complete.

 The Windows Server Sensor is always installed to C:\Program Files\Aella\.

Custom paths are not supported.

11. Select Finish.

The Server Sensor is installed as a service.

You can verify the installation using any of the following techniques:

Check the System | DATA SOURCE MANAGEMENT | Sensors | Sensors list in the
user interface to see that the sensor has registered itself successfully.

Open the Services app and look for the Windows Agent Sensor Ctrl entry.

Access the Server Sensor's CLI and run the show version command. Verify that the
CM Controller field lists the DP from which you downloaded the token for the sensor.

Windows Control Panel Shows Extra Digit in Sensor Version Number

The Windows Control Panel includes an extra leading digit in the Server Sensor version number
so that, for example, a Version 6.3.0 sensor is shown with a version number of 6.6.3.0. The extra
digit is added by the sensor's installation package and can be ignored.

Assigning a Token to the Server Sensor from the CLI

As described in Assigning Tokens, you can apply a token to an installed sensor from the sensor
CLI with the set token command. This can be useful if you need to change a token from the
CLI after the Server Sensor has already been installed. Refer to the table below for a summary
of the available techniques:

 You only need to use one of the options in the table below. These are just different ways to

do the same thing – apply the token.

Option 1. Copy and Paste the

Copy the token string from the Tokens tab and paste it into the CLI command. The syntax

Token String

is as follows:

set token string <pasted string>

Option 2. Upload the Token as

a File to the Sensor

Download the token as a file from the Tokens tab, upload it to the sensor, and reference it

in the set token command. The syntax is as follows:

set token file <path to local file>

For example, the following command points to the token.text file stored in the /tmp

folder:

set token file /tmp/token.text

 This technique only works for Server Sensors. There isn't a way to upload the

token.text file to a newly installed modular sensor virtual machine.

Option 3. Host the Token on

an HTTP Server

Download the token as a file from the Tokens tab, upload it to an HTTP server, and

reference it in the set token command. The syntax is as follows:

set token url http://<url to token>

You can also use an HTTPS server. In that case, the specified URL must also include the

username and password for the server.

Configuring the Server Sensor in the CLI
Applying a token to the Server Sensor automatically configures it with the correct IP address of
its managing DP and its tenant assignment. It also authorizes the Server Sensor. These are all
settings that required manual configuration in previous versions and are no longer required.

However, it is still useful to access the sensor's CLI to verify its operation and change any
necessary settings. To run the Server Sensor's CLI, find the Windows Agent Sensor Command
Line Interface entry in the Windows Start Menu. If it does not appear at first, use the Find
function.

After starting the Windows Server Sensor CLI, a terminal window appears as below. This window
lets you enter CLI commands to the Server Sensor. Enter the show version command to verify
the sensor's operations. In response, the sensor displays output similar to the following:

Using a Proxy with the Windows Server Sensor

If your Windows Server Sensor does not have direct access to the Internet, you can configure it
to use an HTTP proxy for connection to the DP.

 Your HTTP proxy must allow SSL on TCP ports 443 and 8889. The set proxy <proxy> test

command described in the procedure below verifies that the necessary ports are open.

You configure the Windows Server Sensor to use an HTTP proxy in the CLI. The procedure is as
follows:

 The CLI prevents you from entering non-printable characters as part of the username or

password for the proxy, as well as the proxy itself.

1. Access the Server Sensor's CLI.

2. First, we'll use the set proxy <proxy> test command to verify that our proxy is

reachable and that SSL is accepted on both TCP 443 and 8889.

Enter the <proxy> in the following format:

http://[username:password@]<proxy_ip>[:<proxy_port>]

 Stellar Cyber recommends that you always test a proxy successfully before setting

it.

The following example shows an unsuccessful test for a proxy server on 10.1.2.3:8081,
followed by a successful test for the same IP address on port 8080:

WindowsAgentSensor> set proxy http://user:pass@10.1.2.3:8081 test
Test HTTP/HTTPS proxy: http://user:pass@10.1.2.3:8081
Failed testing dev-demo.stellarcyber.cloud:443, err: timed out

WindowsAgentSensor> set proxy http://10.1.2.3:8080 test
Test HTTP/HTTPS proxy: http://10.1.2.3:8080
Passed testing dev-demo.stellarcyber.cloud:443
Passed testing receiver-dev-demo.stellarcyber.cloud:8889

3. Once you've verified that your proxy is working correctly, you can set it with the same

command but leaving out the test parameter. For example:

WindowsAgentSensor> set proxy http://10.1.2.3:8080
Succeed setting proxy

Other Proxy Commands

The following additional commands are useful when working with proxies:

Removing a Proxy – unset proxy

Showing Configured Proxies – show proxy

Review set proxy Syntax – set proxy ?

Troubleshooting a Proxy

This section lists some error messages you may see when configuring a proxy along with
troubleshooting tips for each.

 Your first line of defense when troubleshooting a proxy is the show proxy command. You
can use this to verify the current proxy configuration and ensure that things are set up the

way you intended them to be.

Failed testing xxx.stellarcyber.cloud:443, err: timed out

This error message can appear when the sensor can not reach the proxy server. Check
your proxy configuration with show proxy.

Failed testing xxx.stellarcyber.cloud:443, err: [Errno 10061] No
connection could be made because the target machine actively refused
it

This error message indicates that the sensor could reach the proxy server but the proxy
server did not accept the connection. Check whether the proxy service is up and
running on the specified port and if there are any firewalls along the way that might be
rejecting the connection.

Failed testing receiver-xxx.stellarcyber.cloud:8889, code 403

This error message is most likely triggered because of the proxy server's configuration.
For example:

The proxy server may not allow port 8889 for SSL connections.

The proxy server may not allow clients to connect to the receiver-
xxx.stellarcyber.cloud host.

Failed testing receiver-xxx.stellarcyber.cloud:8889, code 503

This error message usually indicates that the proxy server could not get a response
from receiver-xxx.stellarcyber.cloud:8889 (that is, the destination DP).

Sending DHCP Server Logs to a Modular Sensor

If the sensor has coverage over the DHCP server, you can send the DHCP server logs to a
modular sensor with the log forwarder feature enabled so that they can be used to enrich assets
with DHCP data. Configure this feature in the CLI as follows:

1. Use the following command to forward DHCP logs to a specified modular sensor:

set dhcp_log enable ip <sensor ip address>

For the <sensor ip address>, supply the IP address of a modular sensor with the log
forwarder feature enabled in its sensor profile.

 To use this feature, you must open port 5044 for DHCP beats in any firewalls

between the Server Sensor and the receiving modular sensor.

2. Verify the data entry with the show version command.
3. Enter the quit command to close the CLI.

Filebeat and dhcp_log Are Mutually Exclusive

The dhcp_log option is mutually exclusive with the Filebeat feature that lets Windows Server
Sensors act as a forwarder for syslog records. – you can use one or the other, but not both.

If you apply a Sensor Profile with Filebeat enabled to a Windows Server Sensor with the
dhcp_log feature enabled, the Filebeat settings do not take affect. You must disable dhcp_log

before you use the Filebeat feature.

 Keep in mind that DHCP logs have been included with standard Windows Event Logs since

the Windows Server 2012 release.

Uninstalling the Server Sensor
You can remove the Windows Server Sensor using the standard uninstall workflow from the
Windows Programs and Features control panel.

During the uninstall, you can choose whether to preserve or remove the following:

Remove Data Files

Remove Scheduler Task

Remove Stellar Syswatcher

If you are planning on reinstalling the Server Sensor, Stellar Cyber recommends that you leave
these items unchecked.

To uninstall completely, check each of these options to ensure that the program and all of its data
are removed completely.

 During the uninstallation, a Windows command prompt window may appear. Do not close

this window manually – it closes automatically when the uninstallation is complete.

About Sysmon in this Release
The Windows Server Sensor installation does not download and install the stellar_syswatcher
(Microsoft Sysmon64) service due to potential system crashes in certain operating systems
(Windows 2008R2 and 2012, although possibly others).

You can install the latest version of Sysmon (v13.31 at this writing) manually if you want the
Windows Server Sensor to report Sysmon events to the DP. However, Stellar Cyber strongly
recommends that you test your installation in a non-production environment to verify operations
before moving to production.

Use the following procedure to download Sysmon from Microsoft, install it manually, and verify
operations:

1. Install the Windows Server Sensor using the instructions earlier in this topic.

2. Download the latest version (v13.31) of Sysmon from Microsoft  and extract it to the

system where you want to install it.

3. Install Sysmon64 with the stellar_syswatcher.xml configuration file.

4. Restart the winlogbeat service.

 If you install sysmon after the Windows Server Sensor, you must restart the

winlogbeat service so that it works with Sysmon. If you install Sysmon before the
Windows Server Sensor, Sysmon works with winlogbeat without a restart.

5. Verify that Sysmon64 is installed correctly.

6. Verify that Sysmon events are received properly in the DP's aella-adr index.

Install Sysmon64 with stellar_syswatcher

After downloading and unzipping the installer for Sysmon64 to the target system, you can install
it as follows:

1. Open a command prompt as an administrator (right-click the cmd.exe file in Windows

Explorer and choose Run as administrator).

2. Change directories to the directory where you unzipped the Sysmon64.exe installer.

3. Install Sysmon64.exe with the stellar_syswatcher.xml configuration file using the

following command:

Sysmon64.exe -accepteula -i "c:\ProgramData\StellarCyber\Windows Agent

Sensor\config\stellar_syswatcher.xml"

In response, the system installs and starts the Sysmon64 utility:

Restart the winlogbeat Service if the Windows Server Sensor is Already
Installed

If you install Sysmon after the Windows Server Sensor, you must restart the
winlogbeat service so that it works with Sysmon.

If you install Sysmon before the Windows Server Sensor, Sysmon works with
winlogbeat without a restart.

Verify Sysmon64 Installation

You can verify that Sysmon64 was installed correctly by performing the following tasks:

1. Open the Task Manager (Ctrl-Alt-Del -> Task Manager) and verify that the Sysmon64

service appears in the list.

2. Return to the command prompt and run sysmon64.exe -c to view its current

configuration. Verify that the configuration you see matches the configuration shown
below:

3. Open the Windows Event Viewer and navigate to the following path in the left

navigation pane:

Applications and Services Logs | Microsoft | Windows | Sysmon | Operational

4. Verify that Network connection detected (Event ID 3) events appear in the list as

highlighted in the figure below:

Verify Sysmon Events are Received on DP

You can verify that the manually installed Sysmon64 service is successfully sending events to
the DP with the following procedure:

1. Connect to the DP managing the Windows Server Sensor and navigate to System |

DATA SOURCE MANAGEMENT | Sensors | Sensors.

2. Take note of the name of the sensor where you installed the Sysmon64 service. For

example:

3. Navigate to the Threat Hunting page.

4. Set the Indices dropdown to Windows Events.

5. Locate the Top Log Source Classes panel and verify that it includes Microsoft-

Windows-Sysmon, as in the figure below:

6. Click the button next to the entry for Microsoft-Windows-Sysmon in the Legend to

use it as a filter. For example:

7. Scroll down to the Documents table.

8. Use the Change Columns button to add the Sensor column to the display if it is not

already there.

9. Sort by the Sensor column and scroll to the entries for the sensor you identified at the

start of this procedure to verify that it passes the Sysmon filter. For example:

Collecting Installation Logs for Troubleshooting



If the Windows Server Sensor installation fails, you can rerun the installer with verbose
logging enabled to capture detailed diagnostic information. Add the following parameter to
the installation command:

/l*v C:\temp\msi.log

This option generates a detailed MSI installation log at C:\temp\msi.log, which can be
reviewed to help identify the cause of the installation failure.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

