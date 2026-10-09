Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Duo Security Connectors

This connector allows Stellar Cyber to collect data from external sources and add the records to
the data lake.

Integrating Duo with Stellar Cyber provides advanced identity and access management
capabilities, enabling organizations to manage user access and security policies across their
network, and providing enhanced security controls and compliance features. By combining Duo's
multi-factor authentication with Stellar Cyber's advanced security analytics and machine learning
algorithms, organizations can effectively defend against cyber threats.

 Note that the API for Duo Security is not supported for deployments configured to

communicate through an HTTP proxy.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Duo Security

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

Administrator

Authentication

Telephony

Syslog

msg_class:

duosecurity_administrat
or

Content Type

Index

Locating Records

duosecurity_authenticat
ion

duosecurity_telephony

duosecurity_trust_monit
or

msg_origin.source:

duosecurity

msg_origin.vendor

cisco

msg_origin.category:

endpoint

Trust Monitor

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from Duo Security to get the raw alerts that are stored in the Syslog index.
Select the Trust Monitor content type.

Stellar Cyber maps Duo Trust Monitor events. The events are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.
Deduplication is by duosecurity.sekey.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Hostname, Integration Key, and Security Key

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class: duosecurity_trust_monitor AND _exists_:event.threat.name

Adding a Duo Security Connector
To add a Duo Security connector:

1. Configure Duo Security application protection
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Configuring Duo Security Application Protection

To configure Duo Security application protection:

 Use our example as a guideline, as you might be using a different software version.

1. Log in to Duo.

2. If you don't have the Admin API application available, contact Duo technical support

and request access. When you get access, continue.

3. Click Applications. The Application menu expands.

4. Click Protect an Application. The Protect an Application page appears.

5. Find Admin API. If you start typing in the search bar, the available applications narrow

to match the text you type.

6. Click Protect on the Admin API row. The Admin API page appears.

7. Copy the Integration key, Secret key, and API hostname. You need all of these when

configuring Stellar Cyber.

8. Configure the Settings. At a minimum, select the following permissions: Grant read

information, Grant read log, and Grant read resource.

9. Click Save.

Adding the Connector in Stellar Cyber
To add a Duo Security connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose IdP from the Category dropdown.

5. Choose Duo Security from the Type dropdown.

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

12. Enter the Hostname. This is the Duo API hostname you noted above in Configuring

Duo Security Application Protection.

 Do not include https in this field.

13. Enter the Integration Key you noted above.

14. Enter the Security Key you noted above.

15. Choose the Interval (min). This is how often the logs are collected.

 Note that default setting is 5 minutes, which is the minimum recommended interval

for this connector type.

16. Choose the Content Type you would like to collect. The logs for Administrator,

Authentication, Telephony, and Trust Monitor are supported.

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

