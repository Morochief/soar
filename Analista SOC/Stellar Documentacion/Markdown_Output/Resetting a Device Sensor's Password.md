Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Resetting a Device Sensor's Password

This topic describes how to work with the Stellar Cyber Customer Success team to reset a lost
password for a Stellar Cyber device sensor. This topic applies to both physical and virtual
sensors.

 This procedure is not yet supported for sensors deployed in Google Cloud Platform.

Use the following procedure to reset a sensor's password:

1. Access the serial console for the sensor.

For sensors installed in a VMware environment, you can use the remote
console tool available in the vSphere Client.

For sensors installed in Azure, you can use the Azure Serial Console. Refer to
this article for details  on how to establish a connection using the Azure
Serial Console.

For physical sensors, refer to the PDF Installation Guides for details on
establishing a serial console connection.

2. When you establish a serial console connection to a sensor, the first thing you see is
the AOS version and the Machine ID for the sensor, as illustrated below. If you do not
see these items, press Enter a few times to display them.

 Leave the window showing the Machine ID and AOS version open. You will need to
provide these values to the Stellar Cyber Customer Service team in the next step.

3. Contact the Stellar Cyber Customer Success team , ask for assistance with a lost
password, and supply the Machine ID and AOS version you retrieved in the previous
step. The Customer Success team will use this information to provide you a temporary
password for the sensor.

4. Log in to the sensor with the following credentials:

Login – resetpassword

Password – <provided by Customer Success team>

Once you have successfully logged in using the temporary password, the local
password for the default aella account is reset to its initial value of changeme. The
system requires you to exit by pressing any key.

5. Log in to the sensor using the login of aella and the default password of changeme.

The system will guide you through a mandatory password reset for the aella account.

Log File Entries for Password Changes
The sensor records all password changes to the /var/log/aella/resetpassword.log file.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

