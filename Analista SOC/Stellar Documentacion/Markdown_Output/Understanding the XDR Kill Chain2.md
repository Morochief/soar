✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Understanding the XDR Kill Chain
The Stellar Cyber Open XDR Platform is organized around the XDR Kill Chain, a powerful
framework for understanding and responding to threats on the security attack surface. The
XDR Kill Chain identifies five separate stages on the attack landscape, each with its own
associated tactics and techniques. Tactics and techniques include both those based on the
MITRE | ATT&CK framework  , as well as XDR-specific versions developed by Stellar Cyber.
Stellar Cyber developed the XDR Kill Chain to bring the MITRE | ATT&CK framework into the
platform while addressing some of its shortcomings, such as a lack of high level stages, an
inability to distinguish internal vs. external attacks, and a lack of a robust tagging mechanism for
alerts. The XDR Kill Chain was designed to make analysts more efficient while enabling AI to
better process alerts.
The XDR Kill Chain includes the following stages, each identified by its own distinctive color and
icon. These colors and icons are used consistently throughout the user interface to reinforce
stage identification.
| XDR Kill  Icon | Summary | Associated | Associate Classic Attacks |     |
| -------------- | ------- | ---------- | ------------------------- | --- |
| Chain          |         | MITRE |    | d                         |     |
| Stage          |         | ATT&CK     | XDR Tacti                 |     |
|                |         | Tactics    | cs                        |     |
Port scanning
| Initial  | Attackers are trying to access your network. |             |         |                |
| -------- | -------------------------------------------- | ----------- | ------- | -------------- |
|          |                                              | Resource    | XDR SBA | External brute |
| Attempts |                                              |             |         | force login    |
|          |                                              | Development |        | attempts       |
External
Phishing
Probes of
|     |     | External | XDR NBA |     |
| --- | --- | -------- | ------- | --- |
known
|     |     | Credential |     | security holes |
| --- | --- | ---------- | --- | -------------- |
External
Access 
XDR UBA
Reconnaissance

|          |                                                 | Initial Access |          |          |
| -------- | ----------------------------------------------- | -------------- | --------- | -------- |
| Persiste | Attackers are trying to maintain access to your |                |           |          |
|          |                                                 | Persistence    |  XDR EBA | External |
trojans
| nt  | systems in spite of defensive techniques. |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- |
Account
|          |     | Execution |  External |              |
| -------- | --- | --------- | ---------- | ------------ |
| Foothold |     |           |            | manipulation |
XDR Malw

|     |     |     | Defense | are |     |
| --- | --- | --- | ------- | --- | --- |
Evasion 
XDR Intel
Command and
Control 
Explorati Attackers are inspecting your network, learning Internal Internal port
|     |     |     | Collection  |     |     |
| --- | --- | --- | ------------ | --- | --- |
scans
on about your environment before taking further action. XDR NBA
External
|     |     |     | Discovery  |     |     |
| --- | --- | --- | ----------- | --- | --- |
SQL dumpfile
s
Suspicious
SMB copies
Propagat Attackers are trying to obtain additional privileges Internal
|     |     |     | Internal | Internal |     |
| --- | --- | --- | -------- | -------- | --- |
spyware
| ion | and access and control additional systems on your |     |            |         |          |
| --- | ------------------------------------------------- | --- | ---------- | ------- | -------- |
|     |                                                   |     | Credential | XDR UBA | Internal |
|     | network.                                          |     |            |         | trojans  |
Access 
Internal
Internal brute
|     |     |     | Privilege  | XDR Malw | force |
| --- | --- | --- | ---------- | -------- | ----- |
|     |     |     | Escalation |  are    |       |
Lateral
|     |     |     | Movement |    |     |
| --- | --- | --- | -------- | --- | --- |
Exfiltrati Attackers are trying to steal data, potentially   Syn floods
|     |     |     | Exfiltration |    |     |
| --- | --- | --- | ------------ | --- | --- |
on dumping it in a way that avoids detection, and/or Ransomware
|          |                                    |     | Impact  |     | File action |
| -------- | ---------------------------------- | --- | -------- | --- | ----------- |
| & Impact | vandalizing your systems and data. |     |          |     |             |
anomalies
Additional Tactics
MITRE ATT&CK has three tactics domains: Enterprise, Mobile, and Industrial Control Systems
(ICS). In past releases, Stellar Cyber supported the Enterprise domain as described in the table
above.
Starting in release 6.0.0, Stellar Cyber also supports the Mobile and ICS domains. Armis alert
integration alerts contain ICS domains. See Integration of Third Party Native Alerts.
For the Enterprise tactics, see Enterprise Tactics .
For the Mobile tactics, see Mobile Tactics .
For the ICS tactics, see ICS Tactics .
| XDR Kill Chain Stage | Enterprise                  | Mobile                   |     | ICS                   |     |
| -------------------- | --------------------------- | ------------------------ | --- | --------------------- | --- |
| Initial Attempts     |                             |                          |     | Initial Access TA0108 |     |
|                      | Reconnaissance TA0043       | Initial Access TA0027    |     |                       |     |
|                      | Resource Development TA0042 | Credential Access TA0031 |     |                       |     |
Initial Access TA0001
Credential Access TA0006
Persistent Foothold
|     | Execution TA0002       | Execution TA0041       |     | Execution TA0104   |     |
| --- | ---------------------- | ---------------------- | --- | ------------------ | --- |
|     | Persistence TA0003     | Persistence TA0028     |     | Persistence TA0110 |     |
|     | Defense Evasion TA0005 | Defense Evasion TA0030 |     | Evasion TA0103     |     |

