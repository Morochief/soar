✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Installing a Modular Sensor in Azure
This topic describes how to install a Modular Sensor in a Microsoft Azure environment. Refer to
the following sections for details:
About Modular Sensors
Site Preparation
Authorizing and Installing the Stellar Cyber Software Images
Applying a Token to the Installed Sensor
Configuring a Static IP Address (Optional)
Enabling SSSE3 for the Sensor VM
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
Click to see the minimum system requirements for installing a modular sensor. Then, select an
Azure instance type that meets the stated requirements for your expected sensor workload.
The Azure instance types in the script provided below use the instance type listed below:
 Keep in mind that these are example instance types that meet the requirements stated in
Server Sensor Sizing Specifications. You can select other instance types with the
necessary vCPUs and RAM to perform your expected workload, as stated in the system
requirements.
Modular Sensor – Standard_D16ls_v5
 Before running the installation script, confirm that your Azure subscription has
sufficient DLSv5-series vCPU quota allocated in the target region. Request a
quota increase through the Azure portal at Subscriptions > Usage + quotas if
needed. Deployment with the Standard_D16ls_v5 VM will fail if the required quota
is unavailable.
To prepare for the installation:
1. Open firewall ports for log ingestion.
2. Open firewall ports for the features you plan on enabling in the Modular Sensor Profile
for this sensor.
Request the Sensor Software Image from Stellar Cyber
Contact Stellar Cyber support (support@stellarcyber.ai) to have the sensor images deployed in
your region.

 Do this at least a day before installing, so we have enough time to deploy the images to
your region.
You will need to provide the following information as part of your request:
The Azure region for the sensors your are installing.
The version of your Stellar Cyber platform.
The sensor version required.
 Stellar Cyber support will help you determine the sensor version you need.
You must replace the "<sensor_version>" in the variable section of the sample
installation script with the actual version you are installing (for example,
$imageVersion = "6.6.0").
Supported Azure Regions
Click here to see a list of the supported Azure regions:
Stellar Cyber supports the following Azure regions:
Geography Region
Asia Pacific Southeast Asia
Brazil Brazil South
Canada Canada Central
Europe North Europe
Europe West Europe
Germany Germany West Central
Israel Israel Central
Japan Japan East
United Kingdom UK South
United Kingdom UK West
United States Central US
United States East US
United States East US 2
United States North Central US
United States South Central US
United States West Central US
United States West US

Geography Region
United States West US 2
United States West US 3
Authorizing and Installing the Stellar Cyber Software
Images
You must authorize the Stellar Cyber software images so that they are available in the Azure
portal:
 Use our example as a guideline, as you might be using a different software version.
1. Log in to your Azure portal at https://portal.azure.com/ . The Dashboard appears.
2. Click Azure Active Directory. The Overview appears.
3. Click Properties.
The Properties page appears.
4. Copy the Tenant ID.
You need the Tenant ID both in the following step and later in the procedure.

5. Put your Tenant ID in the following URL and paste it in your browser:
https://login.microsoftonline.com/<tenant id>/oauth2/authorize?client_id=58238038-
43b4-4446-8260-
0fa97ace1085&response_type=code&redirect_uri=https%3A%2F%2Fwww.microsoft.co
m%2F
The Permissions requested message appears.
6. Click Consent on behalf of your organization.
7. Click Accept.
8. Click Enterprise Applications.
The Enterprise applications | All applications page appears.
9. Search for Stellar. The Stellar Cyber applications that you authorized appear.
If you don't see any Stellar Cyber applications, contact Stellar Cyber support.
10. You can either create a new Resource Group for the deployment or deploy into an
existing group. Use this step to create a new Resource Group. Otherwise, you can skip
to the next step.
a. Click Resource Groups.
The Resource groups page appears.

b. Click Add. The Create a resource group page appears.
c. Choose your Subscription.
d. Enter the name of your group in the Resource group field.
e. Choose the Region where you want to deploy the resource. Here's how our
resource group looks so far:
f. Click Review  create.
g. Click Create. The resource group is created and the Resource groups page
appears.
11. Click the name of the resource group where you want to deploy the sensor. This is
either the resource group you just created or an existing resource group.
The group details appear.
12. Click Access control (IAM).
The Access control (IAM) page appears.
13. Click Add role assignments to display the Add role assignment controls.

