Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Stellar Cyber Glossary

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training portal where you can
learn more about this topic by watching the suggested lesson.

F02 Open XDR Architecture Overview (01h:11m)  

Introduction and Agenda (05m:00s)

Build a foundation in the Stellar Cyber Platform architecture, components, and essential terminology.
Familiarize yourself with tools like Interflow, the data lake, and various data indices to support your learning
in the Stellar Cyber curriculum.

M03 Modular Sensor Concepts and Configuration (08h:56m)  

Essential Terminology (16m:00s)

Familiarize yourself with key terminology related to Modular Sensors, including telemetry, metadata,
Interflow, alerts, and cases. Understand how these concepts support data normalization, threat detection,
and analysis.

The first time you access a link on the portal during a session, you must log in to access content.

Term

Description

Access Control List (ACL)

Access Control Lists are a common means used to grant specific permissions to different users or groups of users.

ACLs are frequently employed by many types of vendors, including cloud (AWS, Azure, GCP), switches, and

routers.

Active Directory (AD)

Active Directory is a directory service developed by Microsoft for Windows domain networks. It is included in most

Windows Server operating systems as a set of processes and services. Initially, Active Directory was used only for

centralized domain management.

Stellar Cyber provides connectors that help you ingest logs from both Active Directory and Microsoft Entra

ID (formerly Azure Active Directory).

Advanced Persistent Threat (APT) An advanced persistent threat (APT) is a prolonged and targeted cyberattack in which an intruder gains access to a

network and remains undetected for an extended period of time. APT attacks are initiated to steal data rather than

cause damage to the target organization's network.

Alerts

Alerts are a critical component of Stellar Cyber's ability to discover important events in a sea of data. Using ML

Alerts, third party

techniques as well as algorithms developed over long experience, Stellar Cyber examines raw event data for

evidence of security breaches. Insignificant events are passed over and sifted for anomalies. When anomalies are

found, Stellar Cyber generates alerts that are entered into the Alerts Index and reported in the Stellar Cyber user

interface.

Alerts help drive the action in the home dashboard, the Alert Types page, and the Cases interface. There are many

different types of alerts available in Stellar Cyber, organized by XDR Kill Chain Stage, Tactic, and Technique, with

each focused on a specific type of security threat.

Stellar Cyber supports integration of certain third party native alerts (such as those created from an Endpoint

Detection and Response (EDR) service). Once configured, alerts from these sources are automatically ingested, de-

duplicated and typically normalized and enriched to the Open XDR format, and then mapped to the Alert index. The

alert criteria from the third party source is used but augmented, in most cases, with information from Machine

Learning (ML) and Security Analytics (SA). This allows third party native alerts to be correlated alongside Stellar

Cyber built-in alerts. A summary of how Stellar Cyber manages each third party native alert integration is described

in Integration of Third Party Native Alerts.

Assets

An asset is a server, router, or host system that appears in the private network being monitored by Stellar Cyber.

Assets are automatically registered in Stellar Cyber by sensors. The information used to identify them include MAC

address, IP address, and host name (if available). They can be de-authorized or ignored by user command if

Term

Description

needed. Hosts outside the private network are not considered assets. Using the Asset Analytics screen, you can

examine assets for threat data and also examine performance history.

Automated Threat Hunting (ATH)

Automated Threat Hunting is the practice of proactively searching for cyber threats. ATH automatically seeks out

Azure Blob

threat patterns not usually caught by normal security tools.

Stellar Cyber implements Automated Threat Hunting by providing a means to automate actions based on queries or

rules that you specify and respond to matches by notifications in email or slack, triggering of a webhook, actions on

a Firewall or switch, creating new alerts , disabling a user, or running a script. See more at Automated Threat

Hunting.

Azure Blob Storage is Microsoft's object storage solution for the cloud. Blob Storage is optimized for storing massive

amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition,

such as text or binary data.

Stellar Cyber can use Azure Blobs for data sink storage, including its lower-cost archival classes.

