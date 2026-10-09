Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Installing a Linux Server Sensor

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M06 Open XDR Linux Server Sensor Installation and Configuration (01h:21m)  

Introduction (05m:00s)

Begin with an overview of installing and configuring the Linux Server Sensor in the
Stellar Cyber Platform. Learn how this sensor integrates with the data processor,
handles data forwarding, and supports advanced monitoring features like File
Integrity Monitoring (FIM) and network traffic analysis.

Overview (14m:00s)

Discover how the Linux Server Sensor fits into the Stellar Cyber Platform
architecture. Understand the roles of the data lake and data analyzer, network
prerequisites, and resources needed to ensure efficient data collection and analysis.

Software Installation (14m:00s)

Follow the steps to install the Linux Server Sensor software on a Linux host, from
downloading the installation script to configuring secure communication with the data
processor. Learn how to set up essential configurations and verify a successful
installation using the Stellar Cyber Platform.

Server Sensor Authorization (15m:00s)

Learn how to authorize the Linux Server Sensor within the Stellar Cyber Platform,
then follow a practical demonstration of the complete authorization workflow in the
data processor. Explore how to configure sensor profiles to enable secure data
transfer, assign custom settings for tailored data monitoring, and confirm sensor
status to establish real-time data flow into the data lake.

Server Sensor Validation (20m:00s)

Validate the Linux Server Sensor setup by confirming that configuration aligns with
data processor standards and that Linux event data is forwarding correctly to the
Stellar Cyber Platform. Follow a demonstration to verify connection status, observe
Linux events, and review Interflow records in the data lake to ensure sensor
functionality is operating as expected.

Enhanced FIM (18m:00s)

Learn how to enable and configure File Integrity Monitoring (FIM) on Linux Server
Sensors within the Stellar Cyber Platform, setting up detection for file creation,
deletion, and modification events to strengthen security monitoring. Follow along with
a hands-on demonstration that walks through the configuration process and validates
file monitoring accuracy, confirming that FIM events are captured correctly and
surfaced as Interflow records in the data lake for analysis.

Enhanced Network Traffic (18m:00s)

Configure and validate network traffic monitoring to capture North-South traffic on
Linux servers, and discover how this feature integrates with Interflow to provide
enriched metadata on traffic flows. Watch a demo that walks through the
configuration process and shows how Linux Server Sensor traffic data is captured,
analyzed, and displayed within the Stellar Cyber Platform.

The first time you access a link on the portal during a session, you must log in to access
content.

This topic describes how to install a Linux Server Sensor in a supported target environment
using the installation file downloaded from the Download Images tab in the System | DATA
SOURCE MANAGEMENT | Sensors | Sensor Installation page. Refer to the following sections
for details:

About the Linux Server Sensor

Supported Linux Operating Systems

Installation Prerequisites.

Obtaining the Installation File

Running the Installation Script

Applying a Token to the Installed Sensor

Uninstalling a Linux Server Sensor

About the Linux Server Sensor
A Linux server sensor is a managed background daemon that works as a modular sensor without
log forwarding that also monitors:

Process info
Command execution
Files
File events

The server sensor converts that information to metadata and forwards it to the DP as Interflow.
The DP can then correlate traffic, processes, users, and commands for security, DDoS, and
breach attempt detections.

The server sensor launches the following processes:

aella_audit – collects audit logs and provides file integrity monitoring
aella_conf – handles the configuration
aella_ctrl – monitors other services, and can stop or start them based on the
configuration
aella_flow – collects metadata in traffic
aella_mon – collects system resource usage, including CPU, RAM, and disk

Data collected by the Linux server sensor can feed the following Stellar Cyber indices:

Traffic (aella-adr-*)

Linux Events (aella-audit-*)

Sensor Monitoring (aella-ade-*)

Supported Linux Operating Systems
The table below lists the Linux distributions supported for Linux Server Sensor installation. Each
of the supported Linux distributions uses the same ds_linux_install_all_in_one.sh file from
theDownload Image tab in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor
Installationpage, as summarized below.

Alma Linux 8.10, 9

Amazon Linux 2 and 2023

