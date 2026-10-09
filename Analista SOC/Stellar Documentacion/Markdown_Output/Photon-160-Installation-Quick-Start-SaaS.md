September, 2024

Installation & Quick Start Guide
Photon 160 Installation & Quick Start Guide
Installation & Quick Start Guide
Token-Based Authorization

based
This document describes how to get started using the Photon 160 with token-based
This document describes how to get started using the Photon
based authorization is performed using a token downloaded from the
authorization. Token-based authorization is performed using a token downloaded from the
based authorization is performed using a token downloaded from the
Sensor Installation page.
managing Stellar Cyber server’s Sensor Installation

The steps are as follows:

  Connect power.
  Connect the Photon
Connect the Photon 160 to the network.
  Obtain an installation token from the Stella
Obtain an installation token from the Stellar Cyber GUI.
  Access the Photon 160
  Change the management port settings.
Change the management port settings.
  Apply the installation token in the CLI.
Apply the installation token in the CLI.

160 CLI.

Connecting Power

To connect power to the appliance, have a licensed DC power technician:
To connect power to the appliance, have a licensed DC power technician:
1.  Connect the included power cable to the DC power
Connect the included power cable to the DC power source.
2.  Connect the cable to the Photon
Connect the cable to the Photon 160.
3.  Press the power button.
Press the power button.

Connecting to the Network
Connecting to the Network

to the network:
To connect the Photon 160 to the network:
1.  Connect the management port (
Connect the management port (
2.  Use the
 6 monitor ports

 2..

) to a network accessible by the DP.
1) to a network accessible by the DP

sources (mirror ports or taps).
monitor ports to connect to data sources (mirror ports or taps)

 Stellar Cyber, 2024. All rights reserved.

Photon 160 Installation & Quick Start Guide (Token-Based Authorization)

Obtaining an Installation Token

Some Stellar Cyber deployments use tokens to authorize and configure the installation of a
sensor. Tokens point the installed sensor to the correct DP, assign the specified tenant, and
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

2

Rev 03

Photon 160 Installation & Quick Start Guide (Token-Based Authorization)

Accessing the Model 160 CLI

You can access the Model 160 using any of the following techniques:





HDMI monitor and USB keyboard
Serial console port
SSH to the eth0 Management port (

 1)

The USB and serial console ports are at the front of the appliance. The HDMI and eth0
Management ports are at the rear:

HDMI/USB Access

Connect an HDMI monitor to the HDMI port and a USB keyboard to one of the USB 3.0 ports.

Console Access

For console access use an RJ45 serial cable with the following settings:

  Baud: 115,200
  Flow control: none
  Data bit: 8
  Parity check: none
  Stop bit: 1

SSH Access

The default management IP address on the Photon 160 is 192.168.1.100/24, and the
default gateway IP address is: 192.168.1.1. The default username is aella and the
password is changeme.

For SSH access to the Photon 160:

ssh -l aella@192.168.1.100

Rev 03

3

Photon 160 Installation & Quick Start Guide (Token-Based Authorization)

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
4.  Use the set ntp command to specify the NTP server(s) to use for time synchronization.

Applying the Token to the Sensor

Use the following procedure to apply a token to a sensor.

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
  Verify that the show json command reports some data sent in the BYTE_SENT

column.

4

Rev 03

Photon 160 Installation & Quick Start Guide

Installation & Quick Start Guide (Token-Based Authorization)

Set the Timezone for the

 Sensor

You should use the Edit feature i
sensor.

in the System | Sensors page to set the timezon

ne for the

During installation, the sensor tim
security products may only include the local time without a timezone,
ezone to the same timezone as your security product.
recommends that you set the sensor timezone to the same timezone as your security product.
recommends that you set the sensor tim

may only include the local time without a timezone, Stellar Cy

automatically set to UTC+0. Since the logs for some

mezone is automatically set to UTC+0. Since the l

yber strongly

Understanding the Photon 160 LEDs
Understanding the Photon 160 LEDs

The Photon 160 includes power, hard drive, and network port status LEDs at the rear of the
The Photon 160 includes power, hard drive, and network port status LEDs at the rear of th
The Photon 160 includes power, hard drive, and network port status LEDs at the rear of th
sensor, as illustrated below.

Hard Drive and Power LEDs

The hard drive and power LEDs work as follows:
The hard drive and power LEDs work as follows:

Hard Drive LED

Power LED

OFF

OFF

Orange

OFF

Green

Green

Network Port Status LEDs

Meaning

Power is off

Device is loading at boot
Device is loading at boot

Device is fully powered on
Device is fully powered on

The network port status LEDs are the same for all network ports. The left LED is green and
The network port status LEDs are the same for all network ports. The left LED is green and
The network port status LEDs are the same for all network ports. The left LED is green and
indicates the speed of the connected link. The right LED is orange and blinks if a link is
indicates the speed of the connected link. The right LED is orange and blinks if a link is
indicates the speed of the connected link. The right LED is orange and blinks if a link is
connected.

Green (Speed) LED

Orange (Activity) LED

Meaning

OFF

OFF

ON

Rev 03

OFF

Blinking

Blinking

Not connected to network.
Not connected to network.

Connected to 100 Mbps link
Connected to 100 Mbps link

Device is connected to 1.0 or
Device is connected to 1.0 or
2.5 Gbps link.

5

Photon 160 Installation & Quick Start Guide

Installation & Quick Start Guide (Token-Based Authorization)

Front Power Button

The power button on the front of the Photon 160 also lights in blue when the sensor is powered
The power button on the front of the Photon 160 also lights in blue when the sensor is powered
The power button on the front of the Photon 160 also lights in blue when the sensor is powered
on, as illustrated below:

6

Rev 03

