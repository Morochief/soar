Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Google Cloud Audit Log Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Google Cloud Audit Log

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Admin Activity

Data Access

Policy

Requests

System Event

Index

 Syslog

Locating
Records

msg_cl
ass:

googl
e_clo
ud_ad
min_a
ctivi
ty

googl
e_clo
ud_da
ta_ac
cess

googl
e_clo

Content Type

Index

Locating
Records

ud_po
licy

googl
e_clo
ud_re
quest
s

googl
e_clo
ud_sy
stem_
event

msg_o
rigin.so
urce:

googl
e_clo
ud

msg_o
rigin.ve
ndor:

googl
e

msg_o
rigin.ca
tegory:

paas

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

JSON Key File

To set up the service account for this configuration, the Google Cloud user must have
the role of serviceAccountKeyAdmin.

The following privileges are assigned to the service account for the corresponding log
access: Logs Viewer and Private Logs Viewer (for the Data Access logs).

Audit Logs for the service account must have Admin Read, Data Read, and Data Write
enabled for the Kubernetes Engine API or for Google Cloud Storage.

Adding a Google Cloud Audit Log Connector
To add a Google Cloud Audit Log connector:

1. Enable the Google Cloud Logging API
2. Create a Google Cloud service account
3. Create a JSON key
4. Enable Kubernetes Log access
5. Enable Google Cloud Storage access
6. Add the connector in Stellar Cyber
7. Test the connector
8. Verify ingestion

Enabling the Google Cloud Logging API
To enable the Google Cloud Logging API, follow the guidance in the Google Cloud
documentation to Enable the Logging API .

Creating a Google Service Account
With the API enabled, you can now create a service account.

To create a service account, follow the guidance in the Google Cloud documentation to Create a
service account . For more information on roles, see the Google Cloud documentation for
Access control with IAM .

 Use our example as a guideline, as you might be using a different software version.

1. Navigate to the main menu of https://console.cloud.google.com. 

2. Click  to display the navigation pane.

3. Choose IAM & Admin > Service Accounts. The service accounts pane for the active

project displays.

4. Select your project or verify that you are in your project, then click + Create Service

Account.

5. In the Service account details page, enter a Service Account Name in the first field.
The Service account ID is automatically created based on the name you supplied.

6. Enter a description for this service account, to identify its association with your Stellar

Cyber connector.

7. Click the Create and Continue button.

8. Bypass completing the remaining access control and permission steps, which will be

configured in a later step.

In the section for granting access to the project, do not specify any roles. Click
Continue.

In the section for granting users access to the service account, do not specify
any users. Click Done.

9. The new service account is created and displayed on the Service account details

page.

10. Make note of the email address displayed for the service account.

11. Now give permissions to the Service Account you created. From the IAM & Admin

menu, select IAM.

12. Select the email address and click the Edit icon.

13. In the dialog that opens, click Add another role.

14. Search for Logs Viewer, and select that role.

 This role gives read-only access to Admin Activity, Policy Denied, and System

Event audit logs. If you have just this role, you cannot view Data Access audit logs.

15. Click Add Another Role.

16. Search for Private Logs Viewer, and select that role.

 The Private Logs Viewer role includes the ability to read Data Access audit logs.

17. Click Save.

18. The permissions page now displays the service account with the needed permissions to

collect logs.

Creating a Service Account Key
With a service account, you can now create a key file for uploading to Stellar Cyber.

To create a service account key, follow the guidance in the Google Cloud documentation to
Create a service account key .

 Use our example as a guideline, as you might be using a different software version.

1. Still within the IAM & Admin > Service Accounts page, select the service account you

created. (Verify that you are in your project.)

2. Click  in the actions column for that account and select Manage keys from the menu.

The Keys screen appears.

3. Click the Add Key menu and select Create new key.

4. When the dialog displays a dialog Create private key, select JSON.

5. Click Create. The JSON file is downloaded. Keep this file safe, as you cannot recover
the key if this file is lost. You will upload this file to Stellar Cyber when configuring the
connector.

6. Click Close.

Your key file is used by the Stellar Cyber connector.

Enabling Kubernetes Log Access
To enable access to the logs:

1. Return to the IAM & Admin menu.

2. Select the Audit Logs sub-menu.

3. In the page that displays, locate the Filter field (Enter property name or value) for Data

Access audit logs configuration.

4. Search for Kubernetes and then select Kubernetes Engine API to the left of the

Service label.

5. Enable permissions for Admin Read, Data Read, and Data Write.

6. Click Save.

Enabling Google Cloud Storage Access
To enable access to the logs:

1. Return to the IAM & Admin menu.

2. Select the Audit Logs sub-menu.

3. In the page that displays, locate the Filter field (Enter property name or value) for Data

Access audit logs configuration.

4. Search for storage and then select Google Cloud Storage to the left of the Service

label.

5. Enable permissions for Admin Read, Data Read, and Data Write.

6. Click Save.

7. Navigate to the Logs Explorer and click GCS Bucket to view the bucket logs.

Adding the Connector in Stellar Cyber
With the Google service account set up and the API key ready, you can add the Google Cloud
Audit Log connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose PaaS from the Category dropdown.

5. Choose Google Cloud Audit Logging from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This is the tenant allowed to use the connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Upload the JSON Key File you created above.

13. Choose the Interval (min). This is how often the logs are collected.

14. Choose the Content Type you want to collect. The following logs are supported:

Admin Activity

Data Access

Policy

Requests

System Event

 The Google API requires that the content type you specify here be a type for which

you have viewed logs at least once in the corresponding account.

15. Toggle whether you want to collect All data (default) for the content type or just the

GKE (Google Kubernetes Engine) logs.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active.

Testing the Connector
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

Request

connector configuration.

Did you configure the connector correctly?

401

Unauthorize

d

This error occurs when an authentication credential is

Did you enter your credentials correctly?

invalid or when a user does not have sufficient

privileges to access a specific API.

Are your credentials expired?

Are your credentials entitled or licensed for that

specific resource?

403

Forbidden

This error occurs when the permission or scope is not

Did you enter your credentials correctly?

correct in a valid credential.

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

 The Google API requires that the content type you specify here be a type for which you have
viewed logs at least once in the corresponding account. If you run the test for a content type
that has not been viewed, the test will result in an error.

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

