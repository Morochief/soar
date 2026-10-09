Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Deep Instinct Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.
Review the content in this topic to understand what type of data can be collected and acted upon
for this connector type.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Deep Instinct

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Devices

Events

Syslog, Alerts

Suspicious Events

Syslog

Index

API

Syslog, Assets

https://<custo
mername>.custo
mers.deepinsti
nctweb.com/api
/v1/devices

https://<custo
mername>.custo
mers.deepinsti
nctweb.com/api
/v1/events/

https://<custo
mername>.custo
mers.deepinsti
nctweb.com/api

Content Type

Index

API

/v1/suspicious
-events/

Domain

https://<Hostname>

where <Hostname> is a variable from the configuration of this connector

Response Actions

Action

Required Fields

Contain (Isolate) Host

deep_instinct_asset and deep_instinct.id or

deep_instinct_suspiciousevent and
device_id or

deep_instinct_maliciousevent and
device_id

A
PI

h
t
t
p
s
:
/
/
<
c
u
s
t
o
m
e
r
n
a
m
e
>
.
c
u
s
t
o
m
e
r
s
.
d
e
e
p
i
n
s
t
i
n
c
t
w
e
b

Action

Required Fields

A
PI

.
c
o
m
/
a
p
i
/
v
1
/
d
e
v
i
c
e
s
/
a
c
t
i
o
n
s
/
i
s
o
l
a
t
e
-
f
r
o
m
-
n
e
t
w
o
r
k

h
t
t
p
s
:
/
/
<
c
u
s
t
o

Action

Required Fields

A
PI

m
e
r
n
a
m
e
>
.
c
u
s
t
o
m
e
r
s
.
d
e
e
p
i
n
s
t
i
n
c
t
w
e
b
.
c
o
m
/
a
p
i
/
v
1
/
d
e
v
i
c
e
s
/
a
c
t
i
o
n
s
/

Action

Required Fields

A
PI

r
e
l
e
a
s
e
-
f
r
o
m
-
i
s
o
l
a
t
i
o
n

Third Party Native Alert Integration Details

Devices

Events

This content is not applicable for alerts.

Yes. Records with MITRE | ATT&CK values are de-
duplicated, enriched with Stellar Cyber fields, and
mapped to the Stellar Cyber xdr_event record. If the
incoming Tactic or Technique are blank, the following
values are assigned in Stellar Cyber:
tactic_name= XDR Malware
technique_name = XDR Miscellaneous Malware

Suspicious Events

No.

 For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Hostname and API Token

For Collect, the API token must be created with at least READ_ONLY permission

For Respond, READ_AND_REMEDIATION permissions are required

Locating Records

Use the following to query for records:

msg_origin.vendor: deep_instinct

msg_origin.category: asset, endpoint

msg_origin.source: deep_instinct

msg_class: deep_instinct_asset, deep_instinct_maliciousevent,
deep_instinct_suspiciousevent

Adding a Deep Instinct Connector

To add a Deep Instinct connector:

1. Obtain a Deep Instinct API token
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining a Deep Instinct API Token
As part of this procedure, you specify the credentials of an account on the Deep Instinct server
that will be used to retrieve data.

1. Log into your Deep Instinct Dashboard as an administrative user. Make note of the

fully qualified domain name portion of the URL you used to log in (e.g., just
mycompany.customer.deepinstinct.com). You will need this when you configure the
Stellar Cyber connector.

2. From the Dashboard navigation pane, select Integration & Notification.

3. In the pane that loads, click the link for API Connectors, shown above.

4. Click the button to Create an API Connector.

5. In the Add API Connector dialog, create a name, select the Tenants you want to be
able to use this API connector with Stellar Cyber and specify the Permissions. The
minimum permission required is READ_ONLY. For Respond actions , you must include
READ_AND_REMEDIATION permissions.

6. Click OK to save the settings and create the API Key. The API Connectors pane

displays.

7. Click the API key you created to display it, then copy the key.  Save that key for use

when you configure the Stellar Cyber connector.

Adding the Connector in Stellar Cyber
To add the Deep Instinct connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Deep Instinct from the Type dropdown.

The asterisk (*) indicates a required field.

6. Choose whether you want to only Collect or also Respond.

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

12. Enter the Hostname. This is the FQDN portion of the URL you used for your Deep

Instinct dashboard login, above (for example, mycompany.customer.deepinstinct.com).

13.   Do not include https in the field.

14. In the API Token field, enter the API key you created above.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type. The logs for Devices, Events, and Suspicious Events are

supported.

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

2. Set the Indices to match the type of content you collected:

For Devices, change the Indices to Syslog or Assets. Note that hosts
discovered through this connector show Deep Instinct as a data source.

For Events, change the Indices to Syslog or Alerts.

For Suspicious Events, change the Indices to Syslog.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

