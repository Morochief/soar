Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Webroot Connectors

This connector allows Stellar Cyber to ingest logs from Webroot and add the records to the data
lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Webroot

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Blocked Traffic

Blocked Urls

Endpoints

Phishing

Threat History

Traffic Summary

Index

Syslog

Assets (for Endpoints)

Locating Records

msg_class:

webroot_block
ed_traffic

webroot_block
ed_urls

webroot_endpo
ints

webroot_phish
ing

webroot_threa
t_history

webroot_traff
ic_summary

Content Type

Index

Locating Records

msg_origin.source
:

webroot

msg_origin.vendor

webroot

msg_origin.catego
ry:

endpoint

Domain

https://unityapi.webrootcloudav.com

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Client ID, Client Secret, Username, Password, GSM key (Parent Keycode)

Adding a Webroot Connector
To add a Webroot connector:

1. Obtain Webroot credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Webroot Credentials
Use the following steps as a guide to obtain the credentials required to allow Stellar Cyber to
retrieve data with the Webroot API.

1. Access the Webroot Identity Portal  (Management Console) as the username and

password you will use to configure the Stellar Cyber connector. Make note of the login
information for later use.

 The password should not include non-ASCII special characters.

2. From the left navigation pane, select Settings.

3. When the Settings page displays, select the Unity API Access sub-tab.

4. Click the button to Create New Client Credential.

5. In the dialog that displays, specify a Name and Description for the credential, then

click Next.

6. On the next screen, enable the option to use the event notification API, specifying

Other use ... for the Purpose. Then click Next.

7. On the final screen, click Save.

8. The console displays a dialog with both the Client ID and the Client Secret. Make note
of both of these values. The Client Secret cannot be retrieved later, although it can be
regenerated.

9.  The final information you need is the Parent Keycode, which you will enter as the

GSM Key later. Click the sub-tab for Account Information and record the value for that
field.

10. Review your list of information before proceeding. You should now have:

Username

Password

Client ID

Client Secret

Parent Keycode (GSM key)

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Webroot connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Webroot from the Type dropdown.

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

12. Enter the following information you noted from the previous section:

Enter the Client ID.

Enter the Client Secret.

Enter the Username and Password.

Enter the GSM Key (Parent Keycode).

13. Choose the Interval (min). This is how often the logs are collected.

14. Chose the Content Type. The following are available:

Blocked Urls

Blocked Traffic

Endpoints

Phishing

Threat History

Traffic Summary

15. Click Next. The final confirmation tab appears.

16. Click Submit.

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

Resolving Error Messages for Webroot Connectors

In certain situations, the initial Test for a Webroot connector may report success but then
subsequently display an error message in the Messages column of the System |
INTEGRATIONS | Connectors page. Use the following information to resolve common error
messages for Webroot connectors:

WSAT is not enabled for this site

"{"statusCode":400,"requestId":"c60683f4-09a7-48c2-ae48-
c8df21e8bb90","error":"wsat_not_enabled","error_description":"WSAT is
not enabled for this site.","AdditionalInformation":{}}"

This error message appears when the Security Awareness Training feature in Webroot
is either not enabled or its subscription has expired. Try the following in Webroot:

Make sure that WSAT is enabled in Security Awareness Training > Settings
> Enable Security Awareness Training.

Make sure the Security Awareness subscription has not expired.

DNSP is not enabled for this site

{"statusCode":400,"requestId":"0e12a84d-1123-4c87-937b-
a6469ee52b3c","error":"dnsp_not_enabled","error_description":"DNSP is
not enabled for this site.","AdditionalInformation":{}}

This error message appears when the DNS Protection feature in Webroot is either not
enabled or its subscription has expired. Try the following in Webroot:

Make sure that the DNS Protection subscription in Webroot is not expired.

Make sure that the DNS Protection feature is set to On in Webroot.

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

