Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring SentinelOne Log Ingestion

To configure your SentinelOne endpoint protection system to send logs to Stellar Cyber:

 Use our example as a guideline, as you might be using a different software version.

 During installation, the timezone for sensors are automatically set to UTC+0. Since the logs
for some security products might only include the local time without a timezone, Stellar Cyber
recommends that you set the sensor timezone to the same timezone as your security
product.

1. Log in to SentinelOne.

2. Select INTEGRATIONS.

3. Select SYSLOG.

4. Enable SYSLOG.

5. For the Host, enter the IP address of the Modular Sensor.

6. For the port, enter 5175.

7. Optionally enable TLS.

If you do so, then under Certificate, select Upload. This sends the CA certificate for the
Select to SentinelOne.

8. For Formatting, choose CEF2.

9. Select Save.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

