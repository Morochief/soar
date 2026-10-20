# F01 - Overview Of Stellar Cyber Transcript

> **Curso Oficial:** `Curso F00`  
> **Documento Original:** `f01-overview_of_stellar_cyber_transcript.pdf`  
> **Total Páginas:** 8  
> **Formato:** Transcripción Oficial Stellar Cyber Academy (Markdown)

---


<!-- Página 1 -->

 Overview of Stellar Cyber 
 00:00-01:00 
 Welcome to the Overview of Stellar Cyber. Start your journey to a human-augmented 
 autonomous SOC. One SecOps platform that includes AI-driven SIEM, NDR, OT, ITDR, UEBA, 
 TIP, Open XDR, and multilayer AI. Here is the Stellar Cyber platform user interface. You will 
 learn more about the operations and capabilities this Stellar interface provides throughout 
 this overview. In this overview you will learn about the core operations and key capabilities 
 of the Stellar Cyber platform including data collection and normalization, data enrichment, 
 Interﬂow records, storage--including the Data Lake and Data Sink to cold storage, threat 
 detection, correlation, and alerting; 
 01:00-02:00 
 and ﬁnally, response actions with playbooks. Let us get started, along the way you will see 
 the progress. Let us start with data collection and normalization. To power AI-driven threat 
 detection and automated response, Stellar Cyber collects and normalizes data from 
 on-premises and cloud sources. Let us begin by looking at how data is collected and 
 normalized from on-premises infrastructure. As an open and uniﬁed platform, Stellar Cyber 
 includes hundreds of integrations to collect and normalize data from on-premises 
 infrastructure, security, and identity tools and systems. Here, on the right of the diagram, is 
 the Stellar Cyber platform that can be a SaaS instance, a cloud-native, cloud-hosted 
 deployment, or an on-premises deployment. 
 02:00-03:00 
 On-premises or private cloud-hosted tools forward logs or syslogs and/or network traffic to 
 Stellar Cyber Modular Sensors. Here are some common infrastructure and security tools 
 including ﬁrewalls; network devices, such as routers and switches; endpoint detection and 
 response solutions; vulnerability management tools; and network traffic from SPAN ports or 
 TAP devices. A key component to the Stellar Cyber architecture are Modular Sensors. They 
 are deployed within the network as virtual or hardware appliances. Security and network 
 tools are conﬁgured to send logs to Stellar Cyber Modular Sensors that are log forwarders 
 for the Stellar Cyber platform. Modular Sensors can collect network traffic from switches 
 using SPAN or mirror ports or TAP devices. 
 03:00-04:00 
 Stellar Cyber Modular Sensors include network detection and response (NDR) capabilities. 
 Along with collecting logs, they collect metadata from network traffic, check IDS signatures 
 for IT and OT threats, check for malware, and normalize data into JSON Interﬂow records, 
 which are securely sent to the Stellar Cyber platform over a TLS connection. Next, 
 ESS-00-00-324-v2 

---

