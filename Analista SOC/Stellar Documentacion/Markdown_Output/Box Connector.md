Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Box Connectors

Connectors allow Stellar Cyber to collect data from external sources and add it to the data lake.
There can be any number of Box connectors active.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Box

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Events

Index

Syslog

Locating Records

msg_class:

N/A

msg_origin.source:

box_content_cloud

msg_origin.vendor:

box

msg_origin.category:

saas

Domain

https://api.box.com

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Client ID, Client Secret, and Enterprise ID

Adding a Box Connector
To add a Box connector:

1. Use the Box Developer Console to set up a new Custom App for Stellar Cyber
2. Use the Box Admin Console to authorize the new app
3. Use the Box Admin Console to obtain the Enterprise ID
4. Add the connector in Stellar Cyber
5. Test the connector
6. Verify ingestion

 Use our example as a guideline, as you might be using a different software

version.

Setting up New App in Box and Obtaining Client ID /
Secret
Stellar Cyber must be added as a custom app in your Enterprise Box account. During this
process you will need to make note of your Client ID and Client Secret.

1. Log in to the Box Developer Console with administrative privileges

(http://app.box.com/developers/console). If you logged in to box.com instead, select
Dev Console from the navigation pane.

2. Select the My Apps pane, and then click Create New App. Note that these instructions

are based on creating a Custom App, not an Enterprise App.

The Custom App dialog opens.

3. Select the Server Authentication (Client Credentials Grant) option, supply an App

Name, and click Create App.

4. The new Box application appears in the My Apps pane. Open it.

5. From the Configuration tab, copy the Client ID and save it to a temporary location for

later use in the setup process (refer to the image in the next step).

6. Click the Fetch Client Secret button to retrieve the client secret. Save it to the same

temporary location where you copied the Client ID.

 Note that 2-Step Verification must be enabled for your account before you can use
the Fetch Client Secret button. If it is not already enabled, you can turn it on on the
Account Settings | Account tab, as illustrated below:

7. Ensure that App Access Level is set to App + Enterprise Access.

8. Click on the General Settings tab for your app and copy the Enterprise ID shown

there to the same location where you stored the Client ID and Client Secret.

9. Click on the Configuration tab, scroll down to Application Scopes, and enable each

of the options found there:

10. Navigate to the Authorization tab and click the Review and Submit button to send

your request for application authorization to an Admin user.

11. Exit the Box Developer Console.

Authorizing Stellar Cyber to Access the Box Account
Stellar Cyber must be authorized using the Client ID you obtained above.

Use the Box Admin Console to access your Box account.

1. Log in to your Box Admin Portal as an administrative user.

2. Select the menu option for Admin Console.

3. Select the Apps entry in the left navigation panel and click on the Custom Apps

Manager tab.

4. Click the Add App button, enter the Client ID you created for Stellar Cyber application,

and click Next.

5. Review the information in the dialog that appears and click Authorize.

6. Review the list of applications in the Custom Apps Manager and ensure your new

application is displayed.

Obtaining the Box Enterprise ID
At this point, you have a Client Secret and Client ID. If you have not already noted the
Enterprise ID for your Box account, use this procedure to obtain it.

1. Still logged into your Box Admin Portal as an administrative user with Enterprise

access rights, select Account & Billing on the navigation menu.

2. Make note of the Enterprise ID listed in the displayed Account Information section.

Adding the Connector in Stellar Cyber
Now you are ready to add and configure the Box connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose SaaS from the Category dropdown.

5. Choose Box from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

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

12. Enter the Client ID you noted above.

13. Enter the Client Secret you noted above.

14. Enter the Enterprise ID you noted above.

15. Choose the Interval (min). This is how often the logs are collected.

16. Choose the Content Type you would like to collect. The logs for Events are supported.

17. Click Next. The final confirmation tab appears.

18. Click Submit.

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

2. Select the Indices for Syslog.

The table immediately updates to show ingested Interflow records.

For more information on working with events, refer to Understanding the Event Display.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