Case

Stellar Cyber also leverages ML to correlate disparate alerts into a coalesced case.

A case is a set of multiple correlated alerts and entities constituting a potential unified security attack, ranked by a

dynamically updated score indicating the severity of the attack. Stellar Cyber uses its machine-learning capabilities

to generate cases automatically, grouping related alerts into a unified case for improved attack resolution.

Stellar Cyber reports cases in the Home dashboard, as well as in the Case Management interface, giving you a

powerful tool to organize and respond to security events.

Cold Storage

Cold Storage in Stellar Cyber lets you store snapshot-based data from your data processor (DP) on another server

so that you can analyze it later. You can import the stored data to your working DP or to a dedicated forensic DP.

Refer to Configuring Cold Storage and Data Durability and Availability in Stellar Cyber for information on working

with long-term data storage in Stellar Cyber.

In addition, the Working with Data Management topic provides valuable background on the differences between

snapshots and data sinks, as well as imports and restores, and how they relate to cold storage.

Configuration Manager (CM)

The CM process runs on the Stellar Cyber Data Processor (DP) and is responsible for managing system

components and their configurations, including licensing and health of the Stellar Cyber system.

Connector

Connectors are a method of collecting information and compiling it into Interflow records that are indexed and stored

in the Data Lake. Stellar Cyber develops connectors based on the access methods provided for each external data

source, typically an API. These processes run on the Data Processor (DP) to fetch information actively on a

scheduled basis. There are several connector categories in Stellar Cyber.

Correlation

While alerts are being logged to the Alert index, Stellar Cyber automatically and continuously performs correlation

analysis, identifying commonalities and combining those potentially related alerts into a holistic view that Stellar

Cyber calls a case.

Correlation Method

This Security Analytics method uses rules to identify related elements in different events. When a connection

between events (correlation) is detected, that connection relationship may combine to trigger one of Stellar Cyber's

correlation alert types.

Dark Site

Dashboard

A machine or local network of machines that have no connection to the Internet.

Stellar Cyber is available for dark site deployments. Contact your sales representative for details.

Stellar Cyber provides a variety of ways to view the complex information stored in the Data Lake. In addition to the

different views provided in the XDR Killchain, the Alerts list, the Cases list, and Threat Hunting, there are also

predefined Dashboards (or reports) to visualize specific content. You can also create custom Dashboards to suit

your preferences.

Data Lake (DL)

The Data Lake is the repository of the information that Stellar Cyber stores. The information in the DL is organized

into indices, which are categories that Stellar Cyber uses to group data.

Data Processor (DP)

The indices help make searching much more efficient and effective. An index that stores information directly from the

sensors or collectors is referred to as a "raw" index. The security index contains enhanced data based on data from

one or more of the raw indices.

Refer to Stellar Cyber Architecture for more information on the DL.

The data processor is at the heart of the Stellar Cyber platform for unified Security Operations. The DP
receives all information collected by the system, ingesting and normalizing data from any security, IT, system,
or productivity product. It also includes an embedded web server where you interact with the platform.
Depending on your needs, the DP can be physical, virtual, or a cloud-based service provided by Stellar
Cyber. It can also be a single entity or a scalable cluster that grows with your needs.

Refer to Stellar Cyber Architecture for more information on DP services.

Term

Description

Data Sink

Data Sinks in Stellar Cyber are used as a destination for long term storage of different types of Stellar Cyber data,

including raw data, alerts, assets, and users. You can configure Data Sinks on a wide variety of storage solutions,

including Amazon S3, GCP, OCI, NFS, Azure Blob, and so on. Data Sinks provide long term access to archival data

and also provide value disaster recovery services.

The Working with Data Management topic provides valuable background on the differences between snapshots

and data sinks, as well as imports and restores, and how they relate to cold storage.

Domain Generation Algorithm

(DGA)

Domain generation algorithms are algorithms seen in various families of malware that are used to periodically