<!-- Página 2 -->

 connectors that run on Stellar Cyber Modular Sensors can collect security data from 
 on-premises or private-hosted security tools using APIs or LDAPS. Here Microsoft Active 
 Directory servers are deployed on premises as well as vulnerability management tools such 
 as Tenable. 
 04:00-05:00 
 Stellar Cyber Modular Sensors have built-in connectors for integration with third-party 
 security and identity systems. With the Modular Sensor being within the organization, they 
 can securely connect to Active Directory. They are able to obtain important user 
 information to enrich Interﬂow records with valuable context. The connectors to Active 
 Directory can also be used to block user accounts that have been compromised. 
 Connectors to vulnerability tools such as Tenable can obtain valuable scan data as well as 
 launch scans within the organization. After collecting the information, the Modular Sensor 
 normalizes it into JSON-formatted Interﬂow records. These Interﬂow records are securely 
 transmitted to the Stellar Cyber platform over an encrypted TLS connection. 
 05:00-06:00 
 Stellar Cyber server sensors collect logs and event data from Windows servers and Linux 
 servers. The server sensors run on Windows servers and Linux servers as shown here. They 
 normalize collected logs and event data into JSON Interﬂow records and securely sends 
 them to the Stellar Cyber platform over a secure TLS connection. Building on how Stellar 
 Cyber collects and normalizes data for AI-driven threat detection and response, we will now 
 look at how this applies to systems and services operating within cloud infrastructure. The 
 Stellar Cyber platform also includes a comprehensive set of integrations to collect and 
 normalize data from cloud applications, 
 06:00-07:00 
 cloud infrastructure, identity and access management systems, and cloud security tools and 
 services. The Stellar Cyber platform has built-in connectors speciﬁcally for cloud-accessible 
 services. Cloud security tools and services that can be accessed via connectors via API 
 include: EDR (Endpoint Detection and Response) solutions, email systems, SASE (Secure 
 Access Service Edge) solutions, IAM (Identity and Access Management) providers, Cloud 
 apps, Cloud infrastructure, and Cloud security services. Stellar Cyber platform Connectors 
 collect raw events and security data from cloud applications, cloud infrastructure, identity 
 and access management providers, and a variety of cloud security tools and services. 
 07:00-08:00 
 In this example, the Stellar Cyber platform Connectors use APIs to request and collect raw 
 events and security data directly from cloud security tools and services. After the response 
 is received, the Stellar Cyber platform normalizes the collected raw events and security data 
 into JSON Interﬂow records for secure processing. Next, I will explain Stellar Cyber data 
 ESS-00-00-324-v2 

---

<!-- Página 3 -->

 enrichment. Metadata collected via connectors, sensors, and integrated threat-intelligence 
 feeds is used to enrich Interﬂow records with valuable context. Now here is an example of 
 how the enrichment process works. The Stellar Cyber platform has an Interﬂow record 
 received from a log source sensor or connector as shown here. The Stellar Cyber platform 
 enriches the data within Interﬂow records from many sources including threat-intel feeds for 
 IP and URL reputation, 
 08:00-09:00 
 geolocation, DNS for IP-to-hostname mapping, and identity management solutions 
 including Microsoft Entra ID, formerly known as Azure AD; Active Directory; Okta; Google 
 Workspace; etcetera. The Stellar Cyber platform enriches Interﬂow records collected from 
 all data sources with contextual metadata derived from threat intelligence feeds -- IP and 
 URL reputation sources, malicious IPs, domains, ﬁle hashes, and indicators of compromise 
 (IOCs). Let us take a closer look at the threat intel platform built into Stellar Cyber. Here is an 
 example of the threat intel platform settings in Stellar Cyber. It comes with preconﬁgured 
 threat intelligence feeds such as AlienVault, DHS, ET Pro, PhishTank,  Abuse.ch  , OpenPhish, 
 and Stellar Cyber. 
 09:00-10:00 
 You can bring in premium feeds such as recorded future, SOC Radar, and CrowdStrike or 
 use any standard TAXII feed from your trusted sources. The threat intel platform will collect 
 threat intel at ingestion. It is not only used for enrichment. This way, every IOC adds context 
 for raw data so you catch threats earlier. Now let us continue with enrichment. Interﬂow 
 records are also enriched with geolocation data: country, city, ASN, and location-based risk 
 indicators. Interﬂow records are also enriched with user metadata from identity providers: 
 usernames, user details, privileges, roles, group memberships, and login activity. Enrichment 
 also includes asset metadata: host names, OS, risk scores, location, vendors, types, ﬁle 
 access commands, logins, login failures, alerts, and vulnerabilities. 
 10:00-11:00 
 Interﬂow records are also enriched with the XDR Kill Chain and MITRE ATT&CK framework 
 tactic and technique classiﬁcation. Modular Sensors also enrich Interﬂow records with 
 application and protocol identiﬁcation, deep packet inspection (DPI) for over 4,000 
 applications and protocols including DNS, SMB, HTTP, ICMP, Google Drive, Dropbox, 
 PowerShell, RDP, Windows management instruction, etcetera. Here is an example showing 
 the Stellar Cyber platform getting metadata from an enrichment service, which is then used 
 to enrich an Interﬂow record. The enrichment performed by Stellar Cyber is extremely 
 powerful adding valuable context to identify and investigate threats. 
 ESS-00-00-324-v2 

