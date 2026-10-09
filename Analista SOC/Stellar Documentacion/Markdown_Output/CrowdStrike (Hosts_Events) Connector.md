✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring CrowdStrike (Hosts/Events)
Connectors
Stellar Cyber's CrowdStrike connector integrates CrowdStrike's streaming API to collect
detections and events with the existing connector capability that collects host information.
Integration with CrowdStrike enhances Stellar Cyber's threat detection and response capabilities
by providing real-time visibility into endpoint security events and enabling automated incident
response workflows to contain and mitigate threats. Combining CrowdStrike's endpoint
protection with Stellar Cyber's advanced security analytics and machine learning algorithms
provides a comprehensive security solution for organizations.
Through the Vulnerability content type and the Vulnerability Management API, this connector
supports CrowdStrike Falcon Spotlight.
With this CrowdStrike connector, you can also perform response actions (contain or hide hosts)
on the assets that CrowdStrike Falcon manages.
 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.
Connector Overview: CrowdStrike
Capabilities
Collect: Yes
Respond: Yes
Native Alerts Mapped: Yes
Runs on: DP
Interval: Configurable (Applicable only to Hosts)
Collected Data

| Content Type              |     | Index          | Locating Records |
| ------------------------- | --- | -------------- | ---------------- |
| Host                      |     | Syslog, Assets | msg_class:       |
| File Integrity Monitoring |     | Scans (for     | crowdstrike_host |
Vulnerability)
crowdstrike_fim
Vulnerability
crowdstrike_vulner
Events:
ability
AuthActivityAuditEvent
crowdstrike_<Event
CSPMIOAStreamingEvent
label> (example:
| CSPMSearchStreamingEvent |     |     | crowdstrike_FirewallMat |
| ------------------------ | --- | --- | ----------------------- |
chEvent)
CustomerIOCEvent
crowdstrike_detect
DetectionSummaryEvent
ion_summary
EppDetectionSummaryEvent
crowdstrike_<event
type from metadata
in streaming API>
| FirewallMatchEvent |     |     | (example:               |
| ------------------ | --- | --- | ----------------------- |
| HashSpreadingEvent |     |     | crowdstrike_XdrDetectio |
nSummaryEvent)
IdentityProtectionEvent
IDPDetectionSummaryEvent
msg_origin.source:
IncidentSummaryEvent
crowdstrike
MobileDetectionSummaryEvent
| ReconNotificationSummaryEvent |     |     | msg_origin.vendor: |
| ----------------------------- | --- | --- | ------------------ |
| RemoteResponseSessionEndEvent |     |     | crowdstrike        |
RemoteResponseSessionStartEven
| t   |     |     | msg_origin.category: |
| --- | --- | --- | -------------------- |
ScheduledReportNotificationEvent
endpoint
UserActivityAuditEvent
Other Events
Domain
<Base URL>
where <Base URL> is a variable from the configuration of this connector
Response Actions
| Action | Required Fields | API |     |
| ------ | --------------- | --- | --- |
Contain (Isolate)
|      | dstip, srcip, or | https://api.crowdstrike.com//devices |     |
| ---- | ---------------- | ------------------------------------ | --- |
| Host |                  | /entities/devices-actions/v2 with    |     |
hostip
| Hide Host |     | parameters of |     |
| --------- | --- | ------------- | --- |
host ID or device ID and an action which is
one of contain, lift_containment, hide_host or
unhide_host.
Third Party Native Alert Integration Details
This connector ingests logs from CrowdStrike to get the raw alerts that are stored in the Syslog index.
Select the EppDetectionSummaryEvent content type or the crowdstrike_{metadata.eventType}
(example: crowdstrike_XdrDetectionSummaryEvent) default content type.

Stellar Cyber maps CrowdStrike events. The events are read from the Syslog index, enriched with Stellar
Cyber fields, and mapped (with deduplication) to the Alerts index.
Deduplication is by tenantid and crowdstrike.event.CompositeId.
For details, see Integration of Third Party Native Alerts.
Required Credentials and Configurations
Base URL, Client ID, and Client Secret
The API Key must have the following:
For Hosts, enable Read and Write to collect and to contain or hide hosts as a response
action.
For Vulnerabilities, enable Read to access the Vulnerability Management API.
For Audit Events and Detections, enable Read for those as well as Read for Event
Streams.
Locating Records
To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: ((msg_class:crowdstrike_detection_summary AND
crowdstrike.metadata.eventType:EppDetectionSummaryEvent AND _exists_:
event.threat.name) OR msg_class: crowdstrike_XdrDetectionSummaryEvent)
Adding a CrowdStrike Connector
To add a CrowdStrike connector in Stellar Cyber:
1. Generate the CrowdStrike Falcon API key you will use in Stellar Cyber
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify that assets are received from CrowdStrike
Generating the CrowdStrike Falcon API Key
With streaming APIs enabled, you can generate the CrowdStrike Falcon API key:
 Use our example as a guideline, as you might be using a different software version.
