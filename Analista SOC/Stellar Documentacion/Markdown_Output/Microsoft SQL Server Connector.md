Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Microsoft SQL Server Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.
You can install a connector to retrieve data from a Microsoft SQL Server (MSSQL) database.

This Microsoft SQL Server connector collects either Klassify or Arotron logs stored in the
database. The connector can run on a network/security/modular data sensor.

 The supported data sources are Klassify and Arotron.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Microsoft SQL Server

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: Sensor

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

For Klassify:

Classification Logs

Syslog

msg_class:

Client agent status Logs

Email Logs

Assets (for Client
agent status Logs)

Reclassification and policy
deviation Logs

klassify_classification

klassify_client

klassify_email

Content Type

Index

Locating Records

klassify_reclassificati
on

msg_origin.source:

klassify_data_classific
ation_suite

msg_origin.vendor

klassify

msg_origin.category:

dlp

For Arotron:

Audit

Log

Login

Syslog

msg_class:

mssql_arotron_audit

mssql_arotron_log

mssql_arotron_login

msg_origin.source:

mssql_arotron

msg_origin.vendor

mssql

msg_origin.category:

database

Domain

<Server hostname or IP>

where <Server hostname or IP> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Server hostname or IP, Username, Password, Database Name, and Data Source

Adding a MSSQL Connector
To add a MSSQL connector:

1. Add the connector in Stellar Cyber
2. Test the connector
3. Verify ingestion

Adding the Connector in Stellar Cyber
To add a MSSQL connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Database from the Category dropdown.

5. Choose Microsoft SQL Server from the Type dropdown.

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

12. Enter the Server hostname or IP. This is the hostname or IP address of the MSSQL

server. If entering a hostname, do not include https.

13. Enter the Username of a user with read access to the database.

14. Enter the Password for that user.

 The password should not include non-ASCII special characters.

15. Enter the Database Name. This is the user-defined name of the database you want to

access on the above server.

16. Choose the Data Source. Currently the data sources are Klassify and Arotron.

17. Choose the Content Type you would like to collect.

For Klassify, the logs for Classification Logs, Client agent status Logs,
Email Logs, and Reclassification and policy deviation Logs are supported.

For Arotron, the logs for Audit, Log, and Login are supported.

18. Choose the Interval (min). This is how often the logs are collected.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

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

For Klassify content types, Classification Logs, Client agent status Logs,
Email Logs, and Reclassification and policy deviation Logs, change the
Indices to Syslog.

For Arotron content types, Audit, Log, and Login, change the Indices to
Syslog.

For the Klassify content type, Client agent status Logs only, change the
Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

