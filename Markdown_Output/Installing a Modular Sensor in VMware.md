Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Installing a Modular Sensor in VMware

 Learn more at Stellar Cyber Academy.

The following links take you to courses on the Stellar Cyber Academy technical training
portal where you can learn more about a topic by watching the suggested lessons.

M04 Modular Sensor Installation and Configuration on ESXi (01h:52m)  

Introduction (06m:00s)

Get introduced to installing and configuring a Stellar Cyber Modular Sensor on VMware
ESXi. Learn about log forwarding, network traffic features, and the role of the sensor in
collecting and analyzing telemetry for enhanced security operations.

Overview (33m:00s)

Explore the high-level placement and capabilities of Modular Sensors within the Stellar
Cyber Platform, including key features such as network traffic capture, sandboxing, and
IDS. Review firewall communication requirements for seamless deployment, then watch
a demo of configuring Modular Sensor profiles to manage network flow, log forwarding,
and security data collection to optimize Interflow ingestion into the data lake.

ESXi Configuration (25m:00s)

Configure the ESXi environment to support Modular Sensors within the Stellar Cyber
Platform, covering the creation of port groups, network switches, and virtual network
adapters. Learn how to enable promiscuous mode and set up network interfaces for
both management and traffic monitoring, then follow a demonstration that walks through
each configuration step to facilitate traffic capture and sensor deployment.

Modular Sensor CLI Configuration (17m:00s)

Learn CLI commands to configure network settings, including IP addresses, gateway,
hostname, and DNS for Modular Sensors. Follow along with a hands-on demo showing
each configuration step, then discover how to bind the sensor to the Stellar Cyber
Platform Data Processor to establish connectivity and enable seamless data forwarding.

Modular Sensor Data Processor Configuration (12m:00s)

Discover how to authorize and configure the Modular Sensor within the Stellar Cyber
Platform, ensuring secure communication between sensor and platform components.
Watch a demonstration of the full authorization process, including how to activate
profiles and enable log forwarding through the Stellar Cyber UI. Learn to monitor status
indicators, confirm sensor health, and validate successful integration with the data lake
to support threat intelligence and machine learning workflows.

Modular Sensor Configuration Validation (18m:00s)

Validate the Modular Sensor setup by monitoring syslog traffic and confirming that log
data reaches the Stellar Cyber Platform for processing and analysis. Follow a
demonstration to verify data flow between the Modular Sensor and the Stellar Cyber
Platform, and learn techniques for checking log counters to ensure that sensor output is
correctly forwarded and ingested into the data lake.

The first time you access a link on the portal during a session, you must log in to access
content.

This topic describes how to install a Modular Sensor in a VMware environment using the
installation file downloaded from the Download Images tab in the System | DATA SOURCE
MANAGEMENT | Sensors | Sensor Installation page. Refer to the following sections for
details:

About Modular Sensors

Site Preparation

Obtaining the Installation File

Creating a Virtual Machine Port Group

Installing the Modular Sensor Image

Applying a Token to the Installed Sensor

Configuring a Static IP Address (Optional)

Configure NTP and Set the Timezone

Enabling SSSE3 for the Modular Sensor VM

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
Refer to Virtual Modular Sensor Provisioning and Performance for details on the resources
required to run different combinations of features in a Modular Sensor Profile. Provision your
modular sensor according to the features that you plan on enabling.

You will also need:

A token obtained from the DP that will manage the sensor.

Open firewall ports for log ingestion.

Open firewall ports for the features you plan on enabling in the Modular Sensor Profile
for this sensor.

One physical port on the system will be configured to receive network traffic to be analyzed. It
must have promiscuous mode capability and be connected to an appropriate data source.

In addition, the system BIOS must have VT-d/IOMMU enabled.

Supported ESXi Versions

Sensor installation is supported on the following ESXi versions:

8.0
7.0
6.7

Obtaining the Installation File
You download the installation file for the Modular Sensor for VMware from the Download
Images tab in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor
Installation page. Use the following procedure:

 Only users with the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Sensor Image Download privilege assigned to their profile in System | DATA
SOURCE MANAGEMENT | Sensors | Sensor Installationthe System |
 ORGANIZATION MANAGEMENT | Role-Based Access Privileges interface can download
images.

1. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation page.

2. Set the Sensor Type dropdown to Modular Sensor.

3. Set the Image Type to VMware ESXi.

The display updates to show you the size of the files to be downloaded.

4. Click the Download button. The system downloads the installation file (aella-modular-

ds-6.6.0.ova) along with its corresponding SHA-1 hash file.

Creating a Virtual Machine Port Group
The following procedure creates a new virtual machine port group with port mirroring capabilities.
This is the port group to which we'll connect the new modular sensor's monitor interface for traffic
acquisition in the next procedure.

1. Log in to the vSphere Client, right-click the datacenter or host where you want to install

the port group, and select the Add Networking option from the context menu that
appears.