CentOS 7, 8, 9, 10

CloudLinux 7.9

Debian 8, 9, 10, 11, 12, and 13

Kali Linux 2023.4

Linux Mint 18, 19, 20, 21

Oracle Linux 7.x, 8.x, 9.x, 10.x

Red Hat Enterprise Linux 7, 8, 9, and 10

 Fedora Linux 40+, the upstream distribution of RHEL 10, is also supported.

Rocky Linux 8, 9, 9.3

SUSE Linux Enterprise Server 12 (SP3-SP5), 15 (GA, SP1-SP7), 16 (GA)

Ubuntu 16.04, 18.04, 20.04, 21.04, 22.04, and 24.04

 These are the tested and supported versions. Installation may work successfully in other
versions. The installation script only blocks deployment in target environments with known
incompatibilities.

 The Linux Server Sensor is only supported in 64-bit environments.

  When you execute ds_linux_install_all_in_one.sh in a supported environment, it

automatically detects the target operating system and installs the corresponding image. All
necessary images are bundled with the script – the installer picks the correct one based on
the operating system it detects at run-time.

About the Self-Contained Installation Script

Stellar Cyber uses a self-contained installation script named ds_linux_install_all_in_one.sh
that can install the Linux server sensor on all supported operating systems. The
ds_linux_install_all_in_one.sh script offers the following benefits relative to the installers in
previous releases:

Self-contained – The ds_linux_install_all_in_one.sh script does not need to
download any OS packages or images from the internet. You just need to make sure
that the standard curl, ntp, and zip packages are installed on the target machine. All
other OS packages are bundled with the script.

Operating System Aware – When you execute ds_linux_install_all_in_one.sh in a
supported environment, it automatically detects the target operating system and installs
the correct image. All necessary images are bundled with the script – the installer picks
the correct one based on the operating system it detects at run-time.

Flexible – The same installation script can be used to install in multiple different target
environments, as summarized in the Installation Matrix below.

Linux Server Sensor System Requirements
The Linux Server Sensor uses 5% of the host server's resources, including each CPU core, so
the VM must have at least:

Component

Host CPU

Host RAM

Available SSD Disk Space

Specification

Xeon Core 2 virtual cores (2.0 GHz or more)

12 GB

128 GB

Installation Prerequisites.

All the procedures that follow require that you are logged in to an account with sufficient
system storage and sudo access.

The self-contained installation script (ds_linux_install_all_in_one.sh) requires the
curl, ntp, and zip packages on the target machine. The installer checks for the
presence of curl before installing and returns an error if it is not found.

Enabling SSSE3 for Linux-Based Sensors

The target host must have SSSE3 enabled for its processors in order for the Linux server sensor
to operate correctly.

Click here to see instruction on how to enable SSSE3.

 Sensors installed on Linux hosts must have SSSE3 enabled for their processors in order

to operate correctly. This is true for Modular Sensors and Linux Server Sensors, as well as
legacy Network and Security Sensors.
SSSE3 is typically supported/enabled for most vCPUs, but may not be for certain legacy
AMD vCPUs. See below for instructions on enabling SSSE3.

To enable SSSE3 for a virtual machine:

1. Start the virtual shell (virsh)

2. Type the following command to edit the virtual machine's settings:

edit <virtual_machine_name>

3. Locate the <cpu> section. It should appear similar to the following:

<cpu mode='custom' match='exact' check='partial'>

    <model fallback='allow'>SandyBridge</model>

......

 </cpu>

4. Add the following line to the <cpu> section:

<feature policy='require' name='ssse3'/>

When you are done, the <cpu> section should appear similar to the following:

<cpu mode='custom' match='exact' check='partial'>

    <model fallback='allow'>SandyBridge</model>

    <feature policy='require' name='ssse3'/>

...........

  </cpu>

5. Save changes to the virtual machine and exist virsh.

6. Run the following command:

virsh define /etc/libvirt/qemu/<virtual_machine_name>.xml

 Each virtual machine has a configuration .xml file. Typically, these files are

stored under /etc/libvirt/qemu, but the location may be different for your system.