---

<!-- Página 4 -->

 11:00-12:00 
 Now it is time to learn about Stellar Cyber Interﬂow records. Stellar Cyber Interﬂow records. 
 Data that is collected and enriched by Stellar Cyber from all sources is normalized into 
 standard JSON-formatted records called Interﬂow records. Interﬂow records are stored in 
 Stellar Cyber and are optimized for threat detection and investigation using AI and machine 
 learning. Here is an example of the data sources Stellar Cyber uses to collect important 
 data used in creating Interﬂow records. Here is an example of an Interﬂow record in the 
 Stellar Cyber platform. It has the normalized data as well as the data added during 
 enrichment. 
 12:00-13:00 
 Here you can see the Interﬂow record for this alert has been enriched with source and 
 destination geolocation metadata, threat intel: IP and URL reputation metadata, source and 
 destination IP type metadata, and IDS engine telemetry from Modular Sensors. Interﬂow 
 records are also enriched with user data, asset data, Kill Chain data, IOC matches, DNS 
 domains, application names, ﬁle hashes, and much more depending on the type of alert. 
 storageNow let us learn about storage in Stellar Cyber with the Data Lake and Data Sink. 
 Storage: retention of Interﬂow records within the Stellar Cyber platform. The Stellar Cyber 
 platform includes a Data Lake. 
 13:00-14:00 
 Stellar Cyber also provides cold storage options as a cost-effective way to store data for a 
 longer term. Enriched Interﬂow records are stored in the Data Lake within the Stellar Cyber 
 platform and can be simultaneously replicated to long-term storage using Stellar Cyber 
 Data Sink. For on-premises deployments, platform admins can use Data Sink with Amazon 
 S3 or compatible cold storage systems. For SaaS deployments Stellar Cyber manages the 
 cold storage. The Stellar Cyber Ingestion Dashboards show data stored within the Stellar 
 Cyber platform from each source. Traffic records over time is data stored from network 
 detection and response (NDR) sources, 
 14:00-15:00 
 such as Modular Sensors collecting traffic from the network. Traffic by application is 
 available with the included NDR capabilities that collect metadata from traffic and performs 
 deep packet inspection to determine the applications. Traffic by top sources shows the 
 amount of data collected from each source, based on the time selected. You can view 
 built-in or create custom dashboards as seen here to view data collected by the Stellar 
 Cyber platform. Now let us learn about threat detection, correlation, and alerting. The Stellar 
 Cyber platform uses multi-layer AI for detection, correlation, and triage. Enriched Interﬂow 
 records in the Data Lake are ready to be analyzed. 
 ESS-00-00-324-v2 

---

