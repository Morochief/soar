Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Cynet Connectors

This connector allows Stellar Cyber to ingest logs from Cynet and add the records to the data
lake.

It also lets you lock down a device that is associated with an event reported by another
connector. In Stellar Cyber, this connector is used to contain (isolate) or shut down the host,
using Stellar Cyber actions.

 If you use a Cynet connector to perform a Contain Host or Shutdown Host action on a host
that is already disabled, shutdown, or otherwise not reachable, Cynet returns a status that
the request was successful which is reported in the Stellar Cyber UI. If you are not certain
whether an action was successful, you may verify it in the Cynet dashboard.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Cynet

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Alerts

Audit Logs

Hosts

Syslog

Assets (for
Hosts)

msg_class:

cynet_alert

cynet_audit_log

Content Type

Index

Locating Records

cynet_host

msg_origin.source:

cynet

msg_origin.vendor:

cynet

msg_origin.category:

endpoint

Domain

<Host URL>

where <Host URL> is a variable from the configuration of this connector

Response Actions

Action

Contain Host

Shutdown Host

Required Fields

Any value other than an IP Address in at least one of these fields:
hostip_host, srcip_host, computer_name, or host.name

Any value other than an IP Address in at least one of these
fields: hostip_host, srcip_host, computer_name, or
host.name

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Host URL, Username, Password, and Client ID

Adding a Cynet Connector
To add a Cynet connector in Stellar Cyber:

1. Obtain Cynet credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Cynet Credentials
To configure your Cynet connector in Stellar Cyber, you will need the following information from
your Cynet deployment:

URL for the Cynet API access (https://pov.api.cynet.com/)

Username

Password

 The password should not include non-ASCII special characters.

Client ID for the tenant (site) you want to manage (for MSSP configurations, you can
find the client id in Global Settings > Client Site Manager > Sites Status)

Adding the Connector in Stellar Cyber
With the configuration information handy, you can add the Cynet connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Cynet from the Type dropdown.

The asterisk (*) indicates a required field.

6. For Function, enable Collect. Or, if you want to contain hosts or shutdown hosts,

enable Respond.

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

12. Enter the Host URL. This is the URL noted above for API access.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Enter the Username you noted above.

14. Enter the Password you noted above.

15. Enter the Client ID you noted above.

16. Choose the Interval (min). This is how often the logs are collected.

17. Choose the Content Type you would like to collect. The logs for Hosts, Alerts, and

Audit Logs are supported.

  The Hosts content type is always selected and cannot be removed from the

configuration as it is required for host information.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

The Connector Overview appears.

The new connector is immediately active. For the Respond function, you can now contain hosts
from the event display, and view or edit those actions on the Endpoint Actions page.

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

2. Change the Indices for the type of content you collected:

For Hosts, Alerts, and Audit Logs, change the Indices to Syslog.

For Hosts only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