7. Stop and start the virtual machine in virsh.

Python Requirements

In contrast to previous releases, installations using the self-contained installer
(ds_linux_install_all_in_one.sh) do NOT require Python 2.

NUMA Requirements

To prevent configuration errors, Stellar Cyber recommends that you do not install the Linux
Server Sensor on target hosts with two NUMA nodes. You can use the following command to

check the number of NUMA nodes in your target host:

$ lscpu | grep -i numa

For example, the following example shows the output returned by this command for a system
with two NUMA nodes:

$ lscpu | grep -i numa
NUMA node(s):          2
NUMA node0 CPU(s):     0-19,40-59
NUMA node1 CPU(s):     20-39,60-79

Exclude Server Sensor from AV/EDR Scanning

Stellar Cyber recommends that you prevent potential conflicts by configuring any anti-virus or
EDR software installed on the same host as the Server Sensor to exclude the Server Sensor
installation directories from scanning. The directories to exclude for a Linux Server Sensor are as
follows:

Server Sensor Type

Folders/Files to Exclude from AV/EDR Scanning

Linux

/var/aella

/var/log/aella

/opt/aella

/opt/aelladata

Obtaining the Installation File
You download the installation file for the Linux Server Sensor from the Download Images tab in
the System | DATA SOURCE MANAGEMENT | Sensors | Sensor Installation page.
Use the following procedure:

 Only users with the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Sensor Image Download privilege assigned to their profile in the System |
 ORGANIZATION MANAGEMENT | Role-Based Access Privileges interface can download
images.

1. Navigate to System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Download Image.

2. Set the Sensor Type dropdown to Linux Server Sensor.

The display updates to show you the size of the files to be downloaded.

3. Download.

The system downloads the installation file for your selected target along with its
corresponding SHA-1 hash file.

Running the Installation Script
All the procedures in this section require that you are logged in to an account with sufficient
system storage and sudo access. Regardless of the Linux version the installation steps are as
follows:

1. Open ports on your firewall for the sensor.
2. Obtain a token for the Server Sensor.
3. Use the instructions below to run the installation script and apply the token you
downloaded in the previous steps. The procedure to run the script is the same,
regardless of your operating system. However, there are some notes specific to
different operating systems following the procedure.

4. Applying a token automatically points the sensor at the Stellar Cyber instance where the
token was generated. Alternatively, if you have a data aggregator deployed, you can
use the set aggregator command to specify the IP address of the destination
aggregator.

Running the Installation Script

You run the installation script in the same way for all supported Linux distributions:

 This procedure applies the token to the server sensor as part of the command used to run
the installation script. You can also apply the token after the installation, if you like. Refer to
Applying a Token to the Installed Sensor for details on working with tokens.

1. Copy the installation script to the target host.

2. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation page and click on the Tokens tab.

3. Either download the token as a file or copy the string so you can include it as part of the

command running the installation script. Refer to Obtaining a Token for the
Installation for details.

 You may find it easier to download the token as a file if you plan on reusing it with

multiple sensors.

4. Open a command line session with the target host and change directories to the

location where you copied the installation script.

5. Run the script with ONE of the commands below:

Option 1. Include

the Token String

Option 2. Point to

the Token File

sudo bash ds_linux_install_all_in_one.sh --token <token string>

sudo bash ds_linux_install_all_in_one.sh --token_file <path to token file>

Option 3. Apply a

sudo bash ds_linux_install_all_in_one.sh

Token Later

This command installs the server sensor without applying a token. Refer to Applying a

Token to the Installed Sensor for details on applying a token after installation.

6. Use the aella_cli command to start the Server Sensor CLI.

Additional Arguments for the Installation Script

The table below lists and describes additional supported arguments for the
ds_linux_install_all_in_one scripts:

Argument (Short) Description

--

Optional. You can use these arguments to specify the primary and secondary aggregators for this server

primary_aggregat

sensor. Alternatively, you can do it after sensor installation using the instructions in Connecting the

Sensor to an Aggregator.

or

--

secondary_aggreg

ator

-c | --check

Shows system information, helping you decide whether system resources are sufficient to support server

