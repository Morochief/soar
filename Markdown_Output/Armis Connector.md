Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Armis Connectors

This connector allows Stellar Cyber to ingest logs from Armis and add the records to the data
lake. This connector integrates with the Armis API to query data for several content types.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Armis

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

Activity

Alerts

Applications

Business Applications

Connections

Devices

Operating Systems

Risk Factors

Vulnerabilities

Syslog

Assets (for
Devices)

Scans (for
Vulnerabilities)

msg_class:

armis_activity

armis_alerts

armis_applications

armis_business_app
lications

armis_connections

armis_devices

armis_operating_sy
stems

armis_risk_factors

Content Type

Index

Locating Records

armis_vulnerabilit
ies

msg_origin.source:

armis

msg_origin.vendor:

armis

msg_origin.category:

endpoint

Domain

<FQDN>

where <FQDN> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Armis to get the raw alerts that are stored in the Syslog index. Select the
Alerts content type.

Stellar Cyber maps Armis alerts. The alerts are read from the Syslog index, enriched with Stellar Cyber
fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid, armis.alertId, and host.ip.

 Armis alert integration supports Mobile and Industrial Control Systems (ICS) domains, in addition to

Enterprise.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

FQDN and Secret API Key

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class: armis_alerts AND _exists_: event.threat.name

Adding an Armis Connector
To add an Armis connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Armis Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Armis
credentials:

FQDN: Fully Qualified Domain Name of the instance URL from Armis. It has the format
<instance-name>.armis.com.
To get the instance name, have an Armis service and get the URL from Armis.

Secret API Key: A token generated from the Armis API Management page.
To get the Secret API Key, log in to your Armis instance and generate the key as
follows:
Settings > API Management > Create



The token from Armis is valid for 15 minutes. The connector will try to refresh the token
three (3) minutes before it expires.

Note that only one bearer token can be generated at a time with the API token. A
consecutive call to get a bearer token will invalidate the previous bearer token.

Adding the Connector in Stellar Cyber
To add an Armis connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Armis from the Type dropdown.

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

12. Enter the FQDN you noted above in Obtaining Armis Credentials.

 Do not include the https prefix or a trailing "/" symbol.

13. Enter the Secret API Key you noted above.

14. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The following logs are supported.

Devices

Activity

Alerts

Applications

Business Applications

Connections

Operating Systems

Risk Factors

Vulnerabilities

  The Devices content type is always selected and cannot be removed from the

configuration as it is required for host information.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

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

For all content types except Vulnerabilities, change the Indices to Syslog.

For Vulnerabilities only, change the Indices to Scans.

For Devices only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

