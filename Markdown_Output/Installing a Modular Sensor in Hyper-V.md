Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Installing a Modular Sensor in Hyper-V

This topic describes how to install a Modular Sensor in a Hyper-V environment using the virtual
disk image file downloaded from the Download Images tab in the System | DATA SOURCE
MANAGEMENT | Sensors | Sensor Installation page. Refer to the following sections for details:

About Modular Sensors

Site Preparation

Creating A Virtual Switch

Enabling Promiscuous Mode

Obtaining the Virtual Disk Image

Creating a Modular Sensor VM from the Disk Image

Configuring the Sensor to Accept VLAN-Tagged Traffic

Provision Processors

Adding an Interface

Applying a Token to the Installed Sensor

Configuring a Static IP Address (Optional)

Configure NTP and Set the Timezone

 Use our example as a guideline, as you might be using a different software version.

 Stellar Cyber does not support the installation of third-party software on its virtual or

physical device sensors.

About Modular Sensors
Sensors provide the data gathering foundation for Stellar Cyber's OpenXDR platform, gathering
the right data with context. Modular sensors are purpose-built Stellar Cyber sensors that include
both the host and the Stellar Cyber monitoring software. They are provided as both physical
devices (Photon sensors) and virtual machine images for different target environments.

 Previous releases provided a variety of different types of device sensors, including Network,
Security, and Modular. Going forward, the only type of device sensor is Modular. You can
use the Modular Sensor Profile to enable whatever sensor features you like, creating the
same functionality provided by the different sensor types in previous releases.

A modular sensor lets you easily add the features you like to your sensor. This helps simplify
your deployment and lets you manage the VM requirements for the sensors based on the
modular features they use.

Modular Sensors always include log ingestion. From there, you can enable different features as
part of your modular sensor profile:

Enable the Network Traffic feature to monitor the virtual environment, the physical
environment if connected to the span port of a physical switch, or the LAN segment via
a mirror port on a switch. The sensor monitors network and server response times and
can identify applications.

The sensor converts that information to metadata and forwards it to the DP as Interflow.
The DP can then provide security, DDoS, and breach attempt detections.

Enable the Sandbox and IDS features to improve your security posture:

Sandbox lets you detect malware in files and network traffic through Stellar
Cyber's integrated cloud service and also provides anti-virus services.
IDS lets you detect intrusion attempts using both files and network traffic.

 Keep in mind that VM resource requirements increase as you add more features to the

Modular Sensor Profile. Refer to Virtual Modular Sensor Provisioning and Performance
for details on the resources required to run different combinations of features in a Modular
Sensor Profile, as well as how to use the show module and show module request
CLI commands to compare provisioned resources against those required to run specific
feature combinations. Stellar Cyber only enables a Modular Sensor Profile on a sensor if the
host VM's resources can support it.

Site Preparation
This process requires a Microsoft Hyper-V environment on a Windows server. Windows Server
2019 and 2016 are the tested versions.

Refer to Virtual Modular Sensor Provisioning and Performance for details on the resources
required to run different combinations of features in a Modular Sensor Profile. Provision your
modular sensor according to the features that you plan on enabling.

You will need:

Open firewall ports for log ingestion.

Open firewall ports for the features you plan on enabling in the Modular Sensor Profile
for this sensor.

Server switch with a physical network interface that supports promiscuous mode
One IP address with access to a default gateway.
A token obtained from the DP that will manage the sensor.

Creating A Virtual Switch
The first step is to create a virtual switch through which the Modular Sensor virtual machine
communicates.

 Use our example as a guideline, as you might be using a different software version.

1. Start the Hyper-V manager and open the Virtual Switch Manager from the right-hand
sidebar. Select Create Virtual Switch then choose External Network. The resulting
display is shown in the following image.

2. Select the physical network port that is to be used to connect to the outside world. The

result appears similar to the sample in the following image.

Enabling Promiscuous Mode
You enable promiscuous mode so that the sensor can monitor all traffic. Promiscuous mode can't
be enabled in the user interface, so the following commands must be performed in PowerShell.

In this example, the name of the switch is External. Change this value to the actual name of your
switch in the commands.

C:\Users\Administrator> $a = Get-VMSystemSwitchExtensionPortFeature -FeatureId 776e0ba7-94a1-

41c8-8f28-951f524251b5

C:\Users\Administrator> $a.SettingData.MonitorMode = 2

C:\Users\Administrator> add-VMSwitchExtensionPortFeature -ExternalPort -SwitchName <name of

the switch> -VMSwitchExtensionFeature $a

Obtaining the Virtual Disk Image
You download the virtual disk image for the Modular Sensor for Hyper-V from the Download
Images tab in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor
Installation page. Use the following procedure:

 Only users with the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Sensor Image Download privilege assigned to their profile in the the System |
 ORGANIZATION MANAGEMENT | Role-Based Access Privileges interface can download
