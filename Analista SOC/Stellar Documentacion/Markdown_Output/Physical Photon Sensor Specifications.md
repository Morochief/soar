✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Physical Photon Sensor Specifications
This article describes both the performance you can expect from your physical Stellar Cyber
Photon sensors, as well as details on their physical provisioning.
Photon Sensor Performance Specifications
The table below summarizes the performance you can expect from your physical Photon
sensors.
 New physical sensors are shipped as modular sensors on Ubuntu 22.04.
|            | Supported        | Maximum Throughput | Maximum Throughput      |                                    |
| ---------- | ---------------- | ------------------ | ----------------------- | ---------------------------------- |
| Sensor     |                  |                    |                         | Log Forwarding (Events per Second) |
|            | Monitoring Ports | (Nominal Config*)  | (All Features Enabled*) |                                    |
| Photon 160 | 1 GbE            | Up to 2.0 Gbps     | Up to 1.4 Gbps          | 3984                               |
| Photon 250 | 1 GbE            |                    |                         | 4789                               |
|            |                  | Up to 5.0 Gbps     | Up to 2.5 Gbps          |                                    |
| Photon 400 | 10 GbE & 1 GbE   |                    |                         | 16206                              |
|            |                  | Up to 10.0 Gbps    | Up to 7.0 Gbps          |                                    |
 Keep in mind that log forwarding is handled by the Management port, by default. The other
sensor ports are used primarily for network capture, IDS, and Malware Sandbox purposes.
* About Sensor Throughput Performance
Sensor throughput performance corresponds directly to the features enabled in a sensor's
profile, as well as the type and rate of traffic processed. Actual performance may vary depending
on your environment and sensor configuration.
Maximum Throughput (Nominal Config) shows maximum aggregate ingestion with a
span port and local file assembly, packet forwarding, and log forwarding enabled. The
Network Traffic, Sandbox, and IDS features are not enabled.
Maximum Throughput (All Features Enabled) shows maximum aggregate ingestion
with a span port and all features enabled, including Network Traffic, Sandbox, and

IDS.
Photon Sensor Physical Specifications
The table below provides details on the physical provisioning of Stellar Cyber Photon sensors:
PHOTON-
|     | PHOTON-160 |     | PHOTON-400 |
| --- | ---------- | --- | ---------- |
250
| Maximum    | Up to 2.0 Gbps | Up to 5.0 | Up to 10.0 Gbps |
| ---------- | -------------- | --------- | --------------- |
| Throughput |                | Gbps      |                 |
(Nominal
Config)
Maximum
| Throughput (All |                | Up to 2.5 |                |
| --------------- | -------------- | --------- | -------------- |
|                 | Up to 1.4 Gbps |           | Up to 7.0 Gbps |
| Features        |                | Gbps      |                |
Enabled)
Network
|            | 6 x RJ45 (1Gbps) | 4 x GbE RJ45 | 6 x GbE RJ45 |
| ---------- | ---------------- | ------------ | ------------ |
| Interfaces |                  | MAC 2 x GbE  | 2 x 10G SFP+ |
RJ45
2 x GbE SFP
| CPUs | 4 physical cores | 16 physical | 16 physical cores |
| ---- | ---------------- | ----------- | ----------------- |
cores
| Memory | 16 GB (DDR4 2667 MHz) |               |                         |
| ------ | --------------------- | ------------- | ----------------------- |
|        |                       | 64 GB (2 x 32 | 64 GB (4 x 16 GB) (DDR4 |
|        |                       | GB) (DDR4     | 3200 MHz)               |
2666 MHz)
| Storage        | 238 GB                  | 512 GB | 480 GB       |
| -------------- | ----------------------- | ------ | ------------ |
| Console Access | RJ45 Console (COM) Port | RJ45   | VGA port and |
Console Port
USB keyboard or
iDRAC Virtual Console
(when licensed from Dell)
Size
|     | 7.32" x 4.98" x 2.60" | 9.10” x 7.87” | 17.08” x 1.68” x 28.13” |
| --- | --------------------- | ------------- | ----------------------- |
x 1.73”
| Weight | 3.025 lbs | 2.65 lbs | 38.9 lbs |
| ------ | --------- | -------- | -------- |
Power
|     | AC 100-240V | AC 100-240V | AC 100-240v   |
| --- | ----------- | ----------- | ------------- |
|     | DC 12V, 60W | DC 12V, 60W | DC 240v, 800W |
 Stellar Cyber has the discretion to modify external connectors, size, weight, and power of
any model noted above to accommodate enhancements that do not impact performance.

Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  