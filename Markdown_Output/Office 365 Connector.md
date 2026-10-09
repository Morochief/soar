Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Office 365 Connectors

This connector allows Stellar Cyber to collect data from external sources and add the records to
the data lake.

Integrating Office 365 with Stellar Cyber provides real-time visibility into security events and
alerts, enabling organizations to effectively monitor and respond to security incidents across their
cloud and on-premise environments.

There must be one connector for every Microsoft account to be monitored.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Office 365

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Audit General

Audit Exchange

Audit Sharepoint

Audit Azure Active Directory

DLP All

Windows Events

msg_class:

office365_audit_g
eneral

office365_audit_e
xchange

office365_audit_s
harepoint

Content Type

Index

Locating Records

office365_audit_a
zureactivedirecto
ry

office365_dlp_all

msg_origin.source:

office365

msg_origin.vendor:

office365

msg_origin.category:

office_suite

Domain

<Authentication Endpoint>

where <Authentication Endpoint> is a variable from the configuration of this connector and
will be one of the following, based on the Subscription Plan:

https://manage.office.com (Enterprise Plan)

https://manage-gcc.office.com (GCC Government Plan)

https://manage.office365.us (GCC High Government Plan)

https://manage.protection.apps.mil (DoD Government Plan)

Response Actions

N/A

Third Party Native Alert Integration Details

Office 365 alerts contain events from the AlertTriggered operation, which are sent to the Alerts index.
Select the Audit General content type.

The source records may also include related events in the AlertEntityGenerated operation. Some
information (AlertEntityId and EntityType) from the AlertEntityGenerated operation is merged with the
AlertTriggered operation for the same Alert ID. The information (AlertEntityId and EntityType) is stored in
the event_summary field.

Deduplication is by tenantid and AlertId.

In addition, the AlertEntityGenerated operation can be queried in Original Records, which are sent to
the Windows Events index.

For details, see Integration of Third Party Native Alerts.

For full alert integration of Office 365, including email-related alerts, the following licenses are required:

Microsoft 365 E5

Microsoft Defender for Office 365 P2 as an add-on to a non-E5 license

Required Credentials and Configurations

Office 365 Subscription Plan, Authentication Endpoint, Directory ID, Application ID, and
API Access Key

Microsoft Entra ID App with permissions: ActivityFeed.Read, ActivityFeed.ReadDlp,
ServiceHealth.Read

Locating Records

Use the following to query for records:

msg_origin.source: office365

msg_class: office365_audit_general

To search the alerts in the Alerts index, use the query: msg_class: office365_audit_general AND
Operation:AlertTriggered

To search the Original Records of the alerts in the Windows Events index, use the query: msg_class:
office365_audit_general AND Operation:AlertTriggered AND
Operation:AlertEntityGenerated

Adding an Office 365 Connector
To add an Office 365 connector:

1. Enable the audit log
2. Register the application
3. Add the connector in Stellar Cyber
4. Test the connector
5. Verify ingestion
6. About the query_window_start Field

Enabling the Audit Log
The procedure in this section is for enabling auditing through the Microsoft Purview portal.

The required permissions are:

Organization Management or Audit Logs role in Exchange Online

Global Admin or Compliance Admin in Microsoft 365



Notes:

Audit logs can take up to 24 hours to start appearing after enabling

Standard retention is 180 days (E3) or 365 days (E5)

To enable auditing:

1. Log on to https://purview.microsoft.com.

2. Navigate to Solutions > Audit.

Or direct URL: https://purview.microsoft.com/audit

3. If auditing is not enabled, there will be a banner: Start recording user and admin

activity.

4. Click Start recording user and admin activity.

5. When Audit is enabled, you can see the Search page.

Registering the Application
To register the application in Microsoft Entra ID (formerly Azure Active Directory):

1. Log in to Microsoft Azure at https://portal.azure.com .

2. From Azure services, select Microsoft Entra ID.

3. In the navigation pane, select App registrations.

