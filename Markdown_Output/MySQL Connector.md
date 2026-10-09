Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring MySQL Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.

You can install a connector to the OpenDental MySQL database or another data source. There
can be any number of MySQL connectors.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: MySQL

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

SQL Result

Syslog

msg_class:

OpenDental

or, <data_source> for a
provided Data Source

msg_origin.source:

opendental

or, <data_source> for a
provided Data Source

msg_origin.vendor

Content Type

Index

Locating Records

OpenDental

or, for a provided Data Source:

<data_source> for root
tenant

<data_source>_<tenant_
id> for any non-root tenant

msg_origin.category:

crm

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Server Hostname or IP, Username, Password, Database Name, Select Columns, From Table,
Datetime Column, and Data Source

Adding a MySQL Connector
To add a MySQL connector:

1. Add the connector in Stellar Cyber
2. Test the connector
3. Verify ingestion

Adding the Connector in Stellar Cyber
To add a MySQL connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Database from the Category dropdown.

5. Choose MySQL from the Type dropdown.

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

12. Enter the Server Hostname or IP. This is the hostname or IP address of the MySQL

server. If entering a hostname, do not include https.

13. Enter the Username of a user with read access to the database.

14. Enter the Password for that user.

 The password should not include non-ASCII special characters.

15. Enter the Database Name. This is the name of the database on the MySQL server.

16. Enter the Select Columns that you want to ingest. Separate column names with

commas, or enter * for all columns.

17. Enter the From Table. This is the table name in the database.

18. (Optional) Enter the Where Condition. This is an optional query condition in MySQL

syntax. If you do not want to use a condition, leave it blank.

19. Enter the Datetime Column. This is the column in the database containing the date
and time information for the logs. The Datetime Column accepts epoch, mysql data
type datetime, and timestamp.

20. Enter the Data Source. You can select OpenDental from the dropdown or enter
another Data Source value, which should indicate where the data was from. The
recommended format is <vendor>_<product>.

21. Choose the Interval (min). This is how often the logs are collected.

22. (Optional) Enter the Data Timezone. This is the timezone for the data stored in the

MySQL database.

23. Choose the Content Type you would like to collect. The logs for SQL Result are

supported.

24. Click Next. The final confirmation tab appears.

25. Click Submit.

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

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