14. Click on Privileged administrator roles and choose the Contributor option, as
illustrated below:
15. Leave the default selection of User, group, or service principal in the Assign access
to dropdown.
16. Enter Stellar in the Select field. The available Stellar Cyber software packages appear.
17. Choose Stellar Cyber Software Packages.
18. Click Save. The Resource groups page appears again.
19. Click Home. The Azure services page appears.
20. Click Subscriptions. The Subscriptions page appears.
21. Choose your subscription. The subscription details appear.
22. Click Resource providers.

The Resource providers page appears.
23. Select Microsoft.Network.
24. Click Register.
25. Select Microsoft.Compute.
26. Click Register.
27. Click Cloud Shell.
28. Select the PowerShell option in the dialog box that appears:
29. Create an inbound security group for the sensor using the commands below, replacing
<resource-group> with the name of your resource group and <NSG NAME> with the
name of your network security group:
a. Create the Network Security Group:
az network nsg create -g <resource-group> -n <NSG NAME>
b. Add an inbound rule for SSH (TCP 22), replacing <Trusted CIDR> with the
trusted CIDR range that can SSH into the sensor (for example, 8.8.8.8/32):
az network nsg rule create -g <resource-group> --nsg-name <NSG
NAME> -n AllowSSH --direction Inbound --protocol Tcp --source-
address-prefixes '<Trusted CIDR>' --source-port-ranges '*' --
destination-address-prefixes '*' --destination-port-ranges 22 -
-access Allow --priority 500
c. Add an inbound rule for UDP port 8472, replacing <Trusted CIDR> with the
trusted CIDR range where the DP is deployed:
 You can skip this step if you're not using VxLAN forwarding.

az network nsg rule create -g <resource-group> --nsg-name <NSG
NAME> -n AllowUDP4872 --direction Inbound --protocol Udp --
source-address-prefixes '<Trusted CIDR>' --source-port-ranges
'*' --destination-address-prefixes '*' --destination-port-
ranges 8472 --access Allow --priority 600
30. You use a customized version of the script shown in Azure Installation Script to install
a Modular Sensor in Azure. Before you use the script, you must customize it with
variable definitions that match your Azure subscription and networking environment.
a. Start by pasting the contents of the Azure Installation Script into a text editor.
b. Customize the script with variable definitions that match your Azure
subscription and networking environment for the items listed in Variables for
the Azure Installation Script .
c. Copy and paste the customized script into the Azure Cloud Shell to create the
Modular Sensor.
 Refer to this article for more information on the New-AzVM cmdlet  used by the
script to install a Modular Sensor VM.
31. Once you have finished installation, you can clean up by removing Stellar Cyber
Software Packages from the target resource group.
Azure Installation Script
Paste the contents of this script into a text editor and supply your own values for the variables
shown in angle brackets ("<variable>"). The necessary variables are listed and described in
Variables for the Azure Installation Script.
 Before running the installation script, confirm that your Azure subscription has sufficient
DLSv5-series vCPU quota allocated in the target region. Request a quota increase through
the Azure portal at Subscriptions > Usage + quotas if needed. Deployment with the
Standard_D16ls_v5 VM will fail if the required quota is unavailable.
1 # Only suppress breaking change warnings
2 Set-Item -Path Env:\SuppressAzurePowerShellBreakingChangeWarnings -Value
3 "true"
4 Clear-AzContext -Force
5 #Supply your own values for the variables below:
6 $resourceGroup = "<resource_group_name>"
7 $location = "<region_name>"
8 $vmNamePrefix = "StellarVM-Sensor"
9 $vnetName = "<vnet_name>"
10 $subnetName = "<subnet_name>"
11 $nsg_name = "<nsg_name>"
12 $tenant_customer = "<customer_tenant_id>"
13 $subscription_customer = "<customer_subscrption_id>"
14 #change stellarInstanceType to install Modular Sensor or DP
15 $stellarInstanceType = "Stellar-ModularSensor-Gen2"
16 #$stellarInstanceType = "Stellar-DataProcessor"
17 #install the specified version below
18 $imageVersion = "<sensor_version>"
19
20 ############################################################################
21 #Stellar Cyber parameters, do not change
22 $applicationId = '58238038-43b4-4446-8260-0fa97ace1085'
23 $secret = 'mdb8Q~2-lm0jpEF_lm24K52udUCKZDrD05e_wdmk' | ConvertTo-SecureString
24 -AsPlainText -Force
25 $tenant_stellar = "2f580e30-1cc1-4c08-9e80-704999508e1a"
26 ############################################################################
27

