Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Quick Start: Administrators

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M02 Administration Essentials for Tenants, Users, and System (03h:46m)  

Introduction and Agenda (08m:00s)

Explore essential administrative tasks in the Stellar Cyber Platform, including tenant
configuration, role-based access control, two-factor authentication, and certificate
management for secure access. Learn how to configure custom-branded logos, mail
server settings for alert notifications, and set up the System Action Center for real-time
monitoring and notifications.

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

User Management with Role-Based Action Control (20m:00s)

Discover how to manage user privileges using role-based access control (RBAC) within
the Stellar Cyber Platform. Follow a demonstration on configuring privilege profiles —
including Super Admin, Platform Admin, and Security Admin — and learn how to assign
roles and scopes to control access levels across tenants. Explore how RBAC
configurations help meet organizational security needs while ensuring compliance with
access control policies.

User Management with Multi-Tenant Architecture (36m:00s)

Learn how to assign users to specific tenants or tenant groups, configure API access,
and set up two-factor authentication for secure access. Gain insights into viewing user
activity logs and monitoring active session connections to ensure compliance and
security within the Stellar Cyber Platform.

The first time you access a link on the portal during a session, you must log in to access
content.

Each user's function working with Stellar Cyber can vary. In many deployments, the administrator
will have a different perspective than an analyst. During initial setup and on an ongoing basis,
you will use the Stellar Cyber user interface to integrate data sources, configure dashboards and
automations, and manage the server and users. Those configuration settings are spread
throughout the Stellar Cyber interface.

After reviewing the main Getting Started topic, you may find this section helpful to familiarize
yourself with the location of configuration pages you may need.

This list highlights settings for the server itself.

The System | Administration section addresses the server-level settings such
as users, tenants, licensing, and so on.

As part of your installation, you use the System | ORGANIZATION
MANAGEMENT | Settings page to configure the SSO / authentication
requirements for how your users will access the server.

In the System | ORGANIZATION MANAGEMENT section, create and
manage users from Users and Role-based Access Control. Even if you have
configured SSO, you will still need to set certain user access parameters.

For partner and MSSP deployments, configure Tenants and Tenant Groups,
depending on your organizational needs.

The following list highlights configurations related to data integration and response,
which you begin to use after the fundamental aspects of the server are configured.

Take a look at the Ports list so you are familiar with the ingoing and outgoing
ports that are required for your deployment plan.

External sources for ingestion and response (Connectors and Sensors ) are
added and configured from the System | DATA SOURCE MANAGEMENT
and System | INTEGRATIONS sections.

Each sensor must be associated with a sensor profile, which in turn must be
associated with a specific receiver. Receivers are also configured from the
Collection section.

To manage the volume of data ingested from sensors, you can also set up
traffic and log filters; these are accessed from the Collection section.

Dashboards are configured from the Dashboards menu. You can use these
dashboards to configure and schedule reports Reporting functions are
accessible from the Reporting menu.

Either you or an analyst can configure custom, automated threat hunting
actions from the Automation menu. These automated playbooks based on
specific data and conditions are configured to perform a response action. The
System section includes options to configure recipients on the server, scripts,
and other settings to support playbooks and other general functions.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

