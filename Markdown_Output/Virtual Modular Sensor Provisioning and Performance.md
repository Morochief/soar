✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Virtual Modular Sensor Provisioning and
Performance
This article describes the resources required for the successful installation and operation of
Stellar Cyber virtual modular sensors. Virtual modular sensors install as dedicated VMs with
Stellar Cyber software pre-installed.
Refer to the following sections for details:
What Determines Sensor Performance?
Sensor Provisioning Rules
Sensor Provisioning by Module
What Determines Sensor Performance?
Virtual modular sensor performance depends on the following key factors:
Allocated VM resources (CPU and Memory). Sensor performance scales with CPU and
RAM.
Enabled features (Log Forwarder, Network Traffic, Sandbox, and IDS).
Traffic volume (both peak and sustained events per second, connections per second,
and bandwidth usage).
 More features, deeper inspection, and more traffic always require more CPU and RAM.
Sensor Provisioning Rules
Guarantee your virtual modular sensor performance by following these rules for sensor
provisioning:
Reserve CPU and memory resources in the hypervisor.
Enable SS3 for Linux-based sensors.
Use ≥2.1 GHz processors for validated performance.

Provision at least 1.5 times as much memory as the number of CPU cores to ensure
stable performance. So, for example, if you provision 8 CPUs, you should provision at
least 8 x 1.5 = 12GB of memory.
Provision sensor disk space using the rules in Provisioning Disk Space for Virtual
Modular Sensors.
Stellar Cyber limits the number of log sources you can point at a given sensor as
follows:
Sensors with 8 GB or less of memory accept a maximum of 100 log sources.
Sensors with more than 8 GB of memory accept a maximum of 200 log
sources.
 Log sources beyond the limit are aggregated under the special source IP address
of 0.0.0.0.
 As a simple rule, more traffic and inspection depth require more CPU and memory.
Sensor Provisioning by Module
Stellar Cyber provides virtual modular sensors using specific modules. This section lists the
provisioning you must provide to achieve the performance for your purchased module. See the
sections below for details.
 Stated specifications support the corresponding maximum network traffic inspection
throughput. Performance may vary depending on your environment, configuration, and other
variables.
Network-Module Sensor Specifications
The Network-Module sensor specifications assume a span port, local file assembly, packet
forwarding, log forwarding, and Network Traffic. The Malware Sandbox and IDS features are not
enabled.
Virtual machines for the Network-Module sensors must be provisioned as follows:
Component Network-Module-1G Network-Module-10G
Virtual Cores (reserved) 8 32
RAM (GB) (reserved) 16 64
Maximum throughput (Gbps) Up to 1.0 Up to 10.0
(1 or 2 span ports)
Log Forwarder Events/s 7,000 10,000
Security-Module Sensor Specifications – IDS Only
The Security-Module IDS sensor specifications assume a span port, local file assembly, log
forwarding, Network Traffic, and IDS. The Malware Sandbox feature is not enabled.
Virtual machines for the Security-Module sensors must be provisioned as follows:

Security-Module-200M Security-Module 500M Security-Module 1G Security-Module 10G
Component
|                          | IDS       | IDS       | IDS         | IDS          |
| ------------------------ | --------- | --------- | ----------- | ------------ |
| Virtual Cores (reserved) | 4         | 8         | 16          | 32           |
| RAM (GB) (reserved)      | 8         | 16        | 64          | 64           |
| Maximum throughput       |           |           | Up to 1,000 | Up to 10,000 |
|                          | Up to 200 | Up to 500 |             |              |
(Mbps)
(1 or 2 span ports)
| Log Forwarder Events/s | 1,500 | 1,500 | 7,000 | 10,000 |
| ---------------------- | ----- | ----- | ----- | ------ |
Security-Module Sensor Specifications – IDS and Sandbox
The Security-Module sensor specifications assume a span port, local file assembly, log
forwarding, Network Traffic, Malware Sandbox, and IDS.
Virtual machines for the Security-Module IDS sensors must be provisioned as follows:
Component Security-Module-200M Security-Module-500M Security-Module-1G Security-Module-10G
| Virtual Cores (reserved)  | 4         | 8         | 16          | 32           |
| ------------------------- | --------- | --------- | ----------- | ------------ |
| RAM (GB) (reserved)       |           |           | 64          | 64           |
|                           | 8         | 16        |             |              |
| Maximum throughput (Mbps) |           |           | Up to 1,000 | Up to 10,000 |
|                           | Up to 200 | Up to 500 |             |              |
(1 or 2 span ports)
| Log Forwarder Events/s |       |       | 7,000 | 10,000 |
| ---------------------- | ----- | ----- | ----- | ------ |
|                        | 1,500 | 1,500 |       |        |
Checking Enabled Features on the Sensor
You can see which features are currently enabled on a sensor, as well as its current provisioning
by using the show module command in the Sensor CLI. For example:
Stellar Cyber Provisioning Recommendations
You can see the most recent provisioning guidance from Stellar Cyber by using the show
module request command in the Sensor CLI. For example:

Automatic Resource Checking
When you apply a Modular Sensor Profile, Stellar Cyber automatically checks the CPUs and
RAM provisioned for the target sensor and informs you whether they are sufficient to support the
features enabled in the profile. You can also see the results in the show module command listed
above – the output of the command reports both the name of the Modular Sensor Profile applied
and whether the resource checks passed.
If the resource checks do not pass, Stellar Cyber informs you of the issue and displays the
sensor in the list with a visible warning of the problem. It does not enable the sensor features
until the minimum specifications are met.
 Stellar Cyber only checks the CPUs and RAM against the show module request
recommendations. Disk size checks are not enforced.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  