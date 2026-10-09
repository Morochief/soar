Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring AWS Port Mirroring

You can configure AWS mirroring to monitor traffic from a single mirrored port. You must
configure the mirror port on AWS before you configure Stellar Cyber.

To configure AWS port mirroring:

1. Configure traffic mirroring on AWS  . Take note of:

The VXLAN UDP port number (4789 is the default AWS port)

The VNI, which is the VXLAN ID

Limitations on the instance types supported for traffic mirroring .

When you configure AWS:

Keep the mirror source and target in the same VPC.

Per the AWS traffic mirroring instructions, you must create a traffic mirror
filter  with one or more traffic mirror rules to define the traffic to be mirrored.
You cannot leave the traffic mirror filter empty.

When you create the Traffic Mirror Filter, do not choose any network
services.

The Traffic Mirror Target must be Network Interface.

The Traffic Mirror Session target must be the data sensor interface.

The Traffic Mirror Session number must be 1.

Leave the Traffic Mirror Session Packet Length at the default value.

Do not mirror to an interface running DPDK.

Ensure that your configuration does not create a loop within AWS.

Do not mirror from a source host that sends traffic directly to a destination
interface, as the data sensor might get duplicate traffic.

2. Log in to Stellar Cyber.

3. Go to System | DATA SOURCE MANAGEMENT | Sensors | Sensors. The Sensor

List is displayed.

4. Click  for the data sensor you want to send the traffic to. The Edit Data Sensor

Parameters window is displayed.

5. Enable AWS Mirror. The additional fields are displayed.

6. Enter the Physical Ethernet Port index number. You can find this by using the show

vtep command on the sensor.

7. Enter the VXLAN UDP port number from AWS.

8. Enter the VNI, which is the VXLAN ID you configured in AWS.

9. Click Submit. The parameters are immediately updated.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