| XDR Kill Chain Stage | Enterprise | Mobile | ICS |
| -------------------- | ---------- | ------ | --- |
Command and Control TA0011 Command and Control TA0037 Command and Control TA0101
|     |     | Remote Service Effects TA0039 | Impair Process Control TA0106 |
| --- | --- | ----------------------------- | ----------------------------- |
Exploration
|     | Collection TA0009 | Discovery TA0032  | Discovery TA102   |
| --- | ----------------- | ----------------- | ----------------- |
|     | Discovery TA0007  | Collection TA0035 | Collection TA0100 |
Propagation
Privilege Escalation TA0004 Privilege Escalation TA0029 Privilege Escalation TA0111
Credential Access TA0006 Credential Access TA0031 Lateral Movement TA0109
Lateral Movement TA0008 Lateral Movement TA0033 Inhibit Response Function
TA0107
Network Effects TA0038
| Exfiltration & Impact |                     |                     | Impact TA0105 |
| --------------------- | ------------------- | ------------------- | ------------- |
|                       | Exfiltration TA0010 | Exfiltration TA0036 |               |
|                       | Impact TA0040       | Impact TA0034       |               |
XDR Kill Chain In Action
Consider the classic attack progression shown superimposed on the XDR Kill Chain, below, with
a standard phishing attack moving through multiple stages to eventual data exfiltration:
Alerts are triggered at each of the five XDR Kill Chain stages, identified by their
associated tactic and technique, compatible with the MITRE | ATT&CK matrix.
The XDR Kill Chain easily differentiates external alerts from internal/lateral ones and is
able to capture complex attack progressions using its looped design between
Exploration and Propagation.
XDR Kill Chain stages are generally (but not strictly) progressive in nature. In other
words, an alert might be related to a prior alert in a lower level on the XDR Kill Chain
but sometimes is not.
In addition to being assigned an XDR Kill Chain stage, alerts are also scored for
severity and fidelity, helping you focus on the alerts that matter. Stellar Cyber also
automatically correlates related alerts and groups them into cases.
About XDR Tactics
The XDR Kill Chain augments MITRE | ATT&CK-based tactics and techniques with its own
tactics to cover threat intelligence, malware detection, and anomaly detections. Threat
intelligence is based on reputation analysis, malware detection on known signatures, and
anomalies on deviations from standard observed behavior patterns:

