Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Stellar Cyber SaaS Availability and Architecture

This topic describes the availability, architecture, security, and user experience of the Stellar
Cyber SaaS solution.

Stellar Cyber SaaS Availability
Stellar Cyber SaaS is available in all Oracle Cloud Infrastructure (OCI) regions. Regions are
available in North America, South America, Europe, Asia, and Africa. You can deploy in the
region closest to your operations, ensuring that data stays resident within a country or broader
region, including Oracle Government Cloud.

 For the most up-to-date list of OCI regions, see OCI Regions and Availability Domains  on

the Oracle website.

Architecture
Stellar Cyber SaaS is deployed on OCI as the base infrastructure and leverages a micro-service
architecture to ensure scalability and security across all platform components. With Stellar Cyber
SaaS, the centrally hosted portion of the Open XDR Platform contains Stellar Cyber’s
Connectors, Data Analyzer, and Data Lake microservice groups, which encompass everything
from data collection, processing, and search storage to Machine Learning (ML) and the user
interface.

The only platform components not hosted in the SaaS are Stellar Cyber’s sensors and your third-
party products. Deploy Stellar Cyber’s sensors on-premises or in any SaaS where you need data
collection and threat detection capabilities. Stellar Cyber SaaS upgrades and monitoring occur

on your behalf. For Stellar Cyber’s sensors, you can specify whether you want sensors
automatically or manually upgraded.

High Availability
Built on top of OCI’s highly reliable services, Stellar Cyber natively deploys the Open XDR
Platform’s standard High Availability (HA) features in all SaaS deployments. These features
include node clustering and data buffering. If you have additional HA requirements, Stellar Cyber
can deploy other HA features upon request.

Data Durability and Recovery
Stellar Cyber provides convenient Starter Packs that provide a solid foundation on which to grow
your deployment, starting with 30 days of hot storage for raw data, one year of hot storage for
alerts and cases, and support for either 100 GB of daily ingestion or 3,000 daily monitored
assets, depending on your license type. Regular data and configuration backups are
accompanied by optional cold storage to ensure long-term access to your data, as well as
reliable data recovery.

Refer to Data Durability and Availability in Stellar Cyber for more information about data
durability and availability in Stellar Cyber.

Security
Stellar Cyber SaaS uses additional security controls and various security testing throughout the
development lifecycle. In each SaaS environment, Web Application Firewalls protect all publicly
exposed services. At the service level, the platform communicates securely between services
with only the allowed communication paths. Furthermore,Stellar Cyber SaaS uses Two Factor
Authentication and robust RBAC at the user level. At the data level, data is separated physically
and logically amongst different customers to ensure no commingling or leaking of information.
Additionally, all data in cold storage is encrypted to ensure its security.

Stellar Cyber’s development lifecycle uses application security, vulnerability testing, and red
teaming continuously.

User Experience
Stellar Cyber manages the entire SaaS platform, so you can focus on keeping your business
secure. While notifications of maintenance windows go to all users, you do not have to worry
about the platform’s service levels, monitoring, or stability.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