generate a large number of domain names that can be used as rendezvous points with their command and control

servers.

Domain Name Service (DNS)

DNS is used for tracking Domain Name Service resolution changes for specified domains. If a tracked domain

resolves to a new IP address, Stellar Cyber creates an entry in the Changed Domains to IP Resolutions table in the

Threat Hunting Library's DNS Analysis page. This is part of the data enrichment process.

Endpoint Detection and Response

Endpoint Detection and Response (EDR) is an integrated, layered approach to endpoint protection that combines

(EDR)

real-time continuous monitoring and endpoint data analytics with rule-based automated response.

Stellar Cyber integrates natively with all top EDRs, ingesting logs and generating alerts based on detected events.

Elasticsearch

Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable, full-text

search engine with an HTTP web interface and schema-free JSON documents. Stellar Cyber uses Elastic

technology for data storage and search, including an API for searches and the Kibana plugin.

Enrichment, Extended

Enrichment, Structural

Firewall Actions

For data matching certain criteria, Extended Enrichment leverages external threat intelligence to augment the

Interflow of these data before applying Machine Learning models or Security Analytics methods.

Stellar Cyber augments data with a basic set of enrichment fields to support normalization of incoming data to a

standardized Interflow record. This structural enrichment supports the underlying purpose of Open XDR.

Stellar Cyber has the capability of interfacing with firewall rules. Once configured, Stellar Cyber can mitigate security

breaches by blocking malicious traffic as soon as it is identified. Two modes supported are manual and automated:

You can manually trigger a firewall action from the event display.

An Automated Threat Hunting Playbook may specify a firewall response to be taken automatically when
some condition is met.

Geographic Behavior model

Stellar Cyber tracks login events at geographic locations over time for this Unsupervised ML model. Deviations from

typical or logical patterns trigger an alert.

Graph-based model

The graph based Unsupervised ML model looks for changes in relationships between entities, such as a parent

process and child process. Statistical scores are created and monitored for anomalies. The scores are unique

calculations based on each alert type.

Histogram-based model

This Unsupervised ML model measures the statistical distribution of user login behavior within set 24 hour periods. If

the observed user activity shows very low probability based on the existing patterns, an alert is triggered.

Index

Stellar Cyber organizes data into a set of indices, which helps to speed up your searches. Refer to Index

Definitions & Detailsfor details.

Interflow

Interflow is the record format used by Stellar Cyber to represent raw data, events, and anomalies. On the network,

Interflow is expressed as a JSON object (sometimes referred to as a "hash") that can contain a large variety of keys.

The values stored by each key can be any form of object (string, number, or other object).

A key purpose of the Interflow record is to provide evidence for an event of interest. The extensible nature of the

Interflow record is used by Stellar Cyber to implement its data enhancement and machine learning (ML) functions.

The ability to add fields during its life cycle is also used to adapt connectors that contain new definitions. As a result

Interflow is future-proofed and able to handle new requirements when needed.

Although the names of the keys are largely intuitive for security analysts, a dictionary of the Interflow keys can be

found on its own Interflow page. The Interflow Dictionary function on the Threat Hunting screen also provides a list

of Interflow keys to choose from when searching for threats in the Data Lake. The list of keys will evolve with new

versions of Stellar Cyber. The Event Display component shows the Interflow record in either tabular or raw JSON

form.

Term

Description

Intrusion Detection System (IDS)

An Intrusion Detection System is a monitoring system that detects suspicious activities and generates alerts when

they are detected. Based on these alerts, a security operations center (SOC) analyst or incident responder can

investigate the issue and take the appropriate actions to remediate the threat.

Stellar Cyber sensors include a predefined set of IDS rules that you can enable to detect malicious activities on your

network. The events generated by matched IDS signatures contribute to certain alerts.

Identity Threat Detection and

ITDR involves the detection and response to identity-related threats. In Stellar Cyber, ITDR alert types have been

Response (ITDR)

