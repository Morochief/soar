Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Active Directory Connectors

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

M03 Modular Sensor Concepts and Configuration (08h:56m)  

AD Connector Collection of Asset and User Details (12m:00s)

Discover how the Active Directory (AD) connector collects asset and user details for
enhanced visibility in the Stellar Cyber Platform. Learn how to manage and integrate AD
attributes to enable detailed investigations and user behavior analysis.

AD Connector Response Actions to Disable a User (42m:00s)

Learn to use the AD connector for response actions, including disabling user accounts
directly from the Stellar Cyber Platform. Follow a demonstration of how this action
integrates with incident response workflows, and explore configurations for streamlining
user access management as part of a comprehensive response strategy.

The first time you access a link on the portal during a session, you must log in to access
content.

This connector allows Stellar Cyber to ingest logs from Active Directory (AD) and add the records
to the data lake and, optionally, to issue the Disable User response action.

Active Directory integration with Stellar Cyber enables organizations to monitor and detect
security threats across their network, including domain controllers, workstations, and servers,
while providing quick case response capabilities.

We recommend that you configure an Active Directory connector. It provides the following key
capabilities:

The user information from AD enriches event Interflow records and provides user profile
details for User Behavior Analytics.

The computer information from AD supports Windows Event Collector (WEC), which
lets one server forward the Windows Event logs belonging to several Windows
machines.

Stellar Cyber can be configured to use this connector to disable AD users that have
been identified as a security risk.



The Active Directory Disable User response action supports disabling users with any field
having the following values:

username of the format username

sid of the format S-1-5-21-XXXXXXXXX-XXXXXXXXXX-XXXXXXXXX-XXXX

user principal of the format username@domain.tld

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Active Directory

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: No

Runs on: DP (Respond) or Sensor (Collect and Respond)

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Computers

Users

Windows Events

Assets (for Computers)

msg_class:

AD_computer

AD_user_pro
file

msg_origin.sou
rce:

active_dire
ctory

msg_origin.ven
dor:

microsoft

msg_origin.cate
gory:

Content Type

Index

Locating Records

iam

Domain

<Server Hostname>

where <Server Hostname> is a variable from the configuration of this connector

Response Actions

Action

Disable User

Required Fields

userPrincipalName

 The Active Directory responder does not support Kerberos authentication, only the collector does.

There are two other ways to disable an Active Directory user:

Navigate to Automation | Action History and choose the User Actions tab. See Create a
Disable User Action.

Navigate to Assets | User Behavior Analytics and choose the Users tab. See Disable a User
Action.

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Active Directory Domain, Server Hostname, User Name, and Password, plus Protocol Type
(LDAP, LDAPS, or LDAPS (certificate validation disabled))

 If you select LDAPS, refer to Configuring Certificates for AD Connectors with LDAPS
for details on how to upload and apply a certificate to the sensor running the connector.

In addition, for Kerberos Protocol Type: Realm Name, KDC, Admin Server, and Default Domain

For the Active Directory collector running on Sensor, AD server must be added to the Sensor
DNS

Adding an Active Directory Connector
To add an Active Directory connector:

1. Obtain and verify Active Directory requirements
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining and Verifying Active Directory Requirements
To configure an Active Directory Stellar Cyber connector, you will need the following information:

The Active Directory domain to be monitored

The fully qualified domain name (FQDN) or IP address for an Active Directory Server
configured as a Domain Controller

The protocol type (LDAP, LDAPS, or LDAPS with certificate validation disabled)

(Optional) To support authentication using Kerberos, you will need an AD Server with
Kerberos enabled and you will also need a Kerberos server

Active Directory username and passwords with appropriate permissions

For the Active Directory collector running on Sensor, you need to add the AD server to
the Sensor DNS

 To set up the LDAPS protocol or Kerberos over LDAPS, refer to the Microsoft

documentation and Configuring Certificates for AD Connectors with LDAPS . For
example, look in Active Directory documentation  to troubleshoot Active Directory-related
issues.

 The Windows Server 2025 functional level may enforce the use of LDAPS. You may need to
enable LDAPS to comply with this functional level. Refer to the Microsoft documentation for
Active Directory Domain Services functional levels .

The permissions for the Stellar Cyber Active Directory Respond function are greater than for the
Collect function. You may, optionally, set up two different connector instances for different
purposes, if you want to use different user accounts for the Stellar Cyber collection and response
purposes.

For Collect only configurations, the username and password needs to be a standard
Active Directory user who is a member of the domain to be monitored.

 The password should not include non-ASCII special characters.

For Respond configurations, follow the steps below to ensure the account is configured
appropriately.

1. Launch Active Directory Users and Computers with administrative

credentials.

2. Right click on the Organizational Unit with the user account for which you
want to enable the respond action authority, and select Delegate Control.