<!-- Página 5 -->

 15:00-16:00 
 Stellar Cyber's multilayer AI consists of machine learning (ML) for threat detection and 
 anomaly detection. The Interﬂow records in the Stellar Cyber Data Lake are optimized for 
 multilayer AI with machine learning. Machine learning is used to detect threats by analyzing 
 patterns and data to identify anomalies, behaviors, or indicators that match known or 
 emerging attack techniques. Graph machine learning is used for alert correlation and case 
 creation. Graph machine learning is used to correlate and link related alerts, users, assets, 
 behaviors, and activities into cases, delivering a uniﬁed view that simpliﬁes triage and 
 accelerates Investigations. 
 16:00-17:00 
 Gen AI provides capabilities such as an automated triage agent, AI investigator, and case 
 summarization. Gen AI is used for verdict determination for auto triage, case analysis, case 
 summaries, and for using plain language questions to quickly uncover key insights across 
 your data. The Stellar Cyber platform also includes rules, logic, and playbooks, including 
 signature-based rules, heuristic logic, and custom ATH playbooks. AI is complemented by 
 signature-based rules, heuristic logic, and playbooks to deliver broader threat coverage, 
 more precise detections, and automated response. The Stellar Cyber platform user 
 interface organizes the data processed by multi-layer AI 
 17:00-18:00 
 along with rules and logic so that alerts and events can be quickly found, investigated, and 
 actioned. Alerts detected by the Stellar Cyber platform are automatically categorized into 
 the MITRE ATT&CK framework and the XDR Kill Chain. The XDR Kill Chain enhances MITRE 
 ATT&CK-based tactics and techniques with its own tactics to cover threat intelligence, 
 malware detection, and anomaly detections. Here you can see the alerts that Stellar Cyber 
 has categorized into the MITRE ATT&CK framework. Here the XDR Kill Chain shows how 
 attacks progress across different stages making it easy to see where an attacker is in their 
 campaign. It begins with initial attempts. These are the alerts detected where attackers 
 probe for weaknesses and attempt to gain access. 
 18:00-19:00 
 Next are alerts mapped to persistent footholds where they establish ongoing access and 
 work to avoid detection. Then comes alerts mapped to exploration where attackers search 
 the environment, discover assets, and collect data. The next stage shows alerts mapped to 
 propagation. This is where attackers spread across systems through credential use, privilege 
 escalation, and lateral movement. The ﬁnal and most critical stage shows the alerts 
 mapped to exﬁltration and impact where sensitive data is stolen or systems are disrupted. 
 To see multi-layer AI in action for detection, correlation, and triage, here is an example of a 
 case. Cases are automatically created from alerts, users, assets, processes, and activities, 
 ESS-00-00-324-v2 

---

<!-- Página 6 -->

 collected from different data sources that are correlated automatically using graph 
 machine learning. 
 19:00-20:00 
 Gen AI is used to create a case summary that explains what happened, why it matters, and 
 what to do now. Gen AI is also used to provide the hypothesis for the case, which 
 summarizes the situation, articulating the likely cause, affected assets, and business risk to 
 guide immediate response. Graph machine learning is used to correlate  alerts, users, 
 assets, processes, activities, and other observables, into a case for holistic, automated 
 threat detection and rapid incident response. Gen AI provides recommended steps for 
 investigation, 
 20:00-21:00 
 vulnerability assessments, prioritizing monitoring efforts as well as actions for engaging 
 incident response. Case actions can be performed to mitigate threats using third-party 
 security integrations or scripts using case-speciﬁc attributes such as usernames, host 
 names or IP addresses. Now let’s learn about response actions with playbooks. Here I will 
 show you response actions using on-premises or private cloud-hosted security tools. Stellar 
 Cyber's platform empowers security teams to automate playbooks instantly taking 
 containment actions the moment a threat is detected. Its true strength lies in ﬂexibility, 
 enabling custom threat-hunting searches to become automated triggers that transform 
 discoveries into permanent defenses. 
 21:00-22:00 
 Here is how response actions work with on-premises security tools. In this example, in the 
 company network there are on-premises or private cloud-hosted security and identity tools 
 such as: Active Directory, other identity providers (IdPs), ﬁrewalls, and vulnerability 
 management tools. On the right there is a Stellar Cyber platform instance that is available 
 as SaaS, private cloud, or on premises. Within the company network, there are also one or 
 more Stellar Cyber Modular Sensors that are hardware or virtual appliances. From inside 
 the company network, Modular Sensors open a secure conﬁguration management (CM) 
 connection to the Stellar Cyber platform. Modular Sensors have built-in connectors that can 
 communicate locally, 
 22:00-23:00 
 in this case with systems and services within the company network. Next, let us look at an 
 automated threat hunting playbook example conﬁgured in Stellar Cyber that will use 
 connectors on Modular Sensors to perform the actions on systems or services within the 
 company environment. Here is an automated threat hunting playbook example. The 
 conﬁguration starts by deﬁning the execution frequency of the automated response. This 
 lets you specify how often you want this playbook to run, which can be in minutes, hours, 
 ESS-00-00-324-v2 

