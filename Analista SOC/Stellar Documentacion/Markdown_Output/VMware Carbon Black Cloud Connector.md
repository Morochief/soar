Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring VMware Carbon Black Cloud
Connectors

This connector allows Stellar Cyber to ingest VMware Carbon Black Cloud alerts from an AWS
S3 bucket and add the alerts to the data lake.

It also supports the Contain Host response action.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: VMware Carbon Black Cloud

Capabilities

Collect: Yes

Respond: Yes

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Alert

Endpoint Event

Index

Syslog

Locating Records

msg_class:

Assets (for Alert)

carbonblack_alert

carbonblack_endpo

int_event

msg_origin.source:

carbonblack_cloud

Content Type

Index

Locating Records

msg_origin.vendor:

vmware_carbonblac
k

msg_origin.category:

endpoint

 If there is asset information in the logs for Events and Alerts, the detected assets are reported in the

Assets Index.

Domain

N/A

Response Actions

Action

Contain Host

Required Fields

device_id

The required permissions for response actions are device.quarantine (Execute), device (Read), and
device.bg-scan (Execute).

Third Party Native Alert Integration Details

Alerts of type CB Analytics, Device Control, and Watchlist. Select the Alert content type.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

For Collect: Carbon Black Organization Key, Bucket, Access Key ID, Secret Access Key, Alert
Prefix for Alert Collection, and Endpoint Event Prefix for Endpoint Event Collection

For Respond: Carbon Black Organization Key, Host, API secret key, and API ID

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_origin.source:carbonblack_cloud AND (event.type:(NON_MALWARE OR NEW_MALWARE
OR KNOWN_MALWARE OR RISKY_PROGRAM) OR (NOT _exists_:event.type AND
vmware_carbonblack.type: (CB_ANALYTICS OR DEVICE_CONTROL)))

Adding a VMware Carbon Black Cloud Connector
To add a VMware Carbon Black Cloud connector:

1. Obtain the VMware Carbon Black organization ID
2. Gather / Configure AWS S3 information
3. (Optional) Configure Carbon Black for Respond action
4. Add the connector in Stellar Cyber
5. Test the connector
6. Verify ingestion

Obtaining the VMware Carbon Black Organization ID

Use of this connector requires that you have previously configured your VMware Carbon Black
deployment to send data to AWS S3. You still require the Organization ID to configure the
connector. You can find this in your VMware Carbon Black Cloud portal under Settings |
 API Access | API Keys.

Gathering / Configuring the AWS S3 Information
Use this section to obtain the following required details for use in configuring your connector:

Access Key ID

Secret Access Key

Bucket

Alert Prefix

Endpoint Event Prefix

Creating a User

To add a user with the appropriate permissions:

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. Choose Policies and then choose Create Policy.

4. In the Create policy pane, choose the JSON tab.

5. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

