Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cybereason Connectors

A Stellar Cyber Cybereason connector allows you to ingest Cybereason MalOp and Sensor data,
discover assets, and contain hosts using API calls to the Cybereason server managing those
hosts.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Cybereason

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable for MalOp; 24 hrs for Sensor

Collected Data

Content
Type

Sensor

MalOp

Index

API

Assets

https://<server>:port/rest/sensors/query

Sensor
Monitorin
g

Syslog

Alerts

Syslog

https://<your server>:port/rest/detection/inbox

Domain

https://<Server>:<Port>

where <Server> and <Port> are variables from the configuration of this connector

API

https://<your server
address>/rest/monitor/global/commands/isolate

https://<your server
address>/rest/monitor/global/commands/un-isolate

Response Actions

Action

Contain (Isolate)
Host

R
e
q
ui
re
d
Fi
el
d
s

c
y
b
e
r
e
a
s
o
n
.
p
y
l
u
m
I
d

Third Party Native Alert Integration Details

Sensors

MalOp

This content is not applicable for
alert mapping.

Stellar Cyber can generate alerts
based on the Cybereason sensor
and MalOp data, however the
MalOp records are most applicable
for direct mapping. The value in
malopDetectionType is
reformatted and used for the alert
name. Stellar Cyber has evaluated
each possible alert and assigned a
corresponding MITRE | ATT&CK
Stage, Tactic and Technique.

 For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Username, Password, Server, and Port

 User account must have API privileges

Locating Records

Use the following fields as a guide to query for records:

msg_origin.vendor: cybereason

msg_origin.category: endpoint

MalOp

msg_class:
cybereason_malops_all_types
msg_origin.source:
cybereason_malops_all_types
prior to v4.3.4
msg_class: cybereason_malops
msg_origin.source:
cybereason_malops

Sensors
msg_class: cybereason_sensors
msg_origin.source: cybereason_sensors

Adding a Cybereason Connector
To add a Cybereason connector:

1. Configure Cybereason access
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Configuring Cybereason Access
You must configure Cybereason management before you add the connector in Stellar Cyber and
obtain the following details:

Username

Password

Server address and port for API communication

To obtain the information:

1. Log in to the Cybereason console as an administrative user.

2. Follow guidance in the Cybereason documentation to ensure the server is enabled for

API access.

3. Create a user account for use with Stellar Cyber connector that has API privileges (refer

to "Create a User" in the Cybereason documentation, for example:
https://nest.cybereason.com/user/login?destination=/documentation/product-
documentation/201/create-edit-and-remove-users)  .

For the Sensor content type, you may need to select the following user roles:

For details, refer to Required Roles Per Endpoint  in the Cybereason documentation.

4. Make note of the Cybereason username and password before proceeding to the next

step.

 The password should not include non-ASCII special characters.

Adding the Connector in Stellar Cyber
To add a Cybereason client connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Cybereason from the Type dropdown.

The asterisk (*) indicates a required field.

6. Choose the Function: Collect to collect logs; Respond to contain hosts.

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

11. Click Next. The Configuration tab appears. Complete this screen with the data you

collected from your Cybereason setup steps in the previous section.

The asterisk (*) indicates a required field.

12. Enter the Username for use with the API call you noted above in Configuring

Cybereason Access.

13. Enter the Password corresponding to that username you noted above.

14. Enter the address of the Cybereason Server receiving API calls (for

example: integration.cybereason.net).

15. Enter the associated Port for that server.

16. Enter the Interval (min). If you chose Collect, this is how often the logs are collected.

 The interval setting applies to the MalOp content type. The logs for Sensor are

queried every 24 hours.

17. Choose the Content Type. The logs for MalOp and Sensor are supported.

 The Sensor content type is required to support Respond actions.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

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

2. Change the Indices to Syslog if you set MalOp as a content type. Use the Assets,

Syslog, and Sensor Monitoring indices for the Sensor content type.

The table immediately updates to show ingested Interflow records.

You can also find assets from Cybereason Sensor content reported in the Assets | Asset
Analytics | IP Identified Assets view.

If you configured the connector Respond actions, refer to External Actions: Contain Host to
understand how to work with the Contain Host feature.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