images.

1. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation page.

2. Set the Sensor Type dropdown to Modular Sensor.

3. Set the Image Type toHyper-V.

The display updates to show you the size of the file to be downloaded.

4. Click the Download button. The system downloads the virtual disk image (aella-

modular-ds-6.6.0.vhdx) along with its corresponding SHA-1 hash file.

Creating a Modular Sensor VM from the Disk Image
Use the following procedure to create a Modular Sensor virtual machine from the virtual disk
image you downloaded from the DP in the previous section.

1. Return to the Hyper-V manager and select Action | New | Virtual Machine....

2. Specify a name for the new Modular Sensor. This can be any legal VM name but it is

recommended to adopt a site convention so that the name identifies the type of sensor.
The screen appears similarly to the image below.

3. Enter the Generation parameter. The guest Operating System is a 64-bit OS, so

Generation 1 is a good choice, as illustrated below:

4. Next, assign memory according to the sensor's expected workload, as stated in Server

Sensor Sizing Specifications.

5. Configure the Management network interface. You can either enter a static IP or use a
DHCP server. This is the interface that will be used for the sensor to send its Interflow
data records to the data processor. The networking is configured as in the image below:

6. Connect the Virtual Disk image that you downloaded from the DP in Obtaining the

Virtual Disk Image. Select the Use existing option, as illustrated below and use the
Browse button to point the Location field to the downloaded .vhdx file.

7. The Modular Sensor VM appears in the Hyper-V Manager similarly to the image below:

Configuring the Sensor to Accept VLAN-Tagged Traffic
Capture interfaces for Modular Sensor VMs deployed in Hyper-V must be configured to operate
in trunk mode when ingesting SPAN or mirror feeds that contain 802.1Q VLAN-tagged frames.

Trunk mode ensures that packets with 802.1Q VLAN tags from specified VLAN IDs are not
dropped. This allows the sensor to analyze traffic from multiple VLANs simultaneously.

Configuration Procedure

1. Ensure that the SPAN or mirror feed from the switch arrives on the physical NIC of the

Hyper-V host that is associated with an External Virtual Switch.

2. Configure the Modular Sensor VM capture interface to operate in trunk mode.

Run the following PowerShell command on the Hyper-V host to configure the Modular
Sensor VM capture interface in trunk mode with all VLAN IDs accepted:

Set-VMNetworkAdapterVlan -VMName "<Sensor VM>" -Trunk -
AllowedVlanIdList "1-4094" -NativeVlanId 0

Parameter notes

VMName – Name of the sensor VM.

Trunk – Enables trunk mode on the VM network adapter.

AllowedVlanIdList – VLANs permitted to pass to the VM. In this example, we
are accepting from the entire legal range of 802.1q VLAN IDs (1-4094). If only
specific VLANs are required, replace 1-4094 with a comma-separated list or
range. For example:

"10,20,30-40"

NativeVlanId – Specifies the native VLAN (0 disables untagged assumptions).

 Avoid Access Mode Configuration – Do not configure a single VLAN ID for the capture
NIC. Setting a single VLAN ID places the adapter in access mode, which prevents other
tagged VLAN traffic from reaching the VM.

Verification

After configuration, verify that VLAN tags are visible in captured traffic.

Example command:

tcpdump -i <interface> -e -nn vlan

Expected result:

Captured packets include 802.1Q VLAN tags.
Traffic from the expected VLANs is visible.

Provision Processors
Before you power on the Modular Sensor VM, you must provision sufficient CPU cores to handle
the Sensor's expected workload as summarized in in Server Sensor Sizing Specifications.

1. Select the VM in the list and select the Settings | Processor menu options. Then,

change the number of processors and click OK.

Enabling SSSE3 and Disabling Processor Compatibility Mode

The sensor VM must have SSSE3 enabled and processor compatibility mode disabled in order
for the Modular Sensor to operate correctly.

In most cases, SSSE3 will already be enabled. However, if you encounter issues with packet
collection or Interflow data generation, you can use the instructions below to ensure that SSSE3
is enabled.

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

Ensure that Processor Compatibility Mode is Disabled

Stellar Cyber sensors deployed in Hyper-V must have the processor compatibility feature 
disabled to ensure that the SSSE3 instruction set can be used and that aella_flow runs properly.
Although the sensor VM starts and appears to run correctly with processor compatibility enabled,
stability issues will eventually occur due to high CPU usage.

You can verify that processor compatibility mode is disabled in the same dialog box where you
just assigned CPU cores:

1. Expand the Processor entry in the left pane of the Settings dialog box.

2. Click on the Compatibility entry.

3. Ensure that Migrate to a physical computer with a different processor is disabled

and click OK.

The image below shows you the option that must be disabled for Stellar Cyber sensors:

Ensure that Processor Compatibility Mode is Disabled