1. Log in to CrowdStrike Falcon at https://falcon.crowdstrike.com/ .
2. Click API Clients and Keys.
The API Clients and Keys page appears.
3. Click Add new API client.

The Add new API client window appears.
4. Enter the Client Name.
5. Enable Read and Write for Hosts to contain or hide hosts as a response action.
Enable Read for Vulnerabilities to access the Vulnerability Management API.
Enable Read for Event Streams and the following content, if you also want to collect
the corresponding data: Audit Events and Detections.
 Read for Event Streams is required for the content other than Hosts, as of v4.3.5.
6. Click Add. The API client created window appears.
7. Copy the Client ID and Secret and note the Base URL. You will need these in the next
section.
Adding the Connector in Stellar Cyber
With the configuration information handy, you can add the CrowdStrike connector in Stellar
Cyber:
1. Log in to Stellar Cyber.
2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.
3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.
4. Choose Endpoint Security from the Category dropdown.
5. Choose CrowdStrike from the Type dropdown.
The asterisk (*) indicates a required field.
6. Choose the Function. If you want to collect logs, click the Collect check-box. If you
want to contain or hide hosts, click the Respond check-box.
7. Enter a Name.
 Notes:
This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.
8. Choose a Tenant Name. Use of the connector is restricted to the tenant you select.
9. Choose the device on which to run the connector.
10. (Optional) When the Function is Collect, you can apply Log Filters. For information,
see Managing Log Filters.
11. Click Next. The Configuration tab appears.
The asterisk (*) indicates a required field.
12. Enter the Base URL. This is the URL of your CrowdStrike portal, and can be:
US: api.crowdstrike.com
US-2: api.us-2.crowdstrike.com

EU-1: api.eu-1.crowdstrike.com
US-GOV-1: api.laggar.gcw.crowdstrike.com
 If you are using a government account, contact CrowdStrike support to
enable event streaming.
13. Enter the Client ID you noted above in Generating the CrowdStrike Falcon API Key.
14. Enter the Client Secret you noted above.
15. Enter the Interval (min) if you chose Collect. This is how often the logs are collected
for Host content.
 Interval is applicable only to Host content because the other types are collected
with a streaming API.
16. Select the Content Type for which you enabled the API key. You can filter the event
types you want to include or exclude, using these content tags:
FirewallMatchEvent
Host
HashSpreadingEvent
File Integrity Monitoring
IdentityProtectionEvent
IDPDetectionSummaryEvent
Vulnerability
IncidentSummaryEvent
Assorted Events: MobileDetectionSummaryEvent
AuthActivityAudi ReconNotificationSummaryEvent
tEvent
RemoteResponseSessionEndEvent
CSPMIOAStrea
RemoteResponseSessionStartEvent
mingEvent
ScheduledReportNotificationEvent
CSPMSearchStr
eamingEvent UserActivityAuditEvent
CustomerIOCEv
Other Events: (Use this tag if you want to
ent
DetectionSumm collect event types not specifically listed above)
aryEvent
EppDetectionSu
mmaryEvent
You can optionally add the type Other Events to collect any remaining content types.
17. Click Next. The final confirmation tab appears.
18. Click Submit.
The new connector is immediately active. You can now contain or hide hosts from the event
display, and view or edit those actions on the Endpoint Actions page.
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
using the X button. If the test fails, you can select the  button from the same row to review and
correct issues.
 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.
Repeat the test as needed.
Display sample messages...
Success ! Failure with summary of issue:
Show More example detail:
If the test fails, the common HTTP status error codes are as follows:

HTTP E HTTP Stan
rror dard Error Explanation Recommendation
Code Name
400 Bad This error occurs when there is an error in the
Did you configure the connector correctly?
Request connector configuration.
401 Unauthorize
This error occurs when an authentication credential is Did you enter your credentials correctly?
d
invalid or when a user does not have sufficient
Are your credentials expired?
privileges to access a specific API.
Are your credentials entitled or licensed for that
specific resource?
403 Forbidden This error occurs when the permission or scope is not
Did you enter your credentials correctly?
correct in a valid credential.
Do you have the required role or permissions for
that credential?
404 Not Found This error occurs when a URL path does not resolve Did you enter your API URL correctly?
to an entity.
429 Too Many
This error occurs when the API server receives too The server or user license/quota will eventually
Requests
much traffic or if a user’s license or entitlement quota recover. The connector will periodically retry the
is exceeded. query.
If this occurs unexpectedly or too often, work with
your API provider to investigate the server limits,
user licensing, or quotas.
For a full list of codes, refer to HTTP response status codes .
Verifying Content
To verify Stellar Cyber is receiving content from CrowdStrike:
For Host:
1. Select Assets | Asset Analytics.
2. Select the MAC-Identified Assets tab.
3. Enter crowdstrike in the Search field. The results list is updated.
For other content:
1. Select Threat Hunting.
The Interflow Search tab appears.
2. Change the Indices for the type of content you collected:
For all content types, change the Indices to Syslog.
For Host only, change the Indices to Assets.
For Vulnerability only, change the Indices to Scans.
The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  