3. Select the user or group to which you want to delegate the authority, then

press Next.

4. Select Create Custom Task to Delegate and press Next.

5. In the Delegation of Control Wizard, select the radio button for Only the

following objects in the folder.

6. Check the box for User objects, then press Next.

7. In the Permissions panel section for Show these permissions, uncheck

General and check Property-specific.

8. In the specific permissions section, check the boxes for Read
userAccountControl and Write userAccountControl.

9. Click Next, and then Finish.

Adding the Connector in Stellar Cyber
To add an Active Directory connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose IdP from the Category dropdown.

5. Choose Active Directory from the Type dropdown.

The asterisk (*) indicates a required field.

6. For Function, enable Collect. If you want to be able to disable users, also check the

box for Respond.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this

tenant name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Active Directory Domain to be monitored, for example, stellar.local.

13. Enter the Server Hostname, which is the fully qualified domain name (FQDN) or IP

address for an Active Directory Server configured as a Domain Controller.

 Do not include https in the hostname.

14. Enter the Interval (min). This is how often the logs are collected.

15. Enter the User Name for AD authentication. See the above section for guidance on

permissions for the user account required to collect and respond.

16. Enter the Password.

17. Choose the applicable Protocol Type: LDAP, LDAPS, LDAPS (certificate validation

disabled), or Kerberos.

 If you select LDAPS, refer to Configuring Certificates for AD Connectors with

LDAPS for details on how to upload and apply a certificate to the sensor running the
connector.



Note the following for Kerberos:

You can only configure one Active Directory connector with Kerberos on

each Sensor.

Respond actions in Active Directory are also supported with Kerberos
authentication. However, selecting Data Processor in the Run On field in

the General tab of the Add Connector screen is not supported.

If you enable channel rebinding, you must select Kerberos for the

Protocol Type. By default, NTLM is used, but if you enable channel
rebinding, you must enable Kerberos.

18. (Optional) If you selected Kerberos, the configuration tab has more fields:

The asterisk (*) indicates a required field.

a. Enter the Realm Name. This is your Kerberos realm in uppercase, for

example, STELLAR.LOCAL.

b. Enter the KDC. This is the name or address of a host running a Key

Distribution Center (KDC) for that realm. In most cases, the KDC is the same
as the Server Hostname.

c. Enter the Admin Server. This is the host where the administration server is

running. Typically, this is the master Kerberos server.

d. Enter the Default Domain. This is the Kerberos realm name for a particular

host or domain.

e. (Optional) Enter the KRB5 Configuration File Path. This is the customized
krb5.conf file for Kerberos authentication. For example, a file path might be
/etc/krb5.conf, which indicates the file path on a sensor. (You may need
Customer Support's assistance to upload the file to the sensor.) If a
customized krb5.conf file is not specified, the default conf file is used.

f. (Optional) Select Use SSL to use SSL. It is enabled by default. Deselect the

checkbox to not use SSL with Kerberos.

19. (Optional) Choose the Content Type. The logs for Computers are supported. (The logs
for Users are also supported, but they are hard coded and cannot be selected from the
user interface.)



Stellar Cyber queries computers using LDAP, enriches them with IP address
information through DNS, and populates the Windows Events index.

In addition, the computers are sent to the Assets | Asset Analytics page.

20. Click Next. The final confirmation tab appears.

21. Click Submit.

The new connector is immediately active and collects up to 90 days of activity stored in the AD
server.

Testing the Connector

 If you're running the Active Directory connector on a Sensor, make sure that the Sensor and

DP are running the same version of software. Otherwise the test might not work.

When you add (or edit) a connector, we recommend that you run a test to validate the
connectivity parameters you entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60

seconds for new or modified configuration details to be propagated to the sensor before
performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure
result. A successful test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by
using the X button. If the test fails, you can select the   button from the same row to review and
correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

400

Bad

This error occurs when there is an error in the

Did you configure the connector correctly?

Request

connector configuration.

401

Unauthorize

d

This error occurs when an authentication credential is

Did you enter your credentials correctly?

invalid or when a user does not have sufficient

privileges to access a specific API.

Are your credentials expired?

403

Forbidden

This error occurs when the permission or scope is not

correct in a valid credential.

Are your credentials entitled or licensed for that

specific resource?

Did you enter your credentials correctly?

Do you have the required role or permissions for

that credential?

404

Not Found

This error occurs when a URL path does not resolve

Did you enter your API URL correctly?

to an entity.

429

Too Many

Requests

This error occurs when the API server receives too

The server or user license/quota will eventually

much traffic or if a user’s license or entitlement quota

recover. The connector will periodically retry the

is exceeded.

query.

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Computers and Users, change the Indices to Windows Events.

For Computers only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

