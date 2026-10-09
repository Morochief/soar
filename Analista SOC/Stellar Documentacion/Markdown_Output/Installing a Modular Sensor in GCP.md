Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Installing a Modular Sensor in GCP

This topic describes how to install a Modular Sensor in a Google Cloud Platform (GCP)
environment. Refer to the following sections for details:

About Modular Sensors
Site Preparation
Configuring and Launching the Instance
Applying a Token to the Installed Sensor
Configuring a Static IP Address (Optional)
Configuring Packet Mirroring in GCP
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
Click to see the minimum system requirements for installing a modular sensor.

You must have:

One IP address with access to a default gateway
A Stellar Cyber license that can be applied to the sensor

To prepare for the installation:

1. Open firewall ports for log ingestion.

2. Open firewall ports for the features you plan on enabling in the Modular Sensor Profile

for this sensor.

3. Contact Stellar Cyber support (support@stellarcyber.ai) for access to the image. You

must provide:

The GCP Gmail account name

Do this at least a day before installing, so we have time to deploy the images to your account.

Configuring and Launching the Instance
To configure and launch the instance:

 Use our example as a guideline, as you might be using a different software version.

1. Log in to your Google Cloud Platform Dashboard.

2. Use the dropdown in the toolbar to select the Project where you want to deploy the DP.

3. Select the Compute Engine | VM instances entry from the left navigation panel.

4. Click the Create Instance button.

5. Supply a Name, Region, and Zone for the instance.

6. Choose a Machine type for the instance. You can either choose one of the

preconfigured GCP machine types or create a Custom machine type, so long as the
instance meets the minimum specifications.

In the example below, we are creating a Custom Machine Type with 16 virtual cores
and 32 GB of memory to serve as the foundation for a Security Sensor:

7. Scroll down to the Boot disk section and click the CHANGE button.

8. Click on the CUSTOM IMAGES tab.

9. Click the SELECT A PROJECT button and choose the stellar-official-images project.

 The stellar-official-images entry won't appear until we've made images available
to your account. If you don't see the stellar-official-images entry, make sure your
region is the same one where you asked Customer Success to deploy the images.
If you still don't see the entry, contact Customer Success.

10. Select the entry for your sensor version and type from the Images dropdown.

11. Set the Boot disk type to Balanced persistent disk, choose a size of 100 GB, and

click Select.

You are returned to the Create an instance wizard.

12. Click the Create button to create the instance.

 You can launch the image but you cannot copy it. This means that the VM must be

deployed in the GCP region where the image was authorized.

The VM is now running in the GCP cloud and appears in the Compute engine | VM instances
list, as illustrated below. Copy the External IP address so you can use it to connect to the
Sensor's console in the next section.

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

Configuring Packet Mirroring in GCP
Refer to Configuring GCP Packet Mirroring for details on how to use packet mirroring for
packet acquisition in GCP environments.

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

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

