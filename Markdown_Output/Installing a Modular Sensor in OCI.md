Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Installing a Modular Sensor in OCI

This topic describes how to install a Modular Sensor in an Oracle Cloud Infrastructure
(OCI) environment. Refer to the following sections for details:

About Modular Sensors

Site Preparation

Obtaining the Installation File

Installing the Modular Sensor Image

Applying a Token to the Installed Sensor

Configuring a Static IP Address (Optional)

Configuring a VTAP in OCI

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

You will also need to open firewall ports for the features you plan on enabling in the Modular
Sensor Profile for this sensor.

This topic also describes how to configure a VTAP in OCI to direct data to a load balancer
connected to a Modular Sensor's management port.

Obtaining the Installation File
You download the installation file for the Modular Sensor for OCI from the Download Images tab
in the System | DATA SOURCE MANAGEMENT | Sensors | Sensor Installation
page. Use the following procedure:

 Only users with the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation | Sensor Image Download privilege assigned to their profile in the System |
 ORGANIZATION MANAGEMENT | Role-Based Access Privileges interface can download
images.

1. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors | Sensor

Installation page.

2. Set the Sensor Type dropdown to Modular Sensor.

3. Set the Image Type to KVM.

 The same qcow2 installation file used for KVM can also be used for OCI.

The display updates to show you the size of the file to be downloaded.

4. Click the Download button. The system downloads the installation file (aella-modular-

ds-6.x.x.qcow2.zip) along with its corresponding SHA-1 hash file.

5. Unzip the installation file's contents (virt_deploy_modular_ds.sh and aella-modular-

ds-6.x.x.qcow2).

 You will upload the aella-modular-ds-6.x.x.qcow2 image file to OCI in the next

section.

Installing the Modular Sensor Image
This section describes how to install the Modular Sensor image in OCI:

1. Log in to Oracle Cloud Console at https://cloud.oracle.com/ .

2. Click the main menu icon at the top left of the Oracle Cloud Console.

3. If you do not already have a bucket for the Modular Sensor, navigate to Storage |

 Buckets.

4. Click Create Bucket to add a new bucket. Select the Standard storage tier, supply a

name, and click Create to add the bucket to your account.

5. Click the entry for the bucket you just created. Then, use the Upload button to upload

the aella-modular-ds-5.0.x.qcow2 image you downloaded in Obtaining the
Installation File. The Choose Files from your Computer field lets you either drag and
drop the file or select the file in a standard Browse dialog box.

6. Click the main menu icon and navigate to Compute | Custom Images.

7. Click the Import image button and fill out the Import image dialog box as follows:

Supply a Name.

Use the Bucket field to select the bucket where you uploaded the image at the
start of this procedure.

Use the Object name field to select the aella-modular-ds-6.x.x.qcow2
image.

Set the Operating system to Ubuntu.

Set the Image type field to QCOW2

Leave Launch mode set to Paravirtualized mode.

The figure below provides an example of the settings:

8. When you have finished configuring the settings in the Import image dialog box, click

the Import image button to start the import process.

The Custom image details page appears for the image while it imports. When the image
has finished importing, it appears with a value of Succeededin the State column, as
shown below.

9. Once the image has finished importing, click the Create instance command to create a

new instance based on the image. Set the options in the Create compute instance
dialog box as follows:

Supply an easily identifiable Name for the new instance.

Choose the compartment and availability domain for the new instance.
Make sure you choose the availability domain where you want to receive
traffic.

Leave Image set to aella-modular-ds-6.x.x.

The Shape field lets you select from VMs with a variety of different
provisioning. Choose a shape that corresponds to the resources required by
the features to be enabled in this sensor's Sensor Profile.

 You can customize the CPUs and memory for many of the available
shapes by clicking Change shape and adjusting as necessary. For
example, we know we want to enable the Log Collector, Log Forward, and
Network Traffic features, so we've chosen the VM.Standard.E3.Flex shape
and adjusted its settings to the minimum values of 2 OCPUs and 8 GB of
memory.

Use the Networking options to select the Primary network and Subnet for the
sensor's management interface.

In most cases, you'll want to Assign a public IPv4 address to the
management interface. This lets you manage the sensor from a DP located
outside the OCI public cloud.

Use the Add SSH keys options to decide how you want to connect to the
sensor using SSH. We are letting OCI generate a key pair for us and saving
the resulting private key locally.

You can leave the other options set to their defaults.

The figure below shows our settings so far.

10. When you are satisfied with your settings, click Create to create the instance.

OCI begins to create the instance, tracking its progress in the Instance details | Work
requests display. Once the State shown in the Work requests table shows
Succeeded, as illustrated in the example below, you are ready to authorize the sensor
with a token. See below.

About MTU in Oracle Cloud Infrastructure

Compute instances in Oracle Cloud Infrastructure deploy with their MTU set to 9000 bytes. If you
are deploying the Modular Sensor together with a firewall (for example, a FortiGate firewall), you
can use the Sensor CLI to configure the sensor with an MTU of 1500 bytes to prevent
intermittent traffic drops.

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

Configuring a VTAP in OCI
There are many ways to configure traffic acquisition in OCI. In our example, we'll use the
following technique:

We'll create a VTAP in OCI that mirrors traffic from a specific host whose traffic we want
to monitor.

The mirrored traffic is sent to a Load Balancer in OCI that we'll also create.

We'll also create a capture filter for the VTAP to specify which traffic gets forwarded to
the Load Balancer.

One of the targets of the Load Balancer is the management interface of the Modular
Sensor.

Traffic sent from the Load Balancer to the management interface is encapsulated in
VXLAN packets, so we'll enable and configure the AWS Mirror feature for our
destination Modular Sensor in Stellar Cyber. As part of that configuration, we'll supply
the VXLAN network identifier (VNI) of the VTAP so that the VXLAN traffic is parsed
and the interior packets are read correctly by the sensor.

