Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Best Practices for Coverage

To defend the entire attack surface effectively, Stellar Cyber recommends a platform approach
where a single platform (Stellar Cyber) commands multiple security controls and data sources. A
platform approach means running detections and operations within a single system that has
access to all relevant data.

Stellar Cyber has many native capabilities, but as an Open platform it relies on other additional
controls and data sources to defend the entire attack surface. The illustration below and
recommendations offer generic, high-level guidance on how to get the best results out of Stellar
Cyber when defending an organization. However, SecOps teams will always know their
environment the best. There is always organization-specific context on what parts of the attack
surface are most critical or which threats are most relevant that will help you fine-tune these
generic recommendations.

Overview of the Platform Approach
The figure below illustrates the platform approach, showing the power of using Open XDR to
integrate Stellar Cyber with external Controls and Data for optimal coverage:

The SecOps stack components shown in blue are those that Stellar Cyber offers natively. Stellar
Cyber provides the platform, some network-related controls, and some data-related endpoints
and threat intelligence. There are many other parts of the attack surface that Stellar Cyber does
not offer natively but instead implements using integrations with a control or data source. The
controls and data sources shown in red are the critical integrations most commonly added to
Stellar Cyber. Controls and data sources illustrated in black are still highly valuable, but are less
critical than the ones in red.

For more specific guidance on what to do if certain controls aren’t available or how best to
address more complex environments, refer to the Tactical Recommendations.

Tactical Recommendations

EDR

My organization does not have an EDR...what should I do?

Stellar Cyber recommends that you deploy an EDR if it is within budget constraints and
operationally feasible to do so. However, if for some reason it is not possible, a Next Generation
Antivirus solution is a great alternative – although it is not a complete match to a sophisticated
EDR, it still provides relevant coverage. If installing an agent on non-cloud assets is not possible,
then ensuring Stellar Cyber’s Security Sensors have visibility into the relevant environments is
highly recommended.

Are Stellar Cyber Server Sensors an EDR?

No. Stellar Cyber server sensors are designed to provide a simple means to achieve visibility on
Linux and Windows assets. They do not run active protection or detection on the edge are
primarily used to forward logs. Stellar Cyber runs many detections off of this data, but it is not a
replacement for EDR.

Hybrid Environments

My organization runs in multiple public and private clouds...how do I get consistent visibility?

First, if the clouds you are operating in provide standard cloud logging services (for example,
AWS CloudWatch), those logs should be forwarded to Stellar Cyber. The most consistent data
source, however, will come from deploying Stellar Cyber security sensors in each environment.
This guarantees that the same controls (IDS, Malware Sandbox) and data (deep packet
inspection, network metadata) are available everywhere you operate. Stellar Cyber’s security
sensors can be deployed either physically or virtually, enabling them to deploy in all of your
environments.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