tagged with 'Identity Detection' to make it easier to identify and filter these threats during investigations.

Kafka

Kafka is a distributed event store and stream-processing platform. It is an open-source system developed by the

Apache Software Foundation written in Java and Scala. The project aims to provide a unified, high-throughput, low-

latency platform for handling real-time data feeds.

Log Forwarder

In Stellar Cyber, the log forwarder is a feature that allows sensors to ingest Syslog records from third party

sources.Stellar Cyber includes a wide variety of log parsers that enables it to ingest logs from nearly any source.

Refer to Ingesting Logs for information on setting up log forwarding.

Lucene

Lucene was developed by the Apache Software Foundation. It consists of a search engine library whose software

components and functionalities enable the efficient indexing and searching of data sets. It also includes a Lucene

query language whose syntax and rules allow you to interact with the data set to search, filter, and retrieve specific

data based on the criteria you define.

LTSM-based model

This Supervised ML model (Long- Short- Term Memory) is pre-trained with long-term data and tunes/weights

detected results with short term data.

Machine Learning (ML)

ML is a core component of Stellar Cyber's detection architecture that uses artificial intelligence to examine the

records in the Data Lake and identify evidence of a security breach. When breaches are detected, Stellar Cyber

generates alerts that are stored in an Alerts Index and reported in the Alerts page and the XDR Killchain page. There

are many different types of machine learning algorithms, each programmed to look for a different class or type of

threat.

The ML/SA pipeline, which automatically analyzes and correlates any data from your monitored environment (raw or

from disparate security tools you have deployed) is the core of Stellar Cyber’s multi-modal detection architecture.

The pipeline begins at ingestion and continues through case correlation and response actions.

These ML models are used for known bad patterns based on training performed on large scale datasets. An

example of a bad pattern is a recently registered domain used for data exfiltration. There are enough real world

examples of this type of activity that a model can be constructed to identify it with a certain level of confidence.

Supervised machine learning models require no site-specific training period because they are already "trained" and

ready to be used. In summary, Supervised Machine Learning is used when there are clear identifiers for what "bad"

looks like, but it is far too computationally complex for a simple "rule" to be used.

These ML models use the concept of non-standard patterns to identify bad events that cannot be easily detected by

a rule or known bad pattern. Unsupervised ML models learn the normal pattern for each environment, such as the

application usage that is normal for the users. Similarly, the normal application usage per user is observed. Then,

after the initial training time, the ML model triggers a corresponding alert type when activity appears significantly

different from the observed normal pattern.

Machine Learning, Supervised

Machine Learning, Unsupervised

Mean Time to Detection (MTTD)

Mean Time to Detection is an industry term referring to the mean time it takes to detect a potential attack.

MITRE ATT&CK Framework

The MITRE ATT&CK Framework  is a curated knowledge base that tracks cyber adversary tactics and techniques

used by threat actors across the entire attack lifecycle. The framework is meant to be more than a collection of data;

it is intended to be used as a tool to strengthen an organization’s security posture.

The Stellar Cyber Open XDR Platform augments and extends the MITRE ATT&CK framework with the XDR Kill

Chain, a powerful framework for understanding and responding to threats on the security attack surface. The

XDR Kill Chain identifies five separate stages on the attack landscape, each with its own associated tactics and

techniques. Tactics and techniques include both those based on the MITRE | ATT&CK Framework , as well as

XDR-specific versions developed by Stellar Cyber.

Network Detection and Response

Network Detection and Response (NDR) in the context of cybersecurity refers to the deployment of sensors in

(NDR)

relevant on-premises and cloud environments to monitor network activity. It involves connecting selected contextual

data sources such as endpoint detection and response (EDR) or identity telemetry. The AI engine analyzes network

Term

Description

activity, correlates events across domains, and generates alerts for investigation. NDR is part of a broader security

strategy that includes managing alerts within the platform or forwarding them to other systems, and expanding

detection coverage by adding additional telemetry sources over time.