sensor installation.

Installation Notes for Specific Operating Systems

This section provides some configuration notes for specific operating systems. Check the section
corresponding to your target Linux distribution for details:

Ubuntu Linux 18.04

During installation in Ubuntu 18.04, the installation script may report a certifi package error
similar to the following:

Install certifi, ver 2021.10.8
certifi exists, version 2018.1.18
Package certifi==2018.1.18 isn't sufficient to install agent sensor
Agent sensor needs certifi version 2021.10.8 or higher

You can work around this issue by manually installing version 2021.10.8 of the certifi package
with the following command:

pip install certifi==2021.10.8

Once the correct version of the certifi package is installed, you can re-run the installation script
to install the sensor.

CentOS 8 and 7.9.2009 Prerequisites

CentOS 8 Prerequisite – Update the Base URL to vault.centos.org

You must update the source link for some CentOS 8 environments to vault.centos.org
instead of mirror.centos.org to ensure that dependent packages can be installed.

This issue is present in CentOS 8.5.2111 but may also exist in other CentOS 8 versions. The
symptom for this issue is typically a series of No URLs in mirrorlist errors when installing

in CentOS 8.

The following commands make the necessary changes for most environments to ensure that
dependent packages can be downloaded from vault.centos.org.:

cd /etc/yum.repos.d/

sudo sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*

sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g'

/etc/yum.repos.d/CentOS-*

sudo yum update -y

CentOS 7.9.2009 Prerequisite – Enable the EPEL Repository for pip Installation

CentOS 7.9.2009 does not install pip by default because it is not available in the core CentOS
7 repositories. To ensure that pip is installed, you must enable the Extra Packages for
Enterprise Linux (EPEL) repository. This repository provides additional packages (including
pip) that aren't included in the standard CentOS and Red Hat repositories.

Perform the following the steps to enable the EPEL repository and install pip:

1. Add the EPEL repository with the following command:

sudo yum install epel-release

2. Install pip with the following command:

sudo yum install python-pip

3. Verify pip installation with the following command:

pip --version

Applying a Token to the Installed Sensor
This section provides details on working with tokens. It's generally easiest to apply a token to the
server sensor as part of the command that runs the installation script. However, you can also
apply a token after installation using the instructions in this section.

Obtaining a Token for the Installation

Tokens are required to authorize and configure the installation of a sensor image downloaded
from the DP in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor
Installation page. Tokens point the installed sensor to the correct DP, assign the specified
tenant, optionally provision a sensor profile, and authorize the sensor installation.

Use the following procedure to obtain a token in the Tokens tab:

1. Navigate to System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Tokens.

2. If there is already an unexpired token that you want to use for the installation, you can
either use the Copy button to copy it to the clipboard or use the Download button
to download it as a file.

Copy the token if you plan on applying it by pasting it. The token can be pasted
into the command used to run the installation script or after installation using
the set token string <token> command in the CLI

Download the token as a file if you plan on using one of the following
techniques to apply it:

Pointing to the token file in the command used to run the installation
script.

Uploading the file to the sensor and referring to it in a set token
file <token file> command.

Hosting the file on an HTTP server and referring to it in a set token
url <token url> command.

 Refer to Assigning Tokens for a summary of the different ways in which tokens

can be applied to a sensor installation.

3. You can also click the Generate button to create a new token.

The Generate Installation Token dialog appears:

4. Select the tenant for the token from the Tenant dropdown. This is the tenant to which all
sensors authorized with this token will be automatically assigned. The dropdown lists all
tenants configured for your organization in the System | ORGANIZATION
MANAGEMENT | Tenants page.

5. Select the Sensor Profile to be assigned to all sensors authorized with this token from
the Sensor Profile dropdown. The dropdown lists all sensor profiles available in the
System | Sensor Profiles page for the selected Tenant.

 If you do not want to assign a Sensor Profile with a token, you can set this field to

None (no sensor profile selected). This is also the setting for any tokens migrated
from a pre-5.3.0 release as part of an upgrade.

6. Use the Expiration dropdown to select an expiration date for this token. You can select

