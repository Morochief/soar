Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Trellix (FireEye) Endpoint Security
HX Connectors

This connector allows Stellar Cyber to ingest logs from FireEye (Trellix) HX and add the records
to the data lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Trellix (FireEye) Endpoint Security
HX

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Alerts

Hosts

Host Sets

All content type goes to Syslog index.

Hosts content also goes to Assets index.

Alerts content is mapped from Syslog to the
Alerts index as noted below.

Locating
Records

ms
g_
cla
ss:

fi
re
ey
e_
al
er
ts

Content Type

Index

Locating
Records

fi
re
ey
e_
ho
st
s

fi
re
ey
e_
ho
st
_s
et
s

ms
g_
ori
gin
.so
urc
e:

fi
re
ey
e_
hx

ms
g_
ori
gin
.ve
nd
or

fi
re
ey
e

ms
g_
ori
gin
.ca
teg
ory
:

en
dp
oi
nt

Domain

https://<Hostname>

where <Hostname> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

Stellar Cyber identifies the FireEye data logged into the Syslog index. Select the Alerts content type.

Records of the type Alerts are then normalized, enriched, and mapped to the Alerts index. The following
fields are included as part of the Stellar Cyber alert description: indicator.name and agent.url. Each
relevant Syslog record is compared against existing records in the Alert index and not added to that index
if the values in the following fields match those of an existing record logged in the previous 24
hours: org_id, tenantid, user.name, host.ip, event.name, file.path, process.path.

The following four alert types are supported: IOC, MAL, AMSI, and PROCGUARD. Tactic and Technique
are based on alert type.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Hostname: This is your Trellix (FireEye) Endpoint Security HX host.

ID: This is the username with at least api_analyst role.

Password: This is the password for the above user.

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
queries:

msg_class: fireeye_alerts AND fireeye.source: AMSI

msg_class: fireeye_alerts AND fireeye.source: IOC

msg_class: fireeye_alerts AND fireeye.source: MAL

msg_class: fireeye_alerts AND fireeye.source: PROCGUARD

Adding a Trellix (FireEye) Endpoint Security HX
Connector
To add a Trellix (FireEye) Endpoint Security HX connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining your Trellix (FireEye) Endpoint Security
HX Credentials
Configuring your Stellar Cyber connector requires the following details from your HX deployment:

Hostname: This is your HX host. Example: hexbyd438-hx-webui-
1.hex01.helix.apps.fireeye.com.

ID: This is the username at least api_analyst role. (Refer
to: https://fireeye.dev/docs/endpoint/authentication/ ) for guidance creating this user
and password).

Password: This is the password for the above user.

 The password should not include non-ASCII special characters.

Adding the Connector in Stellar Cyber
With the access information handy, you can add the Trellix (FireEye) Endpoint Security HX
connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Trellix (FireEye) Endpoint Security HX from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.

It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Hostname using the information you noted above in Obtaining your Trellix

(FireEye) Endpoint Security HX Credentials.

 Do not include https in the Hostname.

13. Enter the ID you noted above.

14. Enter the Password for this ID.

15. Choose the Interval (min). This is how often the logs are collected.

 The interval setting applies to the Alerts content type. The logs for Hosts and

Host Sets are queried every 24 hours.

16. Choose the Content Type. The logs for Alerts, Host Sets, and Hosts are supported.

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

Did you configure the connector correctly?

Request

connector configuration.

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

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

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Alerts, Host Sets, and Hosts, change the Indices to Syslog.

For Hosts only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