---

<!-- Página 7 -->

 days, or weeks. Here you deﬁne the content to be monitored. A query or correlation rule 
 determines which activities or data patterns the playbook will watch for helping the system 
 automatically detect and respond to threats that match your custom logic. 
 23:00-24:00 
 Here you deﬁne the condition that triggers the response action. Deﬁning these conditions 
 allows the playbook to recognize speciﬁc threat patterns and automatically initiate the right 
 response. Here is where you deﬁne the response action. ATH playbooks in Stellar Cyber can 
 take a range of automated actions from disabling accounts and blocking IPs to containing 
 hosts through EDR platforms, launching investigations, and notifying teams. These 
 responses transform threat detections into immediate, coordinated defense. Now that the 
 playbook is conﬁgured, let’s take a look at it in action. Here are some examples of response 
 actions: disable a user in Active Directory, block an IP address in a ﬁrewall, send an email or 
 Slack notiﬁcation, run a webhook or script. 
 24:00-25:00 
 After a playbook is conﬁgured and scheduled, the Stellar Cyber platform executes it 
 automatically. When a trigger condition is met, the platform routes the response action 
 through the CM connection to the Modular Sensor connector that interfaces with the 
 on-premises service, such as Active Directory, to disable a user or a ﬁrewall to block an IP 
 address. ATH playbooks can also automate response actions using cloud security tools and 
 services. The Stellar Cyber Open XDR platform includes hundreds of built-in integrations 
 across cloud applications, infrastructure, identity, and security tools, enabling both 
 automated and manually triggered playbooks to mitigate threats. 
 25:00-26:00 
 As an Open XDR platform, Stellar Cyber includes pre-built integrations with a wide range of 
 cloud security tools and services including: EDR (endpoint detection and response) 
 solutions, email systems, cloud apps, cloud infrastructure, cloud security services, SASE 
 (secure access service edge) solutions, and IDP (identity provider) solutions to name a few. 
 Connectors used by playbooks to access cloud services. Example response actions include: 
 disabling a user in an identity provider, performing a remediation action in an EDR solution, 
 blocking an IP address in a ﬁrewall, running a script, running a webhook to open a ticket 
 and sending email and Slack notiﬁcations to alert your security team. 
 26:00-27:00 
 When an ATH playbook triggers a cloud-based action, the Stellar Cyber platform uses its 
 connector to deliver the response action to the appropriate cloud security or identity 
 service for execution. ATH playbooks in Stellar Cyber deliver powerful automated response 
 actions across both on-premises and cloud-security systems. With the ability to seamlessly 
 integrate with hundreds of existing tools and services, they enable faster containment, 
 ESS-00-00-324-v2 

---

<!-- Página 8 -->

 smarter remediation, and continuous protection. Moving security operations closer to a truly 
 human-augmented, autonomous SOC. 
 27:00-28:00 
 We have completed the overview of the Stellar Cyber platform from data collection and 
 normalization through enrichment and Interﬂow records to storage in the Data Lake and 
 Data Sink. We then explored advanced threat detection, correlation and alerting, and 
 ﬁnished with automated response actions using playbooks. Together, these capabilities 
 deliver a uniﬁed, intelligent, and automated security operations platform. Thank you for 
 watching the Overview of the Stellar Cyber SecOps platform that includes AI-driven SIEM, 
 NDR, OT, ITDR, UEBA, TIP, Open XDR, and multi-layer AI. Start your journey to a 
 human-augmented autonomous SOC. Thank you and happy learning! 
 ESS-00-00-324-v2 

---