XDR Malware – Alerts for malware.
XDR Intel – Alerts for threat intelligence.
XDR User Behavior Analytics (UBA) – Alerts for user anomalies.
XDR Network Behavior Analytics (NBA) – Alerts for network anomalies.
XDR Endpoint Behavior Analytics (EBA) – Alerts for host-based anomalies.
XDR Sensor Behavior Analytics (SBA) – Alerts for operational and injection-based
anomalies.
XDR Kill Chain in Stellar Cyber
The XDR Kill Chain appears throughout Stellar Cyber, most prominently as the centerpiece of
the Home Page dashboard, giving you a bird's-eye summary of critical and total alerts at each
Kill Chain stage in the current time interval:
You'll also find the XDR Kill Chain's familiar stages and icons in the Cases page, the various Alert
pages, Threat Hunting, and Reporting, among others.
Anatomy of an Alert
Stellar Cyber categorizes alerts according to their XDR Kill Chain stage, tactic, technique, and
alert name:
Stellar Cyber generates alerts by using machine-learning algorithms to search for specific
security-related events.
The table below summarizes these relationships for IP/Port Scan Anomaly detection:
XDR Kill Chain Stage Initial Intrusions
Tactic (MITRE | ATT&CK or XDR-Extended) TA0043: Reconnaissance
Technique T1595: Active Scanning
Alert External IP/Port Scan Anomaly on 135.x.y.25
Other Components of the Stellar Cyber Data Model
Alerts are just one part of the Stellar Cyber Data Model. The Data model represents all data in its
different forms within Stellar Cyber and is useful to keep in mind when investigating alerts or
cases:
Raw Event - Stellar Cyber starts with raw data ingested from security and IT tools,
including Stellar Cyber sensors.
Signal - Stellar Cyber identifies critical Raw Events with special security value as
signals. Signals are stored in their own dedicated index and are preserved longer than

raw events because of their usefulness (for example, domain creations or Windows
Defender events).
Alert - A specific security-related event generated by Stellar Cyber using machine-
learning algorithms.
 Together, raw events, signals, and alerts are referred to generically as events.
Entity - Stellar Cyber considers assets or users within the enterprise as entities.
Case - Multiple alerts and entities correlated together into a unified security threat.
The figure below illustrates the relationships between the components of the Stellar Cyber data
model.
XDR Kill Chain Stages Described
This section describes the XDR Kill Chain stages in detail.
Initial Attempts
Attackers are looking for a way into the network or the hosts connected to the network. Typical
techniques include:
External port scanning.
Brute force login attempts.
Phishing.
Probes of known security holes.
During the Initial Attempts stage, attackers perform reconnaissance, inspect the network for initial
footholds, attempt to establish resources for further operations, and, crucially, attempt to steal
credentials that can enable access, perhaps via brute force or credential dumping.
Persistent Foothold
Attackers are trying to ensure their ongoing access to network resources, regardless of
defensive measures such as system reboots or credential updates. Typical techniques include:
Copy operation (rcp, rsync, etc.) via SSH after account access is established.
Malware delivery by email, removable memory device, or HTTP transfer using tools
such as wget or curl.
Removing or disabling security software, perhaps via scripts.
External trojans.
This phase also involves the owner of the malware establishing an illicit communication channel
to the infected system. Nearly any protocol can be used and is most often selected to appear as
normal traffic as much as possible so that it is allowed by any firewalls or routers in the path.

For systems that do not have a public IP address, the communication link is typically initiated by
the infected system.
Exploration
Attackers are inspecting your network, performing reconnaissance to learn about your
environment before taking further action. Typical techniques include:
Use of native OS tools for discovery of accessible network shares, browser bookmarks,
and peripherals.
Network sniffing, screenshots, and keyboard logging to collect audio, video, and email.
Internal IP/port scanning, suspicious file copies, URL reconnaissance, and
SQL dumpfiles.
Stellar Cyber looks for deviations from observed network behavior analysis baselines at this
stage, preemptively alerting you to ongoing exploration of your resources by attackers.
Propagation
Attackers are attempting to escalate their privileges, spreading their access to other areas of
your network via lateral movement, malware, and internal credential access. Typical techniques
include:
Internal trojans, spyware, and brute force attacks.
Internal credential stuffing.
Remote desktop exploits.
Stellar Cyber looks for deviations from observed user behavior analysis baselines at this stage,
as well as common credential access, remote desktop, and SMB exploits.
Exfiltration and Impact
When sufficient control is established, attackers use infected systems as desired, either by direct
access or by pre-programmed time release. Typical techniques include:
Leaks of PII
Data exfiltration through remote desktop, Office 365, or DNS tunnels.
Cryptojacking
This is the stage during which intended damage is actually done, including:
Collecting and transmitting sensitive user information
Triggering ransomware
Destroying systems
Modifying data
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  