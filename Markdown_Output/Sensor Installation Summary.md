Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Sensor Installation Summary

The overall installation procedure for a sensor image downloaded from the Stellar Cyber DP in
the System | DATA SOURCE MANAGEMENT | Sensors | Sensor Installation page
is very similar regardless of the sensor type and target environment. The overarching steps are
as follows:

1. Download the installation file(s) for your sensor type and environment in the Download

Image tab.

2. Install the image using the installation instructions for your environment.

3. Copy the token to be used for the authorization and configuration of the sensor from the
Tokens tab. You can copy it either as a string or a file, depending on how you want to
apply the token.

4. Apply the token to the installed sensor from the sensor CLI with the set token

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

5. The CLI reports that the Sensor token is successfully saved.

In addition, the CLI informs you that successful registration with the Stellar Cyber
Platform associated with the token is still pending. The hostname or IP address of the
associated Stellar Cyber Platform is included in the output.

 If you receive an error message instead, it's possible that the token has expired.

Refer to the Tokens tab to see the expiration date. If you are using the File
technique, it's also possible that an extra space or line may have crept into your text
file – check the file to make sure it includes only the token text.

6. Wait a minute or so. Then, verify that the token was successfully applied using any

combination of the following techniques:

Check the System | DATA SOURCE MANAGEMENT | Sensors | Sensors
list in the user interface to see that the sensor has registered itself
successfully.

Verify that the show system command shows all services as running.

Verify that the show receiver command displays a receiver.

Verify that the show json command reports some data sent in the BYTE_SENT
column.

Check the Status in the show cm output.

Check the Ctrl Plane Status in the show version output.

Refer to the installation topic specific to your sensor type and target environment for details.

Using Photon (Hardware) Sensors
You can also use Photon (hardware) sensors from Stellar Cyber with the cloud-based
solution. Refer to PDF Installation Guides for information on installing a physical Photon
sensor.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