specified expiration dates ranging from two weeks to three months.

 You can also select Never expires for the expiration date. However, Stellar Cyber
recommends that you specify expiration dates for your tokens in order to improve
the security of your deployment.

 Remember that when a token expires, sensors authorized with the token

continue to operate as normal. Once a sensor successfully registers with the
Stellar Cyber platform, it no longer uses the token. It is only used for the initial
authorization, registration, and configuration of the sensor.

7. Select Generate.

The system generates the token and displays its contents in the Token field. The dialog
also updates to display the expiration date for the token, as illustrated below.

8. Copy the token to the clipboard immediately or close the dialog and retrieve the token

from the Tokens tab later.

Applying the Token to the Linux Server Sensor

Tokens are required for the installation of a sensor image downloaded from the DP in the
Download Image tab.

You apply tokens to sensors either as part of the command used to run the installation script or
after installation.

The table below summarizes the options for applying a token after installation.

Refer to Running the Installation Script for instructions on including the token as part
of the command used to run the installation script.

1. Use the aella_cli command to start the Server Sensor CLI.

2. Apply the token to the installed sensor from the sensor CLI with the set token

command using one of the options in the table below:

 You only need to use one of the options in the table below. These are just different

ways to do the same thing – apply the token.

Option 1. Copy and Paste

Copy the token string from the Tokens tab and paste it into the CLI command. The

the Token String

syntax is as follows:

set token string <pasted string>

Option 2. Upload the Token

as a File to the Sensor

Download the token as a file from the Tokens tab, upload it to the sensor, and

reference it in the set token command. The syntax is as follows:

set token file <path to local file>

For example, the following command points to the token.text file stored in the

/tmp folder:

set token file /tmp/token.text

 This technique only works for Server Sensors. There isn't a way to upload the

token.text file to a newly installed modular sensor virtual machine.

Option 3. Host the Token

on an HTTP Server

Download the token as a file from the Tokens tab, upload it to an HTTP server,

and reference it in the set token command. The syntax is as follows:

set token url http://<url to token>

You can also use an HTTPS server. In that case, the specified URL must also

include the username and password for the server.

3. The CLI reports that the Sensor token is successfully saved

In addition, the CLI informs you that successful registration with the Stellar Cyber
Platform associated with the token is still pending. The hostname or IP address of the
associated Stellar Cyber Platform is included in the output..

 If you receive an error message instead, it's possible that the token has expired.

Refer to the Tokens tab to see the expiration date. If you are using the File
technique, it's also possible that an extra space or line may have crept into your text
file – check the file to make sure it includes only the token text.

4. Wait a minute or so. Then, verify that the token was successfully applied using any

combination of the following techniques:

Check the System | DATA SOURCE MANAGEMENT | Sensors | Sensors
list in the user interface to see that the sensor has registered itself
successfully.

Check the Status in the show cm output.

Check the Ctrl Plane Status in the show version output.

Verify that the show system command shows all services as running.

Verify that the show receiver command displays a receiver.

Verify that the show json command reports some data sent in the BYTE_SENT
column.

Connecting the Sensor to an Aggregator
When you apply a token to a sensor, the sensor is automatically pointed at the Stellar Cyber
instance where the token was generated. You can reconfigure the sensor to send its data to a
data aggregator before it is sent to the managing Stellar Cyber instance using the set
aggregator command, as described below.

 You must still authorize the sensor with a token before reconfiguring it to send data to an

aggregator.

1. Use the aella_cli command to start the CLI.

2. If you are using an aggregator and did not specify its address during installation, you
can use the set aggregator command to set it now. Specify the IP addresses of a
primary and secondary data aggregator as follows:

set aggregator <primary IP address> <secondary IP address>

3. Exit the CLI with the quit command.

Uninstalling a Linux Server Sensor
Use the following procedure to uninstall Linux Server Sensors:

Debian and Ubuntu Uninstall

To uninstall a sensor on Debian or Ubuntu:

apt-get remove aellads

CentOS, Red Hat, AWS Linux Uninstall

To uninstall a sensor on CentOS, Red Hat, or AWS Linux:

yum remove aellads

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

