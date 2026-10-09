Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Oracle Cloud Infrastructure (OCI)
Streaming Connectors

This connector allows Stellar Cyber to ingest logs from the Oracle Cloud Infrastructure (OCI) and add the
records to the data lake.

OCI integration with Stellar Cyber provides advanced threat detection and response capabilities, combining
Oracle's security solutions with real-time threat intelligence and automated response workflows to improve
case response and threat mitigation.

This connector queries the Oracle Streaming Service to collect log data found within a provided stream name.
The stream can be configured for different log types.

Note the following streaming limits in the Oracle Cloud Infrastructure documentation, Limits on Streaming
Resources .

This connector enables horizontal scaling of OCI connectors. It uses the consumer group feature of
OCI Streaming to handle offsets and partitions. You can manually create multiple OCI connectors for a single
stream with multiple partitions. It is recommended that the number of OCI connectors be less than or equal to

the number of partitions.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data when the

ingestion volume is large, which potentially can lead to data loss. This can happen when the processing
capacity of the collector is exceeded.

Connector Overview: OCI Streaming

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: N/A

Collected Data

Content Type

Log data in provided Stream Name

Index

Syslog

Locating Records

msg_class:

oracle_cloud_audit (if
oracle.oracle.loggroupid is
_Audit)

Content Type

Index

Locating Records

oracle_cloud_guard (if
oracle.source starts with
CloudGuard (case insensitive))

oracle_vcnflow (for VCN flow
logs)

oracle_cloud_waf (if
oracle.type.keyword.is
com.oraclecloud.loadbalance

r.waf)

oracle_cloud_log (default)

msg_origin.source:

oracle_cloud_infrastructu
re

msg_origin.vendor:

oracle

msg_origin.category:

paas (default)

waf (if oracle.type.keyword.is
com.oraclecloud.loadbalance

r.waf)

 If the OCI log type is com.oraclecloud.vcn.flowlogs.DataEvent, VCN flow log information is reported in the

Traffic Index.

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from OCI to get the raw alerts that are stored in the Syslog index.

Stellar Cyber maps OCI CloudGuard alerts. The alerts are read from the Syslog index, enriched with Stellar Cyber fields,
and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid, oracle.data.additionalDetails.tenantId, event.threat.name, and
cloud.resource.id.

The resource types include instances, buckets, and others.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

Bootstrap Server, Username, Auth Token, and Stream Name

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the query: msg_class:
oracle_cloud_guard AND _exists_:event.threat.name

Adding an OCI Streaming Connector
To add an OCI Streaming connector:

1. Obtain your OCI credentials

2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining your OCI Credentials
Follow the guidance in the Oracle documentation cited in OCI Settings to create the credentials for Stellar
Cyber API calls.

OCI Settings

To configure the OCI settings:

1. Log in as an administrative user to the Oracle Cloud console.

2. Skip this step if you have a compartment already. To create a compartment, refer to the Oracle
documentation for Adding Users , search for Create a sandbox compartment, and follow the
procedure. In this example, the compartment is Log-compartment.

3. To create a user and group, navigate to Domains.

By default, there are two domains in OCI. Select the domain in which you want to create a group and
user. In the next step, the example group is created in the Default domain.

4. To create a group, refer to the Oracle documentation for Adding Users , search for Create a group,

and follow the procedure. In this example, the group is Group-log.

5. To create a user, refer to the Oracle documentation for Adding Users , search for Create a user, and
follow the procedure. In this example, the user is demouser@stellarcyber.ai. Then, add the user to the
group. In this example, the group is Group-log in the Default domain.

6. Review the Oracle documentation for How Policies Work . In the root compartment, create a policy

with the following syntax:

Allow group <identity_domain_name>/<group_name> to <verb> <resource-type>
in compartment <compartment_name>

In this example, the group is Group-log in the Default domain and the compartment is Log-
compartment:

Allow group default/Group-log to use stream-pull in compartment Log-
compartment

In another example, there is a user, loguser@stellarcyber, in the group Group-IDCS-log of the
OracleIdentityCloudService, and the compartment is Log-compartment, so the policy will be:

Allow group OracleIdentityCloudService/Group-IDCS-log to use stream-pull in
compartment Log-compartment

7. To set up streaming, review the Oracle documentation for Creating a Stream .

8. To create and configure the Oracle Streaming Service, navigate to Analytics & AI and choose

Streaming under Messaging.

9. Click Create Stream. Add a Stream Name and select the compartment you created earlier. In this
example, the compartment is Log-compartment. If you are creating a stream for the first time, a
default Stream Pool, DefaultPool, is created.

10. To create a Service Connector Hub, refer to the Oracle documentation for Creating a service

connector .