Stellar Cyber can use NFS as a data sink destination.

Network File System (NFS)

The Network File System is a widely available technology that allows data to be shared between various hosts on a

network. NFS also supports the use of Kerberos 5 authentication in addition to DES. Kerberos 5 security is provided

under a protocol mechanism called RPCSEC_GSS.

Stellar Cyber can use NFS as a data sink destination.

NIST Cybersecurity Framework

The NIST Cybersecurity Framework is a set of guidelines for mitigating organizational cybersecurity risks. It is

published by the US National Institute of Standards and Technology based on existing standards, guidelines, and

practices.

Open XDR

Extended detection and response (XDR) is an approach to threat detection and response that provides holistic

protection against cyberattacks, unauthorized access, and misuse.

Open XDR  is a uniﬁed, AI-powered approach to detection and response that collects and correlates data from all

existing security tools to protect the entire enterprise attack surface effectively and efﬁciently. Open XDR, unlike

“closed” XDR, works with any underlying security control, including any EDR, eliminating the need for organizations

to essentially hand over the control of their security stack to any single vendor.

Oracle Cloud Infrastructure (OCI)

A cloud services platform that provides a range of services including computing, storage, and networking. It supports

the deployment of applications and services in various regions around the world, including North America, South

America, Europe, Asia, and Africa. OCI offers capabilities for advanced threat detection and response, integrating

with Stellar Cyber to ingest logs and provide real-time threat intelligence and automated response workflows. It also

supports the use of streaming connectors to collect log data and enhance security operations.

Parser

In the field of information security, parsers are used to analyze logs and search for traces of malware activity. Stellar

Cyber includes log parsers for a wide variety of vendor-specific log formats, as well as generic log formats.

Receiver

A receiver is a task running in the DP that passively listens for input from sensors. There can be any number of

receivers instantiated in the system and each one may serve any number of sensors. There are currently two types

of receivers: packet and JSON. The JSON form is used to process Interflow records from sensors. It defines the IP

address and port number that sensors use to connect to the DP.

S3

Amazon S3 or Amazon Simple Storage Service is a service offered by Amazon Web Services (AWS) that provides

object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that

Amazon.com uses to run its e-commerce network.

Stellar Cyber can use S3 for data sink storage, including its lower-cost archival classes.

Security Alerts Framework

The Security Alerts framework provides a comprehensive solution to view, manage, create, and adjust the alert

rules. The security alerts constantly filter and evaluate all the logs generated from your organization's traffic to trigger

new alerts.

Security Analytics (SA)

Security Analytics are part of Stellar Cyber's detection architecture. They rely on methods that use arithmetic and

logic to test for known security factors, such as an address having a bad reputation, or certain processes being

associated with suspicious RDP activity. Some of the alerts using these methods are based on a combination of

analytics and machine learning or other tools, such as the Malware Sandbox. You can use the features of the

Security Analytics engine to create your own alert definitions and response actions with Stellar Cyber’s Automated

Threat Hunting.

Sandbox, Malware

Certain alerts are triggered based on a combination of activities, including an event generated against data using the

Malware Sandbox at the sensor.

Secure Access Service Edge

(SASE)

Security Information and Event

Management (SIEM)

An architecture delivering converged network and security as a service capabilities. In Stellar Cyber, SASE is a

category of connector, for example, for Cato Networks or Versa Networks Concerto,

Security information and event management is a field within the field of computer security, where software products

and services combine security information management and security event management. They provide real-time

analysis of security alerts generated by applications and network hardware.

Term

Description

There are many SIEM tools available. Stellar Cyber includes SIEM technology and can either replace or

complement your existing SIEM.

Security Orchestration, Automation

and Response (SOAR)

Security orchestration, automation and response (SOAR) technology helps coordinate, execute, and automate tasks

between various people and tools all within a single platform.

A key part of Stellar Cyber's value proposition is its ability to perform end-to-end threat detection and response,

combining multiple capabilities into a single user experience.