Stellar Cyber sensors deployed in Hyper-V must have the processor compatibility feature 
disabled to ensure that the SSSE3 instruction set can be used and that aella_flow runs properly.
Although the sensor VM starts and appears to run correctly with processor compatibility enabled,
stability issues will eventually occur due to high CPU usage.

You can verify that processor compatibility mode is disabled in the same dialog box where you
just assigned CPU cores:

1. Expand the Processor entry in the left pane of the Settings dialog box.

2. Click on the Compatibility entry.

3. Ensure that Migrate to a physical computer with a different processor is disabled

and click OK.

The image below shows you the option that must be disabled for Stellar Cyber sensors:

Adding an Interface
Before you power on the Modular Sensor VM, you must add a monitoring interface used to
gather network data. You connect the monitoring interface to the virtual switch you added in
Creating A Virtual Switch. Use the following procedure:

1. Click Add Hardware | Network Adapter.

 You can only add a network adapter to the VM while it is powered off.

2. Select the virtual switch that you created in in Creating A Virtual Switch, as illustrated

below:

3. Expand the associated network adapter and click Advanced Features.

4. Set the mirroring mode of the aggregator to Destination, as illustrated below:

5. When you have finished adding the interface, power on the Modular Sensor VM.

Applying a Token to the Installed Sensor
The next step in installing a Modular Sensor is to obtain and apply the token used to authorize
and configure the installed sensor.

Obtaining a Token for the Installation

Tokens are required to authorize and configure the installation of a sensor image downloaded
from the DP in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor
Installation page. Tokens point the installed sensor to the correct DP, assign the specified
tenant, optionally provision a selected sensor profile, and authorize the sensor installation.

Use the following procedure to obtain a token in the Tokens tab:

1. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation page and click on the Tokens tab.

2. If there is already an unexpired token that you want to use for the installation, you can
either use the Copy button to copy it to the clipboard or use the Download button
to download it as a file.

Copy the token if you plan on applying it by pasting it into a set token
string <token> command in the CLI.

Download the token as a file if you plan on hosting the file on an HTTP server
and referring to it in a set token url <token url> command.

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
System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles page for the
selected Tenant.

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

7. Click the Generate button.

The system generates the token and displays its contents in the Token field. The dialog
also updates to display the expiration date for the token, as illustrated below.

8. You can use the Copy button to copy the token to the clipboard immediately, or simply

close the dialog and retrieve the token from the Tokens tab later on.

Applying the Token to the Sensor

Tokens are required to complete the installation of a sensor image downloaded from the DP in
the Download Image tab.

You apply tokens to sensors as the last step in the overall installation procedure:

1. Log in to your new Sensor. The default username/password is aella/changeme. You

are immediately prompted to change the password.

2. Apply the token to the installed sensor from the sensor CLI with the set token

command using one of the options in the table below:

 You only need to use one of the options in the table below. These are just two

different ways to do the same thing – apply the token.

Option 1. Copy and

Copy the token string from the Tokens tab and paste it into the CLI command. The

Paste the Token String

syntax is as follows:

set token string <pasted string>

Option 2. Host the Token

on an HTTP Server

Download the token as a file from the Tokens tab, upload it to an HTTP server, and

reference it in the set token command. The syntax is as follows:

set token url http://<url to token>

You can also use an HTTPS server. In that case, the specified URL must also include

the username and password for the server using the following syntax:

set token url https://<user:password>@URL>

3. The CLI reports that the Sensor token is successfully set.

 If you receive an error message instead, it's possible that the token has expired.

Refer to the Tokens tab to see the expiration date. If you are using the File
technique, it's also possible that an extra space or line may have crept into your text
file – check the file to make sure it includes only the token text.

4. Wait a minute or so. Then, verify that the token was successfully applied using any

combination of the following techniques:

Check the System | DATA SOURCE MANAGEMENT | Sensors | Sensors
list in the user interface to see that the sensor has registered itself
successfully.

Verify that the show system command shows all services as running.

Verify that the show receiver command displays a receiver.

Verify that the show json command reports some data sent in the BYTE_SENT
column.

Configuring a Static IP Address (Optional)
By default, the sensor uses DHCP for the management port's IP address. For ease of
troubleshooting, however, Stellar Cyber recommends that you reconfigure the management port
to use a static IP address. The procedure is as follows:

1. Log in to your sensor. The default username/password is aella/changeme, but you

changed this when you applied the token in the previous section.

2. You can set IP parameters manually using commands similar to the following (substitute

your own IP parameters for the ones shown in bold below):

set interface management ip 192.168.14.100/255.255.255.0

set interface management gateway 192.168.14.1

set interface management dns 8.8.8.8

3. Verify the IP settings with the show interfaces command.

4. Log out with the quit command.

Configure NTP and Set the Timezone
Stellar Cyber strongly recommends that configure NTP and set the timezone for the sensor.

Refer to Best Practices for NTP and Timezones for details.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

