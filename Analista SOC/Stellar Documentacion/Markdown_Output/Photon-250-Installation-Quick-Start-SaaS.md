September, 2024

Photon 250 Installation &
SaaS Version

Installation & Quick Start

Quick Start Guide

50 with a SaaS DP. The SaaS DP
This document describes how to get started using the Photon 250 with a SaaS DP. The SaaS DP
This document describes how to get started using the Photon
is a cloud-based instance, hosted by
domain.

based instance, hosted by Stellar Cyber for your use on a *.stellarcyber.

Stellar Cyber for your use on a *.stellarcyber.cloud

The steps are as follows:

1.  Connect power.
2.  Connect the Photon 250 to the network.
Connect the Photon 250 to the network.
3.  Obtain an installation token from the Stellar Cyber GUI.
Obtain an installation token from the Stellar Cyber GUI.
4.  Access the Photon 250 CLI.
5.  Change the management port set
Change the management port settings.
6.  Apply the installation token in the CLI.
Apply the installation token in the CLI.

Connecting Power

To connect power to the appliance, have a licensed DC power technician:
To connect power to the appliance

1.  Connect the included power cable to the DC power source
Connect the included power cable to the DC power source.
2.  Connect the cable to the Photon 250.
Connect the cable to the Photon 250.
3.  Press the power button.

onnecting to the Network
Connecting to the Network

To connect the Photon 250 to the network:
To connect the Photon 250 to the network:

 Stellar Cyber, 2024. All rights reserved.

Photon 250 Installation & Quick Start (SaaS)

1.  Connect the management port (port 3) to a network accessible by the DP.
2.  Use ports 4 – 8 to connect to data sources (mirror ports or taps).

Obtaining an Installation Token

Stellar Cyber uses tokens to authorize and configure the installation of a sensor to be used with
a SaaS DP. Tokens point the installed sensor to the correct DP, assign the specified tenant, and
authorize the sensor installation.

Use the following procedure to obtain a token in the Stellar Cyber GUI:

1.  Navigate to the System | Deployment | Sensor Installation page and click on the

Tokens tab.

2.  If a token already exists for the target tenant for the sensor installation, you can either

use the Copy button to copy it to the clipboard or use the Download button to
download it as a file.

  Copy the token if you plan on applying it by pasting it into a set token string

<token> command in the CLI.

  Download the token as a file if you plan on hosting the file on an HTTP server

and referring to it in a set token url <token url> command.
3.  If there is not already an unexpired token for the target tenant, click the Generate

button.

4.  Select the tenant for the token from the Tenant dropdown. This is the tenant to which

all sensors authorized with this token will be automatically assigned. The dropdown lists
all tenants configured for your organization in the System | Tenants page.

5.  Click the Generate button. The system generates the token and displays its contents in
the Token field. The dialog also updates to display the expiration date for the token.
6.  You can use the Copy button to copy the token to the clipboard immediately, or simply

close the dialog and retrieve the token from the Tokens tab later on.

Accessing the Photon 250 CLI

You can access the appliance through the console port or using SSH.

Console Access

To access via console, connect an RJ45 serial cable to the RJ45 console port. Configure the port
settings to:
  Serial port speed: 9600
  Data Bits: 8
  Parity: None
  Stop Bits: 1
  Flow Control: None

2

Rev 02

Photon 250 Installation & Quick Start

SSH Access

The default management IP address on the appliance is 192.168.1.100/24, and the default
gateway IP address is: 192.168.1.1. The default username is aella and the password is
changeme.

For SSH access to the appliance:

ssh -l aella 192.168.1.100

Change the Management Port Settings

1.  You should still be logged in to your sensor from the previous procedure. If you are not,
log in now using either SSH or a console connection with the credentials you set in the
previous procedure.

2.  You can set IP parameters manually using commands similar to the following (substitute

your own IP parameters for the ones shown in bold below):
  set interface management ip 192.168.14.100/255.255.255.0
  set interface management gateway 192.168.14.1
  set interface management dns 8.8.8.8

3.  Verify the IP settings with the show interfaces command.

Applying the Token to the Sensor

Tokens are required to complete the installation of a sensor to be used with a SaaS DP.

1.  Apply the token to the installed sensor from the sensor CLI with the set token

command. The available techniques are as follows:

  Copy and Paste Token String – Copy the token string from the Tokens tab and

paste it into the CLI command. The syntax is as follows:
set token string <pasted string>

  Host Token on HTTP Server – Download the token as a file from the Tokens tab,
upload it to an HTTP server, and reference it in the set token command. The
syntax is as follows:
set token url http://<url to token>

2.  The CLI reports that the Sensor token is successfully set.

Note: If you receive an error message instead, it's possible that the token has expired.
Refer to the Tokens tab to see the expiration date. If you are using the File technique,
it's also possible that an extra space or line may have crept into your text file – check the
file to make sure it includes only the token text.

3.  Wait a minute or so. Then, verify that the token was successfully applied using any

combination of the following techniques:

  Check the System | Sensors tab in the user interface to see that the sensor has

registered itself successfully.

  Verify that the show system command shows all services as running.
  Verify that the show receiver command displays a receiver.

Rev 02

3

Photon 250 Installation & Quick Start (SaaS)

  Verify that the show json command reports some data sent in the BYTE_SENT

column.

Set the Timezone for the Sensor

You should use the Edit feature in the System | Sensors page to set the timezone for the
sensor.

During installation, the sensor timezone is automatically set to UTC+0. Since the logs for some
security products may only include the local time without a timezone, Stellar Cyber strongly
recommends that you set the sensor timezone to the same timezone as your security product.

4

Rev 02