4. Click New registration.

5. Enter a Name.

6. Choose a supported account type. Accounts in this organizational directory only is

typical.

7. Click Register.

8. Copy the Application (client) ID and Directory (tenant) ID. You will use them to

configure the connector in Stellar Cyber.

9. To set the permissions for your application, in the navigation pane, select API

Permissions.

10. Click Add a permission.

11. Select Office 365 Management APIs.

12. In Request API permissions, select Application permissions.

13. Select permissions for ActivityFeed.Read, ActivityFeed.ReadDlp, and

ServiceHealth.Read.

14. Click Add permissions.

15. If you are the Office 365 super admin, grant the permissions. Select the checkmark to

Grant admin consent for <account name>.

Otherwise, wait for the super admin to grant them.

 Make sure that the permissions are granted. If you add the connector before

permissions are granted, the process fails and you have to start over.

16. When the permissions are granted, in the navigation pane, click Certificates & secrets.

17. Click New client secret.

18. In Add a client secret, enter a Description and choose an expiration.

19. Click Add.

20. Copy the Value. You will use this as the API Access Key to configure the connector in

Stellar Cyber.

Adding the Connector in Stellar Cyber
With the audit log enabled, the app registered, and the two IDs and secret handy, add the Office
365 connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SaaS from the Category dropdown.

5. Choose Office 365 from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

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

12. Select the applicable Office365 Subscription Plan from the menu:

Enterprise Plan

GCC Government Plan

GCC High Government Plan

DoD Government Plan

To learn about Office 365 government environments and customer eligibility for the
Office 365 government plans, refer to the following Microsoft documentation:
https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-
service-description/office-365-us-government/office-365-us-government. 

13. Select the Microsoft Authentication Endpoint you wish to use, the available selections

are:

https://login.microsoftonline.us

https://login.microsoftonline.de

https://login.partner.microsoftonline.cn

https://login.microsoftonline.com

14. Enter the Directory ID. This is the Directory (tenant) ID you copied when you

performed the application registration.

15. Enter the Application ID. This is the Application (client) ID you copied when you

performed the application registration.

16. Enter the API Access Key. This is Value string you copied from Certificates &

secrets.

17. (Optional) Enter a Publisher ID. This ID is used to identify the application querying the

API. If there are no rate limits for querying the API, you can leave this blank.

18. Set the Interval (min). This is how often the logs are collected.

19. Choose the Content Type you want to collect. The following logs are supported:

Audit Azure Active Directory

Audit Exchange

Audit General

Audit Sharepoint

DLP ALL

 The same content types are collected for all Office365 Subscription Plans.

20. Click Next. The final confirmation tab appears.

21. Click Submit.

The new connector is immediately active, but the Office 365 APIs might not be active, especially
if this is the first time you've enabled the Office 365 audit logs. Wait at least 30 minutes before
testing the connector so that Office 365 can complete its background tasks.

The connector collects logs every 5 minutes, but does not collect any historical logs.

Testing the Connector

 If you've just added this connector, wait 30 minutes before testing.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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



If you see an error similar to below, verify that the appropriate permissions have been
granted.

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting. The Interflow Search tab appears.
2. Change the Indices to Windows Events or Alerts. The table immediately updates to

show ingested Interflow records.

About the query_window_start Field
The query_window_start field is a timestamp added to all Microsoft Office 365 connector
events. It records the start of the polling window during which Stellar Cyber collected the event
from Microsoft's  API, reflecting when Microsoft made the event available for retrieval.

The field is stored as a Unix timestamp in milliseconds in the raw event, and is displayed as a
datetime object in the Stellar Cyber user interface. The query_window_start field is consistent

with existing fields such as timestamp and write_time.

Background

Vendors do not always guarantee real-time delivery of events. Some events may be delayed
hours or days before appearing in the vendor's API. The query_window_start field allows you
to determine when the vendor published the event, making it straightforward to identify whether
an ingestion delay originated on the vendor side.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

