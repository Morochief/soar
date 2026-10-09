Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Generic Log Capture

You can capture generic logs from your devices, which you can send to Stellar Cyber Customer
Success. Stellar Cyber can use these logs to generate a custom log parser for your device. Note
that Stellar Cyber cannot use these generic logs for generating alerts.

To send the logs to Stellar Cyber:

1. Configure your device to send logs to UDP port 5201.

2. Allow Stellar Cyber to collect a significant number (100 or more) of logs.

3. In Stellar Cyber, select Threat Hunting.

The Threat Hunting page appears with the Interflow Search tab open by default.

4. Set Indices as Syslog.

5. Search for dev_type:generic_capture.

Stellar Cyber displays the captured logs.

6. Select  to expand a record.

7. Scroll to raw and hover your cursor over its row.

8. Select Show column  in the set of options that appears to add raw to the columns.

This causes the Raw column to appear not just for this row but the entire table.

9. Change the Items per page to a number large enough to encompass all of the logs.

10. Click Export CSV to export the records.

11. Send the downloaded logs to Stellar Cyber Customer Success.

12. Configure your device to stop sending logs to port 5201.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

