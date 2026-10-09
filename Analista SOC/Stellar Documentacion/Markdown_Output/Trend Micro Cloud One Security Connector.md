Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Trend Micro Cloud One Workload
Security Connectors

This connector allows you to discover Trend Micro Cloud One Workload Security managed
computer assets, and add them to the Stellar Cyber data lake for analysis and threat hunting.

This topic refers to configuring a Trend Micro Cloud One Workload Security connector. Also see:

Configuring Trend Micro Apex Central Connectors
Configuring Trend Micro Vision One Connectors

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Trend Micro Cloud One

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

Syslog

Assets (for
Computers)

msg_class:

trendmicro_cloudone
_computers

msg_origin.source:

trendmicro_cloudone

Content Type

Index

Locating Records

msg_origin.vendor:

trendmicro

msg_origin.category:

endpoint

Domain

<API URL>

where <API URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

API URL and API Key

Adding a Trend Micro Cloud One Connector
To add a Trend Micro Cloud One Workload Security connector:

1. Obtain Authentication details for Stellar Cyber integration
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

 Use our example as a guideline, as you might be using a different software version.

Obtaining Authentication Details for Stellar Cyber
Integration
Before you add a Trend Micro Connector, you must obtain information that allows the Stellar
Cyber connector to authenticate correctly.

1. Log in to the Trend Micro Cloud One console as the user who will be associated with

the Stellar Cyber app (http://cloudone.trendmicro.com).

2. When the console has loaded, access the Workload Security screen:

3. Navigate to Administration > User Management > API.

4. Click Add. In the displayed dialog, add the following:

Name: This is the name you will use to identify the app as being associated
with Stellar Cyber

Role: Select Full Access.

5. Click Next.

6. The dialog updates to display the secret key for your new app. Make note of this for use

when you configure your connector. You cannot retrieve this key after you close the
dialog, so make note of it now. If you accidentally lose the information, you must create
a new app.

7. Click Close.

The API Keys screen appears and shows the newly added application in the table.

Adding the Connector in Stellar Cyber
After you have noted the authentication information from the Trend Micro app integration steps,
you can add the Trend Micro Cloud One Workload Security connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors.

The Connector Overview appears.

a. Click System | INTEGRATIONS | Connectors. The Connector Overview

appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Trend Micro Cloud One Workload Security from the dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name for the tenants who will have access to this connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next.

The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the API URL.

This is the API URL associated with the API key. Trend Micro legacy format is
https://cloudone.trendmicro.com/api , but migrated to a regional format as follows:
https://workload.{region}.cloudone.trendmicro.com/api (example: https://workload.us-
1.cloudone.trendmicro.com/api/).

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

13. Enter the API Key.

This is the Secret Key associated with the application you created above in the Trend
Micro Cloud One Workload Security console.

14. Choose the Interval (min).

This is how often the logs are collected.

15. Choose the Content Type you would like to collect.

The logs for Computers are supported.



Stellar Cyber gets the computer object, normalizes some of the fields, creates an
asset record, and populates Syslog. The fields in Syslog are
trendmicro_cloudone.<fieldname>, which may include any of the fields for
Computers as follows: https://cloudone.trendmicro.com/docs/workload-
security/api-reference/tag/Computers 

In addition, the computers are sent to the Assets | Asset Analytics page.

16. Select Next.

The final confirmation tab appears.

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

For Computers only, change the Indices to Syslog.

For Computers only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