VMware Carbon Black policy

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::stellarcarbonblack/*",
                "arn:aws:s3:::stellarcarbonblack"
            ]
        }
    ]
}

6. Choose Next.

7. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

The policy can now be attached to a user.

8. From the IAM navigation pane, choose Users and then choose Create user.

9. On the Specify user details page for User details, enter a User name for the new

user.

10. Choose Provide user access to the – AWS Management Console optional to

produce login credentials for the new user, such as a password.

11. Choose how you want to create the Console password and then choose Next.

12. On the Set permissions page, choose Attach policies directly. Then search for the

policy you created above.

13. Select the checkbox to the left of the policy name, then choose Next.

14. On the Review and create page, verify the information and then choose Create user.

Creating an Access Key

1. Log in to the IAM Console with your AWS account ID, your IAM user name, and

password. You must have the permissions required to create access keys for a user.

2. Choose Users, then click the user name, and click Security credentials.

3. In the Access keys section, choose Create access key. Access keys have two

parts: an access key and a secret access key. Click Create access key.

4. On the Access key best practices & alternatives page, choose Other and then

choose Next.

5. (Optional) On the Set description tag page, enter a description.

6. Click Create access key.

7. On the Retrieve access keys page, choose Show to reveal the value of the user's

secret access key. Save the access key and secret access key in a secure location. You
will need them when configuring the connector in Stellar Cyber.

8. Click Done.

Creating and Configuring the S3 Bucket

1. Navigate to the AWS S3 Console (https://s3.console.aws.amazon.com/s3/home ).

2. From the navigation pane, select Bucket to ensure the buckets dashboard is displayed.

3. Click Create bucket. Give the bucket a unique name that does not contain uppercase

letters or underscores; dashes are allowed.

4. Verify the AWS region is set to the desired value (for example, US East (N. Virginia)

us-east-1).

5. Ensure the check-box for Block all Public Access is enabled/checked. The connector

does not require public access set.

6. At the bottom of the screen, click the button to Create bucket.

7. From the AWS S3 list of buckets, click the name of the bucket you just created.

8. From the bucket details pane, click the button to Create folder. This is the folder to

which you will send data from the VMware Carbon Black console. Note the precise
folder name. You will use this folder name to replace the prefix in the bucket policy in
the next step, in the connector, and when you add a Data Forwarder in the Carbon
Black Cloud console.

 Each VMware Carbon Black Data Forwarder requires its own folder. Otherwise,

data from multiple forwarders can mix in the same folder and impair parsing of data.

9. Now, click the Permissions tab and click the button to Edit the Bucket Policy.

10. Modify the Resource parameter as indicated below to include your Carbon Black
product region and the name of the folder you created above. This pane includes
buttons to sample policies and to an AWS Policy Generator tool  you can use to
create the JSON for your bucket policy.

{

"Version": "2012-10-17",

"Statement": [

{

}

"Sid": "Statement1",

"Principal": {},

"Effect": "Allow",

"Action": [],

"Resource": []

]

}

Following is an example of a complete policy with the region, folder, and allowed actions
specified, using the AWS Policy Generator tool. The most critical element to include is
the Resource field.

{

  "Version": "2012-10-17",

  "Id": "Policy1647298852280",

  "Statement": [

    {

      "Sid": "Stmt1647298832372",

      "Effect": "Allow",

      "Principal": {

        "AWS":

          "arn:aws:iam::132308400445:role/mcs-psc-prod-event-forwarder-us-

east-1-event-forwarder"

        },

      "Action": [

        "s3:PutObject",

        "s3:PutObjectAcl"

      ],

      "Resource":

      "arn:aws:s3:::bucket-name/prefix-folder-name/*"

    }

  ]

}

11. Repeat Step 8 to 10 for each data type you want to collect: once for alerts and once for

endpoint events, ensuring they are in the same bucket.

At this point you should have made note of the following information from your VMware and AWS
steps, above.

Organization ID

Access Key ID

Secret Access Key

Bucket

Alert Prefix

Endpoint Event Prefix

(Optional) Configuring Carbon Black for Respond
Action
To configure settings in VMware Carbon Black for the Contain Host respond action:

1. Log in to VMware Carbon Black.

2. Expand Settings, then click API Access.

3. Click Access Levels.

4. Click Add Access Level.

5. Enter a Name and Description.

6. Select permissions as follows to allow the API key you create to have permissions for

the response action:

For Device > Quarantine (device.quarantine), select Execute.

For Device > General information (device), select Read.

For Device > Background scan (device.bg-scan), select Execute.

7. Click Save.

8. After you create the Access Level, click API Keys and click Add API Key.

9. Enter a Name and Description.

10. For Access Level type, select Custom.

11. Select the name of the Custom Access Level you previously created.

12. (Optional) If you want to restrict the API key to only work on certain IP addresses, you

can enter them in Authorized IP addresses.

13. Click Save.

14. Copy your API ID and API Secret Key. You will use them when configuring the

connector in Stellar Cyber.

15. Locate your ORG KEY as follows:

16. Make note of the ORG KEY. You will use it when configuring the connector in Stellar

Cyber.

Adding the Connector in Stellar Cyber
With the access information handy, you can add a VMware Carbon Black Cloud connector in
Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose VMware Carbon Black Cloud from the Type dropdown.

The asterisk (*) indicates a required field.

6. Choose the Function: Collect to collect logs; Respond for the respond action to

contain hosts. You can select either Collect or Respond or both Collect and Respond.
After you click Next, the configuration will vary, depending on your selection.

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

11. Click Next. The following Configuration tab appears for the Collect function.

The asterisk (*) indicates a required field.

The following Configuration tab appears for the Respond function.

The asterisk (*) indicates a required field.

 If you select both Collect and Respond, the Configuration tab contains the fields

for both.

12. For the Collect function:

a. Enter the Carbon Black Cloud Organization Key you noted above in

Gathering / Configuring the AWS S3 Information.

b. Enter the Bucket. This is the AWS S3 bucket you noted above, configured in

Carbon Black Event Forwarder.

c. Enter the Access Key ID you noted above.

d. Enter the Secret Access Key you noted above.

e. Choose the Interval (min). This is how often the logs are collected.

f. For the logs for Alert Collection, select Collect Carbon Black alert events.

g. Enter the Alert Prefix you noted above, configured in Carbon Black Event
Forwarder for alerts. (For this connector, it is the folder you created in the
bucket above.)

You can just enter alerts if the S3 bucket has the following prefix syntax:
alerts/org_key=my_org/year=2022/month=11/day=23/hour=11/minute=
56/

h. For the logs for Endpoint Event Collection, select Collect Carbon Black

endpoint events.

i. Enter the Endpoint Event Prefix, configured in Carbon Black Event

Forwarder for endpoint events.

13. For the Respond function:

a. Enter the Organization Key. This is the ORG KEY you noted above in

(Optional) Configuring Carbon Black for Respond Action.

b. Enter your Host.

 Do not include the https prefix.

c. Enter the API secret key you noted above.

d. Enter the API ID you noted above.

14. Click Next. The final confirmation tab appears.

15. Click Submit.

The new connector is immediately active and collects logs beginning today.

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

2. Change the Indices for the type of content you collected:

For Alert and Endpoint Event, change the Indices to Syslog.

For Alert only, change the Indices to Assets.

The table immediately updates to show ingested Interflow records.

If you configured the connector Respond action, refer to External Actions: Contain Host to
understand how to work with the Contain Host feature.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

