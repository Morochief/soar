Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Trend Micro Apex Central
Connectors

This connector allows you to discover Trend Micro Apex Central’s managed product servers and
security agents assets, and add those to the Stellar Cyber data lake for analysis and threat
hunting.

This topic refers to configuring a Trend Micro Apex Central connector. Also see:

Configuring Trend Micro Cloud One Connectors
Configuring Trend Micro Vision One Connectors

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Trend Micro Apex Central

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

Agents

Servers

Syslog

Assets (for
Agents and
Servers)

msg_class:

trendmicro_apexcent
ral_agents

trendmicro_apexcent
ral_servers

Content Type

Index

Locating Records

msg_origin.source:

trendmicro_apexcent
ral

msg_origin.vendor:

trendmicro

msg_origin.category:

endpoint

Domain

<User URL>

where <User URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Application ID, API Key, and User URL

Adding a Trend Micro Apex Central Connector
To add a Trend Micro Apex Central connector:

1. Obtain Authentication details for Stellar Cyber integration
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

 Use our example as a guideline, as you might be using a different software version.

Obtaining Authentication Details for Stellar Cyber
Integration
Before you add a Trend Micro Connector, you must obtain information that allows the Stellar
Cyber connector to authenticate correctly.

1. Log in to the Trend Micro Apex Central console as the user who will be associated

with the Stellar Cyber app (http://manage.trendmicro.com).

2. When the console has loaded, make note of the redirected URL associated with that

user's login:

3. Navigate to Administration > Settings > Automation API Access Settings.

4. Click Add. The Application Access Settings pane displays.

Application Name: This is to identify the application as being for use with
Stellar Cyber

Application ID: Used by Trend Micro Apex Central to identify Stellar Cyber

API key: Used by the Stellar Cyber to sign requests sent to Trend Micro Apex
Central

API type: Indicates the API functions that the Stellar Cyber will be using
(Isolate/Restore endpoints)

5. Ensure that the checkbox for Enable application integration using Apex Central

Automation APIs is selected.

6. Configure the following settings.

Application name: Specify an easily identifiable name for the application.

Communication time-out: Optionally adjust the number of seconds allowed
for a request to reach Trend Micro Apex Central (default is 120 seconds).

7. Note all the information for use later. Click Save.

The Automation API Access Settings screen appears and displays the newly added
application in the table.

Adding the Connector in Stellar Cyber
After you have noted the authentication information from the Trend Micro app integration steps,
you can add the Trend Micro Apex Central connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose the Trend Micro Apex Central connector.

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

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Enter the Application ID. This is the ID associated with the application you created in

Trend Micro Apex Central.

13. Enter the API Key. This is the key associated with the application you created in Trend

Micro Apex Central.

14. Enter the User URL. This is the URL unique to the user whose account was used to

create the application in Trend Micro Apex Central.

 For release versions prior to v4.3.4, ensure the URL does not include a trailing "/"

symbol.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Choose the Interval (min). This is how often the logs are collected.

17. Choose the Content Type you would like to collect. The logs for Agents and Servers

are supported.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

For Agents and Servers, change the Indices to Syslog.

For Agents and Servers, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