The procedures below show how to set up a deployment like this. Here's a summary of the
configuration we're going to create:

 You might also want to refer to Oracle Cloud's documentation for the VTAP feature .

Create the Load Balancer and Point it at the Sensor's Management
Interface

1. Click the main menu icon at the top left of the Oracle Cloud Console and select the

Networking | Virtual cloud networks option.

2. Click the Load balancers entry in the Networking menu at the left of the page. Then,
click the Create network load balancer button to add a new network load balancer.

 Make sure you create a network load balancer and not a regular load balancer.

Only a network load balancer can serve as the destination for mirrored traffic from a
VTAP.

3. Click Create load balancer.

4. Supply a name for the load balancer and select a network and subnet. Make sure you

select a network and subnet accessible to the modular sensor's management interface.
For example, in the screenshot below, we're setting up the network load balancer in the
same subnet as the modular sensor shown in the illustration at the start of this section
(subnet-c):

5. Click Next and configure a logical listener for the load balancer.

a. Supply a name for the listener.

b. Set the traffic type to UDP.

c. Set the Ingress traffic port to 4789.

For example:

6. Click Next to display the Select backends screen. This is where we'll point the load

balancer to the modular sensor VM's management interface.

7. Uncheck the Preserve source IP option and click the Add backends button.

8. Use the Compartment and IP address fields to select the management interface of the
modular sensor that we recorded during the installation of the sensor in the previous
sections. In this example, we're selecting the IP address of the Modular Sensor's
management interface shown in the illustration at the start of the section (10.205.3.16).

9. Click Add backends.

10. Select the new backend's entry in the Select backends list.

11. Health checks are mandatory for backends. To ensure successful health checks, you

must set the Protocol and Port fields to an open port on the Modular Sensor's
management port. Stellar Cyber suggests you use the default SSH port settings:

Protocol – TCP

Port – 22

12. Leave the Load balancing policy in the Advanced Options set to 5-tuple hash and

click Next.

13. Click Create network load balancer to finish the creation of the load balancer.

The new network load balancer appears in the list.

 You can click on the network load balancer's entry in the list to view a summary of its

configuration. If the Source/destination header (IP, port) preservation and/or Symmetric
hashing fields appear in this summary, ensure they are both set to disabled. If they are not,
return to the configuration of your backend and make sure the Preserve source IP option is
disabled.

Create the VTAP and Point it at the Load Balancer

1. Click the main menu icon at the top left of the Oracle Cloud Console and select the

Networking | VTAPs option.

2. Click the Create VTAP button.

3. Supply a name for the VTAP.

4. Select the VCN for the VTAP. This should be the VNC where the VM whose traffic you

want to monitor is located (oci-vcn in our example)

5. Use the Source fields to select the traffic the VTAP monitors. In this example, we're

tapping the traffic on a specific instance's VNIC in subnet-a:

Source type is set to Instance VNIC

Subnet is set to subnet-a. This is the subnet for the VM whose traffic we want
to monitor.

VNIC is set to the IP address of the instance we want to monitor 10.205.0.155
in this example).

Here's how the Source fields look for our example:

6. Use the Target fields to select where traffic monitored by the VTAP should be mirrored.

The destination is the Network load balancer we created in the previous section.
Here's how the Target fields look for our example:

7. Your VTAP must use a Capture filter. You can select an existing Capture filter or click
the dropdown and use the Create new capture filter option to add a new one. In our
example, we want all Ingress and Egress traffic. Here's how that filter looks as we
create it:

Here's our sample VTAP configured to send traffic from a specified VNIC to our load
balancer with our new capture filter:

8. Click Create VTAP to add the VTAP.

9. A summary screen appears for your VTAP. Locate the VXLAN network identifier field
and use the Copy button to save it in a text file. You will need to supply this identifier in
Stellar Cyber in the next section.

 If you want to ingest traffic from multiple VTAPs with one Modular Sensor, you can

assign the same VNI to each in OCI.

10. The VTAP does not start forwarding traffic until you click the Start button in the

screen shown above. Click Start to begin forwarding traffic from this VTAP.

Enable the AWS Mirror Feature for the Destination Modular Sensor

Traffic sent from the load balancer to the modular sensor's management interface is
encapsulated in VXLAN packets. You can configure the sensor to parse the VXLAN packets and
read the encapsulated packets by enabling the AWS Mirror feature on the sensor. Use the
following procedure:

 Although the feature is called AWS Mirror, it can be used to enable VXLAN parsing on a

sensor interface regardless of the actual source.

1. Log in to Stellar Cyber.

2. Go to System | DATA SOURCE MANAGEMENT | Sensors | Sensors. The Sensor

List is displayed.

3. Click  for the sensor used as the destination for the load balancer in OCI. The Edit

Data Sensor Parameters window is displayed.

4. Enable AWS Mirror. Additional fields are displayed.

5. Set Physical Ethernet Port to 0. This is the default interface number for the

Management Port on a Modular Sensor. You can verify interface assignments by using
the show vtep command on the sensor.

6. Leave Port set to its default value of 4789.

7. Set VNI to the VXLAN ID for your VTAP in OCI. You copied this from the VTAP's

summary screen in OCI in the previous section.

8. Click Submit. The parameters are immediately updated.

Verify Traffic

You can verify traffic flow from the monitored VM to the modular sensor's management port in the
Threat Hunting interface:

1. Log in to the Stellar Cyber console and navigate to the Threat Hunting page.

2. Set the Indices dropdown to Traffic.

3. Check the Sensors column in the table for traffic from the modular sensor used as the

destination for the VTAP.

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

