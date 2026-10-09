Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cisco AMP Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.

A Cisco Advanced Malware Protection (AMP) connector allows you to collect logs, discover
assets, and see vulnerabilities. There can be any number of Cisco AMP connectors active.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Cisco AMP

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Computers

Events

Vulnerabilities

Assets (for
Computers)

Syslog

Linux

msg_class:

ciscoamp_computers

ciscoamp_events

ciscoamp_vulnerabil
ities

msg_origin.source:

ciscoamp

msg_origin.vendor:

Content Type

Index

Locating Records

ciscoamp

msg_origin.category:

dnssec

Domain

<Host URL>

where <Host URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Host URL, Client ID, and API Key

Adding a Cisco AMP Connector
To add a Cisco AMP connector:

1. Create Cisco AMP API credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Cisco AMP API Credentials
To create Cisco AMP API credentials:

 Use our example as a guideline, as you might be using a different software version.

1. Log in to your Cisco AMP dashboard at https://console.amp.cisco.com  .

2. Click Accounts | API Credentials.

The API Credentials page appears.

3. Click New API Credential. The New API Credential screen appears.

4. Enter an Application name.
5. Choose Read-only for the Scope.

6. Click Create. The API credentials are immediately generated and the API Key Details

page appears.

7. Copy the 3rd Party API Client ID and API Key. You will need these when adding the

connector in Stellar Cyber.

Adding the Connector in Stellar Cyber
With the client ID and API key handy, you can add the Cisco AMP connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Cisco AMP from the Type dropdown.

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

12. Enter the Host URL. Use the Cisco AMP for Endpoints API host
(https://api.amp.cisco.com), not the Console Management URL.

13. Enter the Client ID. This is the 3rd Party API Client ID you noted above in Obtaining

Cisco AMP API Credentials.

14. Enter the API Key you noted above.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Computers, Events,

and Vulnerabilities are supported.

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

2. Change the Indices to Syslog if you chose the Events content type.

The table immediately updates to show ingested Interflow records.

3. Change the Indices to Assets if you chose the Computers content type.

The table immediately updates to show ingested Interflow records. Also, hosts
discovered through this connector show Cisco AMP as a data source.

4. Change the Indices to Linux Events if you chose the Vulnerabilities content type.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

