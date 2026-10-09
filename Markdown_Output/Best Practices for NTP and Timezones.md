Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Best Practices for NTP and Timezones

Stellar Cyber strongly recommends the following best practices for configuration of time settings
on your sensors:

Set the Timezone for Sensors

Enable NTP for Device Sensors

Set the Timezone for Sensors
Stellar Cyber recommends that you set the timezone for all device sensors from the Sensor List.

During installation, the timezone for sensors are automatically set to UTC+0. Since the logs for
some security products may only include the local time without a timezone, Stellar Cyber
strongly recommends that you set the sensor timezone to the same timezone as your
security product.

Stellar Cyber converts all log timestamps to UTC during log ingestion. Timezones are handled as
follows:

If a log includes the timezone, Stellar Cyber preserves that time setting during the
conversion to UTC.

If a log does not include a timezone, Stellar Cyber uses the timezone of the receiving
sensor.

Enable NTP for Device Sensors
Stellar Cyber recommends that you configure your device sensors to use NTP  to ensure
accurate timestamps in records.

 You only need to do this for physical device sensors and virtual sensors deployed in private

clouds. Device sensors deployed in public clouds (AWS, Azure, OCI, and so on)
automatically use the time synchronization service provided by the public cloud vendor.
Server sensors use the time settings for the server hosts on which they are installed.

You can use the set ntp command from the Sensor command line to enable NTP and specify
the time server to be used for synchronization.

 Keep in mind that configuring an NTP server does not set the sensor's timezone. That's why

you need to do both!

Common Issues with NTP Configuration

Some NTP clients may refuse to synchronize the time when the difference between host's time
and server's time are too great (for example, over 1000 seconds). This is sometimes reported as
an NTP Refusing to Sync error.

If you encounter a situation where your sensor seems unable to synchronize its time with the
configured NTP server, try setting the local time for the sensor manually. You can use the set
time command from the sensor's CLI to do this. Once the sensor's local time is once again
within the range of normalcy with the NTP server, time synchronization should work successfully.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