11. Create the connector under the compartment you created earlier.

 Under Configure service connector, note the Source, which is Logging, and the Target, which
is Streaming. They will be used to configure the OCI Streaming connector with a logging source.
Refer to the Oracle documentation for Creating a Connector with a Logging Source .

12. Navigate to Streams under Analytics and locate the stream's Stream Pool. In this example, the

stream name is loguser-stream and the stream pool is the DefaultPool. The compartment is Log-
compartment.

13. Navigate to the Kafka Connection Settings in the DefaultPool.

14. Configure the Kafka Connection Settings as follows:

The format for Bootstrap Servers is: cell-1.streaming.
<region>.oci.oraclecloud.com:9092. For this example, enter: cell-1.streaming.us-
phoenix-1.oci.oraclecloud.com:9092.

 The Bootstrap Servers is required for the OCI Streaming connector configuration.

The format for SASL Connection Strings is: username="
<OCI_tenancy_name>/<domain_name>/<your_OCI_username>/<stream_pool_OCID>
password="AUTH_TOKEN". For this example, enter:

Username:
stellarcyber/Default/StreamUser/ocid1.streampool.oc1.phx.amaaaaaa57526pia6
d4ng2pyndugjosjsehmibndthdxxxxxxxxxxxxxxxxx

or

Username:
stellarcyber/OracleIdentityCloudService/StreamUser/ocid1.streampool.oc1.ph
x.amaaaaaa57526pia6d4ng2pyndugjosjxxxxxxxxx

 The Username is required for the OCI Streaming connector configuration.

15. Navigate to Streams and note the stream name.

 The Stream Name is required for the OCI Streaming connector configuration.

16. To obtain the authentication token, log in using the newly created user, navigate to Profile, and click

My profile. In this example, the new user is demouser@stellarcyber.ai.

17. Navigate to Auth tokens and click Generate token, then note the token.

 The Auth Token is required for the OCI Streaming connector configuration.

Fetching Audit Logs

Once the stream is configured, you need to send audit logs to the configured stream.

Follow the guidance in the Oracle documentation for Creating a Connector with a Logging Source  to
transfer log data from the logging service to a target service.

You can also refer to Overview of Audit .

Log Data in the OCI Stream

Stellar Cyber ingests everything sent to the OCI stream. Most of what is ingested is stored in the Syslog index
verbatim. The exceptions are:

CloudGuard records, which Stellar Cyber normalizes. Stellar Cyber also has an alert integration with
OCI CloudGuard, which is described in Integration of Third Party Native Alerts.

VCN Flow records which Stellar Cyber normalizes and stores in the Traffic index. These records are
identified by the following field:

oracle.type: com.oraclecloud.vcn.flowlogs.DataEvent

Refer to the Oracle documentation: Overview of Streaming  or OCI Streaming FAQ .

Adding the Connector in Stellar Cyber
With the access information handy, you can add an OCI Streaming connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab cannot be
changed after you add the connector.

4. Choose PaaS from the Category dropdown.

5. Choose Oracle Cloud Infrastructure Streaming from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as tenantname-
connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information, see Managing

Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Bootstrap Server you noted above in Obtaining your OCI Credentials.

13. Enter the Username you noted above.

14. Enter the Auth Token you noted above.

15. Enter the Stream Name you noted above.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active.

Testing the Connector
When you add (or edit) a connector, we recommend that you run a test to validate the connectivity parameters
you entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60 seconds for new or

modified configuration details to be propagated to the sensor before performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure result. A
successful test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by using the X
button. If the test fails, you can select the   button from the same row to review and correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the connector status, but

if issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP Er

HTTP Standa

ror

rd Error

Explanation

Code

Name

Recommendation

400

Bad Request This error occurs when there is an error in the connector

Did you configure the connector correctly?

configuration.

401

Unauthorized

This error occurs when an authentication credential is invalid

Did you enter your credentials correctly?

or when a user does not have sufficient privileges to access a

Are your credentials expired?

specific API.

Are your credentials entitled or licensed for that specific

resource?

403

Forbidden

This error occurs when the permission or scope is not correct

Did you enter your credentials correctly?

in a valid credential.

Do you have the required role or permissions for that

credential?

404

Not Found

This error occurs when a URL path does not resolve to an

Did you enter your API URL correctly?

entity.

429

Too Many

Requests

This error occurs when the API server receives too much

The server or user license/quota will eventually recover.

traffic or if a user’s license or entitlement quota is exceeded.

The connector will periodically retry the query.

If this occurs unexpectedly or too often, work with your

API provider to investigate the server limits, user

licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For all logs, change the Indices to Syslog.

For VCN flow logs only, change the Indices to Traffic.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

