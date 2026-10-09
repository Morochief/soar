Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Understanding Tenants

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M02 Administration Essentials for Tenants, Users, and System (03h:46m)  

Multi-Tenant Concepts and Configuration (38m:00s)

Explore multi-tenant architecture within the Stellar Cyber Platform, including how data
segregation, machine learning customization, and operational views support managed
security service providers (MSSPs) managing multiple organizations or business units.
Learn how tenant-specific Interflow data is stored and processed within the data lake,
and how threat intelligence and machine learning models can be scoped and tuned at
the tenant level. Follow a step-by-step demonstration on creating and configuring
tenants, assigning access levels, and setting up a tenant admin user with two-factor
authentication. Discover how tenant boundaries enforce data isolation while allowing
centralized visibility across your environment within the Stellar Cyber Platform.

Tenant Assignment for Stellar Cyber Components (42m:00s)

Discover how to assign tools, queries, dashboards, connectors, and sensors to tenants
within the Stellar Cyber Platform. Learn how Modular Sensors, Windows Server
sensors, Linux Server sensors, and connectors are configured to maintain data
segregation and support tenant-specific machine learning across both SaaS and on-
premises deployments. Explore the practical steps required to ensure that data flowing
into the data lake remains properly isolated per tenant, preserving the integrity of threat
intelligence and Interflow records associated with each organization. Follow along with a
hands-on demonstration that walks through tenant-based assignments for queries and
dashboards, and watch how these configurations come together to support accurate,
tenant-aware analysis across the Stellar Cyber Platform.

The first time you access a link on the portal during a session, you must log in to access
content.

Stellar Cyber is a truly multi-tenant platform. This allows a single Stellar Cyber installation to
serve any number of unique, separate companies, organizations, or departments while keeping
security information fully separated. Not only is the data separate, but machine learning is also
unique for each tenant. This feature has two main use cases:

To implement the MSSP (Managed Security Service Provider) business model where
the serving organization operates and manages Stellar Cyber and provides security
monitoring to any number of client companies. The individual client companies are
tenants, and Stellar Cyber sees each company as a unique and separate entity.
For larger organizations multi-tenancy allows the delegation of security functions to
subordinate departments. For example, a company with offices in different regions can
assign each branch its own Stellar Cyber tenant. The home office operates and
manages the data processor, leaving the branches to focus locally.

This overview page describes the basic concepts that apply across the Stellar Cyber system with
regard to tenants.

Tenant Definition
A tenant is defined in the system using the name assigned by the system administrator. (See
Tenant Users.) The system also assigns a unique ID to each tenant. This ID appear in Interflow
records and can also be seen in the System | ORGANIZATION MANAGEMENT | Tenants page
when the ID option is enabled in the column picker.

For users that have multi-tenant access, the user interface includes a dropdown in the upper
right corner of the screen that lets you select the tenant whose data you want to see. This control
acts as an overall filter for all data record information. If a specific tenant is selected, then only
event and Interflow records that belong to that tenant are displayed and can be acted upon.

The All Tenants selection removes the filter and all records in the Data Lake become
accessible.

 If you have many tenants defined, the Tenants dropdown includes a Search capability that

helps you quickly find exactly the tenant you're seeking, as illustrated below.

The Tenants drop-down menu does not appear for tenant users. Instead the filter is preset to the
Stellar Cyber tenant to which the user has been assigned and cannot be changed.

 A security analyst will typically select a specific tenant when responding to a report regarding

trouble in a specific region or for a specific client.

All Tenants

This might be used when a record or entity is intended to be regarded as enterprise-wide and not
for a specific tenant.

Tenant Users
Users with tenant scope are used to provide visibility-level access to individuals that belong to
the sub-divisions that the tenant represents.

Tenant users:

Do not have access to the case management function.
Cannot create automated threat playbooks.
Cannot take firewall response actions.
Do not have access to configuration and administrative functions.

Attributes of Tenants
The tenant identity appears in almost all data records collected and managed by Stellar Cyber.

Interflow records and events are assigned to a tenant.
Sensors are assigned to a tenant. When they generate Interflow records those data are
keyed to the tenant to which they belong.
Connectors are assigned to a tenant.
Saved queries are tenant-specific. The saved queries that one tenant user creates
cannot be seen by users of other tenants.
Custom dashboards are tenant-specific.

Tenant Groups
You can group tenants, which allows you to easily manage multiple tenants and users at those
tenants.

You can add tenants to groups on the System | ORGANIZATION MANAGEMENT | Tenant
Groups page. See Tenant Groups for more information.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

