Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Product Security Overview

  The Stellar Cyber Open XDR platform is built on industry-leading security and privacy standards
that keep our customer's data secure. Stellar Cyber is committed to helping customers of all
sizes to meet their data protection and compliance requirements. As evidence of this, we have
obtained our SOC 2 Type II report, which attests to the effectiveness and our adherence to
security controls and processes.

The following is an overview of layers of security features implemented in the Stellar Cyber Open
XDR platform:

Stellar Cyber Compliance and Security Posture
Two-Factor Authentication and SSO
Account Lockout
Multi-Tenant Data Segmented
Role-Based Access Control
Audit Logs
Protection of Data in Transit
Protection of Data at Rest

Masked Data in Storage

Additional Security Controls in Stellar Cyber SaaS

Stellar Cyber Compliance and Security Posture
Visit the Stellar Cyber Security Portal  for the latest information on Stellar Cyber's security
posture, including details on compliance, policies, legal standards, data security, and application
security.



Two-Factor Authentication and SSO

All access to Stellar Cyber is authenticated. Two-factor authentication is supported and is
enabled by default in Stellar Cyber SaaS.

Account Lockout
A user account can be locked out after repeated failed login attempts. This is implemented to
protect the platform against brute force account takeover attacks.

Multi-Tenant Data Segmented
Stellar Cyber supports built-in multi-tenancy and supports three levels of access scopes:
Root/Organization, Tenant Group, and Tenant. Data is segmented by tenants. User access can
be limited to the assigned scope, which limits the potential attack surface.

Role-Based Access Control
Default roles with different levels of privileges are defined. Administrators can also create roles
with custom privileges. Role-Based Access Control enables fine-grained control for accessing
sensitive information in Stellar Cyber’s multi-tenant platform and ensures that users are only
allowed to access the data needed for the job.

Audit Logs
Audit logs are kept for all actions to the platform. In SaaS, platform logs are kept in a central
location and can be accessed only by authorized personnel.

Protection of Data in Transit
All communications between Stellar Cyber components that are transported on the public
Internet are encrypted in TLS 1.2 with strong ciphers. This includes Sensor and Data Processor
communications.

Protection of Data at Rest
For Stellar Cyber Open XDR deployed on premise, hot data is stored in the Data Processor’s
local storage. Disk encryption is supported by the Data Processor.

In Stellar Cyber SaaS, data stored in the hot storage and the backup storage are encrypted by
default using the 256-bit Advanced Encryption Standard (AES-256).

Masked Data in Storage

Stellar Cyber automatically identifies sensitive items seen in the clear in ingested data and
masks them in storage for security. Keep in mind the following:

Stellar Cyber does not directly decrypt traffic and only masks data seen in the clear.

Passwords seen in the clear are masked in storage.

Personally identifiable information is masked in storage.

Additional Security Controls in Stellar Cyber SaaS

Stellar Cyber has implemented processes and procedures designed to mitigate the risks an
organization faces. Specifically, Stellar Cyber has implemented the following controls to ensure
the service is operated with high security standards:

Application Security
Separate Production Environment
Access Control to the Production System
High Availability and Disaster Recovery
Formal System Change Management Process
Risk Assessment and Control

Application Security

In Stellar Cyber SaaS, the public interface to the service is protected by Web Application
Firewalls. Firewall rules are configured to allow or deny traffic based on predefined security
criteria so that common attacks are blocked and malicious access can be blocked upon
detection.

Separate Production Environment

The SaaS production environment is completely separate from the Development or Quality
Assurance (QA) environments.

Access Control to the Production System

Access control to the production system follows the least privilege principle. Only authorized
Stellar Cyber personnel are allowed to access the system backend.

High Availability and Disaster Recovery

The security features of High Availability and Disaster Recovery are as follows:

Key service redundancy is implemented to ensure high service availability

Formal backup policies and procedures are in place to ensure that system availability
commitments can be maintained

Data and configuration are backed up automatically

Formal System Change Management Process

Stellar Cyber has a formal software release and deployment procedure that includes logging,
assessing, and authorizing changes before they are implemented. A change control board is
established to review and authorize changes, so the ability to make change requests is
appropriately limited.

Risk Assessment and Control

Stellar Cyber maintains a documented Risk Management Policy to guide employees in
performing risk assessment and treatment. Stellar Cyber has implemented a formal risk
assessment process, including risk assessments and risk treatment plans. Owners are assigned
responsibility for each risk and appropriate risk mitigation methods are in place.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