| 28  | if ($stellarInstanceType -eq "Stellar-DataProcessor") { |     |
| --- | ------------------------------------------------------- | --- |
| 29  |     $osDiskSize = 512                                   |     |
| 30  |     $osVMSize = "Standard_E16s_v3"                      |     |
| 31  | }else{                                                  |     |
| 32  |     $osDiskSize = 128                                   |     |
| 33  |     $osVMSize = "Standard_D16ls_v5"                     |     |
| 34  | }                                                       |     |
35
| 36  | try { |     |
| --- | ----- | --- |
37     $cred = New-Object -TypeName PSCredential -ArgumentList $applicationId,
| 38  | $secret |     |
| --- | ------- | --- |
39     Connect-AzAccount -ServicePrincipal -Credential $cred -Tenant
| 40  | $tenant_stellar |     |
| --- | --------------- | --- |
41     Connect-AzAccount -ServicePrincipal -Credential $cred -Tenant
| 42  | $tenant_customer |     |
| --- | ---------------- | --- |
43     Set-AzContext -Subscription $subscription_customer -Tenant
| 44  | $tenant_customer |     |
| --- | ---------------- | --- |
45
| 46  |     # Get the specific subnet object |     |
| --- | ------------------------------------ | --- |
47     $vnet = Get-AzVirtualNetwork -ResourceGroupName $resourceGroup -Name
| 48  | $vnetName |     |
| --- | --------- | --- |
49     $subnet = Get-AzVirtualNetworkSubnetConfig -Name $subnetName -
| 50  | VirtualNetwork $vnet       |     |
| --- | -------------------------- | --- |
| 51  |     # Get subnet ID        |     |
| 52  |     $subnetId = $subnet.Id |     |
53
54     $randomString = [guid]::NewGuid().ToString("N").Substring(0, 8)
| 55  |     $vmName = "StellarVM-Sensor-$randomString" |     |
| --- | ---------------------------------------------- | --- |
56
| 57  |     $image = "/subscriptions/0e28f851-f477-4f2d-94bc- |     |
| --- | ----------------------------------------------------- | --- |
58 35c00d3d5fd8/resourceGroups/Stellar/providers/Microsoft.Compute/galleries/Stel
59 larCyberSoftwares/images/$stellarInstanceType/versions/$imageVersion"
60
| 61  |     #Networking pieces |     |
| --- | ---------------------- | --- |
62     $pip = New-AzPublicIpAddress -ResourceGroupName $resourceGroup -Location
63 $location -Name "mypublicdns$(Get-Random)" -AllocationMethod Static -
| 64  | IdleTimeoutInMinutes 4 |     |
| --- | ---------------------- | --- |
65     $nsg = Get-AzNetworkSecurityGroup -Name $nsg_name -ResourceGroupName
| 66  | $resourceGroup                               |     |
| --- | -------------------------------------------- | --- |
| 67  |     $nic_name = "Stellar-nic-$randomString"  |     |
Variables for the Azure Installation Script
68     $nic = New-AzNetworkInterface -Name $nic_name -ResourceGroupName
69 $resourceGroup -Location $location -SubnetId $subnetId -PublicIpAddressId
70 $Ypoiup w.Iildl  n-eNeedt wtoo rskuSpepcluyr viatlyuGerso ufoprI dth e$ nvsagr.iaIbdles in the table below in the Azure
71
72  In s t a#lClarteiaotne  Sac rvipirt tbueaflo rema ycohui nues ec oitn ifni tghuer aAtziuorne  Cusloiundg  Sthhee ll$. iKmeaegpe  inv amriinadb lthe eto
| 73  | specify the image |     |
| --- | ----------------- | --- |
74  fo l lo w$vinmgC ornufleisg  fo=r  Nveawri-aAbzlVeMsC:onfig -VMName $vmName -VMSize $osVMSize |
75         Set-AzVMOperatingSystem -Linux -ComputerName $vmName -Credential $cred
| 76  | |   |     |
| --- | --- | --- |
The specified resourceGroup must already exist.
| 77  |         Set-AzVMSourceImage -Id $image |         |     |
| --- | ------------------------------------------------ | --- |
| 78  |         Set-AzVMOSDisk -CreateOption FromImage ` |     |
79  T h e   v a l u e s  y o u   s u p p l y  f o r  t-hDei svknSeitzNeaImneG,B  s$uobsnDeitsNkaSmieze,  a`nd nsg_name arguments must
| 80  |                         -Caching ReadWrite `                                           |     |
| --- | -------------------------------------------------------------------------------------- | --- |
| 81  |  e x i s t  in   th e   s p e c i fi e d   re s o u -rcNea mger o"u$pv.mName-OSDisk" ` |     |
82                         -StorageAccountType "StandardSSD_LRS" |
83         Add-AzVMNetworkInterface -Id $nic.Id The imageVersion must match the sensor version deployed to your account by Stellar
84     $vmConfig = Set-AzVMSecurityProfile -VM $vmConfig -SecurityType
| 85  | "CTyrbusetr esduLpapuonrcth." |     |
| --- | ----------------------------- | --- |
86     $vmConfig = Set-AzVMUefi -VM $vmConfig -EnableVtpm $true -EnableSecureBoot
| 87  | $false                        |     |
| --- | ----------------------------- | --- |
| 88  |     #Create a virtual machine |     |
89     New-AzVM -ResourceGroupName $resourceGroup -Location $location -VM
| 90  | $vmConfig |     |
| --- | --------- | --- |
| 91  |           |     |
92
| 93  | } finally { |     |
| --- | ----------- | --- |
94     ##########################################################################
| 95  | ##                                                    |     |
| --- | ----------------------------------------------------- | --- |
| 96  |     # CLEANUP - Always runs, even if deployment fails |     |
97     ##########################################################################
| 98  | ##  |     |
| --- | --- | --- |
99     Write-Host "Cleaning up Azure connections..." -ForegroundColor Yellow
| 100 |      |     |
| --- | ---- | --- |
    # Disconnect Azure PowerShell
In st a ll atDioins cSocrnipnte Vcatr-iaAbzleAccount -DSecfoinpiteio nCurrentUser -ErrorAction SilentlyContinue | Out-Null

    # Clear Azure contexts
$resourceGroup The name of the Azure Resource Group where the Modular Sensor will be installed.
    Clear-AzContext -Force -Scope CurrentUser -ErrorAction SilentlyContinue | Out-
Null
$l o ca t ioCnlear-AzContext -Force Th-eS Aczoupree  RPergoiocne wshse re- tEhrer MoordAuclatr iSoenns oSri wlilel bnet linysCtaollendt.inue | Out-Null

|         #  | C l e a r   A | z u r e   C L I |
| ---------- | ------------- | --------------- |
Optional. The Modular Sensor VM is named with this prefix followed by a random
| $v     az logout 2>$null m N a m | eP r e fix   =  "S | t e lla r V M -S e nsor" |
| -------------------------------- | ------------------ | ------------------------ |
    az account clear 2>$nulstlring (by default, StellarVM-Sensor-<random-string>). You can rename the VM

    # Clear cached tokens
    Remove-Item -Path "$env:USERPROFILE\.Azure\TokenCache.dat" -Force -ErrorAction

SilentlyContinue
In st a ll atRioenm oSvcreip-tI Vtaermia b-lePath "$enDve:fUinSitEioRnPROFILE\.Azure\AzureRmContext.json" -Force -
ErrorAction SilentlyContinue
within Azure after it is deployed. However, if you would prefer a different default prefix,
# Clear sensitive variables from memory
$secret = $null you can change it here.
$cred = $null
[System.GC]::Collect()
$v n e tN ame The name of the virtual network for the Modular Sensor. You can use the az network
Write-Host "Cleanup complete!" -ForegroundColor Green
} vnet list command to see available virtual networks.
$subnetName The name of the subnet for the Modular Sensor. You can use the az network vnet
subnet list command to see the subnets in a virtual network.
$nsg_name
The name of the Network Security Group for the Modular Sensor. You can use the az
network nsg list command to see available Network Security Groups.
$tenant_customer The Azure tenant ID for the deployment. You can use the az account list --output
table command to see the subscription and tenant IDs available for your account.
$subscription_customer The Azure subscription for the deployment. You can use the az account list --
output table command to see the subscription and tenant IDs available for your
account.
$imageVersion The Stellar Cyber Sensor version you are installing. This must match the sensor version
deployed to your account by Stellar Cyber support.
 Stellar Cyber support will help you determine the sensor version you need. For
example:
$imageVersion = "6.6.0"
 The sensor version for the installation script does not include an "s" at the end,
even if your DP version does.
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
Option 1. Copy and Copy the token string from the Tokens tab and paste it into the CLI command. The
Paste the Token String syntax is as follows:
set token string <pasted string>
Option 2. Host the Token Download the token as a file from the Tokens tab, upload it to an HTTP server, and
on an HTTP Server reference it in the set token command. The syntax is as follows:
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
Enabling SSSE3 for the Sensor VM
The sensor VM must have SSSE3 enabled for its processors in order for the Modular Sensor to
operate correctly. In most cases, SSSE3 will already be enabled. However, if you encounter
issues with packet collection or Interflow data generation, you can use the instructions below to
ensure that SSSE3 is enabled.
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
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  