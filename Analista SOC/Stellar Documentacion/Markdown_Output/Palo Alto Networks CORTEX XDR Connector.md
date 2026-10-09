Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Palo Alto Networks CORTEX XDR
Connectors

This connector allows Stellar Cyber to ingest logs from Palo Alto Networks CORTEX XDR and
add the records to the data lake and, optionally, to issue the Isolate Endpoint response action.

The Palo Alto Networks CORTEX XDR connector integrates with the Palo Alto Networks
CORTEX XDR API to process XDR information and query for several content types.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Palo Alto Networks CORTEX XDR

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: Yes

Runs on: DP

Interval: N/A

Collected Data

Content Type

Index

Locating Records

Alerts

Audit Agent Report Logs

Audit Management Logs

Syslog

Assets (for
Endpoints)

Endpoints

Incidents

Risky Hosts

Risky Users

msg_class:

palo_alto_networks
_cortex_xdr_alerts

palo_alto_networks
_cortex_xdr_events

palo_alto_networks
_cortex_xdr_audit_
agent_report_logs

Content Type

Index

Locating Records

Users

palo_alto_networks
_cortex_xdr_audit_
management_logs

palo_alto_networks
_cortex_xdr_endpoi
nts

palo_alto_networks
_cortex_xdr_incide
nts

palo_alto_networks
_cortex_xdr_risky_
hosts

palo_alto_networks
_cortex_xdr_risky_
users

palo_alto_networks
_cortex_xdr_users

msg_origin.source:

palo_alto_networks
_cortex_xdr

msg_origin.vendor:

palo_alto_networks

msg_origin.category:

endpoint



The Alerts Content Type can result in more than one msg_class as follows:

one palo_alto_networks_cortex_xdr_alerts

multiple palo_alto_networks_cortex_xdr_events

You cannot select palo_alto_networks_cortex_xdr_events as a Content Type.

Domain

<FQDN>

where <FQDN> is a variable from the configuration of this connector

Response Actions

Action

Isolate Endpoint

(Use the Revert button in Automation
| Action History under the Endpoint
Actions tab to unisolate the endpoint.)

Required Fields

endpoint_id

Third Party Native Alert Integration Details

This connector ingests logs from Palo Alto Networks CORTEX XDR to get the raw alerts that are stored in
the Syslog index. Select the Alerts content type.

Stellar Cyber maps Palo Alto Networks CORTEX XDR alerts. The alerts are read from the Syslog index,
enriched with Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and palo_alto_networks.alert_id.

There are the following categories of alerts:

PAN NGFW

XDR Agent

XDR Analytics BIOC*

XDR BIOC*

XDR IOC

* Behavioral Indicator of Compromise (BIOC)

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

API Key ID, API Key, and FQDN

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class: palo_alto_networks_cortex_xdr AND _exists_: event.threat.name

Adding a CORTEX XDR Connector
To add a Palo Alto Networks CORTEX XDR connector:

1. Obtain credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining CORTEX XDR Credentials
Before you configure the connector in Stellar Cyber, you must obtain the following Palo Alto
Networks CORTEX XDR credentials:

API Key ID

API Key

 The API Key has an optional expiration time that can be set by the user.

FQDN

Follow the guidance in Cortex XDR documentation for Get Started with Cortex XDR APIs .

To generate the API Key:

1. Log in as an administrative user to the CORTEX XDR portal .

2. Navigate to Settings | Configurations.

3. In Configurations, select API Keys under Integrations.

4. In the top-right corner, click New Key.

5. In the Generate API Key page, select either Standard or Advanced for the Security
Level of the API key, then select the Role that gives you the appropriate access level
for this key.

 Ensure that the role associated with the account has permission for the content

type.

For Standard:

For Advanced:

 To integrate with CORTEX XSOAR, you must generate an Advanced key.

6. Click Generate.

7. Copy the API key, which you will need when configuring the connector in Stellar Cyber.

 Store the API key in a safe location. It cannot be retrieved later although it can be

regenerated.

8. Click Close.

9. In the API Keys page, locate the API key in the table and note the API key ID, which

you will need when configuring the connector in Stellar Cyber.

10. In the API Keys page, select the API key in the table and click Copy API URL. This is

the FQDN, which you will need when configuring the connector in Stellar Cyber.

 When you copy the API URL, it has the format: https://api-{fqdn}, however when
you enter the FQDN in the next section, do not include the https://api- prefix, but
enter the {fqdn} only.

 You can test authentication by referring to Get Started with Cortex XDR APIs .
With Advanced API keys, use the provided Python 3 example. With Standard API
keys, use either the cURL example or the Python 3 example.

Adding the Connector in Stellar Cyber
To add a Palo Alto Networks CORTEX XDR connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Palo Alto Networks CORTEX XDR from the Type dropdown.

The asterisk (*) indicates a required field.

6. Choose the Function: Collect to collect logs; Respond to isolate endpoints, or both

functions.

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

12. Enter the API Key ID you noted above in Obtaining CORTEX XDR Credentials.

13. Enter the API Key you noted above.

14. Enter the FQDN you noted above.

 When you copy the API URL in Obtaining CORTEX XDR Credentials, it has the

format: https://api-{fqdn}, however when you enter the FQDN here, do not include
the https://api- prefix, but enter the {fqdn} only.

15. Choose the Content Type you would like to collect. The logs for Endpoints, Alerts,

Audit Agent Report Logs, Audit Management Logs, Incidents, Risky Hosts, Risky
Users, and Users are supported.

  The Endpoints content type is always selected and cannot be removed from the

configuration as it is required for host information.

 The logs for Endpoints, Risky Hosts, Risky Users, and Users are queried every

24 hours.

The content types require different licenses as follows:

Content Type

Alerts

Required License

Cortex XDR Prevent, Cortex XDR Pro per Endpoint, or

Cortex XDR Pro per GB

Audit Agent Report Logs

Cortex XDR Prevent, Cortex XDR Pro per Endpoint, or

Cortex XDR Pro per GB

Audit Management Logs

Endpoints

Incidents

Risky Hosts

Risky Users

Users

Cortex XDR Prevent or Cortex XDR Pro per Endpoint

Cortex XDR Prevent, Cortex XDR Pro per Endpoint, or

Cortex XDR Pro per GB

Identity Threat Module

Identity Threat Module

Cortex XDR Pro per Endpoint, Cortex XDR Pro, or Cortex

XDR Pro per GB

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

For all content types, change the Indices to Syslog.

For Endpoints only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