Sensors

Sensors are the components that collect information from key points in the monitored network, compose Interflow

Snapshot Storage

records, and send them to the DP. There are several different types of sensors, each with different capabilities and

suited for individual environments. Regardless of the type, the basic function is the same; when observed events

occur, the sensor generates Interflow records and sends them to a receiver.

Refer to Types of Stellar Cyber Sensors for more information on the different types of sensors used in the Stellar

Cyber platform.

Snapshot storage provides a record of the state of a system at a particular point in time. In Stellar Cyber, snapshots

provide binary backups of the ElasticSearch cluster to external storage configured in the Snapshot Storage

Configuration tab (NFS, AWS S3, Azure, or OCI).

Refer to Working with Data Management for information on the differences between snapshots and data sinks and

the relative benefits of each in Stellar Cyber.

Splunk

Splunk Inc. is an American software company based in San Francisco, California, that produces software for

searching, monitoring, and analyzing machine-generated data via a Web-style interface.

Stellar Cyber can ingest logs from the Splunk Heavy Forwarder and also create Splunk data sinks.

State check model

This Unsupervised ML model is a simple status check. If the status of the device is changed from a specific,

predefined state to another state, the alert is triggered.

Statistically Rare Event model

This Unsupervised ML model looks for events that suddenly appear after a long duration of not appearing (days

silent). Unique key data points are monitored for each alert type within that duration.

SVM-based Classifier model

Stellar Cyber's support vector (SV) models use coordinates as part of a supervised machine learning model to

detect and predict abnormalities.

Syslog

System Logging Protocol (Syslog) is a way network devices can use a standard message format to communicate

with a logging server. It was designed specifically to make it easy to monitor network devices. Devices can use a

Syslog agent to send out notification messages under a wide range of specific conditions.

Training Time

Certain ML models learn the data distribution in your network automatically but require two weeks of observing data

to create an approximation of the real distribution. After that baseline, the model is automatically updated every 24

hours.

TRW model

The Threshold Random Walk (TRW) model. Certain alerts are based on these Unsupervised ML models. Stellar

TSA model

TTPs

Cyber's TRW models monitor for anomalous changes in the ratio between two measurements, such as a significant

increase in login failures. In actuality, a variety of metrics are calculated for the possible thresholds. For example, the

expected failure to success login rates have boundary and low/high thresholds and factors used to tune the scores

assigned to the threshold over time. These complex algorithms are tuned for performance and the nature of the

data.

The Time Series Analytic (TSA) models are Unsupervised ML models based on continuous monitoring of event data

observed by Stellar Cyber on the DP, and evaluation of that data for anomalies. Data are examined over time for

spikes in activity, anomalously low or high values, and rare values. Each time series algorithm accommodates

multiple factors that vary based on the nature of the data, time of day, and other characteristics to trigger more

accurate alerts.

TTPs are tactics, techniques, and procedures. This term is used by cybersecurity professionals to describe the

behaviors, processes, actions, and strategies used by a threat actor to develop threats and engage in cyberattacks.

Stellar Cyber reports TTPs in the detail displays for events.

UNIX Epoch format

The UNIX Epoch format refers to a way of representing time as the number of seconds that have passed since

January 1, 1970, 00:00:00 UTC (Coordinated Universal Time).

Virtual Cloud Network (VCN)

A VCN in the context of Oracle Cloud Infrastructure (OCI) is a customizable and private network within OCI. It is

similar to a traditional network, with firewall rules and specific types of communication gateways that can be set up.

VCNs are used to isolate and secure resources within the cloud environment, and they support the configuration of

subnets, route tables, and gateways. VCN flow logs, which are a type of data event, are reported in the Traffic Index

when using OCI Streaming Connectors.

Term

XDR

Stellar Cyber version 6.6.0s

Description

Extended detection and response (XDR) is an approach to threat detection and response that provides holistic

protection against cyberattacks, unauthorized access, and misuse. See Open XDR.

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

