Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Provisioning Disk Space for Virtual Modular
Sensors

In order to guarantee the performance of your virtual modular sensors, you must provision
sufficient disk space using the instructions in this topic.

The disk space required by a sensor varies depending on the features enabled, expected
data/log volume, number of configured IDS rules, and buffer settings in the Modular Sensor
Profile. The most important factors affecting sensor disk size requirements are as follows:

Enabled Features/Modules – Each module enabled in the Modular Sensor Profile (for
example, log forwarder, IDS, aggregator, sandbox, network traffic) increases disk
requirements. More features running simultaneously require more disk space.

Buffer Settings – The buffer sizes configured in the Modular Sensor Profile for logs,
network traffic, and IDS directly affects disk usage. Larger buffer settings mean more
disk space is needed to store temporary data.

Log and Data Volume – Higher log volume and network traffic increase the amount of
data written to disk, requiring more space for storage and buffering.

Sandbox Activity – Intensive sandboxing or many short sessions can cause disk
usage spikes, requiring extra disk capacity.

To determine an appropriate disk size for your sensor:

1. Start with the default disk size for a Modular Sensor of 76 GB.

 You can't change the disk size for a Modular Sensor below the default of 76 GB.

2. Add the sizes specified in your selected Modular Sensor Profile for the Log Forwarder

Buffer, Network Traffic Buffer, and IDS Buffer options.

3. Provision additional disk headroom based on your expected log/data volume, bursty

traffic environments, and expected sandbox activity. Fine-tune based on your retention
goals, local peaks, and IDS rule set size.

For a Modular Sensor with all features enabled and the Log Forwarder, Network Traffic,
and IDS buffers all configured to their maximum values of 32 GB, Stellar Cyber recommends the

following:

   76 GB Default Disk Size
   32 GB Log Forwarder Buffer
   32 GB Network Traffic Buffer
   32 GB IDS Buffer
+ 100 GB Additional Disk Size
----------------------------------
  272 GB Total Disk Size Required

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