2. Select the Virtual Machine Port Group for a Standard Switch option and click Next.

3. You can add the port group to an existing switch or create a new switch. The following

image shows the attachment being made to an existing switch named vSwitch0.

4. Create a network label with the VLAN ID of 4095, as shown in the image below:

5. At this point the settings should be complete. Click the Finish button, as illustrated

below.

6. Once setup is complete, you can view the new port group by right-clicking the host

where it is installed, selecting Settings from the context menu that appears, and then
selecting the Networking | Virtual Switches entry, as shown in the image below.

7. Click the three-dot icon for the port group and select Edit Settings from the context

menu that appears.

8. Click on the Security entry in the left navigation panel and enable Promiscuous Mode
by checking the corresponding Override and Accept boxes, as shown in the image
below. Then, click OK to apply your settings.

Installing the Modular Sensor Image
This section describes how to install the Modular Sensor image you downloaded from the DP at
the start of the procedure.

Select the option to deploy a new OVF template wizard and use the Local file option, as shown
below.

1. Log in to the vSphere Client.

2. Right-click the datacenter or host where you want to install the Modular Sensor and

select the Deploy OVF Template option from the context menu that appears.

The Deploy OVF Template wizard starts.

 Stellar Cyber provides the Modular Sensor image as an OVA file. The OVA file

includes the necessary OVF file as a component.

3. In the Select an OVF Template step, choose the Local file option and use the Choose
Files button to navigate to the OVA file you downloaded in Obtaining the Installation
File. Once you have selected the OVA file, click Next.

4. In the Select a name and folder step, provide a name for the virtual machine and

select the data center where it will be deployed, as shown below. Then, click Next to
continue.

5. In the Select a compute resource step, select the resource that will run the virtual
machine. This should be same resource where the mirror port is hosted. Then, click
Next to continue.

6. Review the details for the template and click Next to continue.

7. In the Select storage step, select the datastore to be used for the VM's configuration

and disk files and click Next to continue.

8. In the Select networks step, use the Destination Network dropdown to select the

network where the Modular Sensor's management interface connects. Select a network
that can access the DP that will manage the sensor and click NEXT to continue.

9. Review the settings in the Ready to complete step and click FINISH to start the

deployment.

10. The deployment begins. You can keep tabs on its progress in the Recent Tasks panel
at the base of the vSphere Client display. When the deployment completes, you can
select its entry in the left navigation panel to see its settings. For example, in the image
below, we have selected the Modular Sensor named Stellar Modular Docs.

Adding a Monitoring Interface and Connecting it to the Port Group

The next step is to add a second network adapter to the Modular Sensor virtual machine to be
used as a monitor interface. This adapter will monitor traffic on the port group we created in
Creating a Virtual Machine Port Group.

 You can only add a network adapter to the VM while it is powered off.

1. You should still be in the vSphere Client with the Modular Sensor virtual machine

selected. Click the Edit Settings link in the VM Hardware panel.

2. Click the Add New Device button and select Network Adapter from the context menu

that appears.

A new entry appears in the Edit Settings dialog box for New Network.

3. Click the dropdown for the new adapter's network and select the Browse option.

4. Select the entry for the port group you created in Creating a Virtual Machine Port

Group and click OK.

The new network adapter appears in the Edit Settings dialog box connected to the
selected port group.

5. Make sure the Connect box for the new network adapter is checked, as illustrated

above, and then click OK on the Edit Settings dialog box.

6. At this point the Modular Sensor is installed. If you need to provision any additional
resources to support the modular features you anticipate enabling in the sensor's
Sensor Profile, now is a good time to do so while it is still powered off. Then, you can
start the VM.

Applying a Token to the Installed Sensor
The next step is to obtain and apply the token used to authorize and configure the installed
sensor.

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

Enabling SSSE3 for the Modular Sensor VM
The Modular Sensor VM must have SSSE3 enabled for its processors in order to operate
correctly. In most cases, SSSE3 will already be enabled. However, if you encounter issues with
packet collection or Interflow data generation, you can use the instructions below to ensure that
SSSE3 is enabled.

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

Preventing Clock Drift for Stellar Cyber VMs Deployed in ESXi

Virtual machines running on VMware ESXi can experience significant clock drift if the
hypervisor's clock is not properly configured or if NTP synchronization on the ESXi host is
unavailable. To help prevent clock drift on Stellar Cyber virtual machines deployed in ESXi, follow
the guidance in Disabling Time Synchronization for Virtual Machines  on the Broadcom
Support site to disable one-off time synchronization for your Stellar Cyber VMs by adding the
following advanced configuration parameters:

time.synchronize.continue = "FALSE"
time.synchronize.restore = "FALSE"
time.synchronize.resume.disk = "FALSE"
time.synchronize.shrink = "FALSE"
time.synchronize.tools.startup = "FALSE"
time.synchronize.tools.enable = "FALSE"
time.synchronize.resume.host = "FALSE"

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

