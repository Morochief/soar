Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring a Data Aggregator

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M03 Modular Sensor Concepts and Configuration (08h:56m)  

Modular Sensor Aggregator (21m:00s)

Learn how to configure the Modular Sensor Aggregator to consolidate data streams
from multiple sensors into the Stellar Cyber Platform. Follow a demonstration of setting
up aggregation settings and validating data flow, and explore how aggregation optimizes
throughput for efficient processing and threat detection.

The first time you access a link on the portal during a session, you must log in to access
content.

If you have firewalls between your data sensors and the data processor (DP), you must open
ports on each firewall to allow the sensors to reach the DP. You can install a data aggregator to
collect TCP traffic from the sensors and send it to the DP. This limits the number of ports you
need to open on the collecting sensor. In a deployment like this, most ports only need to be open
between the aggregator and the DP. The aggregator acts as a proxy to forward traffic from other
sensors to the DP.

 Important: Stellar Cyber recommends that you deploy an aggregator using a Modular
Sensor with the Aggregator feature enabled in its Sensor Profile rather than using the
purpose-built aggregator image. Installation of aggregators using the purpose-built images is
officially a deprecated feature, although the images are still available.

You must open ports on the firewall to allow the:

Aggregator to reach the DP and other sensors
DP to communicate with the aggregator
Sensors to communicate with the internet and the aggregator

 The aggregator is a single point of failure for your sensors. We strongly recommend that you

install and configure a secondary aggregator.

When you install the aggregator, the DP automatically discovers it, as with any sensor, and lists it
in the System | DATA SOURCE MANAGEMENT | Sensors | Sensors list.

 If you have a sensor that cannot connect to the DP, use the set aggregator command to

add up to two aggregators to the sensor.

Configuring the Aggregator
Configuring an aggregator consists of the following steps, each of which is described in detail
below the summary:

1. Create a Modular Sensor profile for the aggregator in the System | DATA SOURCE

MANAGEMENT | Sensor Profiles tab. Ensure that the Aggregator feature is enabled
in the Modular Sensor profile.

2. Assign the Modular Sensor profile to the sensor to be used as an aggregator.

3. Configure each sensor to use the aggregators.

Creating a Modular Sensor Profile with the Aggregator Feature Enabled

1. Select System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles.

The Sensor Profile Configuration page appears.

2. Select Create and then select Add Modular Sensor Profile.

The ADD SENSOR PROFILE screen appears.

3. Enter the Profile Name.

Stellar Cyber recommends that you establish a naming convention so you can easily
understand the intent of each profile by looking at the name. This field can only contain
alphanumeric characters, underscores, spaces, and dashes.

4. Choose at least one Receiver. Each sensor profile must have at least one receiver,

which is the destination of the data it collects.

 See the Receiver configuration page for more information on creating and

maintaining receivers. Keep in mind that Modular Sensors only use JSON receivers.
They do not use Packet receivers.

5. Customize the settings for the profile.

Since we will use this profile to configure modular sensors as aggregators, we must
make sure the Aggregator feature is enabled, as in the figure below:

 Refer to Configuring Modular Sensor Profiles for details on the different

Modular Sensor feature available in a profile.

6. Select Submit.

The profile is active immediately.

Assigning a Modular Sensor Profile to a Sensor

To assign a Modular Sensor profile to a sensor:

1. Navigate to the System | DATA SOURCE MANAGEMENT | Sensors page.

2. Select the sensor icon

 to edit its settings.

The Edit Sensor Parameters dialog box appears.

3. Use the Sensor Profile dropdown to assign the Modular Sensor profile with the
Aggregator feature enabled that you configured in the previous procedure.

4. Select Submit.

The profile is immediately assigned to that aggregator.

Configuring Sensors to Use an Aggregator
To configure a sensor to use an aggregator:

1. Click on System | DATA SOURCE MANAGEMENT | Sensors | Sensors.

The Sensor list appears.

2. Select

 to edit a sensor.

The Edit Sensor Parameters screen appears.

3. Choose a Primary Aggregator from the dropdown.

4. Choose a Secondary Aggregator from the dropdown.

 The Secondary Aggregator dropdown doesn't appear until you've assigned a

Primary Aggregator.

5. Select Submit.

The sensor immediately starts sending traffic to the primary aggregator.

When you finish configuring all of the sensors, you can remove the associated open ports from
your firewall.

 You can also configure sensors to use an aggregator in the Sensor CLI with the set

aggregator <ip address> command.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

